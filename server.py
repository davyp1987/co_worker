from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/diensten')
def diensten():
    return render_template('diensten.html')

@app.route('/contact')
def contact():
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