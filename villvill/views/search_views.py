from datetime import datetime
from werkzeug.utils import redirect
from flask import Blueprint, render_template, request, url_for, g, flash
from villvill.models import Search
from ..forms import AnswerForm, QuestionForm
from .. import db
from villvill.views.auth_views import login_required

bp = Blueprint('search', __name__, url_prefix='/search')

@bp.route('/')
def search_li():
    page = request.args.get('page', type=int, default=1)    # 페이지
    search_list = Search.query.order_by(Search.create_date.desc())
    search_list = search_list.paginate(page, per_page=10)
    return render_template('search/search_list.html', search_list=search_list)

@bp.route('/<int:search_id>/')
def search_detail(search_id):
    form = AnswerForm()
    search = Search.query.get_or_404(search_id)
    return render_template('search/search_detail.html', search=search, form=form)

@bp.route('/create/', methods=('GET', 'POST'))
@login_required
def create():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        search = Search(subject=form.subject.data, content=form.content.data,
                        create_date=datetime.now(), user=g.user)
        db.session.add(search)
        db.session.commit()
        return redirect(url_for('search.search_li'))
    return render_template('search/search_form.html', form=form)

@bp.route('/modify/<int:search_id>', methods=('GET', 'POST'))
@login_required
def modify(search_id):
    search = Search.query.get_or_404(search_id)
    if g.user != search.user:
        flash('수정권한이 없습니다')
        return redirect(url_for('search.search_detail', search_id=search_id))

    if request.method == 'POST':
        form = QuestionForm()
        if form.validate_on_submit():
            form.populate_obj(search)
            search.modify_date = datetime.now()  # 수정일시 저장
            db.session.commit()
            return redirect(url_for('search.search_detail', search_id=search_id))
    else:
        form = QuestionForm(obj=search)
    return render_template('search/search_form.html', form=form)

@bp.route('/delete/<int:search_id>')
@login_required
def delete(search_id):
    search = Search.query.get_or_404(search_id)
    if g.user != search.user:
        flash('삭제권한이 없습니다')
        return redirect(url_for('search.search_detail', search_id=search_id))
    db.session.delete(search)
    db.session.commit()
    return redirect(url_for('search.search_li'))