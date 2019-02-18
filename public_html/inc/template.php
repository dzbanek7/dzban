<!DOCTYPE html>
<html lang="pl">

  <head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Strona główna</title>

    <!-- Bootstrap core CSS -->
    <link href="static/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="static/css/scrolling-nav.css" rel="stylesheet">
    <link href="static/css/style.css" rel="stylesheet">

  </head>

  <body id="page-top">

    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top" id="mainNav">
      <div class="container">
        <a class="navbar-brand js-scroll-trigger" href="{{ url_for('index') }}">Strona główna</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto">
            <?php
                get_menu($id);
            ?>
          </ul>
        </div>
      </div>
    </nav>

    <header class="bg-primary text-white">
      <div class="container text-center">
        <h1>Apka w PHP</h1>
        <p class="lead">Dodatkowy tekst</p>
      </div>
    </header>

    <section id="tresc">
      <div class="container">
        <div class="row">
          <div class="col-lg-8 mx-auto">
            {% with komunikaty = get_flashed_messages(with_categories=true) %}
            {% if komunikaty %}
                {% for kat, kom in komunikaty %}
                <p class="{{ kat }}">{{ kom }}</p>
                {% endfor %}
            {% endif %}
            {% endwith %}

            {% block tresc %}{% endblock %}
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="py-5 bg-dark">
      <div class="container">
        <p class="m-0 text-center text-white">Copyright &copy; Your Website 2017</p>
      </div>
      <!-- /.container -->
    </footer>

    <!-- Bootstrap core JavaScript -->
    <script src="static/vendor/jquery/jquery.min"></script>
    <script src="static/vendor/bootstrap/js/bootstrap.bundle.min"></script>

    <!-- Plugin JavaScript -->
    <script src="static/vendor/jquery-easing/jquery.easing.min.js"></script>

    <!-- Custom JavaScript for this theme -->
    <script src="static/js/scrolling-nav.js"></script>

  </body>

</html>
