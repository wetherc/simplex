class SimplexView():
    def __init__(self):
        self.title = 'Simplex'

    def render_head(self):
        head = """
        <!doctype html>
        <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en-us">
            <head>
            <title>Simplex</title>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <meta http-equiv="x-ua-compatible" content="ie=edge">

            <link
                rel="stylesheet"
                type=text/css
                href="{{ url_for('static', filename='css/base/standard-page-view.css') }}">
            <link
                rel="stylesheet"
                type=text/css
                href="{{ url_for('static', filename='css/base/main-menu-view.css') }}">
            <link
                rel="stylesheet"
                type=text/css
                href="{{ url_for('static', filename='css/base/nav-view.css') }}">
            </head>
            <body class="page">
            <div class="simplex-page-frame">
        """
        return head

    def render_foot(self):
        foot = """
            </div>  <!-- simplex-page-frame div from header.html -->
        </body>
        <footer>
            <link
            rel="stylesheet"
            type=text/css
            href="{{ url_for('static', filename='external/fontawesome/css/fontawesome.min.css') }}">
            <link
            rel="stylesheet"
            type=text/css
            href="{{ url_for('static', filename='external/fontawesome/css/solid.min.css') }}">
            <link
            rel="stylesheet"
            type=text/css
            href="{{ url_for('static', filename='external/roboto/css/roboto.css') }}">

            <!--
            NOTE: To generate new SRI hashes, you can use
                openssl dgst -sha384 -binary FILENAME.js | openssl base64 -A
            -->
            <!-- <script
            src="{{ url_for('static', filename='js/my-js.js') }}"
            charset="utf-8"
            integrity="sha384-YkP4Y4ArFRZR0Fi01n5cc8Mdm+Occbi9d1kx9b680m1KYVoZHbSUMTad6eeAv9/j"
            crossorigin="anonymous">
            </script> -->
        </footer>
        </html>
        """
        return foot
