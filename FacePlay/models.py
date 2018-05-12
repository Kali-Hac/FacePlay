from django.db import models

# Create your models here.

class Student(models.Model):
	s_id = models.CharField(max_length=12)
	s_name = models.CharField(max_length=10)
	s_pwd = models.CharField(max_length=30)
	s_tel = models.CharField(max_length=20)
	s_face = models.CharField(max_length=100, help_text="存放人脸图片的路径")

class Teacher(models.Model):
	t_id = models.CharField(max_length=12)
	t_name = models.CharField(max_length=10)
	t_tel = models.CharField(max_length=20)
	t_pwd = models.CharField(max_length=30)
	t_face = models.CharField(max_length=100)

class Course(models.Model):
	c_id = models.CharField(max_length=12)
	c_name = models.CharField(max_length=20)
	c_time = models.CharField(max_length=20)
	c_room = models.CharField(max_length=20)

class C_S(models.Model):
	c_id = models.ForeignKey("Course", on_delete=True)
	s_id = models.CharField(max_length=12)

class Photo(models.Model):
	cs_id = models.ForeignKey("C_S", on_delete=True)
	p_time = models.DateTimeField(auto_now=True)
	p_dir = models.CharField(max_length=100)
