from werkzeug.utils import secure_filename
from flask import Blueprint, render_template, request, url_for, Flask
from villvill.models import ImageTest
from .. import db

app = Flask(__name__)
app.debug = True

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload')
def load_file():
   return render_template('image_test.html')

import os
@app.route('/uploader', methods = ['POST'])
def upload_file():
    f = request.files['file']
    if f and allowed_file(f.filename):
        fname = secure_filename(f.filename)
        mtype = f.mimetype
        image_test = ImageTest(name = fname, data = f.read(), mimetype = mtype)
        db.session.add(image_test)
        db.session.commit()
        return 'file uploaded successfully'
    else :
        return 'Only Image available'