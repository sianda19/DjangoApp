import email
#from urllib import request
from django.dispatch import receiver
from django.forms import MultiValueField
#import requests
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from numpy import common_type
from .models import Post, Comment
from .forms import CommentForm
from django.shortcuts import render,redirect
from django.contrib.postgres.search import SearchVector, SearchQuery
from django.contrib.auth import get_user_model
User = get_user_model()

print(User)




def test(request):
     if request.method == 'POST':
       tk = request.POST['content']
     return render(request,'core/add.html',{'object_lists': tk})

def action(request):
 print('cdcdc')
 return render(request, 'core/search.html')

def Email(request):
    current_url = request.resolver_match.url_name
    print(current_url)
    return render(request,'core/email.html')

from .models import camp
from .models import usercamp

'''  def mine(request):
    mine = usercamp.objects.filter(email=request.user.email)
    list = []
    for i in mine:
        #print(i.camp_id)
     query = camp.objects.filter(id=i.camp_id)
     print(query)
     
    #for n in list:
      #  query = n
       # print(query)
        
   # camps = camp.objects.all()
     
    paginator = Paginator(mine, 49) 
    page = request.GET.get('page',1)
    try:
       post_list = paginator.page(page)
    except PageNotAnInteger:
         post_list = paginator.page(1)
    except EmptyPage:
         post_list = paginator.page(paginator.num_pages)
  #  try:
    current = request.user.id
    user = User.objects.get(pk=current)
    bell = user.notifications.unread()
    post_query = Post.objects.filter(author_id=current)

    count = 0
    for post in post_query:
       if Comment.objects.filter(post_id=post.id).count() > 1:
         if post.attendance == 'False':
                count+=1
        #print(count)
    return render(request,
                  'core/mine.html',
                  {'page': page,
                   'object_list': post_list,'bell':bell,'count':count})

def vote(request,id):
    num = camp.objects.get(id=id)
    vote = num.votes
    new = vote + 1
    print(new)
    num.votes = new
    num.save()
    detail = camp.objects.get(id=id)
    usercam = usercamp(camp_id=id,email=request.user.email,level=detail.level,subject=detail.subject,description=detail.description,grade=detail.grade,language=detail.language,author=detail.author,votes=detail.votes)
    usercam.save()
    return redirect("core:camps")

def classes(request,id):
    video = campvedios.objects.filter(camp_id=id)
    return render(request,"core/classes.html",{'vido':video})

def camps(request):
    post_count = Post.objects.all().count()
    comment = Comment.objects.all().count()
    if request.method == "POST":
        sub = request.POST['sub']
        level = request.POST['lev']
        des = request.POST['des']
        grae = request.POST['grade']
        lan = request.POST['lan']
        import uuid
        result = uuid.uuid4()
        uuid_string = str(result)
        print(uuid_string)
        cam = camp(level=level,subject=sub,description=des,grade=grae,language=lan,author=request.user.username,code=uuid_string)
        cam.save()
        return redirect("core:camps")
    else:
     camps = camp.objects.all()
     paginator = Paginator(camps, 49) 
     page = request.GET.get('page',1)
     try:
      post_list = paginator.page(page)
     except PageNotAnInteger:
         post_list = paginator.page(1)
     except EmptyPage:
         post_list = paginator.page(paginator.num_pages)
     current = request.user.id
     user = User.objects.get(pk=current)
     bell = user.notifications.unread()
     post_query = Post.objects.filter(author_id=current)
     count = 0
     for post in post_query:
        if Comment.objects.filter(post_id=post.id).count() > 1:
            if post.attendance == 'False':
                count+=1
     return render(request,
                  'core/camps.html',
                  {'page': page,
                   'object_list': post_list,'bell':bell,'count':count,'P':post_count,'C':comment})    
   '''
#class profile(CreateView):
def profile(request,username):
   # username = self.kwargs["username"]
    print(username)
    user = User.objects.get(username=username)
   # print(user.id)filter(author_id=user.id)
    #print(username)
    query = Post.objects.filter(author_id=user.id)
    query_count = Post.objects.filter(author_id=user.id).count()
    _count = Post.objects.filter(author_id=user.id).filter(attendance="False").count()
    #print(_count)


    print(query)
    current_user = request.user.id
    user = request.user
   # queryset = Post.objects.filter(author_id=query)
    paginator = Paginator(query, 49) 
    page = request.GET.get('page',1)
    try:
     post_list = paginator.page(page)
    except PageNotAnInteger:
         post_list = paginator.page(1)
    except EmptyPage:
         post_list = paginator.page(paginator.num_pages)
  #  try:
    user = User.objects.get(pk=current_user)
    bell = user.notifications.unread()
    post_query = Post.objects.filter(author_id=current_user)

    count = 0
    for post in post_query:
        if Comment.objects.filter(post_id=post.id).count() > 1:
            if post.attendance == 'False':
                count+=1
        #print(count)
         
    return render(request,
                  'core/userproc.html',
                  {'page': page,
                   'object_list': post_list,'bell':bell,'count':count,'username':username,'countit':query_count,'at':_count})
  #  return render(request,'core/userproc.html',{'object_lists':query})
  
