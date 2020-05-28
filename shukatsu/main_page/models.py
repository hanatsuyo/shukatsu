from django.db import models
from django.contrib.auth.models import User




class Company(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
        )
    
    name = models.CharField(
        verbose_name='企業名',
        blank=True,
        null=True,
        max_length=100
        )

    mypage_id = models.CharField(
        verbose_name='マイページID',
        blank=True,
        null=True,
        max_length=100
        )

    mypage_pwd = models.CharField(
        verbose_name='マイページパスワード',
        blank=True,
        null=True,
        max_length=100
        )

    mypage_url = models.URLField(
        verbose_name='マイページURL',
        blank=True,
        null=True
        )
    
    progress = models.CharField(
        verbose_name="選考状況",
        blank=True,
        null=True,
        max_length=100
        )
   
    next_date = models.DateField(
        verbose_name='次回選考日程',
        blank=True,
        null=True,
    )  
    
    next_time = models.TimeField(
        verbose_name='選考時間',
        blank=True,
        null=True,
    )




    

    def __str__(self):
        return self.name,self.mypage_id,self.mypage_pwd,self.mypage_url,self.progress,self.next_datetime


