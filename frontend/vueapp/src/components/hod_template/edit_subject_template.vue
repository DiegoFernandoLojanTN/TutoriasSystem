{% extends 'hod_template/base_template.vue' %}
{% load static %}

{% block content %}

<section class="content">
        <div class="container-fluid">
            <div class="row">
                <div class="col-md-12">
                    <div class="card card-primary">
                    <div class="card-header">
                        <h3 class="card-title">Editar Tutoria</h3>
                    </div>
                    <form role="form" method="POST" action="{% url 'edit_subject_save' %}">
                        {% csrf_token %}
                        {% comment %} Display Messages {% endcomment %}
                        {% include 'message.vue' %}
                            
                        <div class="card-body">
                            <div class="form-group">
                                <label>Nombre del tema</label>
                                <input type="text" class="form-control" name="subject" value="{{ subject.subject_name }}">
                            </div>

                            <div class="form-group">
                                <label>Curso </label>
                                <select class="form-control" name="course">
                                    {% for course in courses %}
                                        <option value="{{ course.id }}" {% if course.id == subject.course_id.id %} selected {% endif %}>{{ course.course_name }}</option>
                                    {% endfor %}
                                </select>
                            </div>

                            <div class="form-group">
                                <label>Profesor </label>
                                <select class="form-control" name="staff">
                                    {% for staff in staffs %}
                                        <option value="{{ staff.id }}" {% if staff.id == subject.staff_id.id %} selected {% endif %}>{{ staff.first_name }} {{ staff.last_name }}</option>
                                    {% endfor %}
                                </select>
                                
                                <input type="hidden" name="subject_id" value="{{ subject.id }}" />
                            </div>
                        </div>

                        <div class="card-footer">
                            <button type="submit" class="btn btn-primary">Actualizar Tutoria</button>
                        </div>
                    </form>
                </div>

{% endblock content %}