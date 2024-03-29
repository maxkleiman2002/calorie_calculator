import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Соединение с БД установлено. ")
    except Error as e:
        print(f"Ошибка {e} перехвачена. ")

    return connection

def execute_query(connection,query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Запрос успешно выполнен.")
    except Error as e:
        print(f"Ошибка {e} перехвачена. ")

def enter_data(connection,query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Данные записаны в поля.")
        cursor.close()

    except Error as e:
        print(f"Ошибка {e} перехвачена. ")


connection = create_connection("calorie_data1.db")

create_product_table = """
CREATE TABLE IF NOT EXISTS product(
id INTEGER ,
name TEXT NOT NULL,
calories INTEGER NOT NULL,
proteins REAL NOT NULL,
fats REAL NOT NULL,
carbohydrates REAL NOT NULL
);
"""

query = execute_query(connection,create_product_table)

create_product = """
INSERT INTO
product (name,calories,proteins,fats,carbohydrates)
VALUES
('Свекла',43, 1.6, 0.2, 10),
('Лук репчатый', 40, 1.1, 0.1, 9),
('Помидоры', 24, 1.1, 0.2, 3),
('Картофель отварной',83, 2.1, 0.6, 16.4),
('Картофель жареный', 185, 2.17, 9.64, 23.39),
('Картофель в мундире', 78, 2.86, 0.1, 13.9),
('Морковь', 35, 1.3, 0.1, 6.9),
('Огурец', 15, 0.7, 0.1, 3.6), 
('Белокачанная капуста', 25, 1.28, 0.1, 5.8),
('Цветная капуста', 25, 1.9, 0.3, 5),
('Зеленый горошок', 73, 5, 0.2, 12.8),
('Баклажан', 25, 1, 0.2, 6),
('Кабачок', 24, 0.6, 0.3, 4.6),
('Тыква', 26, 1, 0.1, 7),
('Перец сладкий', 27, 1.3, 0.1, 5.3),
('Редис', 16, 0.7, 0.1, 3.4),
('Репа', 28, 0.9, 0.1, 6),
('Сельдерей', 13, 0.9, 0.1, 2.1),
('Спаржа', 21, 1.9, 0.1, 3.1),
('Кукуруза вареная', 96, 3.4, 1.5, 18.6),
('Шампиньоны жаренные', 102, 3.6, 9.1, 1.3),
('Маслята маринованные', 24, 0.8, 0, 5.1),
('Белые грибы тушеные', 78, 3.2, 6.3, 2.4),
('Белые грибы вареные', 28, 2.2, 0.5, 3.1),
('Абрикос', 44, 0.9, 0.1, 9),
('Арбуз', 27, 0.7, 0.1, 5.8),
('Апельсин', 43, 0.9, 0.2, 8.1),
('Ананас', 52, 0.3, 0.1, 11.8),
('Банан', 96, 1.5, 0.5, 21),
('Дыня', 35, 0.6, 0.3, 7.4),
('Яблоко', 47, 0.4, 0.4, 9.8),
('Грейпфрут', 35, 0.7, 0.2, 6.5),
('Земляника', 33, 0.7, 0.3, 8),
('Мандарин', 40, 0.8, 0.3, 11.5),
('Виноград', 72, 0.6, 0.6, 15.4),
('Груша', 47, 0.4, 0.3, 10.3),
('Черешня', 52, 1.1, 0.4, 10.6),
('Вишня', 52, 0.8, 0.2, 10.6),
('Лимон', 34, 0.9, 0.1, 3),
('Персик', 45, 0.9, 0.1, 9.5),
('Слива', 46, 0.7, 0.3, 10), 
('Яблоки сушеные', 235, 2, 2, 49),
('Курага', 232, 5.2, 0.3, 51),
('Изюм', 299, 3.3, 0.3, 74.8),
('Чернослив', 256, 2.3, 0.7, 57.5),
('Манго', 60, 0.8, 0.4, 13.4), 
('Авокадо', 212, 2, 20, 6),
('Киви', 61, 1.1, 0.5, 11.7),
('Хлеб белый', 266, 8.9, 3.3, 46.7),
('Хлеб ржаной', 200, 6.3, 1.2, 43.3),
('Каша гречневая', 101, 3, 3.4, 14.6),
('Каша манная', 100, 2.2, 2.9, 16.4),
('Каша овсяная', 109, 2.6, 4.1, 15.5),
('Каша перловая', 135, 2.9, 3.5, 22.9),
('Каша пшеничная', 153, 4.4, 3.6, 25.7),
('Каша рисовая', 144, 2.4, 3.5, 25.8),
('Каша ячная', 96, 2.1, 2.9, 15.3),
('Каша гороховая',130, 10.5, 0.8, 20.4),
('Фасоль', 298, 21, 2 , 47),
('Горох', 298, 20.5, 2, 49.5),
('Макароны вареные', 112, 3.5, 0.4, 23.2),
('Молоко цельное', 67, 3, 4, 4.7),
('Творог нежирный', 110, 22, 0.6, 3.3),
('Творог 2%', 114, 20, 2, 3),
('Творог 4%', 136, 21, 4, 3),
('Творог 5%', 145, 21, 5, 3),
('Творог 9%(полужирный)', 169, 18, 9, 3),
('Творог 11%', 178, 16, 11, 3),
('Творог 18%(жирный)', 236, 15, 18, 2.8),
('Масса творожная 16,5%', 232, 12, 16.5, 9.5),
('Масса творожная 20%', 287, 11.5, 20, 14.5),
('Масса творожная с изюмом 23%', 345, 7.1, 23, 27.1),
('Сырки глазированные 10,9%', 270, 9.4, 10.9, 33.1),
('Сырки глазированные 27,7%', 413, 7.9, 27.7, 32.6),
('Сырки творожные 8%', 181, 15, 8, 11.5),
('Сырки творожные 16,5%', 238, 12, 16.5, 9.5),
('Сырки творожные 23%', 319, 9.1, 23, 18.5),
('Вареники ленивые', 173, 13.2, 7, 13.8),
('Сырники', 212, 15.9, 8.44, 17.39),
('Кефир 2,5%', 53, 2.9, 2.5, 4),
('Йогурт 6%', 92, 5, 6, 3.5),
('Йогурт 1,5%', 57, 4.1, 1.5, 5.9),
('Сливки 20%', 207, 2.5, 20, 4),
('Сливки 35%', 337, 2.2, 35, 3.2),
('Сливки 25%', 251, 2.4, 25, 3.9),
('Сливки 10%', 119, 2.7, 10, 4.5),
('Сливки 8%', 102, 2.8, 8, 4.5),
('Сметана 40%', 381, 2.4, 40, 2.6),
('Сметана 36%', 346, 2.4, 36, 2.6),
('Сметана 30%', 293, 2.3, 30, 3.1),
('Сметана 20%', 206, 2.5, 20, 3.4),
('Сметана 10%', 119, 2.7, 10, 3.9),
('Плавленый сыр КОМО', 237, 10.1, 21, 1.8),
('Сыр голландский', 330, 26.8, 25.2, 0),
('Сыр швейцарский',380, 27, 28, 5),
('Сыр российский', 364, 23.2, 29.5, 0),
('Сыр Рокфор', 369, 22, 31, 2),
('Сыр Камамбер',299, 20, 24, 0.5),
('Сыр Эмменталь', 375, 28.5, 29.1, 4.3),
('Сыр Пармезан', 431, 38, 29, 4.1),
('Сыр овечий', 341, 13.9, 27.9, 8.9),
('Яйцо варёное',155, 13, 11, 1.1),
('Сливочное масло', 717, 0.9, 81, 0.1),
('Масло топленое', 892, 0.2, 99, 0),
('Подсолнечное масло', 884, 0,0, 100),
('Кукурузное масло', 900, 0, 0, 100),
('Оливковое масло', 884, 0, 0 , 100),
('Соевое масло', 884, 0, 0, 100),
('Маргарин', 743, 0.3, 82, 1),
('Сало', 841, 1.4, 92.8, 0),
('Майонез', 629, 2.8, 67, 3.7),
('Мороженое молочное', 132, 3.7, 3.5, 21.3),
('Варенье из айвы', 221, 0.1, 0.1, 58.7),
('Варенье из вишни', 219, 0.3, 0.1, 58),
('Варенье из груши', 273, 0.3, 0.2, 70),
('Варенье из сливы', 203, 0.4, 0.1, 49.6),
('Варенье из персиков', 258, 0.5, 0, 66.8),
('Варенье из яблок', 265, 0.4, 0.3, 68.2),
('Варенье из абрикосов', 236, 0, 0, 62),
('Варенье из малины', 273, 0.6, 0.2, 70.4),
('Яблочное повидло', 250, 0.4, 0, 65),
('Повидло из абрикосов', 241, 0.3, 0, 64),
('Повидло Яблочное', 264, 0,0, 63),
('Сахар', 399, 0, 0, 99),
('Шоколад', 546, 4.9, 31, 61),
('Какао-порошок', 289, 24, 15, 10),
('Мёд', 308, 0.8, 0, 80),
('Торт Прага', 345, 4.2, 12, 47),
('Торт сметанный', 310, 5.9, 13.3, 41.8),
('Кедровый жмых', 432, 31, 19, 33),
('Семена пажитника', 323, 23, 6.4, 58.3),
('Абрикосовая косточка', 440, 14, 27, 56),
('Орех макадамия', 718, 7.9, 75.8, 5.2),
('Фундук', 704, 16, 66, 9.9),
('Семена льна', 534, 18, 42.2, 28.9),
('Семечки тыквенные', 556, 24.5, 45.8, 4.7),
('Кокосовый орех', 354, 3.4, 33.5, 6.2),
('Орех пекан', 691, 9.2, 72, 4.3),
('Кешью', 643, 25.7, 54.1, 13.2),
('Арахис сушеный', 611, 29.2, 50.2, 10.8),
('Орех лещина', 653, 131, 62.6, 9.3),
('Грецкий орех', 654, 15.2, 65.2, 7),
('Кедровые орехи', 673, 11.6, 61, 19.3),
('Фисташки', 556, 20, 50, 7),
('Кешью жареный', 572, 17.5, 42.2, 30.5),
('Финики', 274, 2.5, 0.5, 69.2),
('Арахис', 551, 26.3, 45.2, 9.9),
('Миндаль', 645, 18.6, 57.7, 16.2),
('Окунь речной', 91,19, 0.92, 0),
('Палтус черный', 196, 12.8, 16.1, 0),
('Пеламида', 217, 22.4, 14.2, 0),
('Печень трески', 613, 4.2, 65.7, 1.2),
('Рак речной', 77, 15.9, 0.95, 0),
('Сайра', 205, 19.5, 14.1, 0),
('Сардина океаническая', 166, 19, 10, 0),
('Салат из тунца', 187, 16.04, 9.26, 9.41),
('Севрюга', 160, 16.9, 10.3, 0),
('Скумбрия', 191, 18, 13.2, 0),
('Сом', 115, 17.2, 5.1, 0),
('Судак', 84, 18.4, 1.1, 0),
('Треска', 69, 16, 0.6, 0),
('Треска запеченная', 90, 6, 3.7, 0),
('Треска жареная', 123, 16, 5.1, 3.1),
('Тунец', 139, 24.4, 4.6, 0),
('Тунец в масле', 232, 22, 15.9, 0),
('Хек', 86, 16.6, 2.2, 0),
('Форель', 148, 20.77, 6.61, 0),
('Щука', 84, 18.4, 1.1, 0),
('Язь', 117, 19, 4.5, 0),
('Макрель', 113, 20.7, 3.4, 0),
('Лосось', 153, 20, 8.1, 0),
('Карп жареный', 181, 18.5, 10.5, 3.2),
('Карась', 87, 17.7, 1.8, 0),
('Баранина', 203, 16.3, 15.3, 0),
('Говядина', 187, 18.9, 12.4, 0),
('Баранья Печень', 101, 18.7, 2.9, 0),
('Говяжий Язык', 163, 13.6, 12.1, 0),
('Гуси', 364, 16.1, 33.3, 0),
('Индейка', 197, 21.6, 12, 0.8),
('Конина', 143, 20.2, 7, 0),
('Кролик', 199, 20.7, 12.9, 0),
('Курица', 165, 20.8, 8.8, 0.6),
('Свинина нежирная', 316, 16.4, 27.8, 0),
('Свинина жирная', 489, 11.4, 49.3, 0),
('Телятина', 90, 19.7, 1.2, 0),
('Утки', 346, 6.5, 61.2, 0),
('Цыплята', 156, 18.7, 7.8, 0.4);
"""


value = enter_data(connection,create_product)