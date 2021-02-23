# main.py
from flask import Blueprint, render_template, request, redirect, url_for, send_file
from flask_login import login_required, current_user
import pandas as pd
from . import tools as tool
import shutil
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
        name = tool.change_name(f.filename)
        f.save(secure_filename(name))  
        tool.move_file(name)
        return redirect(url_for('main.upload'))


@main.route('/files')
@login_required
def files():
    archivos = tool.make_tree()
    return render_template('files.html', tables=[archivos.to_html(classes='data')], titles="")



@main.route('/delete', methods=['POST'])
@login_required
def del_files():
    archivo = request.form.get('file_name')
    if request.form['submit_button'] == 'borra':
            print(archivo,"borrar")
            borrado = tool.delete_file(archivo)
            archivos = tool.make_tree()
            return render_template('files.html', tables=[archivos.to_html(classes='data')], respuesta=borrado, titles="")
    elif request.form['submit_button'] == 'descarga':
            print(archivo,"descarga")
            archivos = tool.make_tree()
            path = f"../files/{archivo}"
            descarga = send_file(path, as_attachment=True)
            return redirect(url_for('main.files'))
