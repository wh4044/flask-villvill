from datetime import datetime

from flask import Blueprint, url_for, request, render_template, g, flash
from werkzeug.utils import redirect
from ..forms import AnswerForm
from villvill import db
from villvill.models import Search, S_Answer
from .auth_views import login_required

bp = Blueprint('s_answer', __name__, url_prefix='/s_answer')

@bp.route('/create/<int:search_id>', methods=('POST', ))
@login_required
def create(search_id):
    form = AnswerForm()
    search = Search.query.get_or_404(search_id)
    if form.validate_on_submit():
        content = request.form['content']
        answer = S_Answer(content=content, create_date=datetime.now(), user=g.user)
        search.search_set.append(answer)
        db.session.commit()
        return redirect(url_for('search.search_detail', search_id=search_id))
        
    return render_template('search/search_detail.html', search=search, form=form)

@bp.route('/modify/<int:answer_id>', methods=('GET', 'POST'))
@login_required
def modify(answer_id):
    answer = S_Answer.query.get_or_404(answer_id)
    if g.user != answer.user:
        flash('수정권한이 없습니다')
        return redirect(url_for('search.detail', search_id=answer.search.id))
    if request.method == "POST":
        form = AnswerForm()
        if form.validate_on_submit():
            form.populate_obj(answer)
            answer.modify_date = datetime.now()  # 수정일시 저장
            db.session.commit()
            return redirect('{}#answer_{}'.format(
                url_for('search.search_detail', search_id=answer.search.id), answer.id))
    else:
        form = AnswerForm(obj=answer)
    return render_template('answer/answer_form.html', answer=answer, form=form)

@bp.route('/delete/<int:answer_id>')
@login_required
def delete(answer_id):
    answer = S_Answer.query.get_or_404(answer_id)
    search_id = answer.search.id
    if g.user != answer.user:
        flash('삭제권한이 없습니다')
    else:
        db.session.delete(answer)
        db.session.commit()
    return redirect(url_for('search.search_detail', search_id=search_id))