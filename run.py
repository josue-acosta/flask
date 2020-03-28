from app import app
from livereload import Server

# app configurations
app.config.from_object("config.DevelopmentConfig")

# run settings
if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.serve()
    # app.run()