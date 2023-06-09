# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка «Сияние». Если вы попали в этот репозиторий случайно, 
то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки 
или посмотреть как реализованы запросы к БД. 


Пульт охраны - это сайт, который можно подключить к удалённой базе данных с визитами 
и карточками пропуска сотрудников нашего банка.


### Как установить

Создайте файл .env и вставьте в него секретный ключ, а также данные для получения доступа к базе данных.

- `SECRET_KEY = 213123213`
- `DATABASE_URL = postgres://USER:PASSWORD@HOST:PORT/NAME`

(Пример того, что должно быть в файле .env )

В .env можно включить или отключить DEBUG вписав его в файл(по умолчанию стоит False)


Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

После установки всего необходимого, запустите сайт командой: 

```
python manage.py runserver 0.0.0.0:8000
```

Далее открываем сайт по ссылке:
```
http://127.0.0.1:8000/
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).