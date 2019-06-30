#coding:utf-8
'''
正则表达式练习：
    []里边的字符是或关系。
    ()表示组，里边的字符是与关系。

    .   匹配换行符\n之外的所有字符
    \d  数字
    \D  非数字
    +   前一个字符至少出现一次（可以出现多次）
    *   前一个字符可以出现0次或多次
    $   结尾
    ^   开头
    \b  匹配一个单词的边界
    \B  匹配非单词边界
    ?   前一个字符可有可无（匹配0次或1次）【非贪婪操作符】
    []  括号中的任意字符
    {3} 前一个字符字符个数为3个
    {3,}    前一个字符个数至少为3个
    {3,4}   前一个字符出现3或4个
    \w  单词字符（不能匹配非单词字符&等）
    \W  非单词字符（如空格、&、……等）
    \s  空白字符（回车、制表、\r、\n、\t等）
    \S  非空白字符

    (ab)  将括号中字符作为一个分组
    \num    引用分组num匹配到的字符串(就是说，引用当前正则中的前边的分组结果。如：r"(.*)sf(.+)\2asdf\1" --> \2引用第二个括号)
    (?p<name>)  分组起别名
    (?P=name)   引用别名为name分组匹配到的字符串

    group() 获取匹配成后的分组【参数：0表示所有 1表示第一组 2表示第二组 ...】

    注意：字符串前边加上r表示原始字符串（如：r"\n\w\swoshiyuanshide"）可以忽略转义

    ex:
        email:
            re_p = r"(\w+)@(163|126|gmail|qq|irisking)\.(com|cn|net)$"
            str = "sunjian@irisking.com"
            result = re.match(re_p, str)
            result.group() # sunjian@irisking.com
            result.group(1) # sunjian
            result.group(2) # irisking
            result.group(3) # com


查找：
    re.findall(pattern,string,flags) # 返回所有匹配的，返回列表
        pattern:  正则模式
        string:   字符
        flags:
            re.I  忽略pattern大小写
            re.S  改变pattern中.的行为作用
        eg:
            laguage = 'PythonC#\nJavaPHP'
            result = re.findall('c#.{1}',lanuage,re.I | re.S)
            print(result)

    re.match() # 返回第一个（找到第一个就不往后找了；从起始位置开始往后查找）
        eg:
            # match匹配（字符串第一个必须是正则要求的，返回第一个搜索到的）
            laguage = '2330494'
            result2 = re.match('\d',laguage)
            print('match:',result2.span()) #span() 返回位置


    re.search() # 返回第一个（找到第一个就不往后找了；从任何位置开始往后查找；详见下边的实例）
        eg:
            # search匹配（搜索匹配，返回第一个搜索到的）
            laguage = '玩儿2330494'
            result2 = re.search('\d',laguage)
            print('match:',result2.group()) # 返回字符

替换：
    way1、
        re.sub(pattern,repl,string,count=0,flags=0)
            pattern:    正则
            repl:       替换后的字符串
            string:     原始字符串
            count:      默认参数0（0表示替换的字符串无限制的替换；1表示只替换第一个匹配正则的字符）

            eg:
                laguage = 'PythonC#\nJavaPHPC#'
                result = re.sub('C#','Go',laguage,0)
                print(result)

            eg2:把函数作为参数传递
                s = 'ABC123456789WER'
                    # 把字符串s中，大于等于5的数字替换为9；小于5的替换为0
                def convert(value):
                    matched = value.group()
                    if int(matched) >= 5:
                        return '9'
                    else:
                        return '0'

                r = re.sub('\d',convert,s)#convert函数的返回值，替换‘\d’匹配到的s字符串中的数字(换句话说：就是将s字符串中的数字替换为convert函数的返回值)
                print(r)

    way2、
        lanuage.replace(old,new,count)
            old:    替换前的字符
            new:    替换后的字符
            count:  默认参数0（0表示替换的字符串无限制的替换；1表示只替换第一个匹配正则的字符）
'''

import re

