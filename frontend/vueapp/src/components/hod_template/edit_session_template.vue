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
                        <h3 class="card-title">Editar Sesión</h3>
                    </div>

                    <form role="form" method="POST" action="{% url 'edit_session_save' %}">
                        {% csrf_token %}
                        {% comment %} Display Messages {% endcomment %}
                        {% include 'message.vue' %}

                        <div class="card-body">
                            <div class="form-group">
                                <label>Fecha de inicio de Tutoria </label>
                                <input type="date" class="form-control" name="session_start_year" value="{{ session_year.session_start_year|date:'Y-m-d' }}">
                            </div>

                            <div class="form-group">
                                <label>Fecha de fin de Tutoria </label>
                                <input type="date" class="form-control" name="session_end_year" value="{{ session_year.session_end_year|date:'Y-m-d' }}">
                            </div>
                        </div>

                        <div class="card-footer">
                        <input type="hidden" name="session_id" value="{{ session_year.id }}" />
                            <button type="submit" class="btn btn-primary">Actualizar Sesión</button>
                        </div>
                    </form>
                </div>

  {% endblock content %}