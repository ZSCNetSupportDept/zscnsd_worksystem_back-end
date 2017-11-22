#coding = utf-8

from django.db import models
from django.contrib.auth.models import User


class Announcement(models.Model):
    """
    系统公告
    
    发布在系统首页的系统公告
    
    字段：
        notice_content（公告内容）：
            类型：models.CharField
            接受储存的类型：str
            最大长度：200
            默认值：‘none’
    """
    notice_content = models.CharField(max_length=200, default='none')

    def __str__(self):
        return self.notice_content


class Personal(models.Model):
    """
    个人信息
    
    用于扩展django认证系统的user的所记录的用户信息
    
    字段：
        user（django认证系统的用户实例）：
            类型：models.OneToOneField
            是否允许为空：是
            
        work_number（工号）：
            类型：models.CharField
            接受储存的类型：str
            最大长度：10
            默认值：0
            
        work_area（工作片区）：
            类型：models.CharField
            接受储存的类型：str
            最大长度：30
            是否允许为空；是
            
        week_day（值班日，关系到用户能否签到、能否对工作系统上的单子进行操作）：
            类型：models.IntegerField
            接受储存的类型：int
            [
                0=星期一
                1=星期二
                2=星期三
                3=星期四
                4=星期五
                5=星期六
                6=星期日
                7=每天（组长以上的成员拥有的权限）
            ]
            
        phone_number（成员的私人电话号码）：
            类型：models.CharField
            接受储存的类型：str
            默认值：911
            最大长度：20
            
        name（成员姓名）：
            类型：models.CharField
            接受储存的类型：str
            默认值：0
            最大长度：30
            
        work_phone（工作机）：
            类型：models.CharField
            接受储存的类型：str
            最大长度：20
    """
    user = models.OneToOneField(User, null=True)
    work_number = models.CharField(default=0, max_length=10)
    work_area = models.CharField(max_length=30, null=True)
    week_day = models.IntegerField(default=0)
    phone_number = models.CharField(default=911, max_length=20)
    name = models.CharField(default=0, max_length=30)
    work_phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Extra_Work(models.Model):
    """
    蹭班申请记录

    成员申请蹭班的记录
    
    字段：
        user（django认证系统的用户）：models.CharField
            类型：ForeignKey
            是否允许为空：是
        
        work_number（提交蹭班申请的成员的工号）：
            类型：Cmodels.harField
            接受储存的类型：str
            最大长度：10
            默认值：0
            
        extra_area（申请蹭班的片区）：
            类型：models.CharField
            接受储存的类型：str
            最大长度：20
            默认值：''
        
        status（通过情况，用于记录蹭班申请是否通过）：
            类型：models.IntegerField
            接受储存的类型：int
            默认值：0（待核审）
            [
                0=待核审
                1=批准
                2=拒绝
            ]
            
        add_time（添加蹭班申请的时间）：
            类型：models.DateTimeField
            接受储存的类型：datetime
            是否在记录创建时自动把该字段的值设为创建的时间：是
        
        extra_work_time（蹭班开始的时间）：
            类型：models.CharField
            接受储存的类型：str
            最大长度：30
            默认值：None（不是‘none’）
        
        refuse_reason（拒绝蹭班的理由）：
            类型：models.CharField
            接受储存的类型：str
            最大长度：200
            是否允许空字符：是
            是否允许为空：是
    """
    user = models.ForeignKey(User, null=True)
    work_number = models.CharField(max_length=10, default=0)
    extra_area = models.CharField(max_length=20, default='')
    status = models.IntegerField(default=0)
    add_time = models.DateTimeField(auto_now_add=True)
    extra_work_time = models.CharField(max_length=30, default=None)
    refuse_reason = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.work_number + str(self.add_time)


