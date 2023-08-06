from django import forms 
from django.forms import Form
from .models import Courses, SessionYearModel


class DateInput(forms.DateInput):
    input_type = "date"


class AddStudentForm(forms.Form):
    email = forms.EmailField(label="Correo", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Contraseña", max_length=50, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="Primer Nombre", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Primer Apellido", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Nombre de Usuario", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Direccion", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))

    #Para mostrar cursos
    try:
        courses = Courses.objects.all()
        course_list = []
        for course in courses:
            single_course = (course.id, course.course_name)
            course_list.append(single_course)
    except:
        course_list = []
    
    #Para mostrar años de sesión
    try:
        session_years = SessionYearModel.objects.all()
        session_year_list = []
        for session_year in session_years:
            single_session_year = (session_year.id, str(session_year.session_start_year)+" a "+str(session_year.session_end_year))
            session_year_list.append(single_session_year)
            
    except:
        session_year_list = []
    
    gender_list = (
        ('Masculino','Masculino'),
        ('Femenino','Femenino')
    )
    
    course_id = forms.ChoiceField(label="Curso", choices=course_list, widget=forms.Select(attrs={"class":"form-control"}))
    gender = forms.ChoiceField(label="Género", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
    session_year_id = forms.ChoiceField(label="Año de sesión", choices=session_year_list, widget=forms.Select(attrs={"class":"form-control"}))
    #session_start_year = forms.DateField(label="Inicio de sesión", widget=DateInput(attrs={"class":"form-control"}))
    #session_end_year = forms.DateField(label="Fin de sesión", widget=DateInput(attrs={"class":"form-control"}))
    profile_pic = forms.FileField(label="Foto de perfil", required=False, widget=forms.FileInput(attrs={"class":"form-control"}))



class EditStudentForm(forms.Form):
    email = forms.EmailField(label="Correo", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="Nombre", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Apellido", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Nombre de usuario", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Dirección", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))

    #Para ver cursos
    try:
        courses = Courses.objects.all()
        course_list = []
        for course in courses:
            single_course = (course.id, course.course_name)
            course_list.append(single_course)
    except:
        course_list = []

    #ver sesiones
    try:
        session_years = SessionYearModel.objects.all()
        session_year_list = []
        for session_year in session_years:
            single_session_year = (session_year.id, str(session_year.session_start_year)+" a "+str(session_year.session_end_year))
            session_year_list.append(single_session_year)
            
    except:
        session_year_list = []

    
    gender_list = (
        ('Masculino','Masculino'),
        ('Femenino','Femenino')
    )
    
    course_id = forms.ChoiceField(label="Curso", choices=course_list, widget=forms.Select(attrs={"class":"form-control"}))
    gender = forms.ChoiceField(label="Género", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
    session_year_id = forms.ChoiceField(label="Año de sesión", choices=session_year_list, widget=forms.Select(attrs={"class":"form-control"}))
    # session_start_year = forms.DateField(label="Session Start", widget=DateInput(attrs={"class":"form-control"}))
    # session_end_year = forms.DateField(label="Session End", widget=DateInput(attrs={"class":"form-control"}))
    profile_pic = forms.FileField(label="Foto de perfil", required=False, widget=forms.FileInput(attrs={"class":"form-control"}))