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
                                <h3 class="card-title">Agregar Curso</h3>
                            </div>
                            
                            <form role="form" method="POST" action="{% url 'add_course_save' %}">
                                {% csrf_token %}
                                {% comment %} Display Messages {% endcomment %}
                                {% include 'message.vue' %}
                                    
                                <div class="card-body">
                                    <div class="form-group">
                                        <label>Nombre del Curso</label>
                                        <input type="text" class="form-control" name="course" placeholder="Ingrese el Curso">
                                    </div>
                                </div>

                                <div class="card-footer">
                                    <button type="submit" class="btn btn-primary">Guardar</button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
        
{% endblock %}