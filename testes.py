from app import app, database

# with app.app_context():
#    database.create_all()

# with app.app_context():
#    usuario = Usuario(username='Alexandre', email='alexandre@mgial.com', senha='123456')
#    usuario2 = Usuario(username='Michele', email='michele@gmail.com', senha='123456')
#    database.session.add(usuario)
#    database.session.add(usuario2)
#    database.session.commit()
# with app.app_context():
#    meus_usuarios = Usuario.query.all()
#    print(meus_usuarios)

# with app.app_context():
#    usuario_teste = Usuario.query.filter_by(id=1).first()
#    print(usuario_teste)
#    print(usuario_teste.posts)

# with app.app_context():
#     meu_post = Post(id_usuario=1, titulo="Primeiro Post do Alexandre", corpo="Sabino")
#     database.session.add(meu_post)
#     database.session.commit()

# with app.app_context():
#     post = Post.query.first()
#     print(post.titulo)
#     print(post.autor.email)

# with app.app_context():
#    database.drop_all()
#    database.create_all()