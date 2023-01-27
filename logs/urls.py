from django.contrib import admin
from django.urls import path
from logs.views import viewTODO,viewROBOT,viewPROG,viewINGENER,viewECONOM,viewMEDIA, \
    addTODO, deleteTODO, deleteTODOall, viewabiturient, addabit, modProfile, \
    modHostel, modOther, modOther2, modOther3, search, search2, view11klass, home, abit,viewarch, modstatus

urlpatterns = [
     # Добавили новый маршрут
    path('', home),
    path('admin/', admin.site.urls),
    path('todo/', viewTODO),
    path('robot/', viewROBOT),
    path('prog/', viewPROG),
    path('ingener/', viewINGENER),
    path('econom/', viewECONOM),
    path('media/', viewMEDIA),
    path('11klass/', view11klass),
    path('arch/', viewarch),
    path('add/', addTODO),
    path('delete/<int:i>/', deleteTODO),
    path('deleteall/', deleteTODOall),
    path('abit/', viewabiturient),
    path('abit2/', abit),
    path('addabit/', addabit),
    path('search/', search),
    path('search2/', search2),
    path('modProfile/<int:i>/',modProfile),
    path('modHostel/<int:i>/',modHostel),
    path('modOther/<int:i>/',modOther),
    path('modOther2/<int:i>/',modOther2),
    path('modOther3/<int:i>/',modOther3),
    path('modstatus/<int:i>/',modstatus),

    
]