def search12(request):
    if request.method == "POST":
        sub = request.POST['sub']
        level = request.POST['lev']
        des = request.POST['des']
        grae = request.POST['grade']
        lan = request.POST['lan']
        print(lan)
        queryset = camp.objects.annotate(search=SearchVector("level","subject","language","grade","description")).filter(search=SearchQuery(level)).filter(search=SearchQuery(sub)).filter(search=SearchQuery(lan)).filter(search=SearchQuery(grae)).filter(search=SearchQuery(des))
        print(queryset)
        paginator = Paginator(queryset, 49) 
        page = request.GET.get('page',1)
        try:
         post_list = paginator.page(page)
        except PageNotAnInteger:
         post_list = paginator.page(1)
        except EmptyPage:
         post_list = paginator.page(paginator.num_pages)
        post_count = Post.objects.all().count()
        comment = Comment.objects.all().count()
        current = request.user.id
        user = User.objects.get(pk=current)
        bell = user.notifications.unread()
        post_query = Post.objects.filter(author_id=current)
        count = 0
        for post in post_query:
         if Comment.objects.filter(post_id=post.id).count() > 1:
            if post.attendance == 'False':
                count+=1
        #print(count),"grade", "subject","description","language"  .filter(search=SearchQuery(des)).filter(search=SearchQuery(sub)).filter(search=SearchQuery(lan)).filter(search=SearchQuery(grae))
        return render(request,
                  'core/camps.html',
                  {'page': page,
                   'object_list': post_list,'bell':bell,'count':count,'P':post_count,'C':comment}) 
        
def searchA(request):
    pass

def search(request):
   try:
    if request.method == 'POST':
        tk = request.POST['ccc']    
        seen = request.POST['myselect']   
        sub = request.POST['sub']   
        grade = request.POST['grade']   
        print(seen)
       # paginator = Paginator(comment_list, 45)  
        queryset = Post.objects.annotate(search=SearchVector("title", "content","sub","topic")).filter(search=SearchQuery(tk)).filter(search=SearchQuery(sub)).filter(search=SearchQuery(grade))
        print(queryset)
        lists = []
        for query in queryset:
            count = Comment.objects.filter(post=query).count()
            if seen == 'no':
             if count < 2:
                lists.append(query)
            elif seen == 'yes':
             if count > 2:
                lists.append(query)
     #   paginator = Paginator(queryset, 45)     .filter(search=SearchQuery(tk))     #pag = Paginator(my, 45)  
       # paginator = Paginator(comment_list, 45)  
       # print(paginator)
        post_count = Post.objects.all().count()
        comment = Comment.objects.all().count()
        lists
        paginator = Paginator(lists, 600)  
        page = request.GET.get('page',1)
        try:
         post_list = paginator.page(page)
        except PageNotAnInteger:
         post_list = paginator.page(1)
        except EmptyPage:
         post_list = paginator.page(paginator.num_pages)
        
        curr = request.user.id
        user = User.objects.get(pk=curr)
        bell = user.notifications.unread()
        be = user.notifications.unread()
        int = user.notifications.unread()
        post_query = Post.objects.filter(author_id=curr)
        count = 0
        for post in post_query:
         if Comment.objects.filter(post_id=post.id).count() > 1:
            if post.attendance == 'False':
                count+=1
      
        return render(request,'core/home.html',{'object_list': post_list,'bell':bell,'li':be,'count':count,'P':post_count,'C':comment })
   except:
      return render(request,'core/home.html',{'object_list': post_list})

from collections import Counter
import ast

def sug(request):
    get_post = Post.objects.filter(attendance='False')
    list = []
    sub = []
    for post in get_post:
        list.append(post.title)
        c = Counter(list)
        sub.append(post.sub)
        s = Counter(sub)

    for keys in dict(s):
     s[keys] = "{:,}".format(s[keys])
    subject = dict(s)
    print(dict(subject))
    for keys in dict(c):
     c[keys] = "{:,}".format(c[keys])
    grade = dict(c)

    current = request.user.id
    user = User.objects.get(pk=current)
    bell = user.notifications.unread()
    return render(request,'core/sug.html',{'subject':subject,'grade':grade,'bell':bell})

def run(request):
 if request.method == 'POST':
   pas = request.POST['pass']
   print(pas)
   if pas == '123456kitu':
    pay = paycheck.objects.all()
    fasle = paycheck.objects.all()
    for f in fasle:
     f.true_fasle = 'F'
     f.save()
    for m in pay:
     m.money = '0.0'
     m.save()
 return redirect("core:admin")

