
CREATE TABLE datos(
    dni integer PRIMARY KEY,
    nombre character(30) NOT NULL,
    apellido character(30) NOT NULL,
    fecha_nacimiento date NOT NULL,
    direccion character(30) NOT NULL,
    telefono character(30) NOT NULL,
    mail character(30) NOT NULL,
    estado_civil character(10) NOT NULL
);

