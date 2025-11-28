from flask import Flask, render_template, redirect, url_for, request, session, send_from_directory, flash
from config import Config
from forms import LoginForm, PersonalForm
from models import PersonalModel, ExperienceModel, SkillsModel, EducationModel, ProjectsModel
from werkzeug.security import check_password_hash
from db import get_connection
import pymysql
import os
from functools import wraps

app = Flask(__name__)
app.config.from_object(Config)

# MODELOS
personal_model = PersonalModel()
experience_model = ExperienceModel()
skills_model = SkillsModel()
education_model = EducationModel()
projects_model = ProjectsModel()

# RUTA PRINCIPAL

@app.route('/')
def index():
    personal = personal_model.find(1)
    experiences = experience_model.all()
    education = education_model.all()
    skills = skills_model.all()
    projects = projects_model.all()
    return render_template('index.html',
                            personal=personal,
                            experiences=experiences,
                            education=education,
                            skills=skills,
                            projects=projects)

# CV
@app.route('/download/cv')
def download_cv():
    uploads = os.path.join(app.root_path, 'static', 'uploads')
    return send_from_directory(uploads, 'CV MATEO ULLA.pdf', as_attachment=True)

# MATERIALES

@app.route('/material')
def material():
    books = [
        {
            'title': 'Atomic Habits',
            'description': 'Guía práctica sobre cómo crear buenos hábitos.',
            'filename': 'atomic_habits.pdf',
            'image': 'atomic_habits.jpg'
        },
        {
            'title': 'Padre Rico, Padre Pobre',
            'description': 'Clásico sobre educación financiera.',
            'filename': 'padre_rico_padre_pobre.pdf',
            'image': 'padre_rico_padre_pobre.jpg'
        },
        {
            'title': 'El Patrón Bitcoin',
            'description': 'Historia económica del Bitcoin.',
            'filename': 'el_patron_bitcoin.pdf',
            'image': 'el_patron_bitcoin.jpg'
        }
    ]
    return render_template('material.html', books=books)


@app.route('/download/book/<filename>')
def download_book(filename):
    uploads = os.path.join(app.root_path, 'static', 'uploads')
    return send_from_directory(uploads, filename, as_attachment=True)

# LOGIN / ADMIN

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        conn = get_connection()
        with conn.cursor(pymysql.cursors.DictCursor) as cur:
            cur.execute("SELECT * FROM admin WHERE username=%s", (username,))
            user = cur.fetchone()
        conn.close()

        if user and check_password_hash(user['password'], password):
            session['admin'] = user['username']
            flash('Acceso correcto', 'success')
            return redirect(url_for('admin_edit'))
        else:
            flash('Credenciales inválidas', 'danger')

    return render_template('login.html', form=form)


def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('admin'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

# PANEL ADMIN

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
        flash('Datos personales actualizados.', 'success')
        return redirect(url_for('admin_edit'))

    return render_template('admin_edit.html', form=form, personal=personal)

# CRUD UNIFICADO (Education, Experience, Skills, Projects)

@app.route('/edit/<tipo>/<int:id>', methods=['GET', 'POST'])
@admin_required
def edit_entry(tipo, id):

    modelos = {
        'education': education_model,
        'experience': experience_model,
        'skills': skills_model,
        'projects': projects_model
    }

    if tipo not in modelos:
        flash("Tipo de registro desconocido.", "danger")
        return redirect(url_for('index'))

    modelo = modelos[tipo]
    entry = modelo.find(id)

    if request.method == 'POST':
        data = request.form.to_dict()

        if tipo == 'projects':
            modelo.update(id, data)
        else:
            conn = get_connection()
            cur = conn.cursor()
            placeholders = ", ".join([f"{k}=%s" for k in data.keys()])
            values = list(data.values()) + [id]
            cur.execute(f"UPDATE {tipo} SET {placeholders} WHERE id=%s", values)
            conn.commit()
            conn.close()

        flash("Registro actualizado.", "success")
        return redirect(url_for('index'))

    return render_template("edit_entry.html", tipo=tipo, entry=entry)


@app.route('/add/<tipo>', methods=['GET', 'POST'])
@admin_required
def add_entry(tipo):

    campos = {
        'education': ['institution', 'degree', 'start_year', 'end_year', 'description'],
        'experience': ['company', 'role', 'start_date', 'end_date', 'description'],
        'skills': ['name', 'level'],
        'projects': ['title', 'description', 'github', 'image']
    }

    if tipo not in campos:
        flash("Tipo de registro desconocido.", "danger")
        return redirect(url_for('index'))

    if request.method == 'POST':
        data = request.form.to_dict()

        if tipo == 'projects':
            projects_model.create(data)
        else:
            conn = get_connection()
            cur = conn.cursor()
            columnas = ", ".join(data.keys())
            valores = ", ".join(["%s"] * len(data))
            cur.execute(f"INSERT INTO {tipo} ({columnas}) VALUES ({valores})", list(data.values()))
            conn.commit()
            conn.close()

        flash("Registro agregado.", "success")
        return redirect(url_for('index'))

    return render_template("add_entry.html", tipo=tipo, campos=campos[tipo])


@app.route('/delete/<tipo>/<int:id>')
@admin_required
def delete_entry(tipo, id):

    if tipo == "projects":
        projects_model.delete(id)
        flash("Proyecto eliminado.", "success")
        return redirect(url_for('index'))

    if tipo in ['education', 'experience', 'skills']:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM {tipo} WHERE id=%s", (id,))
        conn.commit()
        conn.close()
        flash("Registro eliminado.", "success")
        return redirect(url_for('index'))

    flash("Tipo inválido.", "danger")
    return redirect(url_for('index'))


# LOGOUT
@app.route('/logout')
def logout():
    session.pop('admin', None)
    flash('Sesión cerrada.', 'info')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
