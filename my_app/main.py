# main.py
import os
from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename


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
    
        return render_template('upload.html',name=current_user.name)


@main.route('/files')
@login_required
def files():
    return render_template('files.html')



