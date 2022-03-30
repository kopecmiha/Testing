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