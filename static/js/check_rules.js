function check()
{
	with(document.all){
		 if(exampleInputName.value==""||exampleInputEmail1.value==""||exampleInputPassword1.value==""){
		 	alert("请填写所有信息！");
		 	return;
		 }
		 // if(exampleInputEmail1.value.indexOf("@")==-1){
		 // 	alert("请输入正确的邮箱！");
		 // 	exampleInputEmail1.value="";
		 // 	return;
		 // }
		 if(exampleInputPassword1.value==='' || exampleInputPassword1.value!=exampleConfirmPassword.value)
		 {
		 	alert("两次密码输入不一致！");
		 	exampleInputPassword1.value = "";
		 	exampleConfirmPassword.value = "";
		 	return;
		 }
		if(open_camera.innerHTML==="请先完善个人信息并确认"){
			// form.action="register";
			// form.method="POST";
			open_camera.innerHTML="点此拍摄人脸";
			register.disabled = "disabled";
			register.innerHTML = "请进行人脸拍摄再注册"
			alert("请进行人脸取照并上传!");
		}
		else{
			if(exampleInputName.value==""||exampleInputEmail1.value==""||exampleInputPassword1.value==""){
		 	alert("请填写所有信息！");
		 	return;
		 }
		 // if(exampleInputEmail1.value.indexOf("@")==-1){
		 // 	alert("请输入正确的邮箱！");
		 // 	exampleInputEmail1.value="";
		 // 	return;
		 // }
		 if(exampleInputPassword1.value==='' || exampleInputPassword1.value!=exampleConfirmPassword.value)
		 {
		 	alert("两次密码输入不一致！");
		 	exampleInputPassword1.value = "";
		 	exampleConfirmPassword.value = "";
		 	return;
		 }
		if(upload_img.value == ""){
			alert("请进行人脸拍摄取照！否则无法进行人脸登录");
			return;
		}
			final_summit();
		}
	}
}
function final_summit(){
	document.forms[0].submit();
}