from django.shortcuts import render , reverse
from .models import TodoBase
from django.http import HttpResponseRedirect
import datetime

def dateadd():
    a = datetime.datetime.today().strftime("%d - %m - %Y")
    return str(a)

def viewTODO(self):
    all_todo_items = TodoBase.objects.all()
    return render(self, 'index.html', {'all_items': all_todo_items})



# Страницы профилей
def viewROBOT(self):
    all_todo_items = TodoBase.objects.all()
    return render(self, 'robot.html', {'all_items': all_todo_items})
def viewPROG(self):
    all_todo_items = TodoBase.objects.all()
    return render(self, 'prog.html', {'all_items': all_todo_items})
def viewINGENER(self):
    all_todo_items = TodoBase.objects.all()
    return render(self, 'ingener.html', {'all_items': all_todo_items})
def viewECONOM(self):
    all_todo_items = TodoBase.objects.all()
    return render(self, 'econom.html', {'all_items': all_todo_items})
def viewMEDIA(self):
    all_todo_items = TodoBase.objects.all()
    return render(self, 'media.html', {'all_items': all_todo_items})


#Операции с пользовалелями
def addTODO(self):
    y = TodoBase(date = dateadd(),
                 name = self.POST['name'],
                 surname = self.POST['surname'],
                 patronymic = self.POST['patronymic'],
                 oldschool = self.POST['oldschool'],
                 school_class = self.POST['school_class'])

    y.save()
    return HttpResponseRedirect(self.POST['upd'])

def deleteTODO(self, i):
    y = TodoBase.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect(self.POST['upd'])

def deleteTODOall(self):
    y = TodoBase.objects.all()
    y.delete()
    return HttpResponseRedirect(self.POST['upd'])

def modProfile(self, i):
    y = TodoBase.objects.get(id=i)
    y.school_class = self.POST['school_class']
    y.save()
    return HttpResponseRedirect(self.POST['upd'])

def modHostel(self, i):
    y = TodoBase.objects.get(id=i)
    y.hostel = self.POST['hostel']
    y.save()
    return HttpResponseRedirect(self.POST['upd'])

def modOther(self,i):
    y = TodoBase.objects.get(id=i)
    y.foreign_language = self.POST['foreign_language']
    y.save()
    return HttpResponseRedirect(self.POST['upd'])

def modOther2(self,i):
    y = TodoBase.objects.get(id=i)
    y.social_benefits = self.POST['social_benefits']
    y.save()
    return HttpResponseRedirect(self.POST['upd'])

def modOther3(self,i):
    y = TodoBase.objects.get(id=i)
    y.other = self.POST['other']
    y.save()
    return HttpResponseRedirect(self.POST['upd'])

def print(self):
    #y = TodoBase.objects.get(id=i)
    p = {
        'q1': 'y.surname',
        'q2': 'y.name',
        'q3': 'y.patronymic'
    }
    return render(self, 'print.html', context=p)


#Страница абитуриента
def viewabiturient(self):
    all_todo_items = TodoBase.objects.all()
    return render(self, 'abit.html', {'all_items': all_todo_items})

def abitprint(self):
    all_todo_items = TodoBase.objects.all()
    return render(self, 'abitprint.html', {'all_items': all_todo_items})

def addabit(self):
    y = TodoBase(date = dateadd(),
                 name = self.POST['name'],
                 surname = self.POST['surname'],
                 patronymic = self.POST['patronymic'],
                 oldschool=self.POST['oldschool'],
                 mark_averange=self.POST['mark_averange'],
                 foreign_language=self.POST['foreign_language'],
                 hostel=self.POST['hostel'],
                 social_benefits=self.POST['social_benefits'],
                    gender = self.POST['gender'],
                    birthdate = self.POST['birthdate'],
                    phone =self.POST['phone'],
                    email = self.POST['email'],
                    sity = self.POST['sity'],
                    street = self.POST['street'],
                    house = self.POST['house'],
                    housing = self.POST['housing'],
                    flat = self.POST['flat'],
                    mother_name = self.POST['mother_name'],
                    mother_surname = self.POST['mother_surname'],
                    mother_patronymic = self.POST['mother_patronymic'],
                    mother_job = self.POST['mother_job'],
                    mother_job_post = self.POST['mother_job_post'],
                    mother_phone = self.POST['mother_phone'],
                    father_name = self.POST['father_name'],
                    father_surname = self.POST['father_surname'],
                    father_patronymic = self.POST['father_patronymic'],
                    father_job = self.POST['father_job'],
                    father_job_post = self.POST['father_job_post'],
                    father_phone = self.POST['father_phone'],
                    mark_math = self.POST['mark_math'],
                    mark_rus = self.POST['mark_rus'],
                    mark_physics = self.POST['mark_physics'],
                    mark_informatics = self.POST['mark_informatics'],
                    mark_social_science = self.POST['mark_social_science'],
                    progress = self.POST['progress'],
                    control = self.POST['control'],
                    control_reason = self.POST['control_reason'],
                    participation = self.POST['participation'],
                    course_vtl_math = self.POST['course_vtl_math'],
                    course_vtl_physics = self.POST['course_vtl_physics'],
                    course_vtl_informatics = self.POST['course_vtl_informatics'],
                    pfdo_sert = self.POST['pfdo_sert'],
                    correct = self.POST['correct'],
                    agreement = self.POST['agreement']
                 )
    y.save()
    return HttpResponseRedirect('/abit/')
