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
                            <h3 class="card-title">Revisar Estudiante</h3>
                        </div>
                        <div class="table-responsive">
                            <table class="table">
                                <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>ID Estudiante</th>
                                    <th>Nombre Estudiante</th>
                                    <th>Fecha</th>
                                    <th>Mensaje</th>
                                    <th>Creado a</th>
                                    <th>Acciones</th>
                                </tr>
                                </thead>
                                {% for leave in leaves %}
                                <tbody>
                                <tr>
                                    <td>{{ leave.id }}</td>
                                    <td>{{ leave.student_id.admin.id }}</td>
                                    <td>{{ leave.student_id.admin.first_name }} {{ feedback.student_id.admin.last_name }}</td> 
                                    <td>{{ leave.leave_date }}</td>
                                    <td>{{ leave.leave_message }}</td>
                                    <td>{{ leave.created_at }}</td>
                                    <td>
                                        {% if leave.leave_status == 0 %}
                                            <a href="{% url 'student_leave_approve' leave_id=leave.id %}" class="btn btn-success">Approve</a>
                                            <a href="{% url 'student_leave_reject' leave_id=leave.id %}" class="btn btn-danger">Reject</a>
                                        {% elif leave.leave_status == 1 %}
                                            <button class="btn btn-warning" disabled="disabled">Aprobado</button>
                                        {% else %}
                                            <button class="btn btn-danger" disabled="disabled">Rechazado</button>
                                        {% endif %}
                                    </td>
                                </tr>
                                </tbody>
                                {% endfor %}
                            </table>
                        </div>
                    </div>
                </div>
            </div>

{% endblock content %}