s='abc'
s=r'ab[ce]d'
print (re.findall(s,'aaabcaaaaaabedaaabcdaaa'))

s='hello world,hello boy'
r=r'^hello'#开头
r2=r'boy$'#结尾
print('00000000000000000000000000000000')
print (re.findall(r2,s))
print('111111111111111111111111111111111')
r='t[ab$]'#结尾
print (re.findall(r,'asdfsdtaatb'))

r='x[a-zA-Z0-9]e'
print (re.findall(r,'afadxEefeafdaxdesdfx3eadfdex'))

r=r"^010-\d{8}"
print (re.findall(r,"010-333333444338"))

r=r"ab*"
#b出现0-多次

r=r"ab+"
#b出现至少一次

r=r"^010-?\d{8}$"
#表示010-开头，其中-可有可无；结尾8个数字

r=r"^010-*\d{8}$"
#表示010-开头，其中-出现0或多次；结尾8个数字
print (re.findall(r,"010-12312456"))

r=r"^\d{3,4}-?\d{8}"#正则电话号码(开头3或4个数字，-可有可无；8个数字)
print (re.findall(r,"2034-324234234"))

p_tel=re.compile(r)#将电话正则编译
p_tel.match("3423")

rs=r's..s'#正则替换
print (re.sub(rs,'jack','swers s323423s sks sssss'))#根据定义的rs正则替换)

#正则切割
rr=r'[\+\-\*/]'
print (re.split(rr,'123+32-234*sdf/sfe'))

#忽略大小写，并且改变换行符的行为
laguage = 'PythonC#\nJavaPHP'
result = re.findall('c#.{1}', laguage, re.I | re.S)
print(result)

#match匹配（字符串第一个必须是正则要求的，返回第一个搜索到的）
laguage = '2330494'
result2 = re.match('\d',laguage)
print('match:',result2.span())#span()返回位置

#search匹配（搜索匹配，返回第一个搜索到的）
laguage = '玩儿2330494'
result2 = re.search('\d',laguage)
print('match:',result2.group()) # 返回字符

# 替换1
laguage = "qweqweqweeeeerrrr"
result = laguage.replace("qwe",'yyyy',0)
print(result)
# 替换2
laguage = 'PythonC#\nJavaPHPC#'
result = re.sub('C#', 'Go', laguage, 0)
print(result)
# 替换3
    # 把函数作为参数传递
s = 'ABC123456789WER'
# 把字符串s中，大于等于5的数字替换为9；小于5的替换为0
def convert(value):
    matched = value.group()
    if int(matched) >= 5:
        return '9'
    else:
        return '0'

r = re.sub('\d',convert,s) # convert函数的返回值，替换‘\d’匹配到的s字符串中的数字
print(r)

print('---------------------group()函数详解---------------------------------------------')
sj = '234234fasdf234234234asd78923faf'
r = re.match('\d',sj)

# 返回字符串的位置
print(r.span())
# 返回字符串
    # 分组可以有多个
print(r.group())

sj2 = 'life is short, i use python. I love python'
r = re.search('life(.*)python(.*)python',sj2)
print(r.group(0,1,2)) # 返回每个组的完整
print(r.groups()) # 返回每个组的实际
print(r.group()) # 返回实际匹配的所有

print("----"*16,'经典例子')
s = "http://www.baidu.com/messagfin.asp?id=77"
'''将.com/后边的字符替换为空'''
# 思路：使用sub函数；先将所有的匹配出来；将较容易的部分先匹配出来；使用lambda表达式将较容易的部分返回
result = re.sub(r"(http://.+?/).*", lambda x:x.group(1), s)
print(result)

