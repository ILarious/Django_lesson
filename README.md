# Мой первый API проект на DRF (пример с занятия 07.08.2023)

---
### ДЗ: 
1. Создать приложение Django DRF (можно использовать проект с урока) 
2. Написать новую модель объявления (*либо постараться и написать комментарии которые ссылаются к объявлению специальным полем) 
3. Создать View (Create, List, RetrieveUpdateDestroy), urls к ним, и сериализаторы по своему усмотрению. 
4. Проверить работоспособность 
5. Оформить репозиторий согласно примеру: https://gitlab.ulinad.space/danilu/first_gitlab_project
---

### Установка

1. Клонировать репозиторий

    ```bash
    git clone https://github.com/ILarious/Django_lesson.git
    ```

2. Установить зависимости

    ```bash
    pip install -r 'requirements.txt'
    ```

3. Мигрировать БД

    ```bash
    python manage.py migrate
    ```
---

### Запуск

1. Добавить переменные окружения согласно .env.example

2. Для запуска введите в консоли:

    ```bash
    python manage.py runserver
    ```
