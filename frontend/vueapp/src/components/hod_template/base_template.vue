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

<body>
	<div class="dashboard-main-wrapper">
		<!-- navbar -->
		<div class="dashboard-header">
			<nav class="navbar navbar-expand-lg bg-white fixed-top">
				<a class="navbar-brand" href="/">Gestion de Tutorias</a>
				<div class="collapse navbar-collapse " id="navbarSupportedContent">
					<ul class="navbar-nav ml-auto navbar-right-top">
						<li class="nav-item dropdown nav-user">
							<a class="nav-link nav-user-img" href="#" id="navbarDropdownMenuLink2" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fas fa-cog mr-1"></i></a>
							<div class="dropdown-menu dropdown-menu-right nav-user-dropdown" aria-labelledby="navbarDropdownMenuLink2">
								<a class="dropdown-item" href="{% url 'admin_profile' %}"><i class="fas fa-cog mr-2"></i>Configuraciones</a>
								<a class="dropdown-item" href="{% url 'logout_user' %}"><i class="fas fa-power-off mr-2"></i>Cerrar sesión</a>
							</div>
						</li>
					</ul>
				</div>
			</nav>
		</div>
		<!-- end navbar -->

		{% block sidebar %}
			{% include 'hod_template/sidebar_template.vue' %}
		{% endblock %}
		
		{% block content %}
			<div class="dashboard-wrapper">
				<div class="dashboard-ecommerce">
					<div class="container-fluid dashboard-content">
		{% endblock %}

		{% block footer %}
			{% include 'footer.vue' %}
		{% endblock %}

	</div>

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