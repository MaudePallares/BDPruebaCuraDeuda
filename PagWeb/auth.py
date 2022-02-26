
from sre_parse import CATEGORIES
from flask import Blueprint, render_template, request, flash, redirect, url_for
from PagWeb import views 
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db 
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth',__name__)
#definimos el login
@auth.route('/login', methods=['GET', 'POST'])   #definimos la ruta de login 
def login():
    if request.method =='POST':
        user = request.form.get('Usuario')
        password = request.form.get('password')

        usuario = User.query.filter_by(user=user).first()
        if usuario:
            if check_password_hash(usuario.password, password):
                flash('Inicio de sesion correcto', category='success')
                login_user(usuario, remember=True)
                return redirect(url_for('views.index'))
            else:
                flash('Contraseña incorrecta, intenta de nuevo', category='error')
        else:
            flash('usuario no existe, registrate porfavor', category='error')

    return render_template("login.html", user = current_user)
#definimos el logout
@auth.route('/logout')   
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
#definimos la ruta de registro de cuenta 
@auth.route('/Registrarse', methods=['GET', 'POST'])    
def sign_up():
    if request.method == 'POST':
        user = request.form.get('Usuario')
        password1 = request.form.get('contrasena1')
        password2 = request.form.get('contrasena2')

        usuario = User.query.filter_by(user=user).first()
        if usuario:
            flash('El usuario ya existe', category='error')
        elif len(user) < 3:
            flash('El usuario debe ser minimo 3 caracteres', category='error')
            return render_template("registro.html")
        elif password1 != password2:
            flash('Las contraseñas no coinciden', category='error')
            return render_template("registro.html")
        elif len(password1) < 3:
            flash('Contraseña muy pequeña', category='error')
            return render_template("registro.html")
        else:
            new_user = User(user=user, password = generate_password_hash(password1, method='sha256'))  # agregamos el usuario a la bd
            db.session.add(new_user)
            db.session.commit()
            flash('Cuenta creada de forma exitosa', category='success')
            return redirect(url_for('views.index'))
 
    return render_template("registro.html", user = current_user)


#no terminado
@auth.route('/principal', methods=['GET', 'POST'])   
def search():
    if request.method == 'POST':

         archivo = pd.read_excel('DocCP/SEPOMEX.xls')
         df = pd.DataFrame(archivo)

         Estados = archivo.sheet_names
         estado = request.form.get('estado')
         colonia = request.form.get('colonia')
         cp =  request.form.get('cp')

         colonias = df[df['d_CP']==cp]['d_asenta']
         flash('el estado es ' + colonias, category='error')
         print(colonias)
    else:
         flash('CODIGO POSTAL NO VALIDO', category='error')
         return render_template("principal.html")


    return render_template("principal.html", user = current_user)