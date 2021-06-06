from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms import validators
from wtforms.fields.core import RadioField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired("제목을 입력해주세요.")])
    content = TextAreaField('내용', validators=[DataRequired("내용을 입력해주세요.")])

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용을 입력해주세요.')])

class UserCreateForm(FlaskForm):
    username = StringField('사용자 이름', validators=[DataRequired("이름을 입력해주세요."), Length(min=3, max=25)])
    nickname = StringField('닉네임', validators=[DataRequired("닉네임을 입력해주세요."), Length(min=2, max=12)])
    password1 = PasswordField('비밀번호', validators=[DataRequired('비밀번호를 입력해주세요.'), EqualTo('password2', '비밀번호가 일치하지 않습니다.')])
    password2 = PasswordField('비밀번호 확인', validators=[DataRequired('비밀번호를 입력해주세요.')])
    email = EmailField('이메일', [DataRequired('이메일을 입력해주세요.'), Email()])
    phone = StringField('휴대전화 번호', validators=[DataRequired('전화번호를 입력해주세요.'), Length(min=10, max = 15)])
    gender = RadioField('성별', validators=[DataRequired('성별을 선택하세요')], choices=[("남자", '남자'), ("여자", '여자')])

class UserLoginForm(FlaskForm):
    username = StringField('사용자 ID', validators=[DataRequired("ID를 입력해주세요."), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired("비밀번호를 입력해주세요.")])
