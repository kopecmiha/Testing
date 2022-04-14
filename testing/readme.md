# Модуль Testing
Создание, редактирование и удаление тестов, вопросов и ответов

Основной url - https://testing-backend.admire.social/test/

#####Создание теста
Метод POST  
Требуется аккаунт преподавателя или декана  
url - /create_test/  
***
Запрос
```json
{
    "specialization_id":1,
    "discipline_id":1,
    "answer_time":240
}
```

Ответ
```json
{
    "message": "Test succesfully created"
}
```
Ошибка при недостаточном доступе
```json
{
    "detail": "You do not have permission to perform this action."
}
```

***

#####Редактирование теста
Метод POST  
Требуется аккаунт преподавателя или декана  
url - /update_test/
***
Запрос
```json
{
    "specialization_id": 2,
    "uuid_testing":"af08d23b-e15d-4548-ae02-84a17c70482c"
}
``` 

uuid_testing - уникальный идентификатор редактируемого теста

Ответ
```json
{
    "title": "SomeTest2",
    "subtitle": "SomeTest",
    "answer_time": 240
}
```
Ошибка при неверном или отсутсвующем uuid_testing
```json
{
    "error": "Testing not found"
}
```
***

#####Удаление теста
Метод POST  
Требуется аккаунт преподавателя или декана  
url - /delete_test/  
***
Запрос
```json
{
    "uuid_testing":"af08d23b-e15d-4548-ae02-84a17c70482c"
}
```

Ответ
```json
{
    "message": "Test succesfully deleted"
}
```
Ответ если тест по введенному uuid не найден
```json
{
    "message": "Nothing to delete"
}
```
***

#####Создание Вопроса
Метод POST  
Требуется аккаунт преподавателя или декана  
url - /create_question/  
***
Запрос
```json
{
    "text":"Где находится тардагукащирдуня",
    "competence_id": 1,
    "uuid_testing":"b8de46bc-2e98-460c-8ac5-90b6adbee1ff",
    "type_answer_question": "RADIO"
}
```

Ответ
```json
{
    "message": "Question succesfully created"
}
```
Ошибка если не предан uuid_testing или неверный
```json
{
    "error": "Testing not found"
}
```

***

#####Редактирование вопроса
Метод POST  
Требуется аккаунт преподавателя или декана  
url - /update_question/
***
Запрос
```json
{
    "text":"Где находится Эльбрус",
    "competence_id": 2,
    "uuid_question": "90584a79-855c-4764-9247-2ae21734988c"
}
``` 

uuid_question - уникальный идентификатор редактируемого вопроса

Ответ
```json
{
    "text": "Где находится Эльбрус",
    "type_answer_question": "RADIO",
    "uuid_question": "90584a79-855c-4764-9247-2ae21734988c",
    "answers": []
}
```
Ошибка при неверном или отсутсвующем uuid_question
```json
{
    "error": "Question not found"
}
```
***

#####Удаление теста
Метод POST  
Требуется аккаунт преподавателя или декана  
url - /delete_question/  
***
Запрос
```json
{
    "uuid_question": "90584a79-855c-4764-9247-2ae21734988c"
}
```

Ответ
```json
{
    "message": "Question succesfully deleted"
}
```
Ответ если вопрос по введенному uuid не найден
```json
{
    "message": "Nothing to delete"
}
```
***

#####Создание ответа
Метод POST  
Требуется аккаунт преподавателя или декана  
url - /create_answer/  
***
Запрос
```json
{
    "text" : "На море",
    "uuid_question": "4a3f6a5a-aa97-4018-91d3-6847d357c1d0",
    "correct_answer" : false
}
```

Ответ
```json
{
    "message": "Answer succesfully created"
}
```
Ошибка если не предан uuid_question или неверный
```json
{
    "error": "Question not found"
}
```

***

#####Редактирование ответа
Метод POST  
Требуется аккаунт преподавателя или декана  
url - /update_answer/
***
Запрос
```json
{
    "text" : "В лесу",
    "uuid_answer": "25e6686d-05c8-4655-92de-0f13c9c2dee8"
}
``` 

uuid_question - уникальный идентификатор редактируемого вопроса

Ответ
```json
{
    "text": "В лесу",
    "uuid_answer": "25e6686d-05c8-4655-92de-0f13c9c2dee8",
    "correct_answer": false
}
```
Ошибка при неверном или отсутсвующем uuid_answer
```json
{
    "error": "Answer not found"
}
```
***

#####Удаление ответа
Метод POST  
Требуется аккаунт преподавателя или декана  
url - /delete_answer/  
***
Запрос
```json
{
    "uuid_answer": "25e6686d-05c8-4655-92de-0f13c9c2dee8"
}
```

Ответ
```json
{
    "message": "Answer succesfully deleted"
}
```
Ответ если вопрос по введенному uuid не найден
```json
{
    "message": "Nothing to delete"
}
```
***

#####Запрос теста
Метод GET  
Требует авторизации  
url - /get_test/b8de46bc-2e98-460c-8ac5-90b6adbee1ff/
***

Ответ
```json
{
    "title": "Test",
    "subtitle": "Тестовый тест",
    "answer_time": 120,
    "uuid_testing": "b8de46bc-2e98-460c-8ac5-90b6adbee1ff",
    "questions": [
        {
            "text": "Что в черном ящике",
            "type_answer_question": "CHECKBOX",
            "uuid_question": "1ff79bfe-b1f0-4dac-8b46-28e7303409be",
            "answers": [
                {
                    "text": "Что то",
                    "uuid_answer": "ac93f72b-9e2a-4460-8c2e-d56f5d22174d",
                    "correct_answer": false
                },
                {
                    "text": "Кто то",
                    "uuid_answer": "28f94f1c-8b60-4ab0-a973-4f0f9d26c6cf",
                    "correct_answer": true
                }
            ]
        },
        {
            "text": "Где находится Эльбрус",
            "type_answer_question": "RADIO",
            "uuid_question": "4a3f6a5a-aa97-4018-91d3-6847d357c1d0",
            "answers": [
                {
                    "text": "На море",
                    "uuid_answer": "bdfdf3e9-bee2-4800-a416-4c2e759dae53",
                    "correct_answer": false
                },
                {
                    "text": "В горах",
                    "uuid_answer": "0efb17bd-0ac5-48a4-b36b-ff32f3aa850c",
                    "correct_answer": true
                }
            ]
        }
    ]
}
```
Ошибка если тест не найден
```json
{
    "error": "Test not found"
}
```
***

#####Список всех тестов
###Потом уберу запрос, когда тесты будут во что то вложены!
Метод GET  
Требует авторизации  
url - /list_test/
***
Ответ
```json
[
    {
        "title": "Test",
        "subtitle": "Тестовый тест",
        "uuid_testing": "b8de46bc-2e98-460c-8ac5-90b6adbee1ff"
    },
    {
        "title": "Куда поехать летом",
        "subtitle": "Просто",
        "uuid_testing": "d1ebf5e4-7d0c-41d7-b1cb-8875097d76bf"
    }
]
```
***