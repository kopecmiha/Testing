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