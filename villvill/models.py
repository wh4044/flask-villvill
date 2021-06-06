from villvill import db

class Transfer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    subject = db.Column(db.String(200), nullable = False)
    content = db.Column(db.Text(), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"),
                        nullable = False)
    user = db.relationship('User', backref=db.backref('trans_set'))

    img1_name = db.Column(db.String(300), nullable = True)
    img1 = db.Column(db.LargeBinary, nullable = True)
    mimetype1 = db.Column(db.String(100), nullable = True)

    img2_name = db.Column(db.String(300), nullable = True)
    img2 = db.Column(db.LargeBinary, nullable = True)
    mimetype2 = db.Column(db.String(100), nullable = True)

    img3_name = db.Column(db.String(300), nullable = True)
    img3 = db.Column(db.LargeBinary, nullable = True)
    mimetype3 = db.Column(db.String(100), nullable = True)

    img4_name = db.Column(db.String(300), nullable = True)
    img4 = db.Column(db.LargeBinary, nullable = True)
    mimetype4 = db.Column(db.String(100), nullable = True)

    img5_name = db.Column(db.String(300), nullable = True)
    img5 = db.Column(db.LargeBinary, nullable = True)
    mimetype5 = db.Column(db.String(100), nullable = True)

    create_date = db.Column(db.DateTime(), nullable = False)
    modify_date = db.Column(db.DateTime(), nullable=True)

class T_Answer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    transfer_id = db.Column(db.Integer, db.ForeignKey('transfer.id', ondelete="CASCADE"))
    transfer = db.relationship('Transfer', backref=db.backref('transfer_set'))
    content = db.Column(db.Text(), nullable = False)
    create_date = db.Column(db.DateTime(), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"),
                        nullable = False)
    user = db.relationship('User', backref=db.backref('transfer_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)

class Search(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    subject = db.Column(db.String(200), nullable = False)
    content = db.Column(db.Text(), nullable = False)
    create_date = db.Column(db.DateTime(), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"),
                        nullable = False)
    user = db.relationship('User', backref=db.backref('sear_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)

class S_Answer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    search_id = db.Column(db.Integer, db.ForeignKey('search.id', ondelete="CASCADE"))
    search = db.relationship('Search', backref=db.backref('search_set'))
    content = db.Column(db.Text(), nullable = False)
    create_date = db.Column(db.DateTime(), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"),
                        nullable = False)
    user = db.relationship("User", backref=db.backref('search_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    nickname = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    phone = db.Column(db.String(64), unique=True, nullable=False)

    gender = db.Column(db.String(10), nullable=False)

    stu_name = db.Column(db.String(300), nullable = False)
    stu = db.Column(db.LargeBinary, nullable = False)
    mimetype = db.Column(db.String(100), nullable = False)