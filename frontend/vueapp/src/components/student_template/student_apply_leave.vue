{% extends 'student_template/base_template.vue' %}
{% load static %}

{% block content %}

        <div class="dashboard-wrapper">
            <div class="dashboard-ecommerce">
                <div class="container-fluid dashboard-content">
                    <div class="row">
                        <div class="col-md-12">
                            <div class="card card-primary">
                            <div class="card-header">
                                <h3 class="card-title">Solicitar baja</h3>
                            </div>

                            {% comment %} Display Messages {% endcomment %}
                            {% include 'message.vue' %}

                            <form method="POST" action="{% url 'student_apply_leave_save' %}">
                                {% csrf_token %}

                                <div class="card-body">
                                    <div class="form-group">
                                        <label>Fecha</label>
                                        <input type="date" name="leave_date" class="form-control" />
                                    </div>
                                    <div class="form-group">
                                        <label>Razón</label>
                                        <textarea name="leave_message" class="form-control" rows="6" placeholder="Mensaje"></textarea>
                                    </div>
                                </div>

                                <div class="card-footer">
                                    <button type="submit" class="btn btn-primary">Aplicar</button>
                                </div>
                            </form>
                            </div>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col-md-12">
                            <div class="card card-success">
                                <div class="card-header">
                                    <h3 class="card-title">Historial</h3>
                                </div>

                                <div class="card-body">
                                    <div class="table-responsive">
                                        <table class="table">
                                            <thead class="thead-light">
                                                <tr>
                                                <th>#ID</th>
                                                <th>Fecha</th>
                                                <th>Mensaje</th>
                                                <th>Estado</th>
                                                </tr>
                                            </thead>
                                            {% for leave in leave_data %}
                                            <tr>
                                                <td>{{ leave.id }}</td>
                                                <td>{{ leave.leave_date }}</td>
                                                <td>{{ leave.leave_message }}</td>
                                                <td>
                                                    {% if leave.leave_status == 1 %}
                                                        <span class="alert alert-success">Aprobado</span>
                                                    {% elif leave.leave_status == 2 %}
                                                        <span class="alert alert-danger">Rechazado</span>
                                                    {% else %}
                                                        <span class="alert alert-warning">Pendiente</span>
                                                    {% endif %}
                                                </td>
                                            </tr>
                                            {% endfor %}
                                        </table>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

{% endblock content %}