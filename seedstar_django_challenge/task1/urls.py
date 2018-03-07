from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

from . import views

app_name="task1"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/', views.list, name='list'),
    url(r'^add/', views.add, name='add'),
    # url(r'^admin/', include(admin.site.urls)),
]


