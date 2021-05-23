import smtplib
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
SUBJECT = "VM test"
s = smtplib.SMTP('smtp.gmail.com', 587)

def sendmail(TEXT,email):
    
    
    
    print("sorry we cant process your candidature")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("customercare.vmware@gmail.com", "124qwr!@$QWR")
    message  = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    s.sendmail("customercare.vmware@gmail.com", email, content)
    s.quit()
def sendgridmail(user,TEXT):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("customercare.vmware@gmail.com", "124qwr!@$QWR")
    
    
    #mailtemptest
    registermsg="""
<!DOCTYPE html>
<html>
    <body>
        <div style="background-color:#eee;padding:10px 20px;">
            <h2 style="font-family:Georgia, 'Times New Roman', Times, serif;color#454349;"><center>VM Customer Care Registration</center></h2>
        </div>
        <div style="padding:20px 0px">
            <div style="height: 500px;width:400px">
                <a href="http://localhost:8080/loginconfirmation/"""+user+""""><img src="http://assets.stickpng.com/images/59060d910cbeef0acff9a661.png" style="height: 300px;"></a>
                <div style="text-align:center;">
                    
                    <p>Ignore this message if you have not registered</p>
                    <a href="#">Read more</a>
                </div>
            </div>
        </div>
    </body>
</html>
"""
    
    registermsg1=Content("text/html",registermsg)




    sg = sendgrid.SendGridAPIClient('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')
    from_email = Email("customercare.vmware@gmail.com")  # Change to your verified sender
    to_email = To(user)  # Change to your recipient
    subject = "VM ware"
    content = Content("text/plain",TEXT)
    mail = Mail(from_email, to_email, subject, registermsg1)

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()
    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mail_json)
    print(response.status_code)
    print(response.headers)
    s.quit()



def worker_reg(user):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("customercare.vmware@gmail.com", "124qwr!@$QWR")
    
    
    #mailtemptest
    registermsg="""
<!DOCTYPE html>
<html>
    <body>
        <div style="background-color:#eee;padding:10px 20px;">
            <h2 style="font-family:Georgia, 'Times New Roman', Times, serif;color#454349;"><center>SELECTED AS VM WORKER!!</center></h2>
        </div>
        <div style="padding:20px 0px">
            <div style="height: 500px;width:400px;align:center;">
                <center><a href="http://localhost:8080/"><img src="https://previews.123rf.com/images/lkeskinen/lkeskinen1702/lkeskinen170211175/71146154-you-have-been-selected-rubber-stamp-grunge-design-with-dust-scratches-effects-can-be-easily-removed-.jpg" style="height: 300px;"></a>
                <div style="text-align:center;">
                    
                    <p>Thank u for registering as worker!</p>
                    <a href="#">Read more</a></center>
                </div>
            </div>
        </div>
    </body>
</html>
"""
    
    registermsg1=Content("text/html",registermsg)




    sg = sendgrid.SendGridAPIClient('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')
    from_email = Email("customercare.vmware@gmail.com")  # Change to your verified sender
    to_email = To(user)  # Change to your recipient
    subject = "VM ware worker selected"
    
    mail = Mail(from_email, to_email, subject, registermsg1)

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()
    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mail_json)
    print(response.status_code)
    print(response.headers)
    s.quit()
    
    
    
    
    
'''send customer the worker detail after confirmation'''

