var port = '8667';
var ip = 'localhost';
function submit()
{
	document.forms[0].submit();
	// console.log(exampleInputEmail1.value,exampleInputPassword1.value);
	 // url需要改,change，192.168.188.105
	 // var exampleInputEmail1 = document.getElementById('exampleInputEmail1');
	 // var exampleInputPassword1 = document.getElementById('exampleInputPassword1');
	 // console.log( exampleInputEmail1.value);
	 // console.log(exampleInputPassword1.value);
	 // $.post("https://"+ip+":"+ port + "/FacePlay/login_check", {'lg_id':exampleInputEmail1.value, 'lg_pwd':exampleInputPassword1.value},
  //     function(data, status){
  //         // $('#msg').html(data);
  //         // 'lg_id' : exampleInputEmail1.value,
	 // 	// 'lg_pwd': exampleInputPassword1.value
  //     })
}

function charts()
{
	$.post("https://"+ip+":"+ port + "/FacePlay/charts", {},
            function(data, status){
              $('#change').html(data);
       })
}

function record()
{
	$.post("https://"+ip+":"+ port + "/FacePlay/record", {},
            function(data, status){
              $('#change').html(data);
       })
}

function read_record()
{
	$.post("https://"+ip+":"+ port + "/FacePlay/read_record", {},
            function(data, status){
              $('#change').html(data);
       })
}

function send_message()
{
	$.post("https://"+ip+":"+ port + "/FacePlay/send_message", {},
            function(data, status){
              $('#change').html(data);
       })
}

function message()
{
	$.post("https://"+ip+":"+ port + "/FacePlay/message", {},
            function(data, status){
              $('#change').html(data);
       })
}
function confirm(option){
	if(option == 1)
		alert("成功受理申诉！学生将从缺课列表中删除");
	else
		alert("成功拒绝申诉！");
	var option = document.getElementById('option');
	option.style.display="none";
}

function send_image()
{
	$.post("https://"+ip+":"+ port + "/FacePlay/send_image", {},
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
	$.post("https://"+ip+":"+ port + "/FacePlay/upload_image", {'t_image': src},
            function(data, status){
              $('#change').html(data);
       })
}

function send_teacher()
{	
	var img = document.getElementById('previewer');
	var msg = document.getElementById('msg');
	var input = document.getElementById("filechooser");
	if(img.src === ''){
		alert("请上传申诉的图片！");
		return;
	}
	// console.log(src);
	// $.post("https://localhost:"+ port + "/FacePlay/send_teacher", {'t_image': src, 't_msg': msg},
 //            function(data, status){
             
 //       })
 alert("提交申诉成功！");
 img.src = '';
 msg.value = '';
 input.value='';

}

function confirm_info(cnt){
	alert('确认并成功提交缺课情况！');
	var state = 'state_' + cnt.toString();
	var s = document.getElementById(state);
	s.style.display = "none";
}

function clean_info()
{
	 $.post("https://"+ip+":"+ port + "/FacePlay/logout", {},
      function(data, status){
          // $('#change').html(data);
      })
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
 