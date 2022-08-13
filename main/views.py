import logging  # импорт журнала ошибок
from flask import render_template, request, Blueprint  # импорт шаблонизатора

from functions import get_posts, content_for_the_posts  # импорт функций
from comfig import POST_PATH  # импорт константы (путь на Json-файл)
from exceptions import DataJsonError  # импорт модуль с классами ошибок

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')  # настройка папки с шаблонами
logging.basicConfig(filename='logger.log', level=logging.INFO, encoding='UTF-8')  # для записей действий


@main_blueprint.route("/")
def main_page():
    logging.info('Открытие главной страницы')  # запись в журнал
    return render_template('index.html')


@main_blueprint.route("/search")
def selected_post_page():
    s = request.args.get('s', '')  # получает аргумент, при отсутствии присвоит пустую подстроку
    logging.info('Выполняется поиск по вхождению')  # запись в журнал
    try:  # проверка на ошибку открытия файла
        posts = get_posts(POST_PATH)
    except DataJsonError:
        return f"Не открывается файл"
    selected_post = content_for_the_posts(posts, s)
    return render_template('post_list.html', posts=selected_post, s=s)  # в шаблон возвращает пост и подстроку