class Check_In(models.Model):
    """
    签到记录
    
    用于记录签到/签退的信息
    
    字段：
        user（django认证系统的用户实例）：
            类型：models.ForeignKey
            是否允许为空：是
        
        work_number（工号）：
            类型：models.CharField
            接受储存的类型：str
            默认值：0
            最大长度：10
        
        taken_toolkit（是否拿了工具包）：
            类型：models.BooleanField
            接受储存的类型：boolean
            默认值：True
            
        check（签到情况）：
            类型：models.IntegerFiedld
            接受储存的类型：int
            默认值：0
            [
                0=签到
                1=签退
           ]
            
        check_in_time（签到时间）：
            类型：models.DateTimeField
            接受储存的类型：datetime
            是否在当前记录被创建时自动把该字段的值设为创建的时间：是
            
        check_out_time（签退时间）：
            类型：models.DateTimeField
            接受储存的类型：datetime
            是否把当前记录状态被改变时的时间设为该字段的值：是
            
        check_in_area（签到片区）：
            类型：models.CharField
            接受储存的类型：str
            最大长度：20
            
        detailed_description（工具包备注）：
            类型：models.CharField
            接受储存的类型：str
            是否允许为null：是
            最大长度：200
        
        cable（网线）：
            类型：models.BooleanField
            接受储存的类型：boolean
            默认值：True
        
        crimping_Tool（网线钳）：
            类型：models.BooleanField
            接受储存的类型：boolean
            默认值：True
            
        switch（交换机）：
            类型：models.BooleanField
            接受储存的类型：boolean
            默认值：True
            
        crystal_Head（水晶头）：
            类型：models.BooleanField
            接受储存的类型：boolean
            默认值：True
            
        measuring_line（测线器）：
            类型：models.BooleanField
            接受储存的类型：boolean
            默认值：True
        
        port_module（端口模块）：
            类型：models.BooleanField
            接受储存的类型：boolean
            默认值：True
            
        key（机房钥匙）：
            类型：models.BooleanField
            接受储存的类型：boolean
            默认值：False
            
        scrwedriver（螺丝刀）：
            类型：models.BooleanField
            接受储存的类型：boolean
            默认值：True
        
        hunt（寻线器）：
            类型：models.BooleanField
            接受储存的类型：boolean
            默认值：False
    """
    user = models.ForeignKey(User, null=True)
    work_number = models.CharField(default=0, max_length=10)
    taken_toolkit = models.BooleanField(default=True)
    check = models.IntegerField(default=0)
    check_in_time = models.DateTimeField(auto_now_add=True)
    check_out_time = models.DateTimeField(auto_now=True)
    check_in_area = models.CharField(max_length=20)

    detailed_description = models.CharField(max_length=200, null=True)
    cable = models.BooleanField(default=True)
    crimping_Tool = models.BooleanField(default=True)
    switch = models.BooleanField(default=True)
    crystal_Head = models.BooleanField(default=True)
    measuring_line = models.BooleanField(default=True)
    port_module = models.BooleanField(default=True)
    key = models.BooleanField(default=False)
    screwdriver = models.BooleanField(default=True)
    hunt = models.BooleanField(default=False)

    def __str__(self):
        return self.work_number + str(self.check_in_time)


class Work_Situation(models.Model):
    """
    报修情况
    
    记录一个报修的处理情况
    
    字段：
        who_do（处理人）：
            类型：models.ManyToManyField
            
        add_time（报修增加的时间）：
            类型：models.DateTimeField
            接受储存的类型：datetime
            是否在记录被创建时自动把该字段的值设为创建的时间：是
        
        last_change_time（报修情况最后处理的时间）：
            类型：models.DateTimeField
            接受储存的类型：datetime
            是否在该记录被改变时自动更改该字段为个改变的时间：是
            
        work_area（报修所在的片区）：
            类型：models.CharField
            接受储存的类型：str
            最大长度：20
            
        account_number（报修的用户的宽带账号）：
            类型：models.CharField
            接受储存的类型：str
            最大长度：20
            是否允许为空：是
            
        telephone_number（报修用户的电话号码）：
            类型：models.CharField
            接受储存的类型：str
            最大长度：20
            
        dormitory_number（宿舍号）：
            类型：models.CharField
            接受储存的类型：str
            最大长度：20
        
        status（报修处理情况）：
            类型：models.IntegerField
            接受储存的类型型：int
            默认值：0
            [
                0=未解决
                1=已解决
                2=推迟
                3=上报
            ]
            
        introduction（故障描述）：
            类型：models.CharField
            接受储存的类型：str
            是否允许空白字符串：是
            默认值：None（不是‘none’）
            最大长度：200
            
        situation_order（工单性质）：
            类型：models.IntegerField
            接受储存的类型：int
            默认值：0
            [
                0=普通
                1=新装
                2=工单
                3=投诉
            ]
            
        operator（运营商）：
            类型：models.CharField
            接受储存的类型：str
            最大长度：200
            默认值：None（不是‘none’）
        

    """
    who_do = models.ManyToManyField(User)
    add_time = models.DateTimeField(auto_now_add=True)
    last_change_time = models.DateTimeField(auto_now=True)
    work_area = models.CharField(max_length=20)
    account_number = models.CharField(max_length=20, null=True)
    telephone_number = models.CharField(max_length=20)
    dormitory_number = models.CharField(max_length=20)
    status = models.IntegerField(default=0)
    introduction = models.CharField(blank=True, default=None, max_length=200)
    situation_order = models.IntegerField(default=0)
    operator = models.CharField(default=None, max_length=200, null=True)

    def __str__(self):
        return str(self.id)+'_' +self.work_area + str(self.add_time)


