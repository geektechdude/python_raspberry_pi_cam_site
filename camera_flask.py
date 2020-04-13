# geektechstuff
# Libraries to import
from flask import Flask, render_template
from picamera import PiCamera
from datetime import datetime
import shutil
import os

app = Flask(__name__,static_url_path='',static_folder='/home/pi/flask_photo/')

def save_photo():
    camera = PiCamera()
    filename = datetime.now().strftime("%H%M%Y%m%d.jpg")
    camera.capture(filename)
    camera.close()
    shutil.copyfile(filename,'/home/pi/flask_photo/latest.jpg')
    new_location = "/home/pi/flask_photo/old_images/"+filename
    shutil.copyfile(filename, new_location)
    if os.path.exists(filename):
        os.remove(filename)
    return()

@app.route('/')
def load_page():
    save_photo()
    time_hour_min = datetime.now().strftime("%H:%M")
    time_date = datetime.now().strftime("%d-%m-%y")
    return render_template("flask_temp.html", time_hour_min=time_hour_min, time_date=time_date)
