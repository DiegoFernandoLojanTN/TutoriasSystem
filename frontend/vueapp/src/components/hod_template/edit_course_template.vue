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
                                <h3 class="card-title">Editar Curso</h3>
                            </div>

                            <form role="form" method="POST" action="{% url 'edit_course_save' %}">
                                {% csrf_token %}
                                {% comment %} Display Messages {% endcomment %}
                                {% include 'message.vue' %}
        
                                <div class="card-body">
                                    <div class="form-group">
                                        <label>Nombre del Curso </label>
                                        <input type="text" class="form-control" name="course" value="{{ course.course_name }}">
                                        <input type="hidden" name="course_id" value="{{ course.id }}" />
                                    </div>
                                </div>

                                <div class="card-footer">
                                    <button type="submit" class="btn btn-primary">Actualizar Curso</button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
        
{% endblock %}