{% extends 'hod_template/base_template.vue' %}
{% load static %}

{% block content %}

        <div class="dashboard-wrapper">
            <div class="dashboard-ecommerce">
                <div class="container-fluid dashboard-content">
                    <a class="btn btn-primary" href="{% url 'add_session' %}" role="button">+ Agregar Sesión</a> <br/>&nbsp;
                    {% comment %} Display Messages {% endcomment %}
                    {% include 'message.vue' %}

                    <div class="row">
                        <div class="col-md-12">
                            <div class="card">
                                <div class="card-header">
                                    <h3 class="card-title">Detalles</h3>

                                    <div class="card-tools">
                                    <div class="input-group input-group-sm" style="width: 150px;">
                                        <input type="text" name="table_search" class="form-control float-right" placeholder="Buscar">

                                        <div class="input-group-append">
                                        <button type="submit" class="btn btn-default"><i class="fas fa-search"></i></button>
                                        </div>
                                    </div>
                                    </div>
                                </div>
                                <div class="card-body table-responsive p-0">
                                    <table class="table table-hover text-nowrap">
                                        <thead>
                                            <tr>
                                            <th>ID</th>
                                            <th>Fecha de inicio de sesión</th>
                                            <th>Fecha de finalización de la sesión</th>
                                            <th>Acciones</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            {% for session_year in session_years %}
                                            <tr>
                                            <td>{{ session_year.id }}</td>
                                            <td>{{ session_year.session_start_year }}</td>
                                            <td>{{ session_year.session_end_year }}</td>
                                            <td>
                                                <a href="{% url 'edit_session' session_year.id %}" class="btn btn-success">Editar</a> 
                                                <a href="{% url 'delete_session' session_year.id %}" class="btn btn-danger">Eliminar</a>
                                            </td>
                                            </tr>
                                            {% endfor %}
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                    </div>

{% endblock content %}