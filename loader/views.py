import logging
from flask import render_template, request, Blueprint  # Добавим импорт шаблонизатора
from functions import *  # импорт функций
from comfig import POST_PATH  # путь на Json-файл и к папке с картинками

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')  # настройка папки с шаблонами
logging.basicConfig(filename='logger.log', level=logging.INFO)  # для записей действий


@loader_blueprint.route("/post", methods=["GET"])  # по запросу просто открывает страницу
def new_post_page():
    return render_template('post_form.html')


@loader_blueprint.route("/post", methods=["POST"])  # добавляет пост страницу
def new_post_upload_page():
    picture = request.files.get('picture')  # получает картинку, файл
    content = request.form.get('content')  # получает текст
    if not picture or not content:  # если отсутствует картинка или текст
        logging.info('Данные не загружены')
        return "Отсутствуют данные"

    posts = get_posts(POST_PATH)  # получает все посты из json-файла списком

    new_picture = save_uploaded_picture(picture)
    new_post = {"pic": new_picture, "content": content}  # сохраняет в формате словарь: картинка-текст
    add_post(posts, new_post)  # вызываем функцию с аргументами
    return render_template('post_uploaded.html', new_post=new_post)
