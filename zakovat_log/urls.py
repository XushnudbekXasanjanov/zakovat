from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('onlyforme/', admin.site.urls),
    path('',Registration,name='index'),
    path('error/',ErrorAll,name='error'),
    path('count-error/',ErrorCount,name='count-error'),
    path('team-error/',ErrorTeam,name='team-error'),
    path('success/',Success,name='success'),
    path('teams/',Table,name='table'),
    path('full-team/',FullTeamError,name='full')
]

