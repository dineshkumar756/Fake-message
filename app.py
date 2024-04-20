import os
import MySQLdb
import smtplib
import random
import string
from datetime import datetime
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash, send_file
from database import db_connect,inc_reg,admin_loginact,ins_loginact,vuact
from database import db_connect,owner_reg,owner_login,cloud_log,aa_log,upload_file,cvf1,ucloud1,uvf1,urequest1,vr3,vr4,vr1,send1,send2,download1,ovf1
# from cloud import uploadFile,downloadFile,close
import Crypto.Cipher
from AES import AESCipher
import random
import base64
import cv2
from cloud import upload_file_to_drivehq
from sendmail import sendmail
from main import generateblockchain
import json, nltk

# def db_connect():
#     _conn = MySQLdb.connect(host="localhost", user="root",
#                             passwd="root", db="assigndb")
#     c = _conn.cursor()

#     return c, _conn


app = Flask(__name__)
app.secret_key = os.urandom(24)

with open('contractions.json', 'r') as f:
    contractions_dict = json.load(f)
contractions = contractions_dict['contractions']

@app.route("/")
def FUN_root():
    return render_template("index.html")
    
@app.route("/upload.html")
def admin():
    return render_template("upload.html")

@app.route("/ohome.html")
def ohome():
    return render_template("ohome.html")

@app.route("/uhome.html")
def uhome():
    return render_template("uhome.html")

@app.route("/chome.html")
def chome():
    return render_template("chome.html")

@app.route("/ahome.html")
def ahome():
    return render_template("ahome.html")

@app.route("/owner.html")
def owner():
    return render_template("owner.html")

@app.route("/ownerreg.html")
def ownerreg():
    return render_template("ownerreg.html")

@app.route("/cloud.html")
def cloud():
    return render_template("cloud.html")

@app.route("/aa.html")
def aa():
    return render_template("aa.html")


@app.route("/user.html")
def ins():
    return render_template("user.html")


@app.route("/increg.html")
def increg():
    return render_template("increg.html")



@app.route("/adminhome.html")
def adminhome():
    return render_template("adminhome.html")



@app.route("/ihome.html")
def ihome():
    return render_template("ihome.html")

@app.route("/vo.html")
def vo():
    data = vp()
    print(data)
    return render_template("vo.html",data = data)

@app.route("/cvf.html")
def cvf():
    data = cvf1()
    print(data)
    return render_template("cvf.html",data = data)

@app.route("/ovf.html")
def ovf():
    data = ovf1()
    print(data)
    return render_template("ovf.html",data = data)

@app.route("/vr.html")
def vr():
    data = vr1()
    print(data)
    return render_template("vr.html",data = data)


@app.route("/uvf.html")
def uvf():
    data = uvf1()
    print(data)
    return render_template("uvf.html",data = data)



@app.route("/download.html")
def download():
    data = download1()
    print(data)
    return render_template("download.html",data = data)





@app.route("/vu.html")
def vu():
    data = vuact()
    print(data)
    return render_template("vu.html",data = data)








@app.route("/index")
def index():
    return render_template("index.html") 


def read_text_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print("File not found at the specified path.")
        return None

import re

def process_tweet(tweet):
    tweet = tweet.lower()                                             # Lowercases the string
    tweet = re.sub('@[^\s]+', '', tweet)                              # Removes usernames
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', ' ', tweet)   # Remove URLs
    tweet = re.sub(r"\d+", " ", str(tweet))                           # Removes all digits
    tweet = re.sub('&quot;'," ", tweet)                           # Remove (&quot;) 
                                                 # Replaces Emojis
    tweet = re.sub(r"\b[a-zA-Z]\b", "", str(tweet))                   # Removes all single characters
    for word in tweet.split():
        if word.lower() in contractions:
            tweet = tweet.replace(word, contractions[word.lower()])   # Replaces contractions
    tweet = re.sub(r"[^\w\s]", " ", str(tweet))                       # Removes all punctuations
    tweet = re.sub(r'(.)\1+', r'\1\1', tweet)                         # Convert more than 2 letter repetitions to 2 letter
    tweet = re.sub(r"\s+", " ", str(tweet))                           # Replaces double spaces with single space    
    return tweet


@app.route("/ucloud", methods = ['GET','POST'])
def ucloud():
    b = request.args.get('b')
    d = request.args.get('d')
    g = request.args.get('g')
    file_path = "C:/Users/Sai Krishna/OneDrive/Desktop/upload/"+ b
    username = 'projectsforu'
    password = '1000projects@shan'
    remote_directory = '/cloud'
    fdata=read_text_from_file(file_path)
    pdata=process_tweet(fdata)
    #upload_file_to_drivehq(file_path, username, password, remote_directory)
    data = ucloud1(b,d,pdata)
    return render_template("chome.html")




@app.route("/urequest", methods = ['GET','POST'])
def urequest():
    b = request.args.get('b')
    c1 = request.args.get('c')
    f = request.args.get('f')
    g = request.args.get('g')
    i1= request.args.get('h')
    data = urequest1(b,c1,f,g,i1)
    return render_template("uhome.html")


@app.route("/vr2", methods = ['GET','POST'])
def vr2():


    b = request.args.get('b')
    c1 = request.args.get('c')
    d = request.args.get('d')
    f = request.args.get('f')
    g = request.args.get('g')
    if c1 == g:
        data1 = vr3(b,d,f)
        data = vr4(d,f)
        return render_template("send.html",data = data)
    else:
        return render_template("chome.html")
    

