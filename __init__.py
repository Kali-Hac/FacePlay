#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
☆*°☆*°(∩^o^)~━━  2018/5/5 15:15        
      (ˉ▽￣～) ~~ 一捆好葱 (*˙︶˙*)☆*°
      Fuction：        √ ━━━━━☆*°☆*°
"""
import os
s=os.listdir('Recognition')
for i in s:
	if i.split('.')[1] == 'txt':
		print(i)