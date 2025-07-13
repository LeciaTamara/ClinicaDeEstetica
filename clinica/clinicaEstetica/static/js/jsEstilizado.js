<script>
    document.getElementById("mostrarMais").addEventListener("click", ()){
        fetch("{% url 'mostrarServicos' %}")
        .then(response => response.text())
        .then(html => {
            document.getElementById()
        })
    }
</script>