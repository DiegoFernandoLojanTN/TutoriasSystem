{% load static %}

<!doctype html>
<html lang="en">
 
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="{% static 'assets/vendor/bootstrap/css/bootstrap.min.css' %}">
    <link href="{% static 'assets/vendor/fonts/circular-std/style.css' %}" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'assets/libs/css/style.css' %}">
    <link rel="stylesheet" href="{% static 'assets/vendor/fonts/fontawesome/css/fontawesome-all.css' %}">
    <link rel="stylesheet" href="{% static 'assets/vendor/charts/chartist-bundle/chartist.css' %}">
    <link rel="stylesheet" href="{% static 'assets/vendor/charts/morris-bundle/morris.css' %}">
    <link rel="stylesheet" href="{% static 'assets/vendor/fonts/material-design-iconic-font/css/materialdesignicons.min.css' %}">
    <link rel="stylesheet" href="{% static 'assets/vendor/charts/c3charts/c3.css' %}">
    <link rel="stylesheet" href="{% static 'assets/vendor/fonts/flag-icon-css/flag-icon.min.css' %}">
    <title>Gestion de Tutorias</title>
    
	{% block custom_css %} {% endblock custom_css %}
    
</head>

<body class="hold-transition login-page" style="margin-left: 30%; margin-right: 30%; margin-top: 10%;">
    
    {% block content %} {% endblock %}

    {% block footer %}
        {% include 'footer.vue' %}
    {% endblock %}

    <script src="{% static 'assets/vendor/jquery/jquery-3.3.1.min.js' %}"></script>
    <script src="{% static 'assets/vendor/bootstrap/js/bootstrap.bundle.js' %}"></script>
    <script src="{% static 'assets/vendor/slimscroll/jquery.slimscroll.js' %}"></script>
    <script src="{% static 'assets/libs/js/main-js.js' %}"></script>
    <script src="{% static 'assets/vendor/charts/chartist-bundle/chartist.min.js' %}"></script>
    <script src="{% static 'assets/vendor/charts/sparkline/jquery.sparkline.js' %}"></script>
    <script src="{% static 'assets/vendor/charts/morris-bundle/raphael.min.js' %}"></script>
    <script src="{% static 'assets/vendor/charts/morris-bundle/morris.js' %}"></script>
    <script src="{% static 'assets/vendor/charts/c3charts/c3.min.js' %}"></script>
    <script src="{% static 'assets/vendor/charts/c3charts/d3-5.4.0.min.js' %}"></script>
    <script src="{% static 'assets/vendor/charts/c3charts/C3chartjs.js' %}"></script>
    <script src="{% static 'assets/libs/js/dashboard-ecommerce.js' %}"></script>
    <script src="{% static 'assets/libs/js/libs.js' %}"></script>

    {% block custom_js %} {% endblock custom_js %}

</body>

</html>