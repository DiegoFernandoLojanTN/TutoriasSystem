{% extends 'student_template/base_template.vue' %}
{% load static %}


{% block custom_css %}
<style>
.attendance_div_red{
    padding: 10px;
    padding-top: 20px;
    background: #f44336;
    border: 10px solid white;
    text-align: center;
    color: #fff;
    border-radius: 30px;
    box-shadow: 1px 1px 1px grey;
    margin-top: 10px;
    margin-bottom: 10px;
}

.attendance_div_green{
    padding: 10px;
    padding-top: 20px;
    background: #4CAF50;
    border: 10px solid white;
    text-align: center;
    color: #fff;
    border-radius: 30px;
    box-shadow: 1px 1px 1px grey;
    margin-top: 10px;
    margin-bottom: 10px;
}
</style>
{% endblock custom_css %}

{% block content %}

        <div class="dashboard-wrapper">
            <div class="dashboard-ecommerce">
                <div class="container-fluid dashboard-content">
                    <div class="row">
                        <div class="col-md-12">
                            <div class="card card-primary">
                            <div class="card-header">
                                <h3 class="card-title">Asistencia para {{ subject_obj.subject_name }}</h3>
                            </div>
            
                            <div class="card-body">
                                <div class="row">
                                    {% for attendance_report in attendance_reports %}
                                        {% if attendance_report.status == True %}
                                            <div class="col-lg-3 attendance_div_green">
                                                <b>Date : {{ attendance_report.attendance_id.attendance_date }}</b> <br/>
                                                    <b>[ Status : Present ]</b>
                                            </div>
                                        {% else %}
                                            <div class="col-lg-3 attendance_div_red">
                                                <b>Date : {{ attendance_report.attendance_id.attendance_date }}</b> <br/>
                                                    <b>[ Status : Absent ]</b>
                                            </div>
                                        {% endif %}
                                    {% endfor %}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

{% endblock content %}