from database import db

class Workshop(db.Model):
    __tablename__ = 'workshops'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    fecha = db.Column(db.String(20), nullable=False)
    hora = db.Column(db.String(10), nullable=False)
    lugar = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)


class Registration(db.Model):
    __tablename__ = 'registrations'

    id = db.Column(db.Integer, primary_key=True)
    workshop_id = db.Column(db.Integer, nullable=False)
    estudiante = db.Column(db.String(100), nullable=False)