def add_complaint(assignedw,user):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("customercare.vmware@gmail.com", "124qwr!@$QWR")
    
    
    #mailtemptest
    registermsg="""<!DOCTYPE html>
<html>
    <head>
<style>
table {
  border-collapse: collapse;
  width: 100%;
}

th, td {
  text-align: left;
  padding: 8px;
}

tr:nth-child(even){background-color: #f2f2f2}

td {
  background-color: #4CAF50;
  color: white;
}
</style>
</head>
    <body>
        <div style="background-color:#eee;padding:10px 20px;">
            <h2 style="font-family:Georgia, 'Times New Roman', Times, serif;color#454349;"><center>COMPLAINT BOOKED SUCCESSFULLY!!</center></h2>
            <table style="width:100%">
  
  <tr>
    <td>Worker Name:</td>
    <td>"""+assignedw[1]+"""</td>
    
  </tr>
  
  <tr>
    <td>Contact number:</td>
    <td>"""+str(assignedw[3])+"""</td>
    
  </tr>
</table>
        </div>
        <div style="padding:20px 0px">
            <div style="height: 500px;width:400px;align:center;">
                <center><a href="http://localhost:8080/"><img src="https://i.pinimg.com/originals/0d/e4/1a/0de41a3c5953fba1755ebd416ec109dd.gif" style="height: 300px;"></a>
                <div style="text-align:center;">
                    
                    <p>contact for further querries!</p>
                    <a href="#">Read more</a></center>
                </div>
            </div>
        </div>
    </body>
</html>
"""
    
    registermsg1=Content("text/html",registermsg)




    sg = sendgrid.SendGridAPIClient('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')
    from_email = Email("customercare.vmware@gmail.com")  # Change to your verified sender
    to_email = To(user)  # Change to your recipient
    subject = "COMPLAINT BOOKED SUCCESSFULLY"
    
    mail = Mail(from_email, to_email, subject, registermsg1)

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()
    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mail_json)
    print(response.status_code)
    print(response.headers)
    s.quit()
    
    
    
    
def worker_notify(name,address,product,brand,contactnum,complaint,user):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("customercare.vmware@gmail.com", "124qwr!@$QWR")
    
    
    #mailtemptest
    registermsg="""
<!DOCTYPE html>
<html>
    <head>
<style>
table {
  border-collapse: collapse;
  width: 100%;
}

th, td {
  text-align: left;
  padding: 8px;
}

tr:nth-child(even){background-color: #f2f2f2}

td {
  background-color: #4CAF50;
  color: white;
}
</style>
</head>
    <body>
        <div style="background-color:#eee;padding:10px 20px;">
            <h2 style="font-family:Georgia, 'Times New Roman', Times, serif;color#454349;"><center>COMLAINT RECEIVED!!</center></h2>
            <table style="width:100%">
  
  <tr>
    <td>Name:</td>
    <td>"""+name+"""</td>
    
  </tr>
  
  <tr>
    <td>Address:</td>
    <td>"""+address+"""</td>
    
  </tr>
  <tr>
    <td>Product:</td>
    <td>"""+product+"""</td>
    
  </tr>
  <tr>
    <td>Brand:</td>
    <td>"""+brand+"""</td>
    
  </tr>
  <tr>
    <td>Contact number:</td>
    <td>"""+contactnum+"""</td>
    
  </tr>
  <tr>
    <td>Complaint:</td>
    <td>"""+complaint+"""</td>
    
  </tr>
</table>
        </div>
        <div style="padding:20px 0px">
            <div style="height: 500px;width:400px;align:center;">
                <center><a href="http://localhost:8080/"><img src="https://media4.giphy.com/media/Ln2dAW9oycjgmTpjX9/giphy.gif" style="height: 300px;"></a>
                <div style="text-align:center;">
                    
                    <p>contact user for further querries!</p>
                    <a href="#">Read more</a></center>
                </div>
            </div>
        </div>
    </body>
</html>
"""
    
    registermsg1=Content("text/html",registermsg)




    sg = sendgrid.SendGridAPIClient('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')
    from_email = Email("customercare.vmware@gmail.com")  # Change to your verified sender
    to_email = To(user)  # Change to your recipient
    subject = "COMLAINT RECEIVED"
    
    mail = Mail(from_email, to_email, subject, registermsg1)

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()
    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mail_json)
    print(response.status_code)
    print(response.headers)
    s.quit()