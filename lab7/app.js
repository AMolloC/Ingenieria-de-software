// app.js
const express = require('express');
const bodyParser = require('body-parser');
const { UserController, upload } = require('./controllers/UserController');
const UserService = require('./services/UserService'); // Importa el servicio de usuarios
const path = require('path');

const app = express();
app.set('view engine', 'pug');
app.set('views', path.join(__dirname, 'views'));

app.use('/uploads', express.static(path.join(__dirname, 'uploads')));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('uploads'));

// Rutas
app.get('/users', UserController.index);
app.get('/users/create', UserController.create);
app.post('/users', upload.single('imagen'), UserController.store);
app.get('/users/:id', UserController.show);
app.get('/users/:id/edit', UserController.edit);
app.post('/users/:id', upload.single('imagen'), UserController.update);
app.post('/users/:id/delete', UserController.delete);

// Ruta para mostrar el formulario de login
app.get('/login', (req, res) => {
  res.render('login'); // Muestra la vista login.pug
});

// Ruta para manejar el envío del formulario de login
app.post('/login', (req, res) => {
  const { username, password } = req.body;

  // Usa el servicio UserService para validar las credenciales
  UserService.validateUser(username, password, (err, user) => {
    if (err) throw err;

    if (user) {
      res.redirect('/users'); // Redirige a /users si las credenciales son correctas
    } else {
      res.render('login', { error: 'Credenciales inválidas' }); // Muestra un error si son incorrectas
    }
  });
});

app.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});
