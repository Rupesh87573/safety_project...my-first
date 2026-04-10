from flask import Flask, request, render_template
import smtplib
from email.message import EmailMessage
import base64
import os

app = Flask(__name__)

EMAIL_ADDRESS = os.environ.get("kumarrupesh829119@gmail.com")
EMAIL_PASSWORD = os.environ.get("Yuvi@8757")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    image = request.form['image']
    location = request.form['location']

    img_data = base64.b64decode(image.split(',')[1])

    msg = EmailMessage()
    msg['Subject'] = 'Safety Alert'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg.set_content(f"Location: {location}")

    msg.add_attachment(img_data, maintype='image', subtype='png', filename='photo.png')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    return "Sent!"
    
if __name__ == "__main__":
    app.run()
