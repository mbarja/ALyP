from flask import (
    Flask,
    render_template,
    make_response,
    jsonify,
    request,
)
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid
import datetime

app = Flask(__name__)

PORT = 5000
HOST = '0.0.0.0'

json = {
    "languajes": {
        "es": "Spanish",
        "en": "English",
        "fr": "French",
    },
    "colors": {
        "r": "Red",
        "g": "Green",
        "b": "Blue",
   }
}

db_string = "postgres://admin:admin@app_db:5432/app_db"

engine = create_engine(db_string, echo=False)

metadata = MetaData()

users_table = Table(
            'datos',
            metadata,
            Column('dni', Integer, primary_key=True),
            Column('nombre', String),
            Column('apellido', String),
            Column('fecha_nacimiento', Date),
            Column('direccion', String),
            Column('telefono', String),
            Column('mail', String),
            Column('estado_civil', String),
           )

metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

class Datos(declarative_base()):
    __tablename__ = 'datos'

    dni = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    fecha_nacimiento = Column(Date)
    direccion = Column(String)
    telefono = Column(String)
    mail = Column(String)
    estado_civil = Column(String)

    def __init__(self, dni,nombre, apellido, fecha_nacimiento, direccion, telefono, mail, estado_civil):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.telefono = telefono
        self.mail = mail
        self.estado_civil = estado_civil

def existe_usuario(dni):
    query = session.query(Datos).filter(Datos.dni == dni).first()
    if not query:
        return False
    else:
        return True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/alta_datos", methods=["POST"])
def post_datos():
    dni = request.form.get('dni')
    if existe_usuario(dni):
        data = {'error': True, 'dni': True}
    else:
        fechaNacimiento = datetime.datetime.strptime(request.form.get('fecha_nacimiento'), "%m/%d/%Y").strftime("%Y-%m-%d")
        datos = Datos(
            dni,
            request.form.get('nombre'),
            request.form.get('apellido'),
            fechaNacimiento,
            request.form.get('direccion'),
            request.form.get('telefono'),
            request.form.get('mail'),
            request.form.get('estado_civil')
        )
        session.add(datos)
        session.commit()
        data = {'error': False}
    return make_response(jsonify(data), 200)


if __name__ == '__main__':
    print(f"Datos microservice runnning in port {PORT}")
    app.run(host=HOST, port=PORT, debug=True)