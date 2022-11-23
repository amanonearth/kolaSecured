from flask import Flask, render_template, request, redirect, url_for
import sys
sys.path.insert(0, '/Users/a-manonearth/Sites/ST/Scanning Engine')
sys.path.insert(0, '/Users/a-manonearth/Sites/ST/Rating Engine')
from rate import rating
from main import check_xss, scan_sql_injection
import json


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/kolaTest3.0', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('team-single.html')
    else:
        URL = request.form['url']
        if URL:
            ll = check_xss(URL)
            sqli = scan_sql_injection(URL)
            ratings = rating(ll[2], sqli)
            return render_template('test.html', web=URL, len= len(ll[0]), result=ll[0], jsonfile = json.dumps(ll[1]), vuln=ll[2], rat=ratings)
        else:
            return render_template('team-single.html')
    

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html')

@app.route('/about', methods=['GET','POST'])
def about():
    if request.method == 'GET':
        return render_template('about.html')


@app.route('/services', methods=['GET','POST'])
def services():
    if request.method == 'GET':
        return render_template('services.html')

@app.route('/kolaSecured3.1', methods=['GET','POST'])
def kolaSecured():
    if request.method == 'GET':
        return render_template('kolaSecured3.1.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
