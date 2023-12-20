

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()
# Create your models here.

class Faculty(models.Model):

    name: str = models.CharField(max_length=150)
    date_created= models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
class SpecialtyTypeEnum(models.TextChoices):
    SECOND = 'SECOND'
    FOURTH = 'FOURTH'

class Specialty(models.Model):

    name: str = models.CharField(max_length=150)
    faculty_id: Faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name="specialties")
    duration = models.CharField(max_length=50,choices=SpecialtyTypeEnum.choices, default=SpecialtyTypeEnum.FOURTH)

    def __str__(self) -> str:
        return self.name

class Group(models.Model):

    name: str = models.CharField(max_length=30)
    specaialty_id= models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="groups")
    date_created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Student(models.Model):

    name: str = models.CharField(max_length=60)
    surname: str = models.CharField(max_length=60)
    user_id: User = models.OneToOneField(User, related_name="student", on_delete=models.CASCADE)
    group_id: Group = models.ForeignKey(Group, on_delete=models.RESTRICT, related_name="students")

    def __str__(self) -> str:
        return self.name
    

class StuffPositionEnum(models.TextChoices):
    RECTOR = 'RECTOR'
    PRORECTOR = 'PRARECTOR'
    DEKAN = 'DEKAN'

class Stuff(models.Model):

    name: str = models.CharField(max_length=60)
    surname: str = models.CharField(max_length=60)
    salary = models.DecimalField(max_digits=7, decimal_places=2)
    position: StuffPositionEnum= models.CharField(max_length=50,choices = StuffPositionEnum.choices, default = StuffPositionEnum.DEKAN)
    user_id: User = models.OneToOneField(User, related_name="stuff", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class TeacherProfessionEnum(models.TextChoices):
    DOSENT = 'DOSENT'
    LABORANT = 'LABORANT'
    PROFESSOR = 'PROFESSOR'

class Teacher(models.Model):

    name: str = models.CharField(max_length=60)
    surname: str = models.CharField(max_length=60)
    salary = models.DecimalField(max_digits=7, decimal_places=2)
    profession: TeacherProfessionEnum = models.CharField(max_length=50,choices = TeacherProfessionEnum.choices, default = TeacherProfessionEnum.LABORANT)
    user_id: User = models.OneToOneField(User, related_name="teacher", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class SubjectSmestrTypeEnum(models.TextChoices):
    FIRST = 'FIRST'
    SECOND = 'SECOND'


class SubjectCourseTypeEnum(models.TextChoices):
    FIRST = 'FIRST'
    SECOND = 'SECOND'


class SubjectList(models.Model):

    name: str = models.CharField(max_length=150)
    teacher_id: Teacher = models.ManyToManyField(Teacher, related_name = "subjectlists")

    def __str__(self) -> str:
        return self.name

class Subject(models.Model):
    subject_list_id: SubjectList = models.OneToOneField(SubjectList, related_name="subject", on_delete=models.CASCADE)
    smestr_type: SubjectSmestrTypeEnum = models.CharField(max_length=50,choices=SubjectSmestrTypeEnum.choices, default=SubjectSmestrTypeEnum.FIRST)
    course_type: SubjectCourseTypeEnum = models.CharField(max_length=50,choices=SubjectCourseTypeEnum.choices, default=SubjectCourseTypeEnum.FIRST)
    lecture_teacher_id: Teacher = models.OneToOneField(Teacher, related_name="lecture_subject", on_delete=models.CASCADE)
    exercise_teacher_id: Teacher = models.OneToOneField(Teacher, related_name="exercise_subject", on_delete=models.CASCADE)
    group_id: Group = models.ForeignKey(Group, related_name="subjects", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.subject_list_id.name
    
    
class Statistic(models.Model):
    point = models.IntegerField()
    student_id = models.ForeignKey(Student, on_delete = models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete = models.CASCADE)
    point_type = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.point

