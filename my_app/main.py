# main.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/upload')
@login_required
def upload():
    return render_template('upload.html', name=current_user.name)


@main.route('/files')
@login_required
def files():
    return render_template('files.html')

@main.route('/upload')
def media_file(filename):
    pass