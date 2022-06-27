from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Replicando la estructura de nuestra BDD
class Streamer(db.Model):

    # SQL nos colcoa por default un identificador para cada elemento, pero aca tenemos que detallarlro
    rowid = db.Column(db.Integer, primary_key=True)
    # recibe un limte de caracteres, puede se un unico dato, no puede ser nulo
    name = db.Column(db.String(200), unique=True, nullable=False)
    subs = db.Column(db.Integer)
    followers = db.Column(db.Integer)