@app.route("/send", methods = ['GET','POST'])
def send():


    b = request.args.get('b')
    d = request.args.get('d')
    f = request.args.get('f')
    data = send1(b,d,f)
    skey = data[0][0]
    sendmail(skey,f)
    send2(b,d,f)
    
    return render_template("send.html")

@app.route("/down1", methods = ['GET','POST'])
def down1():


    b = request.args.get('b')
    d = request.args.get('d')
    e = request.args.get('e')
    f = request.args.get('f')
    return render_template("d1.html",b=b,d=d,e=e,f=f)
    

# @app.route("/uactivate")
# def uactivate():
#     status = uviewact(request.args.get('a'),request.args.get('b'))
#     data = admin_viewusers()
#     if status == 1:
#        return render_template("viewusers.html",m1="sucess",users=data)
#     else:
#        return render_template("viewusers.html",m1="failed",users=data)   
# -------------------------------Registration-----------------------------------------------------------------    



@app.route("/inceregact", methods = ['GET','POST'])
def inceregact():
   if request.method == 'POST':    
      
      status = inc_reg(request.form['username'],request.form['password'],request.form['email'],request.form['address'])
      
      if status == 1:
       return render_template("user.html",m1="sucess")
      else:
       return render_template("increg.html",m1="failed")



@app.route("/oregact", methods = ['GET','POST'])
def oregact():
   if request.method == 'POST':    
      
      status = owner_reg(request.form['username'],request.form['password'],request.form['email'],request.form['address'])
      
      if status == 1:
       return render_template("owner.html",m1="sucess")
      else:
       return render_template("ownerreg.html",m1="failed")





@app.route("/uploadact", methods = ['GET','POST'])
def owner_upload():
   if request.method == 'POST':
      file = request.files['file']
      fname  = request.form['fname']
      email = session['email']
      data = file.read()
      print(data)
      
      print(type(data))
      string_data = data.decode('utf-8')
      pdata=process_tweet(string_data)
      print(type(pdata))
      AESkey_16 = os.urandom(16) 
      aescipher = AESCipher(AESkey_16)   
      encodedkey = base64.b64encode(AESkey_16)
      strkey1 = str(encodedkey, 'utf-8')
      aesencrypted = aescipher.encrypt(pdata)
      print('aesEncrypted: %s' % aesencrypted)
      print("encodedAESkey_16: %s" % strkey1)
      print("AESkey_16: %s" % AESkey_16)
      status = upload_file(fname,email,pdata,aesencrypted,strkey1)
      if status == 1:
          return render_template("upload.html",m1="success")
      

def save_string_to_file(file_name, file_content):
    with open(file_name, 'w') as file:
        file.write(file_content)


@app.route("/dact", methods = ['GET','POST'])
def dact():
   if request.method == 'POST':
      fname  = request.form['fname']
      skey  = request.form['skey']
      ctext  = request.form['ctext']            
      decodedkey1 = base64.b64decode(skey)            
      aescipherdec = AESCipher(decodedkey1)   
      aesdecrypted = aescipherdec.decrypt(ctext)
      print(type(aesdecrypted))
      print('aesDecrypted: %s' % aesdecrypted)
      save_string_to_file(fname, aesdecrypted)
      return render_template("uhome.html",m1="success")



      
# #-------------------------------ADD_END---------------------------------------------------------------------------
# # -------------------------------Loginact-----------------------------------------------------------------
@app.route("/adminlogact", methods=['GET', 'POST'])       
def adminlogact():
    if request.method == 'POST':
        status = admin_loginact(request.form['username'], request.form['password'])
        print(status)
        if status == 1:
            session['username'] = request.form['username']
            return render_template("adminhome.html", m1="sucess")
        else:
            return render_template("admin.html", m1="Login Failed")

@app.route("/clogin", methods=['GET', 'POST'])       
def clogin():
    if request.method == 'POST':
        status = cloud_log(request.form['username'], request.form['password'])
        print(status)
        if status == 1:
            session['username'] = request.form['username']
            return render_template("chome.html", m1="sucess")
        else:
            return render_template("cloud.html", m1="Login Failed")

@app.route("/alogin", methods=['GET', 'POST'])       
def alogin():
    if request.method == 'POST':
        status = aa_log(request.form['username'], request.form['password'])
        print(status)
        if status == 1:
            session['username'] = request.form['username']
            return render_template("ahome.html", m1="sucess")
        else:
            return render_template("aa.html", m1="Login Failed")


@app.route("/ologin", methods=['GET', 'POST'])       
def ologin():
    if request.method == 'POST':
        status = owner_login(request.form['email'], request.form['password'])
        print(status)
        if status == 1:
            session['email'] = request.form['email']
            return render_template("ohome.html", m1="sucess")
        else:
            return render_template("owner.html", m1="Login Failed")



@app.route("/inslogin", methods=['GET', 'POST'])       
def inslogin():
    if request.method == 'POST':
        status = ins_loginact(request.form['email'], request.form['password'])
        print(status)
        if status == 1:
            session['email'] = request.form['email']
            return render_template("uhome.html", m1="sucess")
        else:
            return render_template("user.html", m1="Login Failed")
        



# # -------------------------------Loginact End-----------------------------------------------------------------


   
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
