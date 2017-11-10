from django.shortcuts import render
from django.http import HttpResponse
import random
import json

storys = [
    {1:u'我想成立一个',2:u'项目',3:u'，<br>受众只有',4:u'你',5:u'一个，<br>用一生的时间提高',6:u'你',7:u'的生活质量'},
    {1:u'<br>我想和',2:u'你',3:u'<br>从诗词歌赋<br>聊到',4:u'创行项目'},
    {1:u'祝',2:u'你',3:u'来生<br>不带金箍不做狗<br>有合适的',4:u'项目',5:u'<br>和',6:u'爱你',7:u'的人'},
    {1:u'<br>当我看到了',2:u'你',3:u',<br>我才知道<br>我为什么来到了',4:u'创行'},
    {1:u'<br>关于',2:u'创行',3:u'，',4:u'<br>你',5:u'有什么想问的<br>都可以来吻我'},
    {1:u'<br>未经思考，加了',2:u'创行',3:u'<br>未经允许，喜欢了',4:u'你'},
    {1:u'<br>我就是喜欢看',2:u'你',3:u'看不惯我，<br>却不得不陪我<br>一起加',4:u'创行',5:u'的样子'},
    {1:u'我做过许多调研，<br>熬过许多备赛的夜，<br>却只',2:u'爱',3:u'过一个<br>正当最好年龄的',4:u'你'},
    {1:u'这个世界上<br>有这样一个',2:u'创行',3:u'，<br>是为了这个世界上<br>有这样一个',4:u'你'},
    {1:u'<br>有些人光是在',2:u'创行',3:u'遇到<br>就已经赚了,<br>所以不遗憾！'},
    {1:u'<br>可爱不是长久之计<br>可',2:u'爱',3:u'我是'},
    {1:u'<br>给',2:u'你',3:u'一个人生建议:<br>和我在一起'},
    {1:u'我',2:u'爱你',3:u'<br>如鲸向海<br>如鸟投林<br>如',4:u'你',5:u'入',6:u'创行'},
    {1:u'<br>谢谢',2:u'你',3:u'长得这么好看，<br>调研的日子就算再辛苦，<br>看到',4:u'你',5:u'就开心很多了'},
    {1:u'<br>今夜我不关心',2:u'项目<br>',3:u'我只想',4:u'你'},
    {1:u'后海有树的院子,<br>夏代有工的玉。<br>此时此刻的',2:u'创行',3:u'，<br>二十来岁的',4:u'你'},
]

def dashboard(request):
    return render(request,'base.html')

def index(request):
    return render(request, 'index.html')

def name(request):
    name = request.GET['name']
    story =  json.dumps(random.choice(storys))
    index = list(map(str, range(len(story))))
    capital = index[::2]
    enactus = {'name':name,'story':story,'index':index,'capital':capital}
    return render(request, 'name.html', enactus)
