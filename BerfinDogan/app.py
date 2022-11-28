from flask import Flask, render_template, request, redirect, url_for
import os,subprocess
import json
from flask import jsonify

__author__ = 'Berfin Dogan'

###############################################################
with open("nosql_data.json","w") as f:
    f.write("{}")
###############################################################


app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="GET":
        return render_template("index.html")
    if request.method=="POST":
        global link_
        link_=request.form["fname"]
        return redirect(url_for('generated_link'))
        #return redirect(url_for('ip_logger',link_=link_))
    

@app.route("/<link_>",methods=["GET"])
def ip_logger(link_):
    
    subprocess.call(["D:\Python\python.exe","ip_logger.py",request.remote_addr])
    return jsonify({'ip': request.remote_addr}), 200

@app.route("/generated_link",methods=["GET"])
def generated_link():
    link='http://berfindogan.ml/%s'%(link_)
    return render_template("link.html",link=link)

@app.route("/About")
def about():
    return render_template("about.html")
@app.route("/info")
def info():
    return render_template("info.html")
@app.route("/results",methods=["GET"])
def results():
    with open('nosql_data.json', 'r') as f:
        data = json.load(f)
    print(data)
    return render_template("ip_results.html",results1=data['IP'],results2=data['STATUS'],results3=data['COUNTRY'],results4=data['COUNTRY CODE'],results5=data['REGION'],results6=data['CITY'],results7=data['ZIP'],results8=data['LAT'],results9=data['LON'],results10=data['TIMEZONE'],results11=data['ISP NAME'])

if __name__ == "__main__":
    app.run('0.0.0.0',80)
