{% extends 'hod_template/base_template.vue' %}
{% load static %}

{% block content %}

<div class="dashboard-wrapper">
    <div class="dashboard-ecommerce">
        <div class="container-fluid dashboard-content">
            <div class="row">
                <div class="col-md-12">
                    <div class="card card-primary">
                    <div class="card-header">
                        <h3 class="card-title">Agregar Tutoría</h3>
                    </div>

                    <form role="form" method="POST" action="{% url 'add_subject_save' %}">
                        {% csrf_token %}
                        {% comment %} Display Messages {% endcomment %}
                        {% include 'message.vue' %}

                        <div class="card-body">
                            <div class="form-group">
                                <label>Tema para Tutoria </label>
                                <input type="text" class="form-control" name="subject" placeholder="Ingrese tema de tutoria">
                            </div>

                            <div class="form-group">
                                <label>Curso </label>
                                <select class="form-control" name="course">
                                    {% for course in courses %}
                                        <option value="{{ course.id }}">{{ course.course_name }}</option>
                                    {% endfor %}
                                </select>
                            </div>

                            <div class="form-group">
                                <label>Profesor </label>
                                <select class="form-control" name="staff">
                                    {% for staff in staffs %}
                                        <option value="{{ staff.id }}">{{ staff.first_name }} {{ staff.last_name }}</option>
                                    {% endfor %}
                                </select>
                            </div>

                        </div>

                        <div class="card-footer">
                            <button type="submit" class="btn btn-primary">Guardar</button>
                        </div>
                    </form>
                </div>

{% endblock content %}