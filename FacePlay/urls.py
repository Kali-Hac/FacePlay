#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
☆*°☆*°(∩^o^)~━━  2018/5/3 17:01        
      (ˉ▽￣～) ~~ 一捆好葱 (*˙︶˙*)☆*°
      Fuction： 新建urls.py来映射url √ ━━━━━☆*°☆*°
"""
from django.conf.urls import url
from . import views
app_name = 'FacePlay'
urlpatterns = [
    # ex: /mysample/
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^forgot-password$', views.forgot, name='forgot'),
    url(r'^register$', views.register, name='register'),
    url(r'^upload$', views.upload, name='upload'),
    url(r'^identify_face$', views.identify_face, name='identify_face'),
    url(r'^face_result$', views.face_result, name='face_result'),
    url(r'^login_check$', views.login_check, name='login_check'),
    url(r'^charts$', views.charts, name='charts'),
]