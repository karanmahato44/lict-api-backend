from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator




# faculties

class Faculty(models.Model):
  faculty_name = models.CharField(max_length=100, validators=[RegexValidator(r'^[A-Za-z0-9_]+$', 'Only alphabets, numbers, and underscores are allowed in the faculty name.')])
  batch_year = models.PositiveSmallIntegerField()

  def __str__(self):
    return f'{self.faculty_name}_{self.batch_year}'
  
  class Meta:
     constraints = [models.UniqueConstraint(fields=['faculty_name', 'batch_year'], name='unique_faculty_name_batch_year')]




# semesters

class Semester(models.Model):
  SEMESTER_CHOICES = [
      ('1', 'SEM_1'),
      ('2', 'SEM_2'),
      ('3', 'SEM_3'),
      ('4', 'SEM_4'),
      ('5', 'SEM_5'),
      ('6', 'SEM_6'),
      ('7', 'SEM_7'),
      ('8', 'SEM_8'),
  ]
  semester = models.CharField(max_length=1, choices=SEMESTER_CHOICES, default=1)
  # "faculty" will be a foreign key in this table, one to many, a faculty(fk) can have many semesters(current class/table/col/row)
  faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='faculty_semesters')

  def __str__(self):
     return f'{self.faculty}_SEM_{self.semester}'
  
  class Meta:
     constraints = [models.UniqueConstraint(fields=['semester', 'faculty'], name='unique_semester_faculty')]




# subjects

class Subject(models.Model):
    subject_name = models.CharField(max_length=100, unique=True, validators=[RegexValidator(r'^[A-Za-z0-9_]+$', 'Only alphabets, numbers, and underscores are allowed in the subject name.')])
    faculties = models.ManyToManyField(Faculty, related_name='faculty_subjects')
    semesters = models.ManyToManyField(Semester, related_name='semester_subjects')
    
    def __str__(self):
       return f'{self.subject_name}'
    



# teachers

class Teacher(models.Model):
  teacher_name = models.CharField(max_length=100, validators=[RegexValidator(r'^[A-Za-z ]+$', 'Only alphabets and spaces are allowed in the teacher name.')])
  email = models.EmailField(unique=True)
  phone = models.CharField(max_length=20, unique=True, validators=[RegexValidator(r'^\+?\d{1,3}[-.\s]?\d{1,14}$', 'Enter a valid phone number.')])
  faculties = models.ManyToManyField(Faculty, related_name='faculty_teachers')
  semesters = models.ManyToManyField(Semester, related_name='semester_teachers')
  subjects = models.ManyToManyField(Subject, related_name='subject_teachers')

  def __str__(self):
     return f'{self.teacher_name}'




# students

class Student(models.Model):
    student_name = models.CharField(max_length=100, validators=[RegexValidator(r'^[A-Za-z ]+$', 'Only alphabets and spaces are allowed in the student name.')])
    email = models.EmailField(unique=True)
    reg_no = models.CharField(max_length=100, unique=True, validators=[RegexValidator(r'^[\w\-]+$', 'Only alphanumeric characters, hyphens ("-"), and underscores ("_") are allowed in the registration number.')])
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='faculty_students')
    semesters = models.ManyToManyField(Semester, related_name='semester_students')
    
    def __str__(self):
        return f'{self.student_name}_{self.faculty}'




# grades

class Grade(models.Model):
    gpa = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0.00), MaxValueValidator(4.00)])
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_grade')
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='semester_grade')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject_grade')

    def __str__(self):
        return f'{self.student}_{self.subject}_{self.semester}_{self.gpa}'
    
    class Meta:
       constraints = [models.UniqueConstraint(fields=['student', 'semester', 'subject'], name='unique_student_semester_subject')]