print('-----------'*20)
str = '---------start download---------https://cbu01.alicdn.com/img/ibank/2019/450/752/11264257054_586706785.jpg"></a></div><div class="broadcastMe-item" style="width: 388px;"><a href="https://fujioem.com/2165" target="_blank" rel="nofollow"><img src="https://sc02.alicdn.com/kf/UTB8oVttO3QydeJk43PU5jcyQpXaX.gif"></a></div><div class="broadcastMe-item" style="width: 388px;"><a href="https://38855268.com/sxsp.html" target="_blank" rel="nofollow"><img src="https://cbu01.alicdn.com/img/ibank/2019/450/752/11264257054_586706785.jpg"></a></div><div class="broadcastMe-item" style="width: 388px;"><a href="http://vip.988340.com:966/3377.html" target="_blank" rel="nofollow"><img src="https://sc02.alicdn.com/kf/HTB1rFIsc25G3KVjSZPx5jbI3XXad.gif"></a></div><div class="broadcastMe-item" style="width: 388px;"><a href="https://58qp682.com/?c=KF62C" target="_blank" rel="nofollow"><img src="https://cbu01.alicdn.com/img/ibank/2019/450/752/11264257054_586706785.jpg'
print(type(str))
str = '<div class="main-content"><img src="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555975.jpg" border="0"><br><img src="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555979.jpg" border="0"><br><img src="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555981.jpg" border="0"><br><img src="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555982.jpg" border="0"><br><img src="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555984.jpg" border="0"><br><img src="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555989.jpg" border="0"><br><img src="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555990.jpg" border="0"><br><img src="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555993.jpg" border="0"><br><img src="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555996.jpg" border="0"><br><img src="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555997.jpg" border="0"><br><img src="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555988.jpg" border="0"><br><img src="http://p7.urlpic.club/pic1893/upload/image/20190627/62713556000.jpg" border="0"></div>'

