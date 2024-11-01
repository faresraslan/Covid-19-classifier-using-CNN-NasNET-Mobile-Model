'''
created by team 5 in fci suez university
we used NasNanMobile to train the model

'''
from flask import Flask , flash ,request , redirect,url_for,render_template
import urllib.request
import os
from werkzeug.utils import secure_filename
import keras
import pandas as pd
import numpy as np
import tensorflow as tf
from model import predict , img_re

# load the model 
new_model=keras.models.load_model("C:/Users/ALARAFAT/Desktop/NasNetMobile(Team 5)/Flask_App/NasNetMobile .h5")
#create flask app
app = Flask(__name__)
#get path that use to store the user inpute image
UPLOAD_FOLDER ='static/uploads/x/'
app.secret_key = 'cairocoder-ednalan'
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config['MAX_A'] = 16 *1024*1024

#vailedate inpute image
ALLOWED_IMAGE_TYPES = set(["png", "jpg", "jpeg", "gif"])

def allowed_file(filename):
    print("Check if image types is allowed")
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_IMAGE_TYPES

#create home page
@app.route("/", methods=["GET", "POST"])


#function to upload image from user          
def upload_img():

    folder =  UPLOAD_FOLDER
    for filenames in os.listdir(folder):
        file_path = os.path.join(folder, filenames)
        os.remove(file_path)

    if request.method == "POST":
        if 'file' not in request.files.keys():
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No image selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('Image successfully uploaded and displayed below')
            x='C:/Users/ALARAFAT/Desktop/NasNetMobile(Team 5)/Flask_App/static/uploads'
            img_por = img_re(x)
            pre = predict(img_por)
            
            if pre == 0:
                return render_template('normal.html', filename='r.jpg')
            else:
                return render_template('unhelthy.html', filename='r4.jpg')
            
                
            
        else:
            flash('Allowed image types are - png, jpg, jpeg, gif')
            return redirect(request.url)
    
    else:
        return render_template("index.html")
    


@app.route('/display/<filename>')

def display_image(filename):
    return redirect(url_for('static',filename='uploads/'+filename) ,code=301 )





if __name__ == "__main__":
    app.run(debug=False)


