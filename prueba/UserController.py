from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'tu_secreto_aqui'  # Necesario para usar flash messages

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def password_valid(self, password):
        return self.password == password

class UserController:
    def __init__(self):
        self.user_list = [
            User(1, 'johnDoe', 'password123'),
            User(2, 'janeDoe', 'ilovejavascript'),
            User(3, 'admin', 'admin123'),
            User(4, 'user123', 'pass123'),
            User(5, 'testUser', 'testPassword'),
            User(6, 'ramiro', '123'),
            User(7, 'abel', 'abel123')
        ]

    def acces_allowed(self, username, password):
        return any(user.username == username and user.password_valid(password) for user in self.user_list)

# Crear una instancia de UserController
ctrlUser = UserController()
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html') 

@app.route('/')
def home():
    return render_template('login.html')  # Asegúrate de tener el archivo login.html en la carpeta 'templates'

@app.route('/login', methods=['POST'])
def login():
    cuenta = request.form['cuenta']
    contrasena = request.form['contrasena']
    
    if ctrlUser.acces_allowed(cuenta, contrasena):
        flash('Acceso permitido', 'success')
        return redirect(url_for('dashboard'))  
    else:
        flash('Acceso denegado', 'danger')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
