"""medical URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.indexr,name='index'),
    path('regr',views.regr,name='regr'),
    path('patient',views.patient_reg,name='patient'),
    path('doctor', views.doctor_reg, name='doctor'),
    path('reg', views.reg, name='reg'),
    path('loginr',views.loginr,name='loginr'),
    path('login',views.login,name='login'),
    path('logout', views.logout, name='logout'),
    path('blogr',views.blogr,name='blogr'),
    path('buploads',views.bupload,name='buploads'),
    path('draft-datas',views.draft_data,name='draft-datas'),
    path('post-datas', views.post_data, name='post-datas'),
    path('blogforms', views.blogform, name='blogforms'),
    path('allblogs/', views.allblog, name='allblogs'),
    path('category/<str:category>/', views.category_blog, name='category_blogs'),
    path('updateb/<int:id>/', views.update_blog, name='updateb'),
    path('deleteb/<int:id>/', views.delete_blog, name='deleteb'),
    path('publishb/<int:id>/', views.publish_blog, name='publishb'),
    path('viewb/<int:id>/', views.view_blog, name='viewb'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
