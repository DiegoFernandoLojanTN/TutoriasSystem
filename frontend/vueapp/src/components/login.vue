{% extends 'base.vue' %}
{% load static %}

{% block content %}

<div id="app">
    {% include 'loginTuto.vue' %}
</div>
  
<script>
import Vue from 'vue';
import loginTuto from '@/components/loginTuto.vue';
  
new Vue({
    el: '#app',
    components: {
        loginTuto,
    },
});
</script>

{% endblock %}