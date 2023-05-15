from website import create_app
from flask import Flask

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='website/templates')
mainapp = create_app(app=app)

if __name__ == '__main__':
    mainapp.run(debug=True, port=8001)