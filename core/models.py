from email.policy import default
from django.db import models
from django.conf import settings
from datetime import datetime


v = datetime.today().strftime('%Y-%m-%d')

class Tag(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    author = models.ForeignKey(
    settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now_add=True)
    country = models.TextField(default='country')
    province = models.TextField(default='province')
    place = models.TextField(default='place')
    school = models.TextField(default='school')
    grade = models.TextField(default='school')
    attendance = models.TextField(default='False')
    sub = models.TextField(default='sub')
    topic = models.TextField(default='topic')
    username = models.TextField(default='username')


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    image = models.ImageField(upload_to='pop',blank=True, null=True)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    numbers = models.IntegerField(default=0)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {}'.format(self.name)

class invites(models.Model):
    user_mail = models.TextField(default ='N/A')
    inviter_mail = models.EmailField(max_length=100)

from django.contrib.auth.models import User


class code(models.Model):
    email = models.EmailField(max_length=100)
    code = models.TextField(default='N/A')

class details(models.Model):
    email = models.EmailField(max_length=100)
    visit = models.ImageField(default='N/A')

class worker(models.Model):
    email = models.EmailField(max_length=100)
    true_fasle = models.TextField(default='F')


class paycheck(models.Model):
    reciver = models.TextField(default='N/A')
    money = models.TextField(default='0.0')
    true_fasle = models.TextField(default='F')


class place(models.Model):
    country = models.TextField(default='country')
    province = models.TextField(default='province')
    place = models.TextField(default='place')
    school = models.TextField(default='school')
    grade = models.TextField(default='grade')
    email = models.IntegerField(default=0)

class others(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    author = models.IntegerField(default=0)
    content = models.TextField()
    image = models.ImageField(upload_to='', blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now_add=True)
    id2 = models.IntegerField(default=0)
    sub = models.TextField(default='sub')
    topic = models.TextField(default='topic')
   # ctime = models.DateTimeField(auto_now_add=True, default=datetime.now())
    #uptime = models.DateTimeField(auto_now=True, default=datetime.now())   
class validate(models.Model):
    com = models.IntegerField(default=0)

class camp(models.Model):
    level = models.TextField(default="text")
    subject = models.TextField(default="text")
    votes = models.IntegerField(default=0)
    grade = models.TextField(default="text")
    description = models.TextField(default="des")
    language = models.TextField(default="en")
    author = models.TextField(default="author")
    code = models.TextField(default="code")
    
class usercamp(models.Model):
    camp_id = models.IntegerField(default=0)
    email = models.TextField(default="email")
    level = models.TextField(default="text")
    subject = models.TextField(default="text")
    votes = models.IntegerField(default=0)
    grade = models.TextField(default="text")
    description = models.TextField(default="des")
    language = models.TextField(default="en")
    author = models.TextField(default="author")
    
class campvedios(models.Model):
    vedio = models.FileField(upload_to='', blank=True, null=True)
    camp_id = models.IntegerField(default=0)

class comemnts_camp(models.Model):
    content = models.TextField(default="text")
    camp_id = models.IntegerField(default=0)

    
    
    
    
    
    
    

    
    