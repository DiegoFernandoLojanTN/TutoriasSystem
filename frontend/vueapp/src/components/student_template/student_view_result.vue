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
                                    <h3 class="card-title">Resultados</h3>
                                </div>
                                <div class="card-body">
                                <div class="table-responsive">
                                        <table class="table">
                                            <thead class="thead-light">
                                            <tr>
                                                <th>#ID</th>
                                                <th>Tutoría</th>
                                                <th>Marcas asignadas</th>
                                                <th>Marcas examen</th>
                                                <th>Estado</th>
                                            </tr>
                                            </thead>
                                            {% for row in student_result %}
                                            <tr>
                                                <td>{{ row.id }}</td>
                                                <td>{{ row.subject_id.subject_name }}</td>
                                                <td>{{ row.subject_assignment_marks }}</td>
                                                <td>{{ row.subject_exam_marks }}</td>
                                                <td>
                                                    {% if row.subject_exam_marks >= 40 %}
                                                        <span class="alert alert-success">Aprobado</span>
                                                    {% else %}
                                                        <span class="alert alert-danger">Reprobado</span>
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