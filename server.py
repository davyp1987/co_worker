"""Module server"""
import json
import sys
import os
from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

def config_read():
    """read config file"""
    with open(os.path.join(sys.path[0], "configuration.json"), "r") as jsonfile:
        data = json.load(jsonfile)
        app.config['MAIL_SERVER'] = data['smtp_settings']['MAIL_SERVER']
        app.config['MAIL_PORT'] =  int(data['smtp_settings']['MAIL_PORT'])
        app.config['MAIL_USE_SSL'] = bool(data['smtp_settings']['MAIL_USE_SSL'])
        app.config['MAIL_USERNAME'] = data['smtp_settings']['MAIL_USERNAME']
        app.config['MAIL_PASSWORD'] = data['smtp_settings']['MAIL_PASSWORD']

config_read()
mail = Mail(app)

def send_test_email(result):
    """send test email"""
    try:
        """ send test email """
        msg = Message("Contact form from Co-worker website",
                    sender="test@gmail.com",
                    recipients=["davy.pouillie@gmail.com"])

        msg.html = """
        Hello there, <br><br>

        You just receive a contact form from: <br><br>
        Name: {} <br>
        FirstName: {} <br>
        Email: {} <br>
        Phone: {} <br>
        Company: {} <br>
        Reason: {} <br>
        Message: {} <br><br>
        copy: {} <br><br>

        regards, <br>
        Webmaster

        """.format(result['name'], result['firstname'], result['email'], result['phone'], result['company'], result['reason'], result['message'], result['copy'])

        mail.send(msg)
    except:
        print("error")

@app.route('/')
def home():
    """home url"""
    return render_template('index.html')


@app.route('/index')
def index():
    """home url"""
    return render_template('index.html')

@app.route('/diensten')
def diensten():
    return render_template('diensten.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():

    if request.method == 'POST':
        result = {}

        result['name'] = request.form['naam']
        result['firstname'] = request.form['voornaam']
        result['email'] = request.form['email'].replace(' ','').lower()
        result['phone'] = request.form['telefoon']
        result['company'] = request.form['bedrijfsnaam']
        result['reason'] = request.form.get('reden')
        result['message'] = request.form['message'].replace('\n', '<br>')
        result['copy'] = request.form['copy']

        send_test_email(result)
        print("test")

        return render_template('verzonden.html')

    return render_template('contact.html')

@app.route('/office_assistant')
def office_assistant():
    return render_template('office_assistant.html')

@app.route('/opvolgen_betalingen')
def opvolgen_betalingen():
    return render_template('opvolgen_betalingen.html')

@app.route('/simpele_boekingen')
def simpele_boekingen():
    return render_template('simpele_boekingen.html')

@app.route('/social_media')
def social_media():
    return render_template('social_media.html')

@app.route('/onderhoud_website')
def onderhoud_website():
    return render_template('onderhoud_website.html')

@app.route('/consulting')
def consulting():
    return render_template('consulting.html')

@app.route('/sales_management')
def sales_management():
    return render_template('sales_management.html')

@app.route('/marketing_sales')
def marketing_sales():
    return render_template('marketing_sales.html')

@app.route('/sourcing')
def sourcing():
    return render_template('sourcing.html')

@app.route('/purchase_management')
def purchase_management():
    return render_template('purchase_management.html')

@app.route('/privacy_policy')
def privacy_policy():
    return render_template('privacy_policy.html')

@app.route('/cookie_policy')
def cookie_policy():
    return render_template('cookie_policy.html')

@app.route('/disclaimer')
def disclaimer():
    return render_template('disclaimer.html')

if __name__ == '__main__':
  app.run(debug=True)
