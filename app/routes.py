# flask
from flask import request, render_template, redirect, url_for, send_from_directory # noQA
# freeze-flask deps
from functools import partial
# data deps
from datetime import datetime
# the app
from app import app

######### build data
########### TODO: replace this stuff with a config object
## find copyright date -relative to (static) site generation
copyright_date = datetime.now().year
employment_status=True
seeking_employment=True


######## routes

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html', title='Home',
                           copyright_date=copyright_date,
                           employment_status=employment_status,
                           seeking_employment=seeking_employment )

if __debug__:
    @app.route('/test')
    @app.route('/test.html')
    def test():
        return render_template('test.html', title='Test',
                               copyright_date=copyright_date,
                               employment_status=employment_status,
                               seeking_employment=seeking_employment )

@app.route('/resume')
@app.route('/resume.html')
def resume():
    return render_template('resume.html', title='Resume',
                           copyright_date=copyright_date,
                           employment_status=employment_status,
                           seeking_employment=seeking_employment )

@app.route('/projects')
@app.route('/projects.html')
def projects():
    return render_template('projects.html', title='Projects',
                           copyright_date=copyright_date)

@app.route('/projects_old')
@app.route('/projects_old.html')
def projects_old():
    return render_template('projects_old.html', title='Older Projects',
                           copyright_date=copyright_date)

@app.route('/about_me')
@app.route('/about_me.html')
def about_me():
    return render_template('about_me.html', title='About Me', copyright_date=copyright_date)

@app.route('/about_site')
@app.route('/about_site.html')
def about_site():
    return render_template('about_site.html', title='About Site', copyright_date=copyright_date)

@app.route('/robots.txt')
@app.route('/sitemap.xml')
@app.route('/README.md')
@app.route('/favicon.ico')
def static_from_root():
    if request.path == '/favicon.ico':
        return send_from_directory(app.static_folder, request.path[1:], mimetype='image/vnd.microsoft.icon')
    return send_from_directory(app.static_folder, request.path[1:])


# freeze-flask will use this to copy these files into root
ROOT_ASSETS = ("favicon.ico", 'README.md', 'robots.txt', 'sitemap.xml')
for asset in ROOT_ASSETS:
    url = "/"+asset
    name = asset.replace(".", "_")
    app.add_url_rule(url, name, partial(app.send_static_file, filename=asset))
