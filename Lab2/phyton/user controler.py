class Usuario:
    def __init__(self, id, nombre_de_usuario, contraseña):
        self.id = id
        self.nombre_de_usuario = nombre_de_usuario
        self.contraseña = contraseña

    def contraseña_valida(self, contraseña):
        return self.contraseña == contraseña

class UserController:
    def __init__(self):
        self.usuarios = [
            Usuario(1, 'johnDoe', 'contraseña123'),
            Usuario(2, 'janeDoe', 'ilovejavascript'),
            Usuario(3, 'admin', 'admin123'),
            Usuario(4, 'usuario123', 'contraseña123'),
            Usuario(5, 'testUser', 'testPassword'),
            Usuario(6, 'abel', 'abel123'),
            Usuario(7, 'ramiro', '123')
        ]

    def obtener_usuarios(self):
        return self.usuarios

    def acceso_permitido(self, nombre_de_usuario, contraseña):
        return any(usuario.nombre_de_usuario == nombre_de_usuario and usuario.contraseña_valida(contraseña) for usuario in self.usuarios)
