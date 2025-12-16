from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workshops.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# =======================
# MODELOS
# =======================

class Workshop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(200))
    fecha = db.Column(db.String(20))
    hora = db.Column(db.String(20))
    lugar = db.Column(db.String(100))
    categoria = db.Column(db.String(50))

class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_estudiante = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    workshop_id = db.Column(db.Integer, db.ForeignKey('workshop.id'), nullable=False)

# =======================
# CREAR BD
# =======================

with app.app_context():
    db.create_all()

# =======================
# ENDPOINTS
# =======================

# GET todos los talleres
@app.route('/workshops', methods=['GET'])
def get_workshops():
    workshops = Workshop.query.all()
    return jsonify([
        {
            "id": w.id,
            "nombre": w.nombre,
            "descripcion": w.descripcion,
            "fecha": w.fecha,
            "hora": w.hora,
            "lugar": w.lugar,
            "categoria": w.categoria
        } for w in workshops
    ]), 200


# GET taller por ID
@app.route('/workshops/<int:id>', methods=['GET'])
def get_workshop(id):
    workshop = Workshop.query.get_or_404(id)
    return jsonify({
        "id": workshop.id,
        "nombre": workshop.nombre,
        "descripcion": workshop.descripcion,
        "fecha": workshop.fecha,
        "hora": workshop.hora,
        "lugar": workshop.lugar,
        "categoria": workshop.categoria
    }), 200


# POST crear taller
@app.route('/workshops', methods=['POST'])
def create_workshop():
    data = request.json

    workshop = Workshop(
        nombre=data['nombre'],
        descripcion=data.get('descripcion'),
        fecha=data.get('fecha'),
        hora=data.get('hora'),
        lugar=data.get('lugar'),
        categoria=data.get('categoria')
    )

    db.session.add(workshop)
    db.session.commit()

    return jsonify({"mensaje": "Taller creado correctamente"}), 201


# PUT modificar taller
@app.route('/workshops/<int:id>', methods=['PUT'])
def update_workshop(id):
    workshop = Workshop.query.get_or_404(id)
    data = request.json

    workshop.nombre = data.get('nombre', workshop.nombre)
    workshop.descripcion = data.get('descripcion', workshop.descripcion)
    workshop.fecha = data.get('fecha', workshop.fecha)
    workshop.hora = data.get('hora', workshop.hora)
    workshop.lugar = data.get('lugar', workshop.lugar)
    workshop.categoria = data.get('categoria', workshop.categoria)

    db.session.commit()
    return jsonify({"mensaje": "Taller actualizado correctamente"}), 200


# DELETE eliminar taller
@app.route('/workshops/<int:id>', methods=['DELETE'])
def delete_workshop(id):
    workshop = Workshop.query.get_or_404(id)
    db.session.delete(workshop)
    db.session.commit()
    return jsonify({"mensaje": "Taller eliminado correctamente"}), 200


# POST registrar estudiante
@app.route('/workshops/<int:id>/register', methods=['POST'])
def register_student(id):
    workshop = Workshop.query.get_or_404(id)
    data = request.json

    if not data or 'nombre_estudiante' not in data or 'correo' not in data:
        return jsonify({"error": "Datos incompletos"}), 400

    registration = Registration(
        nombre_estudiante=data['nombre_estudiante'],
        correo=data['correo'],
        workshop_id=workshop.id
    )

    db.session.add(registration)
    db.session.commit()

    return jsonify({"mensaje": "Estudiante registrado correctamente"}), 201


# =======================
# EJECUTAR
# =======================

if __name__ == '__main__':
    app.run(debug=True)

# GET estudiantes registrados en un taller
@app.route('/workshops/<int:id>/registrations', methods=['GET'])
def get_registrations(id):
    workshop = Workshop.query.get_or_404(id)

    registrations = Registration.query.filter_by(workshop_id=id).all()

    return jsonify([
        {
            "id": r.id,
            "nombre_estudiante": r.nombre_estudiante,
            "correo": r.correo
        } for r in registrations
    ]), 200
