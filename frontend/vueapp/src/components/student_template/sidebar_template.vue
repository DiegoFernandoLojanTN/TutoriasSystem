<div class="nav-left-sidebar sidebar-dark">
    <div class="menu-list">
        <nav class="navbar navbar-expand-lg navbar-light">
            <a class="d-xl-none d-lg-none" href="">Panel</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation"><span
                    class="navbar-toggler-icon"></span></button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="nav nav-pills nav-sidebar flex-column">
                    <li class="nav-divider">Menu</li>

					<li class="nav-item">
						{% url 'student_view_attendance' as student_view_attendance %}
						<a href="{{ student_view_attendance }}" class="nav-link {% if request.path == student_view_attendance %} active {% endif %}">
							<span class="fa fa-fw fa-calendar-alt"></span>&nbsp&nbsp&nbspVer Asistencia
						</a>
					</li>

					<li class="nav-item">
						{% url 'student_view_result' as student_view_result %}
						<a href="{{ student_view_result }}" class="nav-link {% if request.path == student_view_result %} active {% endif %}">
							<span class="fa fa-fw fa-tasks"></span>&nbsp&nbsp&nbspVer Resultado
						</a>
					</li>

					<li class="nav-item">
						{% url 'student_apply_leave' as student_apply_leave %}
						<a href="{{ student_apply_leave }}" class="nav-link {% if request.path == student_apply_leave %} active {% endif %}">
							<span class="fa fa-fw fa-envelope-open"></span>&nbsp&nbsp&nbspSolicitar baja
						</a>
					</li>

					<li class="nav-item">
						{% url 'student_feedback' as student_feedback %}
						<a href="{{ student_feedback }}" class="nav-link {% if request.path == student_feedback %} active {% endif %}">
							<span class="fa fa-fw fa-comments"></span>&nbsp&nbsp&nbspEnviar Comentario
						</a>
					</li>
                </ul>
            </div>
        </nav>
    </div>
</div>