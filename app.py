from flask import Flask
from flask import render_template, request
import os, json, requests, string
#from flaskext.mysql import MySQL

app = Flask(__name__)

#mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'Bucket'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

#mysql.init_app(app)
#conn = mysql.connect()
#cursor = conn.cursor()

@app.route('/')
def pilot():
    return render_template('index.html')

@app.route('/getIPaddress')
def getIPaddress():
    url = "http://ip-api.com/json"
    headers = {
        'cache-control': "no-cache",
        'postman-token': "296295f4-b262-d151-48cb-8a1681db44b2"
    }
    response = requests.request("GET", url, headers=headers)
    return response.text;

@app.route('/getAllVisitors')
def getAllVisitors():
    return "yup"    

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000,ssl_context=('cert.pem', 'key.pem'))