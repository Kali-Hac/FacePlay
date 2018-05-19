## 这是一个django2.0+项目，主应用名为FacePlay,主项目名为hc。
### 所需主要配置
- Python 3.6
- Django 2.0.5 (用于前后台交互)
- cv2，base64 （用于图像处理）
- numpy (用于高性能矩阵运算——图形向量计算)
- pytorch (构建人脸识别SphereFace模型)
- mtcnn (用于快速人脸检测)

### SphereFace模型(需要先下载并放在主目录下)
- 本作品(团队成员)已自实现论文中的模型并验证了性能，已开源至
[https://github.com/DQ0408/SphereFace-TensorFlow](https://github.com/DQ0408/SphereFace-TensorFlow)
- 该模型是本作品人脸识别的关键组件
(A TensorFlow implementation for SphereFace!The code can be trained on LFW.)
**SphereFace: Deep Hypersphere Embedding for Face Recognition**

- **请将训练好的pytorch模型文件夹model/放在主目录下**
- 模型下载地址：

链接：[https://pan.baidu.com/s/1vkov3YQ3liHf1hGFDuvr-w](https://pan.baidu.com/s/1vkov3YQ3liHf1hGFDuvr-w) 

密码：3byb
### 使用方法
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
例如：https://ip:port/FacePlay/login
**如采用默认设置则为[https://localhost:8667/FacePlay/login](https://localhost:8667/FacePlay/login)**

### 项目结构
- FACEs 存放用户的头像，文件夹名为id，文件名为手机号
- Recognition 存放被教师上传需要被识别出人的图片以及缺席人
- SphereFace 存放训练好的SphereFace人脸识别模型
- hc/hc admin项目后台控制所在目录
- server.crt/server.key django项目在https环境下运行所需要的秘钥
- 其它在主目录的图像均为临时图像（已隐藏并无上传）
- main.py人脸检测、人脸识别主要文件

### 作品截图(注册->登录->教师端->学生端)
[](p/注册.png)
[](p/注册2.png)
[](p/登录.png)
[](p/登录2.png)
[](p/教师.png)
[](p/教师1.png)
[](p/教师1.5.png)
[](p/教师2.png)
[](p/教师3.png)
[](p/教师4.png)
[](p/学生1.png)
[](p/学生2.png)