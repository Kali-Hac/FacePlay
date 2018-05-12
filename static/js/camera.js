var port = '8778';
var ip = 'localhost';
//访问用户媒体设备的兼容方法
function getUserMedia(constrains,success,error){
    if(navigator.mediaDevices.getUserMedia){
        //最新标准API
        navigator.mediaDevices.getUserMedia(constrains).then(success).catch(error);
    } else if (navigator.webkitGetUserMedia){
        //webkit内核浏览器
        navigator.webkitGetUserMedia(constrains).then(success).catch(error);
    } else if (navigator.mozGetUserMedia){
        //Firefox浏览器
        navagator.mozGetUserMedia(constrains).then(success).catch(error);
    } else if (navigator.getUserMedia){
        //旧版API
        navigator.getUserMedia(constrains).then(success).catch(error);
    }
}

var video;
var canvas;
var context;
var localstream;
//成功的回调函数
function success(stream){
    //兼容webkit内核浏览器
    var CompatibleURL = window.URL || window.webkitURL;
    //将视频流设置为video元素的源
    video.src = CompatibleURL.createObjectURL(stream);
    //用于关闭
    localstream = stream;
    //播放视频
    video.play();
}
//关闭摄像头的函数
function vidOff() {
  video.pause();
  video.src = "";
  localstream.getTracks()[0].stop();
  console.log("Vid off");
}

//异常的回调函数
function error(error){
    console.log("访问用户媒体设备失败：",error.name,error.message);
}

function open_camera(option){
  video=document.getElementById("video");
  canvas = document.getElementById("canvas");
  context = canvas.getContext("2d")
 if(option==="register"){
 var open_camera=document.getElementById("open_camera");
  if(open_camera.innerHTML==="请先完善个人信息并确认"){
    alert("请先完善个人信息并确认");
    return;
  }
  if (navigator.mediaDevices.getUserMedia || navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia){
    //调用用户媒体设备，访问摄像头
    getUserMedia({
        video:{width:480,height:320}
    },success,error);
  }  else {
    alert("你的浏览器不支持访问用户媒体设备");
  }
    var form = document.getElementById("form");
    form.action="register";
    form.method="POST";
    var block = document.getElementById("camera_block");
    block.style.display='block';
   //注册拍照按钮的单击事件
    document.getElementById("capture").addEventListener("click",function(){
    var photo_block = document.getElementById("canvas");
    photo_block.style.display='block';
    var upload_block = document.getElementById("upload");
    upload_block.style.display='block';
    //绘制画面
    context.drawImage(video,0,0,480,320);
    // 将画布转化为图片
    // vidOff();
});
}

  
if(option === 'login'){
   change_login();
   if (navigator.mediaDevices.getUserMedia || navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia){
    //调用用户媒体设备，访问摄像头
    getUserMedia({
        video:{width:360,height:300}
    },success,error);
    } else {
    alert("你的浏览器不支持访问用户媒体设备");
    }
    //change
    var interval = setInterval(function(){
      context.drawImage(video,0,0,360,300);
      take_face();
      var process_show = document.getElementById("process_show");
      if(process_show!=null && process_show.style.display==="block"){
        clearInterval(interval);
         $.post("https://"+ip+":"+ port + "/FacePlay/face_result", {},
            function(data, status){
              $('#change').html(data);
        })
      }
      },2000); //两秒执行一次人脸识别

    // setTimeout(function(){
    //   context.drawImage(video,0,0,360,300);
    //   take_face();
    //   },2000);

   // setTimeout(function(){
   //  context.drawImage(video,0,0,360,300);
   //  take_face();
   // }, 2500);//最快1s+使画布初始化
}
}

function take_face(){
  var temp_img = document.getElementById("temp_img");
  var image = document.getElementById("image");
  var msg = document.getElementById("msg");
  setTimeout(function(){
  temp_img.src = canvas.toDataURL('image/png');
  msg.innerHTML = "人脸正在识别中..."
  temp_img.onload = function(){
     image.value = temp_img.src;
     // document.forms[0].submit();
     // url需要改,change
     $.post("https://"+ip+":"+ port + "/FacePlay/identify_face", {'image_base64' : image.value},
      function(data, status){
          $('#change').html(data);
      })
    }
  },1200);
}

function take_photo(){
  canvas = document.getElementById("canvas");
  var temp_img = document.getElementById("temp_img");
  var image = document.getElementById("image");
  var upload = document.getElementById("upload");
  upload.style.display = "block";
  upload.style["background-color"] = "#12f519";
  upload.disabled = "disabled";
  upload.innerHTML = "照片正在生成中..."
  setTimeout(function(){
      temp_img.src = canvas.toDataURL('image/png');
      // image.value = canvas.toDataURL('image/png');
      // temp_img.src = image.value;
  var register = document.getElementById("register");
  // console.log(temp_img.complete);
  temp_img.onload = function(){
     image.value = temp_img.src;
    // console.log(temp_img.complete);
      upload.style["background-color"] = "#0cd06c";
      upload.innerHTML = "人脸取照成功！点击注册即可";
      register.disabled = "";
      register.innerHTML = "确认注册";
    }
  },2000); 
}

function change_login(){
  var div1=document.getElementById("login");  
  var div2=document.getElementById("facelogin");  
  if(div1.style.display=='block') div1.style.display='none';  
  else div1.style.display='block';  
  if(div2.style.display=='block') {
    div2.style.display='none';
    vidOff();
    }  
  else div2.style.display='block';  
}

// 上传图片
    function post_img(){
        document.forms[1].submit();
    }