def reco_search(request):
     if request.method == 'POST':
        tk = request.POST['ccc']     
        sub = request.POST['sub']   
        grade = request.POST['grade']   
        queryset = others.objects.annotate(search=SearchVector("title", "content","sub","topic")).filter(search=SearchQuery(tk)).filter(search=SearchQuery(sub)).filter(search=SearchQuery(grade))
        print(queryset)
        paginator = Paginator(queryset, 500)  
        page = request.GET.get('page')
        try:
         post_list = paginator.page(page)
        except PageNotAnInteger:
         post_list = paginator.page(1)
        except EmptyPage:
         post_list = paginator.page(paginator.num_pages)
        
        curr = request.user.id
        user = User.objects.get(pk=curr)
        bell = user.notifications.unread()
        be = user.notifications.unread()
        int = user.notifications.unread()

        post_query = Post.objects.filter(author_id=curr)

        count = 0
        for post in post_query:
         if Comment.objects.filter(post_id=post.id).count() > 1:
            if post.attendance == 'False':
                count+=1
        #print(count)

        return render(request,
                  'core/recomendation.html',
                  {'page': page,
                   'reco': post_list,'bell':bell,'li':be,'count':count})

from .models import invites
from .models import code 
from .models import campvedios
from .models import comemnts_camp

def com(request,str):
    
    if request.method == "POST":
        content = request.POST['txt']
        id = camp.objects.filter(code=str)
        for i in id:
            idz = i.id
            break
        save_comment = comemnts_camp(content=content,camp_id=idz)
        save_comment.save()
        campz = camp.objects.filter(code=str)
        for ids in campz:
         videos = campvedios.objects.filter(camp_id=ids.id)
        comments = comemnts_camp.objects.all()
        # print(videos)
        return render(request,'core/privi.html',{'vido':videos,'com':comments})
    
def com2(request,str):
    
    if request.method == "POST":
        content = request.POST['txt']
        id = camp.objects.filter(id=str)
        for i in id:
            idz = i.id
            break
        save_comment = comemnts_camp(content=content,camp_id=idz)
        save_comment.save()
        campz = camp.objects.filter(id=str)
        for ids in campz:
         videos = campvedios.objects.filter(camp_id=ids.id)
        comments = comemnts_camp.objects.all()
        # print(videos)
        return render(request,'core/privi.html',{'vido':videos,'com':comments})
    
    
def videos(request,str):
    if request.method =="POST":
        id = camp.objects.filter(code=str)
        for i in id:
            idz = i.id
            break
        video = request.FILES['filename']
        save_video = campvedios(vedio=video,camp_id=idz)
        save_video.save()
        comments = comemnts_camp.objects.all()
        return render(request,'core/privi.html')
        
def tutor(request,code):
    campz = camp.objects.filter(code=code)
    for ids in campz:
     videos = campvedios.objects.filter(camp_id=ids.id)
     print(videos)
    comments = comemnts_camp.objects.all()
    return render(request,'core/privi.html',{'vido':videos,'com':comments})
    
def main_view():
    pass
      
def save_code(request):
  try:
    current = request.user.email
    id = request.user.id
    if code.objects.filter(email=current).exists():
       queryset = code.objects.get(email=current)
       print(queryset)
       curr = request.user.id
       user = User.objects.get(pk=curr)
       bell = user.notifications.unread()
        
       return render(request,'users/ref.html',{'code':queryset,'bell':bell})
    else:     
     import uuid
     result = uuid.uuid4()
     uuid_string = str(result)
     if code.objects.filter(code=uuid_string).exists():
       cd = str(uuid.uuid4())
     else:
        cd = uuid_string
     current = request.user.email
     save = code(email=current,code=cd)
     save.save()
    current2 = request.user.email
    if invites.objects.filter(user_mail=current2).exists():
        print('jjj')
    else:
     try:
        save2 = invites(user_mail=current2,inviter_mail=main_view.main)
        save3 = invites(user_mail='thandokhulu12345@gmail.com',inviter_mail=main_view.main)
        save4 = invites(user_mail='rorisangmasthole@gmail.com',inviter_mail=main_view.main)
        print('hghrbs')
        save2.save()
        save3.save()
        save4.save()
     except AttributeError:
         pass
    queryset = code.objects.get(email=current)
    return render(request,'users/ref.html',{'code':queryset,'bell':bell})
  except:
       queryset = Post.objects.all()
       return render(request,'core/home.html',{'object_list':queryset})

def sow(request):
    return render(request, 'core/email.html')

def date(request):
  if request.method == 'POST':
    tk = request.POST['ccc']     
    seen = request.POST['myselect'] 
    sub = request.POST['sub']   
    grade = request.POST['grade'] 
    print(seen)
    current = request.user.id
    queryset = Post.objects.annotate(search=SearchVector("title", "content","sub","topic")).filter(search=SearchQuery(tk)).filter(author_id=current).filter(search=SearchQuery(sub)).filter(search=SearchQuery(grade))
    print(queryset)
    lists = []
    for query in queryset:
        count = Comment.objects.filter(post=query).count()
        if seen == 'no':
            if count < 1:
             lists.append(query)
        elif seen == 'yes':
            if count > 1:
              lists.append(query)
    lists
    paginator = Paginator(lists, 300)  
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
        
    curr = request.user.id
    user = User.objects.get(pk=curr)
    bell = user.notifications.unread()
    be = user.notifications.unread()
    int = user.notifications.unread()

    post_query = Post.objects.filter(author_id=curr)

    count = 0
    for post in post_query:
        if Comment.objects.filter(post_id=post.id).count() > 1:
            if post.attendance == 'False':
                count+=1
        #print(count)
    post_count = Post.objects.filter(author_id=curr).count()
    post_count_2 = Post.objects.all().count()
    comment = Comment.objects.all().count()
    return render(request,
                  'core/user.html',
                  {'page': page,'P':post_count_2,'C':comment,
                   'object_list': post_list,'user_count':post_count,'bell':bell,'li':be,'count':count})
  #except ValueError:
         #    return render(request,
               #   'core/home.html'
                #  )
   # curr = request.user.id
    #if request.method == 'POST':
    #    tk = request.POST['ccc']   
    #    seen = request.POST['ccc']        
    #    queryset = Post.objects.annotate(search=SearchVector("title", "content")).filter(search=SearchQuery(tk)).filter(author_id=curr)
   # return render(request,'core/mypost.html', {'object_list': queryset} )

