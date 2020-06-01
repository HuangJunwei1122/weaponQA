from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from WeaponQAs.functions.module_lev import fetch_answer
from WeaponQAs.functions.recom import recom
import os


import json


# Create your views here.


def index(request):
    """主页"""
    # 主页
    return render(request, 'WeaponQAs/ui.html')


def search(request):
    """返回答案"""
    print("request method:", request.method)
    pic_name = os.listdir('D:\\PC_projests\\WeaponsQA\\WeaponQAs\\static\\images\\')
    pics = [os.path.splitext(i)[0] for i in pic_name]
    print("pics name:", pics)
    if request.method == 'POST' and request.POST.get('question') != '':
        question = request.POST.get('question')
        a = fetch_answer(question)[0]
        r = str(recom(question))
        print("推荐：", r)
        print(type(r))
        for pic in pics:
            if pic in question:
                pic_path = "<img src='static/images/{}.jpg'>".format(pic)
                print("pic_path:", pic_path)
                result = {"answer": a, "recommendation": r, "pic_path": pic_path}
                return HttpResponse(json.dumps(result, ensure_ascii=False),
                                    content_type="application/json,charset=utf-8")
        pic_path = "<b>很抱歉，这个问题暂时无相关展示</b>"
        result = {"answer": a, "recommendation": r, "pic_path": pic_path}
        return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json,charset=utf-8")

