

from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from sendemail import *
import smtplib
import datetime,random
app = Flask(__name__)
  
#mysql config

app.config['MYSQL_HOST'] = 'remotemysql.com'
app.config['MYSQL_USER'] = 'S6aZ89wZGp'
app.config['MYSQL_PASSWORD'] = 'Fop6x99LzK'
app.config['MYSQL_DB'] = 'S6aZ89wZGp'
mysql = MySQL(app)
app.secret_key = 'a'
mailid=""
user_name=""

notify=[["Saminathan","Worker added successfully"],["Ram", "Cannot add worker"]]
usernotify=[["sam","nothing"]]
@app.route('/')
def home():
    return render_template("login.html")

@app.route('/loginpage',methods =['GET', 'POST'])
def login():
    
    global userid,mailid,user_name
    msg = ''
   
  
    if request.method == 'POST' :
        email = request.form['email']
        password = request.form['your_pass']
        if(email=="customercare.vmware@gmail.com" and password=="pass"):
                user_name="admin"
                return redirect(url_for("dash"))
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user_details WHERE email = % s AND password = % s', (email, password ),)
        account = cursor.fetchone()
        print (account)
        if account:
            session['loggedin'] = True
            session['id'] = account[0]
            userid=  account[0]
            session['email'] = account[1]
            user_name=account[0]
            msg = 'Logged in successfully !'
            
            msg = 'Logged in successfully !'
            mailid=email
            return redirect(url_for("userdb"))
            
        else:
            msg = 'Incorrect username / password !'
            return render_template('login.html', msg = msg)

        
@app.route('/register')
def reg():
    return render_template("register.html")
   
@app.route('/register_det', methods =['GET', 'POST'])
def registet():
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
        cursor.execute('INSERT INTO user_details VALUES(%s,%s,%s,%s,%s,%s,%s,%s,"FALSE")',(name,email,password,mobile,address,city,state,pincode))
        mysql.connection.commit()
        msg = 'You have successfully registered !'
        TEXT = "Hello "+name + ",\n\n"+ """Thanks for registring at VMcustomer care """ 
        message  = 'Subject: {}\n\n{}'.format("templatetest", TEXT)
        
        
        
        
        #sendmail(message,email)
        sendgridmail(email,TEXT)
   return redirect(url_for("home"))
            

@app.route('/loginconfirmation/<email>')
def logcheck(email):
    if(user_name==""):
        return redirect(url_for("home"))
    cursor = mysql.connection.cursor()
    cursor.execute('UPDATE user_details SET verification="True" WHERE email=%s',(email,))
    mysql.connection.commit()
    return redirect(url_for("home"))

@app.route('/work_completed/<id>')
def workcompleted(id):
    if(user_name==""):
        return redirect(url_for("home"))
    current_time = datetime.datetime.now()
    cdate=str(current_time.day)+"/"+str(current_time.month)+"/"+str(current_time.year)
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE complaints SET `completed date`=%s WHERE `id`=%s",(cdate,id))
    mysql.connection.commit()
    msg="Complaint id "+id
    msg2="Successfully completed"
    usernotify.insert(0,[msg,msg2])
    return redirect(url_for("userdb"))


@app.route('/user_dashboard')
def userdb():
    if(user_name==""):
        return redirect(url_for("home"))
    print("samiiiii"+user_name)
    return render_template('user_dashboard.html',name=user_name,notificationlist=usernotify)


@app.route('/all_complaints')
def allcomplaints():
    if(user_name==""):
        return redirect(url_for("home"))
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM complaints WHERE name=%s',(user_name,))
    arr=cursor.fetchall()
    mysql.connection.commit()
    return render_template('user/all_complaints.html',arr=arr,name=user_name,notificationlist=usernotify)
    
@app.route('/current_complaints')
def currentcomplaints():
    if(user_name==""):
        return redirect(url_for("home"))
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM complaints WHERE name=%s',(user_name,))
    arr=cursor.fetchall()
    mysql.connection.commit()
    print(arr)
    return render_template('user/current_complaints.html',arr=arr,name=user_name,notificationlist=usernotify)

@app.route('/Workers')
def worker():
    if(user_name!="admin"):
        return redirect(url_for("home"))
    return render_template('admin/add_worker.html',notificationlist=notify)
    
@app.route('/bookcomplaint')
def bookcomplaint():
    if(user_name==""):
        return redirect(url_for("home"))
    return render_template('user/bookcomplaint.html',name=user_name,notificationlist=usernotify)