from notifications.signals import notify

def cash(request,string):
    current_user = request.user.email
    if invites.objects.filter(inviter_mail=request.user.email).exists():
       count = invites.objects.filter(inviter_mail=request.user.email).count()
    else:
        count = 0
    if worker.objects.filter(email=request.user.email).exists():
        true_f = paycheck.objects.get(reciver=request.user.email)
        num = int(true_f.money[0])
        if num > 2:
         true_f.true_fasle = 'T'
         true_f.save()
         messages.success(request, 'Check your email in few minutes.')
         wages = paycheck.objects.get(reciver=current_user)
         pass_wages = wages.money
         money = float(pass_wages)
         two = round(money,3)
         return render(request,'users/profile.html',{'wage':two,'invites':count})
        else:
         wages = paycheck.objects.get(reciver=current_user)
         pass_wages = wages.money
         money = float(pass_wages)
         two = round(money,3)
         messages.success(request, 'Your money is less than minimum.')
         return render(request,'users/profile.html',{'wage':two,'invites':count})
    else:
       # wages = paycheck.objects.get(reciver=current_user)
       # pass_wages = wages.money
       # money = float(pass_wages)/16
        two = 0.0
     #   messages.success(request, 'Your money is less than $2.')
        messages.success(request, 'You are not registered as a worker.')
        return render(request,'users/profile.html',{'wage':two,'invites':count})

def terms(request):
    return render(request,'core/term.html')

def sample(request):
    current_user = request.user.id
    user = request.user
    post_count = Post.objects.all().count()
    comment = Comment.objects.all().count()
    queryset = Post.objects.filter(author_id=current_user)
    user_set = Post.objects.filter(author_id=current_user).count()

    paginator = Paginator(queryset, 40) 
    page = request.GET.get('page')
    try:
     post_list = paginator.page(page)
    except PageNotAnInteger:
         post_list = paginator.page(1)
    except EmptyPage:
         post_list = paginator.page(paginator.num_pages)
    try:
     user = User.objects.get(pk=current_user)
     bell = user.notifications.unread()

     post_query = Post.objects.filter(author_id=current_user)

     count = 0
     for post in post_query:
        if Comment.objects.filter(post_id=post.id).count() > 1:
            if post.attendance == 'False':
                count+=1
        #print(count)
         
     return render(request,
                  'core/user.html',
                  {'page': page,
                   'object_list': post_list,'bell':bell,'count':count,'user_count':user_set,'P':post_count,'C':comment })
    except:
     #   return redirect('core:home')
      return render(request,
                  'core/user.html',
                  {'page': page,
                   'object_list': post_list,'user_count':user_set,'P':post_count,'C':comment })
       
from .models import paycheck
from django.core.paginator import Paginator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
class HomeView(ListView):
    def get(self,request):
        #------------------------------------------------------------------
        curr = self.request.user.id
        queryset = Post.objects.all()
        post_count = Post.objects.all().count()
        comment = Comment.objects.all().count()
        comment_list = []
        for i in queryset:
         comment_count = Comment.objects.filter(post_id=i.id).count()
         comment_list.append(comment_count)
        my_list = comment_list
       # lists = []
      #  for query in queryset:
       #     count = Comment.objects.filter(post=query).count()
       # my = lists.append(count)
        paginator = Paginator(queryset, 45)  
        pag = Paginator(my_list, 45)  
        #pag = Paginator(my, 45)  
       # paginator = Paginator(comment_list, 45)  
       # print(paginator)
        page = request.GET.get('page')
        try:
         post_list = paginator.page(page)
        # post = pag.page(page)
        except PageNotAnInteger:
         post_list = paginator.page(1)
        # post = pag.page(1)
        except EmptyPage:
         post_list = paginator.page(paginator.num_pages)
        # post = pag.page(pag.num_pages)
        try:
         user = User.objects.get(pk=curr)
         bell = user.notifications.unread().count()
         notif = bell = user.notifications.unread()

         post_query = Post.objects.filter(author_id=curr)

         count = 0
         for post in post_query:
             if Comment.objects.filter(post_id=post.id).count() > 1:
                 if post.attendance == 'False':
                     print(post)
                     count+=1
         print(count)
            
         return render(request,
                  'core/home.html',
                  {'page': page,
                   'object_list': post_list,'bell':bell,'li':notif,'count':count,'P':post_count,'C':comment})
        except:
           return render(request,
                  'core/home.html',
                  {'page': page,'P':post_count,'C':comment ,'object_list': post_list})

