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
    url(r'^record$', views.record, name='record'),
    url(r'^message$', views.message, name='message'),
    url(r'^student$', views.student, name='student'),
    url(r'^send_message$', views.send_message, name='send_message'),
    url(r'^read_record$', views.read_record, name='read_record'),
    url(r'^send_image$', views.send_image, name='send_image'),
    url(r'^upload_image$', views.upload_image, name='upload_image'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^.+$', views.page_not_found, name='page_not_found')
]

