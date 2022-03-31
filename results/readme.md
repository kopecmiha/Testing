# Модуль Results
Ответы на тесты

Основной url - https://testing-backend.admire.social/results/

#####Создание тестовой сессии
Метод POST  
url - /start_testing_session/
Требуется авторизованный пользователь
***
Запрос
```json
{
    "test_uuid": "b8de46bc-2e98-460c-8ac5-90b6adbee1ff"
}
```

Ответ
```json
{
    "message": "Test session created",
    "session_uuid": "51594be3-66d5-4ef7-acaf-addf898b69f2"
}
```
***

#####Завершение тестовой сессии
Метод POST  
url - /finish_testing_session/
Требуется авторизованный пользователь
***
Запрос
```json
{
    "session_uuid": "60dd463d-92a6-46d7-9ac0-3cfa98875580"
}
```

Ответ
```json
{
    "message": "Test session finished"
}
```

Ответ если сессия не найдена
```json
{"error": "Session not found"}
```
***

#####Ответ на вопрос
Метод POST  
url - /user_answer/
Требуется авторизованный пользователь
***
Запрос
```json
{
    "session_uuid":"60dd463d-92a6-46d7-9ac0-3cfa98875580",
    "question_uuid":"1ff79bfe-b1f0-4dac-8b46-28e7303409be",
    "answers_uuids":["ac93f72b-9e2a-4460-8c2e-d56f5d22174d"]
}
```

Ответ если все корректно
```json
{
    "message": "Result appended"
}
```

Ответ если сессия не найдена(некорректный uuid сессии или пользователь)
```json
{"error": "Session not found"}
```

Ответ ответ на завершенный тест
```json
{"error": "Testing finished"}
```

Ответ если время вышло
```json
{"error": "Time is over"}
```

Ответ если не найден вопрос по question_uuid
```json
{"error": "Question not found"}
```

Ответ если не найдены ответы по answers_uuids
```json
{"error": "Answers not found"}
```
***

#####Результаты теста
Метод GET  
url - /get_self_answers/b8de46bc-2e98-460c-8ac5-90b6adbee1ff/
Требуется авторизованный пользователь
URL параметром передается uuid теста
***

Ответ 
```json
[
    {
        "session_uuid": "60dd463d-92a6-46d7-9ac0-3cfa98875580",
        "test_started": "2022-03-30T12:41:27.880777Z",
        "test_finished": "2022-03-30T16:19:36.202388Z",
        "testing": {
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
        },
        "user": 11,
        "useranswers_set": [
            {
                "question_uuid": "1ff79bfe-b1f0-4dac-8b46-28e7303409be",
                "answers": [
                    {
                        "text": "Что то",
                        "uuid_answer": "ac93f72b-9e2a-4460-8c2e-d56f5d22174d",
                        "correct_answer": false,
                        "question": 1
                    }
                ]
            }
        ]
    }
]
```
***