class Work_Order_Image(models.Model):
    """
    新装工单照片
    
    移动新装要求上传的三张照片，照片使用七牛云储存，目前用不上
    
    字段：
        work_order（照片对应的新装单）：
            类型：models.ForeignKey
            对应外键：Work_Situation
            
        to_id（对应的work_situation在数据库中的id）：
            类型：models.IntegerField
            接受类型：int
            默认值：0
            
        url（图片在七牛上的url）：
            类型：models.URLField
            接受类型：str
            最大长度：200
            
            
    """
    work_order = models.ForeignKey(Work_Situation)
    to_id = models.IntegerField(default=0)
    url = models.URLField(max_length=200)

    def __str__(self):
        return str(self.to_id)


class History(models.Model):
    """
    历史记录
    
    报修处理的历史记录
    
    字段：
        who（工作人员）：
            类型：models.ManyToManyField
            
        to_id（对应的work_situation在数据库中的id）：
            类型：models.IntegerField
            接受储存类型：int
            默认值：0
        
        time（操作时间）：
            类型：models.DateTimeField
            接受储存的类型：datetime
            是否在记录被创建时自动把该字段的值设为创建的时间：是
            
        record（操作记录）：
            类型：models.CharField
            接受储存的类型：str
            最大长度：400
            
        to_who（？）；
            类型：models.IntegerField
            接受储存的类型：int
            默认值：0
        
        who_do（工作人员？）：
            类型：models.CharField
            接受储存的类型：str
            最大长度：400
            是否允许为null：是
        
        name（工作人员姓名）：
            类型：mdoels.CharField
            接受储存的类型：str
            最大长度：20
            是否允许为null：是
            
        
    """
    who = models.ManyToManyField(User)
    to_id = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)
    record = models.CharField(max_length=400)
    to_who = models.IntegerField(default=0)
    who_do = models.CharField(max_length=400, null=True)
    name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return str(self.to_id) + '_' + self.name + '_' + str(self.time)


class Experience(models.Model):
    """
    维修经验
    
    记录成员分享的维修经验
    
    字段：
        name（成员姓名）：
            类型：models.CharField
            接受储存的类型：str
            最大长度：20
            
        who_do（成员工号）：
            类型：models.IntegerField
            接受储存的类新：int
            默认值：0
            
        time（分享经验的时间）：
            类型：models.DateTimeField
            接受储存的类型：datetime
            是否在记录被创建时自动把该字段的值设为创建的时间：是
            
        record（经验内容）：
            类型：models.CharField
            接受储存的类型：str
            最大长度：400
            
        title（经验标题）：
            类型：models.CharField
            接受储存的类型：str
            最大长度：20
            是否允许为null：是
            
    """
    name = models.CharField(max_length=20)
    who_do = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)
    record = models.CharField(max_length=400)
    title = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.title + '_' + self.name





'''
-----------------------------
2017/11/22
注释 by 咸猫 
-----------------------------
'''