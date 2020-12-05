
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

  
INSERT INTO datos (dni,nombre,apellido,fecha_nacimiento,direccion,telefono, mail, estado_civil)
  VALUES(31662636,'Octavio', 'Gomez', '1985-08-31', 'Rondeau 873', '2804303427', 'octaviogomez07gmail.com', 'soltero');

SELECT * FROM datos;
