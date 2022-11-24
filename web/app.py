from flask import Flask, render_template, request, redirect, url_for
import sys
sys.path.insert(0, '/Users/a-manonearth/Sites/ST/Scanning Engine')
sys.path.insert(0, '/Users/a-manonearth/Sites/ST/Rating Engine')
sys.path.insert(0, '/Users/a-manonearth/Sites/ST/NFT Engine')
sys.path.insert(0, '/Users/a-manonearth/Sites/ST/Reporting Engine')

from rate import rating
from main import check_xss, scan_sql_injection, get_all_forms
from nft import host_nft, generate_image
from report import pdf_generation
import json
import pickle as pk
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index1.html')

def rfc_preproc(url):
    if "https://" in url:
        val = 1
    elif "http://" in url:
        val=0
    x= str(get_all_forms(url))
    df = [[len(x),1,1,val]]
    df = pd.DataFrame(df)
    return df

def pre_scan_injection(URL):
    if "=" in URL:
        sqli = scan_sql_injection(URL)
    else:
        sqli = 0
    return sqli

@app.route('/kolaTest3.0', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('team-single.html')
    else:
        URL = request.form['url']
        favicon = request.form['favicon']
        if URL:
            kola_rfc = pk.load(open('kola_rfc.pickle', 'rb'))
            test_cases = kola_rfc.predict(rfc_preproc(URL))
            if test_cases[0] ==2:
                ll, ll1 = check_xss(URL)
                # ll1 = json.loads(ll1)
                if len(URL.split("=")) != 1:
                    sqli = pre_scan_injection(URL)
            else:
                ll = check_xss(URL)
            try:
                pdf_generation(ll1, URL)
                ratings = rating(ll[2], sqli)
            except:
                ratings = 5
            generate_image("background.png", favicon, ratings)
            nft = host_nft("output.png")

            return render_template('test.html', web=URL, len= len(ll[0]), nft_link = nft, result=ll[0], jsonfile = json.dumps(ll[1]), vuln=ll[2], rat=ratings)
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