from django.contrib import messages
from .models import validate

import cv2
import datetime

y = '01'
print(int(y) * 0.1)


def sat(request,ints,str1,int2,com):
        try:
         co = Comment.objects.get(id=com)
         f = str(co.image)
         f1 = f[f.find(".")+1:].split()[0]
         if f1 == 'mp4':
          data = cv2.VideoCapture(f'media\{f}')
          frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
          fps = int(data.get(cv2.CAP_PROP_FPS))
          seconds = int(frames / fps)
          video_time = str(datetime.timedelta(seconds=seconds))
          if video_time[0] == '0':
            i = int(video_time[2:4]) * 3
           #print(video_time[2:4])
          # print(i)
          else:
             mul = int(video_time[0])
             mul2 = int(video_time[2:4])
             i = (mul * 60 + mul2) * 3
 
        except:
            i = ints
            
       # print(co.image)
        get_post = Post.objects.get(id=int2)
        grade = get_post.slug
        print(grade)

        if validate.objects.filter(com=com).exists():
            messages.success(request, 'Solution already approved.')
            return redirect(f'http://127.0.0.1:8000/post/{int2}/{grade}')
           #return redirect('http://127.0.0.1:8000/')
            #return redirect('http://127.0.0.1:8000/')
        else:
            update= Post.objects.get(id=int2)
            update.attendance = 'True'
            update.save()
            get_post = Post.objects.get(id=int2)
            grade = get_post.slug
            if (grade == 'grade4' or grade == 'grade5' or grade == 'grade6'):
                rate = 0.001
            elif (grade == 'grade7' or grade == 'grade8' or grade == 'grade9'):
                rate = 0.004
            elif (grade == 'grade10' or grade == 'grade11' or grade == 'grade12'):
                rate = 0.005
            else:
                rate = 0.006
            sa = validate(com=com)
            sa.save()
            email=User.objects.get(username=str1)
            if worker.objects.filter(email=email).exists():
               # add_to_money = i * rate
                add_to_money = 0.06
                pay = paycheck.objects.get(reciver=email)
                prev_money = pay.money
                new_money = float(prev_money) + add_to_money
                print(new_money)
                string_form = round(new_money,3)
                pay.money = str(string_form)
                pay.save()
            else:
                   pass
            messages.success(request, 'Solution approved.')
            return redirect(f'http://127.0.0.1:8000/post/{int2}/{grade}')
            #return redirect('http://127.0.0.1:8000/')


def category2(request,username):
   try:
    post_count = Post.objects.all().count()
    comment = Comment.objects.all().count()
    curr1 = request.user.id
    query = Post.objects.filter(sub=username)
    curr = request.user.id
    paginator = Paginator(query, 45) 
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    user = User.objects.get(pk=curr)
    bell = user.notifications.unread()
    post_query = Post.objects.filter(author_id=curr)

    count = 0
    for post in post_query:
        if Comment.objects.filter(post_id=post.id).count() > 1:
            if post.attendance == 'False':
             count+=1

    return render(request,
                  'core/home.html',
                  {'page': page,
                   'object_list': post_list,'bell':bell,'count':count,'P':post_count,'C':comment })
   except:
       return render(request,
                  'core/home.html',
                  {'page': page,
                   'object_list': post_list,})
       
def category(request,username):
    curr1 = request.user.id
    post_count = Post.objects.all().count()
    comment = Comment.objects.all().count()
    query = Post.objects.filter(sub=username).filter(author_id=curr1)
    curr = request.user.id
    paginator = Paginator(query, 45) 
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    user = User.objects.get(pk=curr)
    bell = user.notifications.unread()
    post_query = Post.objects.filter(author_id=curr)

    count = 0
    for post in post_query:
        if Comment.objects.filter(post_id=post.id).count() > 1:
            if post.attendance == 'False':
             count+=1

    return render(request,
                  'core/user.html',
                  {'page': page,
                   'object_list': post_list,'bell':bell,'count':count,'P':post_count,'C':comment })
    
    
class View(ListView):
    template_name = 'core/add.html'
    def post(self, request, *args, **kwargs):
     if request.method == 'POST':
        tk = request.POST['content']
        return render(request,'core/add.html',{'object_lists': tk})
    queryset = Post.objects.filter(author_id=0)

class viewView(ListView):
    def get(self,request):
        curr = self.request.user.id
        post_count = Post.objects.all().count()
        comment = Comment.objects.all().count()
        queryset = Post.objects.all()
        paginator = Paginator(queryset, 45) 
        page = request.GET.get('page')
        try:
         post_list = paginator.page(page)
        except PageNotAnInteger:
         post_list = paginator.page(1)
        except EmptyPage:
         post_list = paginator.page(paginator.num_pages)
        try:
         user = User.objects.get(pk=curr)
         bell = user.notifications.unread()
         post_query = Post.objects.filter(author_id=curr)

         count = 0
         for post in post_query:
             if Comment.objects.filter(post_id=post.id).count() > 1:
                 if post.attendance == 'False':
                     count+=1
        # print(count)

         return render(request,
                  'core/home.html',
                  {'page': page,
                   'object_list': post_list,'bell':bell,'count':count,'P':post_count,'C':comment})
        except:
             return render(request,
                  'core/home.html',
                  {'page': page,
                   'object_list': post_list,'P':post_count,'C':comment})
      
