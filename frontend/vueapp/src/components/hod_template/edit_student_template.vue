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
                                <h3 class="card-title">Editar Estudiante</h3>
                            </div>
                            {% comment %} Displaying the Django Form using forms.py EditStudentForm {% endcomment %}
                            {% url 'edit_student_save' as action_path %}
                            {% include 'hod_template/form_template.vue' with messages=messages form=form action_path=action_path button_text="Actualizar Estudiante" %}
                        </div>
                    </div>
                </div>

  {% endblock content %}