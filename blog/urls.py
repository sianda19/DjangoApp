"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls import include
from core.views import main_view
import notifications.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('core.urls', 'core'), namespace='core')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('<str:ref_code>', main_view, name='main-view'),
    path('', main_view, name='main-view'),
 #   path('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
   # path('mom/', include(('core.urls', ''), namespace='core')),

]

from django.conf import settings
from django.views.static import serve
from django.urls import include, re_path

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]

#handler404 = 'core.views.entry_not_found'
#handler500 = 'entry_not_found'

'''if settings.DEBUG == False:
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    pass'''
