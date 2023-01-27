from django.db import models


class TodoBase(models.Model):
    name = models.TextField()
    surname = models.TextField()
    patronymic = models.TextField()
    gender = models.TextField()
    birthdate = models.TextField()
    oldschool = models.TextField()
    phone = models.TextField()
    email = models.TextField()
    sity = models.TextField()
    street = models.TextField()
    house = models.TextField()
    housing = models.TextField()
    flat = models.TextField()
    hostel = models.TextField()
    mother_name = models.TextField()
    mother_surname = models.TextField()
    mother_patronymic = models.TextField()
    mother_job = models.TextField()
    mother_job_post = models.TextField()
    mother_phone = models.TextField()
    father_name = models.TextField()
    father_surname = models.TextField()
    father_patronymic = models.TextField()
    father_job = models.TextField()
    father_job_post = models.TextField()
    father_phone = models.TextField()
    social_benefits = models.TextField()
    mark_averange = models.TextField()
    mark_math = models.TextField()
    mark_rus = models.TextField()
    mark_physics = models.TextField()
    mark_informatics = models.TextField()
    mark_social_science = models.TextField()
    progress = models.TextField()
    control = models.TextField()
    control_reason = models.TextField()
    participation = models.TextField()
    school_class = models.TextField()
    foreign_language = models.TextField()
    course_vtl_math = models.TextField()
    course_vtl_physics = models.TextField()
    course_vtl_informatics = models.TextField()
    pfdo_sert = models.TextField()
    correct = models.TextField()
    agreement = models.TextField()
    date = models.TextField()
    other = models.TextField()
    ank1 = models.TextField()
    ank2 = models.TextField()
    ank3 = models.TextField()
    ank4 = models.TextField()
    ank5 = models.TextField()
    ank6 = models.TextField()
    status = models.TextField()


