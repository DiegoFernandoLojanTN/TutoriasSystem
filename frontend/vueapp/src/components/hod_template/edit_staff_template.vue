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
                        <h3 class="card-title">Editar Profesor</h3>
                    </div>

                    <form role="form" method="POST" action="{% url 'edit_staff_save' %}">
                        {% csrf_token %}
                        {% comment %} Display Messages {% endcomment %}
                        {% include 'message.vue' %}

                        <div class="card-body">
                            <div class="form-group">
                                <label>Correo</label>
                                <input type="email" class="form-control" name="email" value="{{ staff.admin.email }}">
                            </div>

                            <div class="form-group">
                                <label>Usuario</label>
                                <input type="text" class="form-control" name="username" value="{{ staff.admin.username }}">
                            </div>

                            {% comment %} <div class="form-group">
                                <label>Password</label>
                                <input type="password" class="form-control" name="password" value="{{ staff.admin.password }}">
                            </div> {% endcomment %}

                            <div class="form-group">
                                <label>Nombre</label>
                                <input type="text" class="form-control" name="first_name" value="{{ staff.admin.first_name }}">
                            </div>

                            <div class="form-group">
                                <label>Apellido</label>
                                <input type="text" class="form-control" name="last_name" value="{{ staff.admin.last_name }}">
                                <input type="hidden" name="staff_id" value="{{ staff.admin.id }}" />
                            </div>

                            <div class="form-group">
                                <label>Direccion</label>
                                <textarea class="form-control" name="address">{{ staff.address }}</textarea>
                            </div>
                        </div>

                        <div class="card-footer">
                        <button type="submit" class="btn btn-primary">Actualizar Profesor</button>
                        </div>
                    </form>
                </div>

{% endblock content %}