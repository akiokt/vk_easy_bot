### Данный бот работает на технологии LongPoll.
### Права, необходимые боту: messages

---
### Создание команд:
#### 1. Заходим в commands.json
#### 1.1 Между {} пишем команды с использованием синтаксиса "команда": "текст"
#### 1.X Если нужно больше одной команды, после каждой пары "команда": "текст" пишем запятую. Если "команда": "текст" последняя, то запятую не пишем!
#### 1.XX ВАЖНО: команды необходимо писать ТОЛЬКО маленькими буквами!
#### 1.2 Сохраняем изменения

---
#### Настроить символ/слово с которого должно начинаться сообщение можно в файле commands.json -> "startwith": "сюда писать символ/слово".

---
### Как поставить бота:
#### 1. Настройка группы вк.
#### 1.1 Заходим в Управление -> Сообщения
#### 1.2 Сообщения сообщества ставим включены
#### 1.3 Заходим Настройки для бота и Возможности ботов: Включены
#### 1.4 Заходим в настройки -> работа с API
#### 1.5 Выбираем Long Poll api и выбираем версию API 5.130
#### 1.6 Напротив Long Poll API ставим с "выключено" на "включено"
#### 1.7 Заходим в Типы событий и выбираем: Входящие, исходящие сообщения и действия с сообщениями
#### 1.8 Заходим в Ключи доступа и жмём Создать ключ и выбираем "Разрешить приложению доступ к сообщениям сообщества"
#### 1.9 Открываем файл config.json и вместо "YOUR API HERE" вписываем ваш ключ.
#### 2. Настройка Pythonanywhere.
#### 2.1 Заходим на сайт pythonanywhere.com и регистрируемся (выбираем Create a beginner account)
#### 2.2 После регистрации вам предлагают пройти тур по сайту,но он нам не нужен и поэтому закройте его (кнопочка "end tour")
#### 2.3 Заходим в Files и по очереди (не архивом) загружаем файлы на сервер
#### 2.4 Переходим в Dashboard и жмём на $Bash (ждите, пока не появится "время ~ $")
#### 2.5 Пишем pip3 install --user vk_api
#### 2.6 После установки этого пакета (Как понять? Вы сможете снова писать в консоли) пишем python3 bot.py
#### 2.7 Поздравляю, вы успешно запустили бота.

---
### В будущем:
- #### Больше типов поддерживаемых комманд (принятие в группу, автопостинг и прочее)
- #### Добавление символа/слова для команды бота: !, @, name и прочее (сделано ★).
- #### Добавление команд через чат с ботом
- #### Добавление и удаление ролей (с уровнем доступа)
