from flask import render_template

from app import app


@app.errorhandler(404)
def page_not_found(e):
    # if page not found - redirects to 404 error page
    return render_template('404_page.html'), 404
