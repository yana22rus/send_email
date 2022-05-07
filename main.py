from os import getenv
import smtplib
from email.mime.text import MIMEText
from flask import Flask,render_template,request



app = Flask(__name__)



@app.route("/registration",methods=["GET","POST"])
def registration():

    if request.method == "POST":

        email = request.form["email"]

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(getenv("email"), getenv("pswd"))

        with open("email.html") as f:

            html_email = f.read()

        html_email = html_email.replace("username",request.form["username"])

        msg = MIMEText(html_email,"html")

        server.sendmail(getenv("email"), email, msg.as_string())

        return render_template("registration.html")



    return render_template("registration.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)