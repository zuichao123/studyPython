#coding:utf-8
import pygame
import pygame.locals
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

    #左移
    def move_left(self):
        self.x -= 5

    #右移
    def move_right(self):
        self.y += 5

    #开火
    def fire(self):
        self.bullet_list.append(HeroBullet(self.screen,self.x,self.y))

#敌人的飞机类
class EnemyPlane(BasePlane):
    def __init__(self,screen_temp):
        BasePlane.__init__(self,screen_temp,0,0,"./feiji/enemy0.png")
        self.direction = "right"#用来存储飞机默认的显示方向

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
        BaseBullet.__init__(self,screen_temp,x+40,y-20,"./feiji/bullet.png")

    #玩家子弹移动方法
    def move(self):
        self.y -= 20

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
        self.y += 5

    #敌机飞机的判断出界的方法
    def judge(self):
        if self.y > 852:
            return True
        else:
            return False

#获取键盘事件类
def key_control(hero_temp):
    # 获取事件，比如按键等
    for event in pygame.event.get():

        # 判断是否是点击了退出按钮
        if event.type == pygame.QUIT:
            print("exit")
            exit()
        # 判断是否是按下了键
        elif event.type == pygame.KEYDOWN:
            # 检测按键是否是a或者left
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                print('left')
                hero_temp.move_left()
            # 检测按键是否是d或者right
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                print('right')
                hero_temp.move_right()
            # 检测按键是否是空格键
            elif event.key == pygame.K_SPACE:
                print('space')
                hero_temp.fire()

#主函数
def main():
    #1.创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480,852),0,32)

    #2.创建一个背景图片
    background = pygame.image.load("./feiji/background.png")

    #3.创建一个飞机对象
    hero = HeroPlane(screen)

    #4.创建一个敌机
    enemy = EnemyPlane(screen)

    while True:
        screen.blit(background,(0,0))#将背景图片放到窗口中
        hero.display()#玩家机显示
        enemy.display()#敌机显示
        enemy.fire()#敌机开火
        pygame.display.update()#刷新显示
        key_control(hero)#调用键盘监听方法移动玩家飞机
        time.sleep(0.01)

if __name__ == "__main__":
    main()