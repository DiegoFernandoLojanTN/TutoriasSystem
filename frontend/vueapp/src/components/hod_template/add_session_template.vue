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
                                <h3 class="card-title">Agregar Sesión</h3>
                            </div>

                            <form role="form" method="POST" action="{% url 'add_session_save' %}">
                                {% csrf_token %}
                                {% comment %} Display Messages {% endcomment %}
                                {% include 'message.vue' %}
                                    
                                <div class="card-body">
                                    <div class="form-group">
                                        <label>Año de inicio de sesión</label>
                                        <input type="date" class="form-control" name="session_start_year">
                                    </div>
                                    <div class="form-group">
                                        <label>Año de finalización de la sesión</label>
                                        <input type="date" class="form-control" name="session_end_year">
                                    </div>
                                </div>

                                <div class="card-footer">
                                    <button type="submit" class="btn btn-primary">Guardar</button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>

  {% endblock content %}