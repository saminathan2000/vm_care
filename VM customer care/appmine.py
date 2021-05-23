# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 18:48:33 2021

@author: saminathan
"""
import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask_mail import Mail, Message

#mysql config
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'remotemysql.com'
app.config['MYSQL_USER'] = 'S6aZ89wZGp'
app.config['MYSQL_PASSWORD'] = 'Fop6x99LzK'
app.config['MYSQL_DB'] = 'S6aZ89wZGp'
mysql = MySQL(app)
app.secret_key = 'a'


#sendgrid config
app.config['SECRET_KEY'] = 'top-secret!'
app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'apikey'
app.config['MAIL_PASSWORD'] = os.environ.get('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')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('saminathanhappy@gmail.com')
app.config.from_pyfile('sendgridcon.env')
mail = Mail(app)

@app.route('/')
def home():
    return render_template("login.html")

@app.route('/uploaddata',methods =["POST"])
def uploaddata():
   if(request.method=="POST"):   
    email=request.form["email"]
    password=request.form["your_pass"]
    '''cursor=mysql.connection.cursor()
    cursor.execute('INSERT INTO newtable VALUES(NULL,%s,%s,%s,%s)',(name,email,stream,address))
    mysql.connection.commit()
    a="You have successfully registered "'''
    if(email=="saminathanhappy@gmail.com"):
        a="sammm"
    else:
        a="noneee"
   return render_template("login.html",msg=a)  
    
@app.route('/register')
def reg():
    return render_template("register.html")

@app.route('/register_det',methods =['GET', 'POST'])
def regform():
   msg="Successfully registered" 
   if request.method == 'POST' : 
    name=request.form["name"]
    email=request.form["mailid"]
    password=request.form["pass"]
    repassword=request.form["re_pass"]
    mobile=request.form["mobile"]
    address=request.form["address"]
    city=request.form["city"]
    state=request.form["state"]
    pincode=request.form["pincode"]
    
    if(password!=repassword):
        msg="password mismatch"
    cursor=mysql.connection.cursor()
    cursor.execute('SELECT name FROM user_details WHERE email=%s',(email,))
    mysql.connection.commit()
    name1=cursor.fetchone()
    if(name1!=None):
        msg="Email already registered!"
        
    if(msg=="Successfully registered"):
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO user_details VALUES(%s,%s,%s,%s,%s,%s,%s,%s)',(name,email,password,mobile,address,city,state,pincode))
        mysql.connection.commit()
   return render_template('register.html',msg=msg)
@app.route('/display')
def display():
    cursor=mysql.connection.cursor()
    na="saminathan"
    cursor.execute('DELETE FROM user_detail WHERE city="city1"')
    mysql.connection.commit()
    #account=cursor.fetchone()

@app.route('/mailer')
def index():
    if True:
        recipient = "saminathanpersonnel@gmail.com"
        msg = Message('Twilio SendGrid Test Email', recipients=[recipient])
        msg.body = ('Congratulations! You have sent a test email with '
                    'Twilio SendGrid!')
        msg.html = ('<h1>Twilio SendGrid Test Email</h1>'
                    '<p>Congratulations! You have sent a test email with '
                    '<b>Twilio SendGrid</b>!</p>')
        mail.send(msg)
        
    return render_template('register.html')

    return render_template("register.html") 
if __name__=='__main__':
    app.run(debug=True)
