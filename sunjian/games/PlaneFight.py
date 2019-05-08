#coding:utf-8
import pygame
from pygame import *
import time
import random

'''
   飞机大战
'''
#基类
class Base(object):
    def __init__(self,screen_temp,x,y,image_name):
        self.x = x
        self.y = y
        self.screen = screen_temp#窗口
        self.image = pygame.image.load(image_name)#图片路径
'''----------------------------------------------------'''
#飞机基类
class BasePlane(Base):
    def __init__(self,screen_temp,x,y,image_name):
        Base.__init__(self,screen_temp,x,y,image_name)
        self.bullet_list = []#存储发射出去的子弹对象引用
    #飞机显示方法
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))#将图片填充到指定的坐标
        #循环判断子弹是否越界
        for bullet in self.bullet_list:
            bullet.display()#子弹显示
            bullet.move()#子弹移动
            if bullet.judge():#判断子弹，如果出界的话
                self.bullet_list.remove(bullet)#删除此子弹

#玩家飞机类
class HeroPlane(BasePlane):
    def __init__(self,screen_temp):
        BasePlane.__init__(self,screen_temp,210,700,"./feiji/hero1.png")#super().__init__()的方法

    # 显示英雄
    def display(self):
        # 调用父类方法正常显示飞机
        BasePlane.display(self)
        # 遍历所以子弹是否击中敌机
        for bullet in self.bullet_list:
            # 判断当前子弹是否击中飞机
            if bullet.judge_jizhong(self.enemy):
                self.enemy.bomb(True)

    # # 左移
    # def move_left(self):
    #     print('--left move')
    #     self.x -= 5
    #
    # # 右移
    # def move_right(self):
    #     print('--right move')
    #     self.x += 5
    #
    # # 上移
    # def move_up(self):
    #     print('--up')
    #     self.y -= 5
    #
    # # 下移
    # def move_down(self):
    #     print('--down')
    #     self.y += 5

    # 开火
    def fire(self,enemy):
        self.enemy = enemy
        self.bullet_list.append(HeroBullet(self.screen,self.x,self.y))

# 敌人的飞机类
class EnemyPlane(BasePlane):
    def __init__(self,screen_temp):
        BasePlane.__init__(self,screen_temp,0,0,"./feiji/enemy0.png")
        self.direction = "right"# 用来存储飞机默认的显示方向

        # 添加爆炸效果
        self.bomb_image_list = [] # 存放爆炸图片
        self.__get_bomb_image() # 加载爆炸图片
        self.isbomb = False # Fale没有爆炸，True爆炸
        self.image_num = 0 # 显示过的图片数，变化
        self.image_index = 0 # 要显示图片的下标，变化

    def bomb(self,isbomb):
        self.isbomb = isbomb

    # 加载爆炸图片
    def __get_bomb_image(self):
        for i in range(1,4):
            image = "./feiji/enemy0_down"+str(i)+".png"
            self.bomb_image_list.append(pygame.image.load(image))
        #总数有多少张
        self.image_length = len(self.bomb_image_list)

    def display(self):
        # 判断是否要爆炸
        if self.isbomb:
            bomb_image = self.bomb_image_list[self.image_index] # 获取爆炸图片第image_index张
            self.screen.blit(bomb_image, (self.x, self.y)) # 将爆炸图片填充到界面中的飞机坐标处
            self.image_num += 1 # 已显示图片张数
            if self.image_num == (self.image_length + 1): # 判断，如果已显示的爆炸图片张数等于列表中的张数
                self.image_num = 0 # 重置已显示的爆炸图片数量
                self.image_index += 1 #爆炸图片索引加1

                if self.image_index > (self.image_length - 1): # 如果，爆炸图片索引大于图片张数-1
                    self.image_index = 4 # 设置索引
                    time.sleep(2)
                    exit()  # 炸完了咋样？可以
        else:
            BasePlane.display(self)

    #敌机移动方法
    def move(self):
        if self.direction == "right":
            self.x += 5
        elif self.direction == "left":
            self.x -= 5

        if self.x > 480-50:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"

    #敌机开火方法
    def fire(self):
        random_num = random.randint(1,100)
        if random_num == 68 or random_num == 38:
            self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y))