def entry_not_found(request, exception, template_name='core/posts.html'  ):
    return render(request, template_name)

from .models import worker
from swapper import load_model
Notification = load_model('notifications', 'Notification')
#from core.models import Notification


class Postsee(DetailView):
   # mode = Notification
    model = Post
    template_name = "core/post.html"
    
    def get_context_data(self,**kwargs):
        curr = self.request.user.id
        print(curr)
        email = self.request.user.email
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        id = self.kwargs["p"]
        print(id)
       # slug = self.kwargs["slug"]
        form = CommentForm()
        post = get_object_or_404(Post, pk=pk)
        comments = post.comment_set.all()
        user_id = Post.objects.get(id=pk)
        author_id = user_id.author_id
        #sender = User.objects.get(id=curr)
        recipient = User.objects.get(id=author_id)

        notification = get_object_or_404(
        Notification,id=id)
        notification.mark_as_read()
#recipient=recipient,
        context['post'] = post
        context['comments'] = comments
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            try:
             img = request.FILES['img']
            except:
                img=''
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        current1 = request.user.email
        current2 = request.user.username
        user_id = request.user.id


        post = Post.objects.filter(id=self.kwargs['pk'])[0]
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form

        if form.is_valid():
            content = form.cleaned_data['content']
           # count = 0
        #    if worker.objects.filter(email=current1).exists():
          #      for letter in content:
          #          if letter == '(':
          #           count+=3
           #     add_to_money = count
            #    print(add_to_money)
           #     pay = paycheck.objects.get(reciver=current1)
            #    prev_money = pay.money
            #    new_money = float(prev_money) + add_to_money
            #    string_form = round(new_money/16,2)
            #    print(round(string_form),2)
            #    wages = paycheck.objects.get(reciver=current1)
#wages.money = str(string_form)
           #     wages.save()
               
          #  else:
           #     pass
            from datetime import date, timedelta
            startdate = date.today().strftime('%Y-%m-%d')
            print(startdate)

            comment = Comment.objects.create(
            name=current2,email=current1,
            content=content, post=post,image=img
            )

            form = CommentForm()
            context['form'] = form
            return self.render_to_response(context=context)

        return self.render_to_response(context=context)

class Reco(DetailView):
   # mode = Notification
    model = Post
    template_name = "core/post.html"
    
    def get_context_data(self,**kwargs):
        curr = self.request.user.id
        print(curr)
        email = self.request.user.email
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
      #  id = self.kwargs["p"]
      #  print(id)
       # slug = self.kwargs["slug"]
        form = CommentForm()
        post = get_object_or_404(Post, pk=pk)
        comments = post.comment_set.all()
        user_id = Post.objects.get(id=pk)
        author_id = user_id.author_id
        #sender = User.objects.get(id=curr)
       # recipient = User.objects.get(id=author_id)

      #  notification = get_object_or_404(
       # Notification, recipient=recipient, id=id)
       # notification.mark_as_read()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            try:
             img = request.FILES['img']
            except:
                img=''
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        current1 = request.user.email
        current2 = request.user.username
        user_id = request.user.id


        post = Post.objects.filter(id=self.kwargs['pk'])[0]
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form

        if form.is_valid():
            content = form.cleaned_data['content']
          #  count = 0
          #  if worker.objects.filter(email=current1).exists():
             #   for letter in content:
#if letter == '(':
              #       count+=3
              #  add_to_money = count
              #  print(add_to_money)
              #  pay = paycheck.objects.get(reciver=current1)
              #  prev_money = pay.money
              #  new_money = float(prev_money) + add_to_money
              #  string_form = round(new_money/16,2)
              #  print(round(string_form),2)
              #  wages = paycheck.objects.get(reciver=current1)
              #  wages.money = str(string_form)
              #  wages.save()
               
           # else:
          #      pass
            from datetime import date, timedelta
            startdate = date.today().strftime('%Y-%m-%d')
            print(startdate)

            comment = Comment.objects.create(
            name=current2,email=current1,
            content=content, post=post,image=img
            )

            form = CommentForm()
            context['form'] = form
            return self.render_to_response(context=context)

        return self.render_to_response(context=context)