str = '<!DOCTYPEhtml><htmllang="zh-CN"><head><metacharset="gb2312"><metahttp-equiv="Content-type"name="viewport"content="initial-scale=1.0,maximum-scale=1.0,user-scalable=no,width=device-width"><title>牛仔短裤女生-半岛影院</title><metaname="keywords"content="半岛影院"><metaname="description"content="半岛影院bandao345.com"><linkrel="stylesheet"href="/static/css/style.css"></head<body><divid="nav"class="nav-wrap"><divclass="area"><dl><dt><spanclass="logo"><ahref="/">bandao345.com</a></span><<ddclass="mt"><ahref="/"><iclass="icon-home"></i></a></dd><dd><ahref="/app.html"target="_blank"><iclass="icon-app"></i><spanclass="pc">APP下载</span></a></dd></dl></div></div><divclass="slider-spons"><divid="sliderBox"><divclass="broadcastMe"style="width:388px;"><divclass="broadcastMe-list"style="width:1940px;margin-left:-776px;"><divclass="broadcastMe-item"style="width:388px;"><ahref="http://vip.988340.com:966/3377.html"target="_blank"rel="nofollow"><imgsrc="https://sc02.alicdn.com/kf/HTB1rFIsc25G3KVjSZPx5jbI3XXad.gif"></a></div><divclass="broadcastMe-item"style="width:388px;"><ahref="https://38855268.com/sxsp.html"target="_blank"rel="nofollow"><imgsrc="https://cbu01.alicdn.com/img/ibank/2019/450/752/11264257054_586706785.jpg"></a></div><divclass="broadcastMe-item"style="width:388px;"><ahref="https://fujioem.com/2165"target="_blank"rel="nofollow"><imgsrc="https://sc02.alicdn.com/kf/UTB8oVttO3QydeJk43PU5jcyQpXaX.gif"></a></div><divclass="broadcastMe-item"style="width:388px;"><ahref="https://58qp682.com/?c=KF62C"target="_blank"rel="nofollow"><imgsrc="https://cbu01.alicdn.com/img/ibank/2019/450/752/11264257054_586706785.jpg"></a></div><divclass="broadcastMe-item"style="width:388px;"><ahref="http://vip.988340.com:966/3377.html"target="_blank"rel="nofollow"><imgsrc="https://sc02.alicdn.com/kf/HTB1rFIsc25G3KVjSZPx5jbI3XXad.gif"></a></div></div><divid="broadcastMe-tool"class="broadcastMe-tool"style="margin-left:-75px;"><divclass=""></div><divclass=""></div><divclass="active"></div><divclass=""></div></div><divid="broadcastMe-btn-left"class="broadcastMe-btnbroadcastMe-btn-left">&lt;</div><divid="broadcastMe-btn-right"class="broadcastMe-btnbroadcastMe-btn-right">&gt;</div></div></div></div><divid="menu"clas<divclass="area"><dlclass="first"><dt><ahref="/video/">视频</a></dt><dd><ahref="/video/remenshijian/">热门事件</a<dd><ahref="/video/toupai/">偷拍自拍</a></dd><dd><ahref="/video/kongjiemote/">空姐模特</a></dd><dd><ahref="/video/zhubowanghong/">主播网红</a></d<dd><ahref="/video/luanluntouqing/">乱伦偷情</a></<dd><ahref="/video/huwaiyezhan/">户外野战</a></dd><dd><ahref="/video/nvshenzonghe/">女神综合</a></dd><dd><ahref="/video/sanjilunli/">三级伦理</a></dd></dl<dl><dt><ahref="/dianying/">电影</a></dt><dd><ahref="/dianying/wuma/">日韩无码</a></dd><dd><ahref="/dianying/oumeixingai/">欧美A片</a></dd><dd><ahref="/dianying/meituizhifu/">美腿制服</a></dd><dd><ahref="/dianying/shaofurenqi/">少妇人妻</a></dd><dd><ahref="/dianying/qunjiaolinglei/">群交另类</a></dd><dd><ahref="/dianying/youma/">有码AV</a></dd><dd><ahref="/dianying/dongmankatong/">动漫卡通</a></dd<dd><ahref="/dianying/zhongwenzimu/">中文字幕</a></dd></dl<dl><dt><ahref="/tupian/">图片</a></dt><dd><ahref="/tupian/yazhoutupian/">亚洲图片</a></dd><ahref="/tupian/oumeisetu/">欧美色图</a></dd><dd><ahref="/tupian/wangyouzipai/"class="cur">偷拍dd><ahref="/tupian/meituisiwa/">美腿丝袜</a></dd><dd><ahref="/tupian/qingchunweimei/">清纯唯美</a></dd<dd><ahref="/tupian/dongmankatong/">卡通动漫</a></dd></dl<dl><dt><ahref="/xiaoshuo/">小说</a></dt><dd><ahref="/xiaoshuo/jiqingwenxue/">激情小说<<dd><ahref="/xiaoshuo/jtll/">家庭乱伦</a></dd><dd><ahref="/xiaoshuo/xywx/">校园武侠</a></dd></dl<dl><dt><ahref="/xiazai/">下载</a></dt><dd><ahref="/xiazai/yzwm/">亚洲无码</a></dd><dd><ahref="/xiazai/ymjp/">有码精品</a></dd><dd><ahref="/xiazai/omjq/">欧美激情</a></dd><dd><ahref="/xiazai/sjxz/">三级写真</a></dd><dd><ahref="/xiazai/zpdp/">正片大片</a></dd><dd><ahref="/xiazai/hjxz/">合集下载</a></dd></dl></div></div><divid="topBox"><divclass="mod"><divclass="area"><h1class="h1-title">牛仔短裤女生</h1><divclass="main-content"><imgsrc="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555975.jpg"border="0"><br><imgsrc="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555979.jpg"border="0"><br><imgsrc="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555981.jpg"border="0"><br><imgsrc="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555982.jpg"border="0"><br><imgsrc="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555984.jpg"border="0"><br><imgsrc="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555989.jpg"border="0"><br><imgsrc="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555990.jpg"border="0"><br><imgsrc="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555993.jpg"border="0"><br><imgsrc="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555996.jpg"border="0"><br><imgsrc="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555997.jpg"border="0"><br><imgsrc="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555988.jpg"border="0"><br><imgsrc="http://p7.urlpic.club/pic1893/upload/image/20190627/62713556000.jpg"border="0">v><divclass="post-link"><ahref="javascript:void(0);"class="prev">上一篇<spanclass="mobile">：无</span></a><ahref="/tupian/wangyouzipai/2019062802072160112.html"class="next">下一篇<spanclass="mobile">：<h2>街拍性感红衣美女</h2></span></a></div></div></div><divid="bottomBox"></div><scriptsrc="/static/js/common.js"></script><scriptsrc="/static/js/base.js"></script><divid="coupletBox"></div><divid="footer"class="footer"><divclass="area">本站含有成人内容，适合18岁以上的成人浏览。</div></div><divid="guide"class="area"style="display:none;"><divclass="guide"><spanclass="pc"><ahref="/"class="home"title="回首页"><span>回首页</span></a><ahref="javascript:void(0)"onclick="goTop();"class="gotop"title="回顶部"><span>回顶部</span></a></span><spanclass="mt"><ahref="javascript:void(0)"id="btnGotop"onclick="goTop();"title="回顶部"><iclass="icon-top"></i></a></span></div></div><divstyle="display:none"><scriptsrc="/static/js/count.js"></script><scriptsrc="http://s11.cnzz.com/z_stat.php?id=1275132709&amp;web_id=1275132709"language="JavaScript"></script><scriptsrc="http://c.cnzz.com/core.php?web_id=1275132709&amp;t=z"charset="utf-8"type="text/javascript"></script><ahref="https://www.cnzz.com/stat/website.php?web_id=1275132709"target="_blank"title="站长统计">站长统计</a></div></body></html>'
str = 'src="https://cbu01.alicdn.com/img/ibank/2019/450/752/11264257054_586706785.jpg"'
img = re.findall(r'src="(.*?\d+\.jpg)', str)
print(img)
print(re.findall('.*?/(\d+)/.*', img[0]))
print(re.findall('.*?/(\d+|\d+_\d+)\.jpg', img[0]))
print('-----------------------------------------------------------')

