var port = '8778';

function submit()
{
	// document.forms[0].submit();
	// console.log(exampleInputEmail1.value,exampleInputPassword1.value);
	 // url需要改,change，192.168.188.105
	 $.post("https://localhost:"+ port + "/FacePlay/login_check", {'lg_id' : exampleInputEmail1.value,
	 	'lg_pwd': exampleInputPassword1.value},
      function(data, status){
          $('#msg').html(data);
      })
}

function charts()
{
	$.post("https://localhost:"+ port + "/FacePlay/charts", {},
            function(data, status){
              $('#change').html(data);
       })
}

function record()
{
	$.post("https://localhost:"+ port + "/FacePlay/record", {},
            function(data, status){
              $('#change').html(data);
       })
}

function read_record()
{
	$.post("https://localhost:"+ port + "/FacePlay/read_record", {},
            function(data, status){
              $('#change').html(data);
       })
}

function send_message()
{
	$.post("https://localhost:"+ port + "/FacePlay/send_message", {},
            function(data, status){
              $('#change').html(data);
       })
}

function send_image()
{
	$.post("https://localhost:"+ port + "/FacePlay/send_image", {},
            function(data, status){
              $('#change').html(data);
       })
}

function upload_image()
{	
	var src = document.getElementById('previewer').src;
	if(src === ''){
		alert("请在图片完全上传后再确认进行识别！");
		return;
	}
	// console.log(src);
	$.post("https://localhost:"+ port + "/FacePlay/upload_image", {'t_image': src},
            function(data, status){
              $('#change').html(data);
       })
}

function clean_info()
{
	 // $.post("http://localhost:8080/FacePlay/logout", {'image_base64' : image.value},
  //     function(data, status){
  //         $('#change').html(data);
  //     })
}
 // // 点击按钮，浏览本地图片
 //    function openBrows(){
 //        var ie = navigator.appName == "Microsoft Internet Explorer" ? true:false;
 //        if(ie){
 //            document.getElementById("file").click();
 //            document.getElementById("filename").value = document.getElementById("file").value;
 //        } else {
 //            var a = document.createEvent("MouseEvents");
 //            a.initEvent("click",true,true);
 //            document.getElementById("file").dispatchEvent(a);
 //        }
 //    }

 //    // 提交表单
 //    function saveFile(){
 //        document.getElementById("arryForm").submit();
 //    }

 //    jQuery(function(){
 //        faceDo();
 //    });

 //    function faceDo(){
 //        var msg = jQuery("#path").attr("src");
 //        jQuery.ajax({
 //            type:"post",
 //            url:"/",
 //            data:{"path":msg},
 //            success:function(data){
 //                jQuery("#p_message").prepend(data);
 //                jQuery(".bs").removeClass().empty();
 //            }

 //        });

 //    }
 