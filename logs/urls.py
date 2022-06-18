from django.contrib import admin
from django.urls import path
from logs.views import viewTODO,viewROBOT,viewPROG,viewINGENER,viewECONOM,viewMEDIA, \
    addTODO, deleteTODO, deleteTODOall, viewabiturient, addabit, modProfile, \
    modHostel, modOther, modOther2, modOther3, abitprint, print

urlpatterns = [
    path('/', admin.site.urls),
    path('todo/', viewTODO),
    path('robot/', viewROBOT),
    path('prog/', viewPROG),
    path('ingener/', viewINGENER),
    path('econom/', viewECONOM),
    path('media/', viewMEDIA),
    path('add/', addTODO),
    path('delete/<int:i>/', deleteTODO),
    path('deleteall/', deleteTODOall),
    path('abit/', viewabiturient),
    path('addabit/', addabit),
    path('abitprint/', abitprint),
    path('modProfile/<int:i>/',modProfile),
    path('modHostel/<int:i>/',modHostel),
    path('modOther/<int:i>/',modOther),
    path('modOther2/<int:i>/',modOther2),
    path('modOther3/<int:i>/',modOther3),
    path('print/', print),
    
]
