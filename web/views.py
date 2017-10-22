from django.shortcuts import render
from django.http import HttpResponse
import random

storys = [
    '，我想成立一个项目，受众只有你一个，用一生的时间提高你的生活质量',
    '，我想和你从诗词歌赋聊到创行项目',
    '，祝你来生不带金箍不做狗，有合适的项目和爱你的人',
    '，当我看到了你，我才知道我为什么来到了创行',
    '，关于创行，你有什么想问的都可以来吻我',
    '，未经思考，加了创行；未经允许，喜欢了你',
    '，我就是喜欢看你看不惯我，却不得不陪我一起加创行的样子',
    '，我做过许多调研，经过许多类型的专案，熬过许多备赛的夜，却只爱过一个正当最好年龄的你',
    '，这个世界上有这样一个创行，是为了这个世界上有这样一个你',
    '，有些人光是在创行遇到了就已经赚了，所以不遗憾！'
]

def dashboard(request):
    return render(request,'base.html')

def index(request):
    return render(request, 'index.html')

def name(request):
    name = request.GET['name']
    story =  random.choice(storys)
    enactus = {'name':name,'story':story}
    return render(request, 'name.html', enactus)
