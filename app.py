import sys
import subprocess
import pkg_resources

required = {'flask'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
print("checking files")

from flask import Flask,render_template
try: 
    app = Flask(__name__)

    @app.route('/')
    def Home():
        return render_template('home.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/contact')
    def contact():
        return render_template('contact.html')


    @app.route('/temp')
    def temp():
        return render_template('temp_test.html')


except Exception:
    pass

app.run('host=0.0.0.0')
