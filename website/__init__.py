
import sys
sys.path.append("..")
def create_app(app):
    
    app.config['SECRET_KEY'] = 'randomstrings'
    app.config['UPLOAD_FOLDER'] = 'inputs/images'
    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app