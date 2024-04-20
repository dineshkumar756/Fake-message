import sqlite3
import hashlib
import datetime
import MySQLdb
from flask import session
from flask import Flask, request, send_file
import io
import base64
import pandas as pd
import pickle
import re
import os
import numpy as np

pickle_in = open('model_fakenews.pickle','rb')
pac = pickle.load(pickle_in)
tfid = open('tfid.pickle','rb')
tfidf_vectorizer = pickle.load(tfid)

def db_connect():
    _conn = MySQLdb.connect(host="localhost", user="root",
                            passwd="root", db="fn")
    c = _conn.cursor()

    return c, _conn



# -------------------------------Registration-----------------------------------------------------------------

def uactivate1(b,d):
    try:
        c, conn = db_connect()
        print(b,d)
        id="0"
        
        j = c.execute("update owner set status='activated' where username='"+b+"' and email='"+d+"'")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))

def ucloud1(b,d,fdata):
    try:
        c, conn = db_connect()
        print(b,d)
        id="0"
        abc = fdata
        input_data = [abc.rstrip()]
        # transforming input
        tfidf_test = tfidf_vectorizer.transform(input_data)
        # predicting the input
        y_pred = pac.predict(tfidf_test)
        result='' 
         
        val=0
        print("ccccccccccccccccccccccccccccccccccccccc")
        print(y_pred[0])
        if y_pred[0] == 'FAKE':
           result='Fake message'          
        else:
           result='Genuine message'     

        status1 = result
        
        j = c.execute("update upload set status='uploadtocloud' ,status1='"+status1+"' where fname='"+b+"' and email='"+d+"'")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))
    
def uactivate3(b,d):
    try:
        c, conn = db_connect()
        print(b,d)
        id="0"
        
        j = c.execute("update user set status='activated' where username='"+b+"' and email='"+d+"'")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))


def vr3(b,d,f):
    try:
        c, conn = db_connect()
        print(b,d)
        id="0"
        
        j = c.execute("update request set status='verified' where fname='"+b+"' and email='"+d+"' and uemail='"+f+"'")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))

def send2(b,d,f):
    try:
        c, conn = db_connect()
        print(b,d)
        id="0"
        
        j = c.execute("update request set status='keysent' where fname='"+b+"' and email='"+d+"' and uemail='"+f+"'")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))


def urequest1(b,c1,f,g,i1):
    try:
        c, conn = db_connect()
        print(b,c1,f,g,i1)
        id="0"
        uemail = session['email']
        j = c.execute("insert into request (id,fname,email,ctext,uemail,msg,status) values ('"+id +
                      "','"+b+"','"+c1+"','"+f+"','"+uemail+"','"+i1+"','requested')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))

def inc_reg(username,password,email,address):
    try:
        c, conn = db_connect()
        print(username,password,email,address)
        id="0"
        status = "pending"
        j = c.execute("insert into user (id,username,password,email,address) values ('"+id +
                      "','"+username+"','"+password+"','"+email+"','"+address+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))

def upload_file(fname,email,string_data,aesencrypted,strkey1):
    try:
        c, conn = db_connect()
        print(fname,email,string_data,aesencrypted,strkey1)
       
        id="0"
        status = "pending"
        status1 = "pending"
        j = c.execute("insert into upload (id,fname,email,data,skey,ctext,status,status1) values ('"+id +
                      "','"+fname+"','"+email+"','"+string_data+"','"+strkey1+"','"+aesencrypted+"','"+status+"','"+status1+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))

def owner_reg(username,password,email,address):
    try:
        c, conn = db_connect()
        print(username,password,email,address)
        id="0"
        status = "pending"
        j = c.execute("insert into owner (id,username,password,email,address) values ('"+id +
                      "','"+username+"','"+password+"','"+email+"','"+address+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))
    



# def vp():
#     c, conn = db_connect()
#     c.execute("select * from owner ")
#     result = c.fetchall()
#     conn.close()
#     print("result")
#     return result


def cvf1():
    c, conn = db_connect()
    c.execute("select * from upload ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result


def ovf1():
    c, conn = db_connect()
    email = session['email']
    c.execute("select * from upload where email='"+email+"' ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def vr1():
    c, conn = db_connect()
    c.execute("select * from request where status='requested' ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result


def uvf1():
    c, conn = db_connect()
    c.execute("select * from upload where status='uploadtocloud' ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def vr4(d,f):
    c, conn = db_connect()
    c.execute("select * from request where email='"+d+"' and uemail='"+f+"' ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def send1(b,d,f):
    c, conn = db_connect()
    c.execute("select skey from upload where fname='"+b+"' and email='"+d+"' ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result


def download1():
    c, conn = db_connect()
    uemail = session['email']
    c.execute("select * from request where  uemail='"+uemail+"' and status='keysent' ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result



    





def vuact():
    c, conn = db_connect()
    c.execute("select * from user  ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result










# # -------------------------------Registration End-----------------------------------------------------------------
# # -------------------------------Loginact Start-----------------------------------------------------------------

def admin_loginact(username, password):
    try:
        c, conn = db_connect()
        j = c.execute("select * from admin where username='" +
                      username+"' and password='"+password+"'")
        c.fetchall()
        conn.close()
        return j
    except Exception as e:
        return(str(e))


def cloud_log(username, password):
    try:
        c, conn = db_connect()
        j = c.execute("select * from cloud where username='" +
                      username+"' and password='"+password+"'")
        c.fetchall()
        conn.close()
        return j
    except Exception as e:
        return(str(e))

def aa_log(username, password):
    try:
        c, conn = db_connect()
        j = c.execute("select * from aa where username='" +
                      username+"' and password='"+password+"'")
        c.fetchall()
        conn.close()
        return j
    except Exception as e:
        return(str(e))


def ins_loginact(email, password):
    try:
        c, conn = db_connect()
        
        j = c.execute("select * from user where email='" +
                      email+"' and password='"+password+"'  "  )
        c.fetchall()
        
        conn.close()
        print(".....")
        print(c)
        return j
    except Exception as e:
        return(str(e))

def owner_login(email, password):
    try:
        c, conn = db_connect()
        
        j = c.execute("select * from owner where email='" +
                      email+"' and password='"+password+"'  "  )
        c.fetchall()
        
        conn.close()
        return j
    except Exception as e:
        return(str(e))

if __name__ == "__main__":
    print(db_connect())