class PostView(DetailView):
    model = Post
    template_name = "core/post.html"
    
    def get_context_data(self,**kwargs):
        curr = self.request.user.id
        print(curr)
        email = self.request.user.email
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        slug = self.kwargs["slug"]
        form = CommentForm()
        post = get_object_or_404(Post, pk=pk, slug=slug)
        comments = post.comment_set.all()
       # user_id = Post.objects.get(id=pk)
       # author_id = user_id.author_id
       # title = user_id.title

       # sender = User.objects.get(id=curr)
        #recipient = User.objects.get(id=author_id)
       # message = "This is"
      #  notify.send(sender=sender, recipient=recipient, verb=str(pk),
      #  description=title)

        context['post'] = post
        context['comments'] = comments
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        curr = self.request.user.id
        pk = self.kwargs["pk"]
        print(pk)
        user_id = Post.objects.get(id=pk)
        author_id = user_id.author_id
        title = user_id.topic
        if request.method == 'POST':
            try:
             img = request.FILES['img']
            except:
                img=''
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        current1 = request.user.email
        current2 = request.user.username
        user_id = request.user.id
        sender = User.objects.get(id=curr)
        recipient = User.objects.get(id=author_id)
        message = "This is"
        notify.send(sender=sender, recipient=recipient, verb=str(pk),
        description=title)
        post = Post.objects.filter(id=self.kwargs['pk'])[0]
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form

        if form.is_valid():
            content = form.cleaned_data['content']
           # n = Post.objects.filter(id=pk)
           # #for i in n:
               # print(i)
          # # if worker.objects.filter(email=current1).exists():
            #  if i.attendance == 'False':
             #   list = []
              #  list.append(content)
              #  for item in list:
              #   n = len(item.split())
              #  add_to_money = n * 0.1
              #  pay = paycheck.objects.get(reciver=current1)
               # prev_money = pay.money
               # new_money = float(prev_money) + add_to_money
               # print(new_money)
               # string_form = round(new_money,2)
               # pay.money = str(string_form)
               # pay.save()
             # else:
              #     pass
               
          #  else:
              #  pass
            from datetime import date, timedelta
            startdate = date.today().strftime('%Y-%m-%d')
            #print(startdate)
            list = []
            list.append(content)
            for item in list:
             n = len(item.split())

            comment = Comment.objects.create(
            name=current2,email=current1,
            content=content, post=post,image=img,numbers=n
            )

            form = CommentForm()
            context['form'] = form
            return self.render_to_response(context=context)

        return self.render_to_response(context=context)


class PostCreateViews(LoginRequiredMixin, CreateView):
    model = Post
    #fields = ["image","title"]      fields = ["title", "content", "image","sub","topic"]
    
   
    fields = ["title","image","sub"]
    def get_success_url(self):
        from datetime import date
        startdate = date.today().strftime('%Y-%m-%d')
        curr = self.request.user.id
        user_name = self.request.user.username
        #email = self.request.user.email
        try:
         x = place.objects.get(email=curr)
         places = x.place
         province = x.province
         country = x.country
         school = x.school
         grade = x.grade
         sa = Post.objects.filter(author_id=curr)
         for s in sa:
          s.place = places
          s.province = province
          s.school = school
          s.country = country
          s.grade = grade
          s.save()
          from .models import others
         post = Post.objects.all()
         lists = []
         for po in post:
             if po.place == places and po.province == province and po.school == school and po.country == country and po.grade == grade and po.author != curr:
              if Comment.objects.filter(post_id=po.id).exists():
               content = po.content
               slug = po.slug
             # author = po.author.filter(created=startdate)
               image = po.image
               tags = po.tags
               created = po.created_on
               update = po.updated_on
               title = po.title
               id = po.id
               sub = po.sub
               topic = po.topic
               if others.objects.filter(content=content).filter(author=curr).exists():
                pass
               else:
                sender = User.objects.get(id=curr)
                notify.send(sender=sender, recipient=sender, verb=str(id),
                description=f"Recomendation({po.sub})")
                re = others(slug=slug,content=content,image=image,title=title,author=curr,id2=id,sub=sub,topic=topic)
                re.save()
        except:
            pass
              
        messages.success(
            self.request, 'Your post has been created successfully.')
        return reverse_lazy("core:home")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.slug = slugify(form.cleaned_data['title'])
        obj.save()
        return super().form_valid(form)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    #fields = ["image","title"]      fields = ["title", "content", "image","sub","topic"]

    fields = ["title", "content", "image","sub"]
    def get_success_url(self):
        from datetime import date
        startdate = date.today().strftime('%Y-%m-%d')
        curr = self.request.user.id
        user_name = self.request.user.username
        #email = self.request.user.email
        try:
         x = place.objects.get(email=curr)
         places = x.place
         province = x.province
         country = x.country
         school = x.school
         grade = x.grade
         sa = Post.objects.filter(author_id=curr)
         for s in sa:
          s.place = places
          s.province = province
          s.school = school
          s.country = country
          s.grade = grade
          s.save()
          from .models import others
         post = Post.objects.all()
         lists = []
         for po in post:
             if po.place == places and po.province == province and po.school == school and po.country == country and po.grade == grade and po.author != curr:
              if Comment.objects.filter(post_id=po.id).exists():
               content = po.content
               slug = po.slug
             # author = po.author.filter(created=startdate)
               image = po.image
               tags = po.tags
               created = po.created_on
               update = po.updated_on
               title = po.title
               id = po.id
               sub = po.sub
               topic = po.topic
               if others.objects.filter(content=content).filter(author=curr).exists():
                pass
               else:
                sender = User.objects.get(id=curr)
                notify.send(sender=sender, recipient=sender, verb=str(id),
                description=f"Recomendation({po.sub})")
                re = others(slug=slug,content=content,image=image,title=title,author=curr,id2=id,sub=sub,topic=topic)
                re.save()
        except:
            print('fdsggg')
            pass
              
        messages.success(
            self.request, 'Your post has been created successfully.')
        return reverse_lazy("core:home")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.slug = slugify(form.cleaned_data['title'])
        obj.save()
        return super().form_valid(form)

    
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "content", "image"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update = True
        context['update'] = update

        return context

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been updated successfully.')
        return reverse_lazy("core:home")

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been deleted successfully.')
        return reverse_lazy("core:home")

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)

