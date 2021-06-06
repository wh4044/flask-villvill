from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from werkzeug.utils import secure_filename
import functools

from villvill import db
from villvill.forms import UserCreateForm, UserLoginForm
from villvill.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    form =  UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(phone=form.phone.data).first()
        if not user:
            f = request.files['image']
            if f and allowed_file(f.filename):
                fname = secure_filename(f.filename)
                mtype = f.mimetype
                user = User(username=form.username.data,
                            password=generate_password_hash(form.password1.data),
                            email=form.email.data,
                            nickname=form.nickname.data,
                            phone=form.phone.data,
                            stu_name = fname,
                            mimetype = mtype,
                            stu = f.read(),
                            gender = form.gender.data)
                
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('main.index'))
            else:
                flash('선택된 사진이 없거나 올바르지 않은 확장명입니다.')
        else:
            flash('이미 존재하는 사용자입니다.')
    return render_template('auth/signup.html', form=form)


@bp.route('/login/', methods=("GET", "POST"))
def login():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            error = "아이디 혹은 비밀번호를 확인해주세요."
        elif not check_password_hash(user.password, form.password.data):
            error = "아이디 혹은 비밀번호를 확인해주세요."
        
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('main.index'))
        flash(error)
    return render_template('auth/login.html', form=form)

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)

@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view