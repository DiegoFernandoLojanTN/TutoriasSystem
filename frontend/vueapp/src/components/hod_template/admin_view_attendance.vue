{% extends 'hod_template/base_template.vue' %}
{% load static %}

{% block content %}

<div class="dashboard-wrapper">
    <div class="dashboard-ecommerce">
        <div class="container-fluid dashboard-content">

            <div class="row">
                <div class="col-md-12">
                    <!-- general form elements -->
                    <div class="card card-primary">
                    <div class="card-header">
                        <h3 class="card-title">Ver Asistencia</h3>
                    </div>
                        {% comment %} Display Messages {% endcomment %}
                        {% include 'message.vue' %}
                            
                        <div class="card-body">
                           
                            <div class="form-group">
                                <label>Tutoria </label>
                                <select class="form-control" name="subject" id="subject">
                                    {% for subject in subjects %}
                                        <option value="{{ subject.id }}">{{ subject.subject_name }}</option>
                                    {% endfor %}
                                </select>
                            </div>

                            <div class="form-group">
                                <label>Fecha de Reunion </label>
                                <select class="form-control" name="session_year_id" id="session_year_id">
                                    {% for session_year in session_years %}
                                        <option value="{{ session_year.id }}">{{ session_year.session_start_year }} hasta {{ session_year.session_end_year }}</option>
                                    {% endfor %}
                                </select>
                            </div>


                        </div>
                        <!-- /.card-body -->

                        <div class="card-footer">
                            <button type="button" class="btn btn-primary" id="fetch_attendance">Obtener fecha de asistencia</button>
                        </div>

                        <div class="card-footer">
                            <div class="form-group" id="attendance_block" style="display:none;">
                                    <label>Fecha de asistencia</label>
                                    <select class="form-control" name="attendance_date" id="attendance_date">
                                        
                                    </select>
                                </div>
                            </div>

                            <div class="form-group">
                                <div class="alert alert-danger" id="error_attendance" style="display:none;">

                                </div>

                                <div class="alert alert-success" id="success_attendance" style="display:none;">
                                    
                                </div>
                            </div>

                            <div class="card-footer" id="fetch_student_block" style="display:none;">
                                <button type="button" class="btn btn-primary" id="fetch_student">Obtener datos del estudiante</button>
                            </div>
                            <div class="card-footer" id="student_data"></div>
                        </div>

{% endblock content %}

{% block custom_js %}

<script>
    $(document).ready(function(){
        

        //Fetching Attendance Date

        $("#fetch_attendance").click(function(){
                var subject = $("#subject").val()
                var session_year_id = $("#session_year_id").val()


                $.ajax({
                    url:'{% url 'admin_get_attendance_dates' %}',
                    type:'POST',
                    data:{subject:subject, session_year_id:session_year_id},
                })

                
                .done(function(response){
                    var json_data = JSON.parse(response);
                    if(json_data.length>0)
                    {
                        var html_data = "";
                        for (key in json_data)
                        {
                            html_data+="<option value='"+ json_data[key]["id"] +"'>"+ json_data[key]["attendance_date"] +"</option>"
                        }
                        $("#error_attendance").vue("");
                        $("#error_attendance").hide();
                        $("#attendance_block").show();
                        $("#fetch_student_block").show();
                        $("#attendance_date").vue(html_data);
                        //console.log(response)
                        //alert("Something")
                    }
                    else
                    {
                        $("#error_attendance").vue("No se encontraron datos de asistencia.");
                        $("#error_attendance").show();
                        $("#attendance_block").hide();
                        $("#fetch_student_block").hide();
                        $("#attendance_date")="" //Empty the Date Dropdown also
                    }
                    
                })

                .fail(function(){
                    alert("Error al obtener las fechas de asistencia.")
                    $("#error_attendance").vue("");
                    $("#fetch_student_block").hide();
                    $("#attendance_block").hide();
                });

                
        })

        // Ahora trabajando en Buscar estudiante después de la fecha de asistencia seleccionada
        $("#fetch_student").click(function(){

            // Visualización de estudiantes según el personal, el curso y la sesión inscritos
            var attendance_date=$("#attendance_date").val()

            $.ajax({
                url:'{% url 'admin_get_attendance_student' %}',
                type:'POST',
                data:{attendance_date:attendance_date},
            })

            
            .done(function(response){
                var json_data=JSON.parse(response);
                //console.log(json_data)
                //Displaying Attendance Date Input and Students Attendance
                var div_data="<div class='form-group'><label>Asistencia Estudiantil: </label></div>"
                div_data+="<div class='form-group'><div class='row'>"

                for(key in json_data)
                {
                    div_data+="<div class='col-lg-3'><div class='form-check'>";

                    div_data+="<label class='form-check-label'>"+ json_data[key]['name']+" </label> ";
                    
                    // Displaying Present and Absent

                    if(json_data[key]['status'])
                    {
                        div_data+="<b>[ Present ]</b>";
                    }
                    else
                    {
                        div_data+="<b>[ Absent ]</b>";
                    }
                    //Displaying Present and Absent Ends Here
                    

                    div_data+="</div></div> ";
                }
                div_data+="</div></div>";
                
                $("#student_data").vue(div_data);

            })
            .fail(function(){
                alert("Error al obtener estudiantes.")
            })


        })

    })
</script>
{% endblock custom_js %}