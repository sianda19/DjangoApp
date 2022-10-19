from argparse import Action
from django.urls import path
from . import views

from .views import HomeView, PostView,PostCreateViews, PostCreateView, PostUpdateView, PostDeleteView, viewView,View,Postsee,Reco
#HomeView,
urlpatterns = [
    path('users/profile/<str:string>/cashout',views.cash,name='cashout'),

    path('',views.sample , name='home'),
    path('posts',HomeView.as_view() , name='posts'),
    path('tutor/<str:code>/',views.tutor,name='tutor'),
    path('search12',views.search12,name=' search12 '),
    path('post/created/', PostCreateViews.as_view(), name='post_c'),
    path('tutor/<str:str>/save',views.videos,name='save'),
    path('post/<pk>',Reco.as_view(),name='recos'),
    path('post/<int:ints>/<str:str1>/<int:int2>/<int:com>/', views.sat, name='sat'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('views', viewView.as_view(), name='views'),
    path('post/<pk>/<slug:slug>', PostView.as_view(), name='post'),
    path('post/<pk>/<p>/', Postsee.as_view(), name='see'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('submit', views.search, name='submit'),
    path('bus', views.sow, name='bus'),
    path('add', View.as_view(), name='add'),
    path('test', views.test, name='test'),
    path('bbb', views.action,name='bbb'),
    path('email', views.Email,name='email'),
    path('admin', views.Admin,name='admin'),
    path('code',views.save_code,name='code'),
    path('date',views.date,name='date'),
    path('location',views.location,name='location'),
    path('reco',views.reco,name='reco'),
    path('recomend',views.reco_search,name='recomend'),
    path('reload',views.run,name='reload'),
    path('sug',views.sug,name='sug'),
    path('users/signup/terms',views.terms,name='terms'),
   # path('class/<int:id>/',views.classes,name='class'),
    #path('vote/<int:id>/',views.vote,name='vote'),
  #  path('submit_camp',views.camps,name='submit_camp'),
    path('<username>',views.category2, name='category2'),
    path('<username>',views.category, name='category'),
    path('<username>/',views.category3, name='category3'),
    path('post/<username>/',views.profile, name='profile'),
]





