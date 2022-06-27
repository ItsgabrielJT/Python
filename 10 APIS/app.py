from flask import Flask
from Model import db, Streamer

app = Flask(__name__) # __name__ es el nombre de nuestro fichero
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database\\streamers.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # Nos quita unos avisos, pero no afecta en nada al codigo

db.init_app(app) #  A que BDD se tiene que concectar

# La direccion anterior ees la ip de nuestro ordenador
@app.route("/") # Estamos diciendo con el slash que nos diriga a esta direccion http://127.0.0.1:4000
def Home():
    return "<h1> Welcome a mi pagina </h1>"

# Nos devulve nuestros datos de streamers
@app.route("/api/streamers")
def getStreamers():
    streamers = Streamer.query.all()
    print(streamers)
    return "<h1> Success !!! </h1>"




if __name__ == "__main__":
    app.run(debug=True, port=4000)


