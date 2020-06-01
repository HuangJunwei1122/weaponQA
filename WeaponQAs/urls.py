"""定义WeaponQAs的URL模式"""

from django.conf.urls import url
from django.views.static import serve

from . import views
app_name = 'WeaponQAs'
urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
    # 点击“查询”后返回的页面
    url(r'^search$', views.search, name='answer'),
    url(r'^pic$', serve, {'document_root': r'D:\PC_projests\WeaponsQA\WeaponQAs\static'}),
]
