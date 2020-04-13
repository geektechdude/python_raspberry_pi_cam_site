# geektechstuff

# Libraries to import
from flask import Flask, render_template
from picamera import PiCamera
from time import sleep
from datetime import datetime

app = Flask(__name__,static_url_path='',static_folder='/home/pi/flask_photo/')

def time_now():
    time_now = datetime.now().strftime("%H%M%Y%m%d")
    return(time_now)

def save_photo():
    camera = PiCamera()
    filename = datetime.now().strftime("%H%M%Y%m%d.jpg")
    camera.capture(filename)
    camera.close()
    sleep(2)
    return(filename)

@app.route('/')
def load_page():
    filename = save_photo()
    time = time_now()
    return render_template("flask_temp.html",filename=filename,time=time)