str = 'src="https://cbu01.alicdn.com/img/ibank/2019/450/752/11264257054586706785.jpg"'
img = re.findall(r'src="(.*?\d+\.jpg)', str)
print(img)
print(re.findall('.*?/(\d+)/.*', img[0]))
print(re.findall('.*?/(\d+|\d+_\d+)\.jpg', img[0]))
print('-----------------------------------------------------------2')



str = '<div class="main-content"><img src="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555975.jpg" border="0" ><br><img src="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555979.jpg" border="0" ><br><img src="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555981.jpg" border="0" ><br><img src="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555982.jpg" border="0" ><br><img src="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555984.jpg" border="0" ><br><img src="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555989.jpg" border="0" ><br><img src="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555990.jpg" border="0" ><br><img src="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555993.jpg" border="0" ><br><img src="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555996.jpg" border="0" ><br><img src="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555997.jpg" border="0" ><br><img src="http://p7.urlpic.club/pic1893/upload/image/20190627/62713555988.jpg" border="0" ><br><img src="http://p7.urlpic.club/pic1893/upload/image/20190627/62713556000.jpg" border="0" ></td>\r\n\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t</div>\r\n\t\t<div class="post-link"><a href="javascript:void(0);" class="prev">\xc9\xcf\xd2\xbb\xc6\xaa<span class="mobile">\xa3\xba\xce\xde</span></a><a href="/tupian/wangyouzipai/2019062802072160112.html" class="next">\xcf\xc2\xd2\xbb\xc6\xaa<span class="mobile">\xa3\xba<h2>\xbd\xd6\xc5\xc4\xd0\xd4\xb8\xd0\xba\xec\xd2\xc2\xc3\xc0\xc5\xae</h2></span></a></div>\r\n\t</div>\r\n</div>\r\n<div id="bottomBox"></div>\r\n<script src="/static/js/common.js"></script>\r\n<script src="/static/js/base.js"></script>\r\n<div style="display:none"><script src="/static/js/count.js"></script></div>\r\n</body>\r\n</html>'
img = re.findall('<div(.*)</div>', str)

img = re.findall(r'src="(.*?\d+\.jpg)', str)
print(img)

for i in range(2,3):
    print(i)
