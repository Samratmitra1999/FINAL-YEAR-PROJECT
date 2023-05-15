import json
from flask import Blueprint, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
import sys
from wtforms.validators import InputRequired
import calendar
import time
views = Blueprint('views', __name__)

current_GMT = time.gmtime()

time_stamp = calendar.timegm(current_GMT)

sys.path.append("..")
from src.npr import main
class UploadFileForm(FlaskForm):
    file = FileField("Upload Image File", validators=[InputRequired()])
    submit = SubmitField("Upload File")
    
def loadCarDetails():
    data = json.load(open('static/results/output.json'))
    return data['current']

def loadHistory():
    data = json.load(open('static/results/output.json'))
    if data.get('history') is not None:
        return data['history']
    else:
        return []
        
@views.route('/', methods=["GET",'POST'])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        path = os.path.join("static/inputs/images",secure_filename(str(time_stamp)+"_"+file.filename))
        output_path = os.path.join("static/results/images",secure_filename("output_"+str(time_stamp)+"_"+file.filename))
        img_view_path = os.path.join("results/images/",secure_filename("output_"+str(time_stamp)+"_"+file.filename))
        file.save(path)
        main(path,output_path)
        data = loadCarDetails()
        return render_template("home.html", form=form, filename = img_view_path, vehicledetails = data)
    return render_template("home.html", form=form)

@views.route('/about')
def about():
    return render_template("about.html")

@views.route('/team')
def team():
    return render_template("team.html")

@views.route('/getinfo')
def getinfo():
    return render_template("getinfo.html")

@views.route('/addinfo')
def addinfo():
    return render_template("rtoinfo.html")    

@views.route('/history')
def history():
    data = loadHistory()
    return render_template("history.html", vehicledetails = data)