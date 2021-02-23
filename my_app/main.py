# main.py
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
import shutil
from werkzeug.utils import secure_filename
from . import tools as tool


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/upload')
@login_required
def upload():
    return render_template('upload.html', name=current_user.name)


@main.route('/uploader', methods=['GET', 'POST'])
def file_post():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))    
        tool.move_file(f.filename)
        return redirect(url_for('main.upload'))


@main.route('/files')
@login_required
def files():
    return render_template('files.html')



