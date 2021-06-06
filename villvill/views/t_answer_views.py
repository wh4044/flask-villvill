from datetime import datetime

from flask import Blueprint, url_for, request, render_template, g, flash
from werkzeug.utils import redirect
from ..forms import AnswerForm
from villvill import db
from villvill.models import Transfer, T_Answer
from .auth_views import login_required

bp = Blueprint('t_answer', __name__, url_prefix='/t_answer')

@bp.route('/create/<int:transfer_id>', methods=('POST', ))
@login_required
def create(transfer_id):
    form = AnswerForm()
    transfer = Transfer.query.get_or_404(transfer_id)
    if form.validate_on_submit():
        content = request.form['content']
        answer = T_Answer(content=content, create_date=datetime.now(), user=g.user)
        transfer.transfer_set.append(answer)
        db.session.commit()
        return redirect(url_for('transfer.transfer_detail', transfer_id=transfer_id))
        
    return render_template('transfer/transfer_detail.html', transfer=transfer, form=form)

@bp.route('/modify/<int:answer_id>', methods=('GET', 'POST'))
@login_required
def modify(answer_id):
    answer = T_Answer.query.get_or_404(answer_id)
    if g.user != answer.user:
        flash('수정권한이 없습니다')
        return redirect(url_for('transfer.detail', transfer_id=answer.transfer.id))
    if request.method == "POST":
        form = AnswerForm()
        if form.validate_on_submit():
            form.populate_obj(answer)
            answer.modify_date = datetime.now()  # 수정일시 저장
            db.session.commit()
            return redirect('{}#answer_{}'.format(
                url_for('transfer.transfer_detail', transfer_id=answer.transfer.id), answer.id))
    else:
        form = AnswerForm(obj=answer)
    return render_template('answer/answer_form.html', answer=answer, form=form)

@bp.route('/delete/<int:answer_id>')
@login_required
def delete(answer_id):
    answer = T_Answer.query.get_or_404(answer_id)
    transfer_id = answer.transfer.id
    if g.user != answer.user:
        flash('삭제권한이 없습니다')
    else:
        db.session.delete(answer)
        db.session.commit()
    return redirect(url_for('transfer.transfer_detail', transfer_id=transfer_id))