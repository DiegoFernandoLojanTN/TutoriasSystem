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
                        <h3 class="card-title">Agregar Profesor</h3>
                    </div>

                    <form role="form" method="POST" action="{% url 'add_staff_save' %}">
                        {% csrf_token %}
                        {% comment %} Display Messages {% endcomment %}
                        {% include 'message.vue' %}

                        <div class="card-body">
                            <div class="form-group">
                                <label>Correo</label>
                                <input type="email" class="form-control" name="email" placeholder="Ingrese su Correo" id="id_email">
                            </div>

                            <div class="form-group">
                                <label>Nombre de Usuario</label>
                                <input type="text" class="form-control" name="username" placeholder="Ingrese su Nombre de Usuario" id="id_username">
                            </div>

                            <div class="form-group">
                                <label>Contraseña</label>
                                <input type="password" class="form-control" name="password" placeholder="Ingrese su Contraseña">
                            </div>

                            <div class="form-group">
                                <label>Primer Nombre</label>
                                <input type="text" class="form-control" name="first_name" placeholder="Ingrese su Nombre">
                            </div>

                            <div class="form-group">
                                <label>Primer Apellido</label>
                                <input type="text" class="form-control" name="last_name" placeholder="Ingrese su Apellido">
                            </div>

                            <div class="form-group">
                                <label>Direccion</label>
                                <textarea class="form-control" name="address" placeholder="Ingrese su Direccion"></textarea>
                            </div>
                        </div>

                        <div class="card-footer">
                            <button type="submit" class="btn btn-primary">Guardar</button>
                        </div>
                    </form>
                </div>

{% endblock content %}

{% block custom_js %}
{% comment %} Checking if email and username already exists or not usin Ajax {% endcomment %}

    <script>
        $(document).ready(function(){
            // keyup event will be triggered when user leaves keyboard
            $("#id_email").keyup(function(){
                var email = $(this).val();

                if(email!=""){
                    $.ajax({
                        url : '{% url 'check_email_exist' %}',
                        type : 'POST',
                        data : {email:email}
                    })
                    .done(function(response){
                        //console.log(response);

                        if(response == "True"){
                            $(".email_error").remove();
                            $("<span class='email_error' style='color: red; padding: 5px; font-weight: bold;'>Correo electrónico no disponible. </span>").insertAfter("#id_email")
                        }
                        else{
                            $(".email_error").remove();
                            $("<span class='email_error' style='color: green; padding: 5px; font-weight: bold;'> Correo electrónico disponible.</span>").insertAfter("#id_email")
                        }
                    })

                    .fail(function(){
                        console.log("Fallida");
                    })
                }
                else{
                    $(".email_error").remove();
                }
                
            })

            $("#id_username").keyup(function(){
                var username = $(this).val();
                
                if(username!=""){
                    $.ajax({
                        url : '{% url 'check_username_exist' %}',
                        type : 'POST',
                        data : {username:username}
                    })
                    .done(function(response){
                        //console.log(response);

                        if(response == "True"){
                            $(".username_error").remove();
                            $("<span class='username_error' style='color: red; padding: 5px; font-weight: bold;'> Nombre de usuario no disponible. </span>").insertAfter("#id_username")
                        }
                        else{
                            $(".username_error").remove();
                            $("<span class='username_error' style='color: green; padding: 5px; font-weight: bold;'> Nombre de usuario disponible. </span>").insertAfter("#id_username")
                        }
                    })

                    .fail(function(){
                        console.log("Fallido");
                    })
                }
                else{
                    $(".username_error").remove();
                }
                
            })
        })
    </script>

{% endblock custom_js %}