@app.route('/workerdata', methods =['GET', 'POST'])
def addworker():
   if(user_name!="admin"):
        return redirect(url_for("home"))
   msg="Worker added successfully" 
   if request.method == 'POST' : 
    email=request.form["mailid"]
    name=request.form["name"]
    mobile=request.form["mobile"]
    password=request.form["pass"]
    gender=request.form["gender"]
    
    address=request.form["address"]
    city=request.form["city"]
    
    
    
    cursor=mysql.connection.cursor()
    cursor.execute('SELECT name FROM workers WHERE email=%s',(email,))
    mysql.connection.commit()
    name1=cursor.fetchone()
    if(name1!=None):
        msg="Worker Email already registered!"
        
        
    else:
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO workers VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,"NA")',(name,email,mobile,password,gender,address,city))
        mysql.connection.commit()
        
        
        
        
        
        
        #sendmail(message,email)
        worker_reg(email)
   notify.insert(0,[name,msg])
   return render_template('admin/add_worker.html',notificationlist=notify)


@app.route('/addcomplaint', methods =['GET', 'POST'])
def addcomp():
   if(user_name==""):
        return redirect(url_for("home"))
   msg="worker assigned successfully" 
   msg2="Check your mail for the details"
   if request.method == 'POST' : 
    
    name=request.form["name"]
    complaint=request.form["complaint"]
    product=request.form["product"]
    brand=request.form["brand"]
    contactnum=request.form["contactnum"]
    city=request.form["city"]
    current_time = datetime.datetime.now()
    cdate=str(current_time.day)+"/"+str(current_time.month)+"/"+str(current_time.year)
    
    
    if(True):
        
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM workers WHERE work="NA"')
        freeworkers=cursor.fetchall()
        print("freeeeeeeeeeeeeeeeeeeeeeeeeee")
        print(freeworkers)
        mysql.connection.commit()
        cursor=mysql.connection.cursor()
        cursor.execute('SELECT address FROM user_details WHERE email=%s',(mailid,))
        mysql.connection.commit()
        address=cursor.fetchone()
        
        print(len(freeworkers))
        
        
        assignedw=None
        if(freeworkers==()):
            msg="Sorry! NO workers free"
            msg2="Try again later"
        else:
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO complaints VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,"-")',(name,product,brand,contactnum,city,complaint,cdate))        
            mysql.connection.commit()
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT id FROM complaints ORDER BY ID DESC')
            currid=cursor.fetchone()
            mysql.connection.commit()
            for freeworker in freeworkers:
                if(freeworker[7]==city):
                    assignedw=freeworker
                    
            if(assignedw==None):
                assignedw=freeworkers[random.randint(0,len(freeworkers)-1)]
            print("maaaaaaaail: "+mailid)
            print(name,address,product,brand,contactnum,complaint)
            cursor = mysql.connection.cursor()
            cursor.execute('UPDATE workers SET work=%s WHERE email=%s',("Working on "+str(currid[0]),assignedw[2]))
            mysql.connection.commit()
            #sendmail(message,email)
            add_complaint(assignedw,mailid)
            worker_notify(name,address[0],product,brand,contactnum,complaint,assignedw[2])
   usernotify.insert(0,[msg,msg2])
   return redirect(url_for("userdb"))

@app.route('/dashboard')
def dash():
    if(user_name!="admin"):
        return redirect(url_for("home"))
    return render_template('admin_dashboard.html',notificationlist=notify)


@app.route('/current_works')
def current_table():
    if(user_name!="admin"):
        return redirect(url_for("home"))
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM complaints ')
    arr=cursor.fetchall()
    mysql.connection.commit()
    
    return render_template('admin/current_works.html',arr=arr,notificationlist=notify)

@app.route('/allworkers')
def all_workers():
    if(user_name!="admin"):
        return redirect(url_for("home"))
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM workers')
    arr=cursor.fetchall()
    mysql.connection.commit()
    
    return render_template('admin/workers.html',arr=arr,notificationlist=notify)

@app.route('/deleter')
def deleter():
    cursor=mysql.connection.cursor()
    
    cursor.execute('DELETE FROM workers WHERE name="sam"')
    mysql.connection.commit()

    
    return render_template('register.html')

@app.route('/logout')

def logout():
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   return render_template('home.html')


    
if __name__ == '__main__':
   app.run(host='0.0.0.0',debug = True,port = 8080)