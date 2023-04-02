from flaskr import create_app
from .modelos import db, Cancion, Usuario, Album, Medio
from .modelos import AlbumSchema

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

#PRUEBA
with app.app_context():
    album_schema = AlbumSchema()

    #c2 = Cancion(titulo="Prueba2", minutos=10,segundos=25, interprete='Gina' )
    u = Usuario(nombre='Juan', contrasena='123456')
    a = Album(titulo='Prueba',anio=199, descripcion='texto', medio=Medio.CD)
    c = Cancion(titulo="Prueba", minutos=2,segundos=25, interprete='Xander' )
    u.albumes.append(a)
    a.canciones.append(c)
    db.session.add(u)
    db.session.add(c)
    db.session.commit()
    
    #db.session.add(c2)
    print(Usuario.query.all())
    print(Album.query.all())
    print(Album.query.all()[0].canciones)
    print(Cancion.query.all())
    print([album_schema.dumps(album) for album in Album.query.all()])
    #db.session.delete(a)
    #print(Album.query.all())
    #print(Cancion.query.all())
