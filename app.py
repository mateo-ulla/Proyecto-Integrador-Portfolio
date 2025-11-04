# app.py

from flask import Flask, render_template, redirect, url_for, request, session, send_from_directory, flash
from config import Config
from forms import LoginForm, PersonalForm
from models import PersonalModel, ExperienceModel, SkillsModel, EducationModel
from werkzeug.security import check_password_hash
from db import get_connection
import os

app = Flask(__name__)
app.config.from_object(Config)

# modelos
personal_model = PersonalModel()
experience_model = ExperienceModel()
skills_model = SkillsModel()
education_model = EducationModel()

# ruta principal 
@app.route('/')
def index():
    personal = personal_model.find(1)
    experiences = experience_model.all()
    education = education_model.all()
    skills = skills_model.all()
    return render_template('index.html', personal=personal, experiences=experiences, education=education, skills=skills)

# ruta para descargar cv (archivo pdf en static/uploads)
@app.route('/download/cv')
def download_cv():
    uploads = os.path.join(app.root_path, 'static', 'uploads')
    return send_from_directory(uploads, 'CV MATEO ULLA.pdf', as_attachment=True)

# login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("select * from admin where username=%s", (username,))
            user = cur.fetchone()
        if user and check_password_hash(user['password'], password):
            session['admin'] = user['username']
            flash('Acceso correcto', 'success')
            return redirect(url_for('admin_edit'))
        else:
            flash('Credenciales invalidas', 'danger')
    return render_template('login.html', form=form)

# decorador simple para proteger admin 
def admin_required(f):
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('admin'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

# pagina de edicion admin
@app.route('/admin', methods=['GET', 'POST'])
@admin_required
def admin_edit():
    personal = personal_model.find(1)
    form = PersonalForm(obj=personal)
    if form.validate_on_submit():
        data = {
            'name': form.name.data,
            'title': form.title.data,
            'phone': form.phone.data,
            'email': form.email.data,
            'linkedin': form.linkedin.data,
            'github': form.github.data,
            'about': form.about.data
        }
        personal_model.update(data)
        flash('Datos personales actualizados', 'success')
        return redirect(url_for('admin_edit'))
    return render_template('admin_edit.html', form=form, personal=personal)

# logout
@app.route('/logout')
def logout():
    session.pop('admin', None)
    flash('Sesion cerrada', 'info')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
