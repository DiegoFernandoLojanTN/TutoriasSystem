{% if messages %}
    <div class="form-group">
        <div class="col-12">
        {% for message in messages %}
            {% if message.tags == 'error' %}
            <div class="alert alert-danger alert-dismissible fade show" role="alert" style="margin-top: 10px;">
                {{ message }}
                <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            </div>
            {% elif message.tags == 'success' %}
            <div class="alert alert-success alert-dismissible fade show" role="alert" style="margin-top: 10px;">
                {{ message }}
                <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            </div>
            {% endif %}
        {% endfor %}
        </div>
    </div>
{% endif %}