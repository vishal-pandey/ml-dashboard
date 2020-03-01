from django.conf.urls import url
from dashboard import views
# SET THE NAMESPACE!
app_name = 'dashboard'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^$' ,views.index, name='index'),
    url(r'^upload' ,views.upload_dataset, name='upload'),
    url(r'^list_dataset' ,views.list_dataset, name='list_dataset'),
]