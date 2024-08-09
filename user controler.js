clase UserController {
    constructor() {
        esto.listausuarios = [
            nuevo Usuario(1, 'johnDoe', 'contraseña123'),
            nuevo Usuario(2, 'janeDoe', 'ilovejavascript'),
            nuevo Usuario(3, 'admin', 'admin123'),
            nuevo Usuario(4, 'usuario123', 'contraseña123'),
            nuevo Usuario(5, 'testUser', 'testPassword'),
            nuevo Usuario(5, 'abel', 'abel123'),
            nuevo Usuario(6, 'ramiro', '123')
        ];
    }

    obtenerUsuarios() {
        devuelve esto.userList;
    }

    accesoPermitido(nombre de usuario, contraseña) {
        devuelve esto.userList.some(usuario => usuario.nombredeusuario === nombredeusuario && usuario.contraseñaValid(contraseña));
    }
}