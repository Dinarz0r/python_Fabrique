Задача: спроектировать и разработать API для системы опросов пользователей.

Функционал для администратора системы:

    Для авторизации тестовый аккаунт.
    login: admin
    password: admin

- Для авторизации в системе http://localhost:8000/login/ или http://localhost:8000/api/auth/login/
- Для выхода из системы http://localhost:8000/api/auth/logout/
- Для добавления опроса трибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата
  старта" у опроса менять нельзя (http://localhost:8000/api/polls/ (исключительно для авторизованного пользователя))
- Для изменения/удаления опросов. http://localhost:8000/api/polls/<id_опроса_(например_1,_2,_3)> (исключительно для
  авторизованного пользователя)
- для http://127.0.0.1:8000/api/question/ добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст
  вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов))
- для изменения/удаления вопроса http://127.0.0.1:8000/api/polls/<id_вопроса>/questions/

Функционал для пользователей системы:

- получение списка активных опросов http://localhost:8000/api/polls/ (не для авторизованного пользователья будут
  выводится все активные опросы и в нем вложены вопросы)
- для получения списка вопросов http://localhost:8000/api//question/
- прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой
  ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве
  опросов
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя

- документация по API для разработчиков http://localhost:8000/swagger/ или через административную
  панель http://127.0.0.1:8000/admin/doc/

Некоторые моменты не реализовал так как нужно углубляться в документацию посчитал что в рамках поставленных сроков (3
часов) это сложно.