from .models import place

def location(request):
  curr = request.user.id
  if place.objects.filter(email=curr).exists():
    if request.method == 'POST':
        pro = request.POST['cn']
        province = request.POST['province']
        school = request.POST['school']
        places = request.POST['place']
        grae = request.POST['grade']
        email = request.user.id

        prov = place.objects.filter(email=email)
        for i in prov:
         i.place =places
         i.province= province
         i.school = school
         i.country =pro
         i.grade = grae
         i.save()
    return render(request,'core/form.html')
    #return redirect('core:home')
  else:
    if request.method == 'POST':
        pro = request.POST['cn']
        province = request.POST['province']
        school = request.POST['school']
        places = request.POST['place']
        grade = request.POST['grade']
        email = request.user.id
        prov = place(province=province,school=school,place=places,email=email,country=pro,grade=grade)
        prov.save()
        return redirect('core:home')

    else:
        return render(request,'core/form.html')
       # return redirect('core:home')


from .models import others

def reco(request):
    current = request.user.id
    x = place.objects.get(email=current)
    post_count = Post.objects.all().count()
    comment = Comment.objects.all().count()
    places = x.place
    province = x.province
    country = x.country
    school = x.school
    grade = x.grade
    sa = Post.objects.filter(author_id=current)
    for s in sa:
        s.place = places
        s.province = province
        s.school = school
        s.country = country
        s.grade = grade
        s.save()
    from .models import others
    post = Post.objects.all()
    lists = []
    for po in post:
        if po.place == places and po.province == province and po.school == school and po.country == country and po.grade == grade and po.author != current:
            if Comment.objects.filter(post_id=po.id).exists():
              content = po.content
              slug = po.slug
             # author = po.author.filter(created=startdate)
              image = po.image
              tags = po.tags
              created = po.created_on
              update = po.updated_on
              title = po.title
              id = po.id
              sub = po.sub
              topic = po.topic
              if others.objects.filter(content=content).filter(author=current).exists():
               pass
              else:
               re = others(slug=slug,content=content,image=image,title=title,author=current,id2=id,sub=sub,topic=topic)
               re.save()
    my_reco = others.objects.filter(author=current)
    print(my_reco)
    paginator = Paginator(my_reco, 45) 
    page = request.GET.get('page')
    try:
     post_list = paginator.page(page)
    except PageNotAnInteger:
     post_list = paginator.page(1)
    except EmptyPage:
     post_list = paginator.page(paginator.num_pages)
    
    user = User.objects.get(pk=current)
    bell = user.notifications.unread()
    post_query = Post.objects.filter(author_id=current)

    count = 0
    for post in post_query:
        if Comment.objects.filter(post_id=post.id).count() > 1:
            if post.attendance == 'False':
                count+=1
         #print(count)
   
    return render(request,'core/recomendation.html',{'reco':post_list,'bell':bell,'count':count,'P':post_count,'C':comment  })


def Admin(request):
    pay = paycheck.objects.all()
    use = User.objects.all().count()
    #print(user)
    current = request.user.id
    user = User.objects.get(pk=current)
    bell = user.notifications.unread()
    post_query = Post.objects.filter(author_id=current)
    count = 0
    for post in post_query:
        if Comment.objects.filter(post_id=post.id).count() > 1:
            if post.attendance == 'False':
                count+=1
    
    return render(request,'core/Admin.html',{'checks':pay,'D':use,'bell':bell})


def category3(request,username):
    post_count = Post.objects.all().count()
    comment = Comment.objects.all().count()
    my_reco = others.objects.filter(sub=username)
    paginator = Paginator(my_reco, 45) 
    page = request.GET.get('page')
    try:
     post_list = paginator.page(page)
    except PageNotAnInteger:
     post_list = paginator.page(1)
    except EmptyPage:
     post_list = paginator.page(paginator.num_pages)
    current = request.user.id
    user = User.objects.get(pk=current)
    bell = user.notifications.unread()
    post_query = Post.objects.filter(author_id=current)

    count = 0
    for post in post_query:
        if Comment.objects.filter(post_id=post.id).count() > 1:
            if post.attendance == 'False':
                count+=1
         #print(count)
   
    return render(request,'core/recomendation.html',{'reco':post_list,'bell':bell,'count':count,'P':post_count,'C':comment })



