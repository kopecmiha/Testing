# Модуль Features
Создание, редактирование и удаление тестов, вопросов и ответов

Основной url - https://testing-backend.admire.social/test/

#####Создание дисциплины
Метод POST  
Требуется аккаунт преподавателя или декана  
url - /features/discipline/ 
***
Запрос
```json
{
        "title": "SomeTitle",
        "specialization_id": 3,
        "competences_ids": [1,2,3]
}
```
***

#####Редактирование дисциплины
Метод PUT  
Требуется аккаунт преподавателя или декана  
url - /features/discipline/<id>
***
Запрос
```json
{
        "title": "SomeTitle",
        "specialization_id": 3,
        "competences_ids": [1,2,3]
}
```
***

#####Создание компетенции
Метод POST  
Требуется аккаунт преподавателя или декана  
url - /features/competence/
***
Запрос
```json
{
        "code": "ОК-123",
        "specialization_id": 3
}
```
***

#####Редактирование компетенции
Метод PUT  
Требуется аккаунт преподавателя или декана  
url - /features/competence/<id>
***
Запрос
```json
{
        "code": "ОК-124",
        "specialization_id": 4
}
```
***

#####Запрос компетенции по специальности
Метод GET  
Требуется аккаунт преподавателя или декана  
url - /features/get_competences_by_specialization/<id>/
***
Ответ
```json
[
    {
        "id": 2,
        "code": "УК-1",
        "specialization": {
            "id": 3,
            "title": "TEST",
            "code": "201"
        }
    },
    {
        "id": 35,
        "code": "ОК-123",
        "specialization": {
            "id": 3,
            "title": "TEST",
            "code": "201"
        }
    }
]
```
***

#####Запрос компетенции по дисциплине
Метод GET  
Требуется аккаунт преподавателя или декана  
url - /features//features/get_competences_by_discipline/<id>/
***
Ответ
```json
[
    {
        "id": 2,
        "code": "УК-1",
        "specialization": {
            "id": 3,
            "title": "TEST",
            "code": "201"
        }
    },
    {
        "id": 35,
        "code": "ОК-123",
        "specialization": {
            "id": 3,
            "title": "TEST",
            "code": "201"
        }
    }
]
```
***