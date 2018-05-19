## 这是一个django2.0+项目，主应用名为FacePlay,主项目名为hc。
	在hc主目录下运行下面指令开启后台测试服务器
```
python manage.py runserver_plus --cert server.crt 0.0.0.0:8667
```

- **为了让django支持https协议(以便部署并测试)，需先：**
- pip install django-extensions 
- pip install django-werkzeug-debugger-runserver 
- pip install pyOpenSSL 

> 该项目已经配置好了SSL证书并使用server.crt，若要手动配置请参考[WINDOWS系统下创建自签名SSL证书](http://www.webprague.com/detail.html?id=34) 

- 8667为可选参数，为开启端口值
- 若改变8667，需要同时改变static/js/camera.js和static/js/submit.js里的port值，同理若自定义IP而不是0.0.0.0，也需要改变上述两个文件里的IP值，即
```
var port = '8667';
var ip = 'localhost';
```

然后同个局域网下可以访问项目运行后台所在ip的地址+项目名
例如https://ip:port/FacePlay/login
**如采用默认设置则为[https://localhost:8667/FacePlay/login](https://localhost:8667/FacePlay/login)**

### 项目结构
- FACEs 存放用户的头像，文件夹名为id，文件名为手机号
- Recognition 存放被教师上传需要被识别出人的图片以及缺席人
- SphereFace 存放训练好的SphereFace人脸识别模型
- hc/hc admin项目后台控制所在目录
- server.crt/server.key django项目在https环境下运行所需要的秘钥
- 其它在主目录的图像均为临时图像（已隐藏并无上传）
- main.py人脸检测、人脸识别主要文件
