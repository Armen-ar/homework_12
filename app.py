from flask import Flask, render_template, send_from_directory
from main.views import main_blueprint  # Импортируем блюпринты из их пакета
from loader.views import loader_blueprint  # Импортируем блюпринты из их пакета

app = Flask(__name__)
app.register_blueprint(main_blueprint)  # Регистрируем блюпринт
app.register_blueprint(loader_blueprint)  # Регистрируем блюпринт


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory('uploads', path)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
