from flask import Blueprint, render_template, url_for, request, current_app
from werkzeug.utils import redirect
from werkzeug.utils import secure_filename
# from villvill.models import ImageTest
from .. import db


bp = Blueprint('main', __name__, url_prefix='/')
@bp.route('/hello')
def hello_villvill():
    return 'Hello, VillVill!'

@bp.route('/')
def index():
    current_app.logger.info("INFO 레벨로 출력")
    return render_template('main.html')

# @bp.route('/image')
# def index1():
#     return render_template('image_test.html')


# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
# def allowed_file(filename):
# 	return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

# @bp.route('/upload')
# def load_file():
#    return render_template('image_test.html')

# import os
# @bp.route('/uploader', methods = ['POST'])
# def upload_file():
#     f = request.files['file']
#     if f and allowed_file(f.filename):
#         fname = secure_filename(f.filename)
#         mtype = f.mimetype
#         image_test = ImageTest(name = fname, data = f.read(), mimetype = mtype)
#         db.session.add(image_test)
#         db.session.commit()
#         return 'file uploaded successfully'
#     else :
#         return 'Only Image available'

# from flask import Response
# @bp.route('/show/<img_id>')
# def show(img_id):
#     img = ImageTest.query.filter_by(id=img_id).first()
#     return Response(img.data, mimetype=img.mimetype) 

# from base64 import b64encode
# @bp.route('/show/<img_id>')
# def show(img_id):
#     img = ImageTest.query.filter_by(id=img_id).first()
#     image = b64encode(img.data).decode("utf-8")
#     return render_template('show.html', image = image)