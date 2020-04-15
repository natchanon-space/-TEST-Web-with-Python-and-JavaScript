//setup flask for Windows
    set FLASK_APP=app.py
    set FLASK_ENV=development

//note
    "index.html" and any other template files should be stored in a directory named templates

//hyperlink ex.
    <a href="{{ url_for('function')}}"> ... </a>
