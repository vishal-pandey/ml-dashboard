from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from login import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^special/',views.special,name='special'),
    url(r'^login/',include('login.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)