'''----------------------------------------------------------------------'''
#子弹基类
class BaseBullet(Base):
    #子弹显示方法
    def display(self):
        #在窗口中填充子弹
        self.screen.blit(self.image,(self.x,self.y))

#玩家飞机的子弹
class HeroBullet(BaseBullet):
    def __init__(self,screen_temp,x,y):
        BaseBullet.__init__(self,screen_temp,x+40,y-10,"./feiji/bullet.png")

    # 判断是否击中敌机
    def judge_jizhong(self, enemy):
        if self.x > enemy.x and self.x < enemy.x + 56:
            if self.y > enemy.y and self.y < enemy.y + 31:
                print("击中敌机了..")
                return True
        else:
            return False

    #玩家子弹移动方法
    def move(self):
        self.y -= 10 # speed

    #判断玩家子弹是否出界的方法
    def judge(self):
        if self.y < 0:
            return True
        else:
            return False

#敌机飞机的子弹
class EnemyBullet(BaseBullet):
    def __init__(self,screen_temp,x,y):
        BaseBullet.__init__(self,screen_temp,x+25,y+40,"./feiji/bullet1.png")

    #敌机飞机子弹的移动方法
    def move(self):
        self.y += 10 # speed

    #敌机飞机的判断出界的方法
    def judge(self):
        if self.y > 852:
            return True
        else:
            return False

class PlaneGame(object):
    # 键盘控制
    def key_control(self):
        # 监听键盘的代码
        for event in pygame.event.get():
            # 判断是否点击了退出按钮
            if event.type == QUIT:
                # 退出
                print("exit")
                exit()
                # 判断是否按下了键
            if event.type == KEYDOWN:
                # 检查按钮是否是a或者left
                if event.key == K_LEFT or event.key == K_a:
                    print("left")
                    self.hero.x -= 5
                    # 检查按钮是否是d或者right
                elif event.key == K_RIGHT or event.key == K_d:
                    # 右方向键
                    print("right")
                    self.hero.x += 5
                elif event.key == K_UP or event.key == K_w:
                    # 上方向键
                    print("up")
                    self.hero.y -= 5
                elif event.key == K_DOWN or event.key == K_s:
                    # 下方向键
                    print("down")
                    self.hero.y += 5
                elif event.key == K_SPACE:
                    # 上方向键
                    print("space-空格建")
                    self.hero.fire(self.enemy)
                elif event.key == K_b:
                    # 按b键了
                    print("爆炸")
                    self.enemy.isbomb = True

    def main(self):

        pygame.init()
        # 设置键盘重复
        pygame.key.set_repeat(True)

        # 1.创建一个窗口，用来显示内容
        screen = pygame.display.set_mode((480, 852), 0, 32)

        # 2.创建一个背景图片
        background = pygame.image.load("./feiji/background.png")

        # 3.创建一个飞机对象
        self.hero = HeroPlane(screen)

        # 4.创建一个敌机
        self.enemy = EnemyPlane(screen)

        # 播放背景音乐
        # 初始化背景音乐
        # pygame.mixer.init()
        # 设置音量
        # pygame.mixer.music.set_volume(100)
        # pygame.mixer.music.load("./bgmusic/bgm_zhandou1.mp3")
        # 循环播放多少次
        # pygame.mixer.music.play(1)

        while True:
            screen.blit(background, (0, 0))  # 将背景图片放到窗口中
            self.hero.display()  # 玩家机显示
            self.enemy.display()  # 敌机显示
            self.enemy.move()  # 敌机移动
            self.enemy.fire()  # 敌机开火
            pygame.display.update()  # 刷新显示
            self.key_control()  # 调用键盘监听方法移动玩家飞机
            time.sleep(0.01)


if __name__ == "__main__":
    PlaneGame().main()