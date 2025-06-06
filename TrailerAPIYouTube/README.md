# Install Project API-Trailer films YouTube

1.Інсталювати мову программування Python3 на сайті : https://www.python.org/downloads/
2.Інсталювати модулі для программи 
  * pip install flask 
  * pip install requests
  * pip install jsonify

# Отримання API : YouTube v3 Data API

Для того щоб отримати подивіться відео-інструкцію тут : https://www.youtube.com/watch?v=TE66McLMMEw

# Отримання API : TMDB API

Для того щоб отримати подивіться відео-інструкцію тут : https://www.youtube.com/watch?v=FlFyrOEz2S4&pp=ygUOI3RlbWFrZXJldGFhcGk%3D

# Як звернутись до API ?

Для того щоб звернутись до API потрібно в полі прописати відносний шлях : http://127.0.0.1:8000/api/search/us-US/Назва Фільму 


*Наприклад* 

http://127.0.0.1:8000/api/search/us-US/Интерстеллар

Воно нам виведе результат в хедерах 

{
  "results": [
    {
      "id": 157336,
      "title": "\u0418\u043d\u0442\u0435\u0440\u0441\u0442\u0435\u043b\u043b\u0430\u0440"
    },
    {
      "id": 336592,
      "title": "\u0418\u0437\u0443\u0447\u0435\u043d\u0438\u0435 \u00ab\u0418\u043d\u0442\u0435\u0440\u0441\u0442\u0435\u043b\u043b\u0430\u0440\u00bb"
    }
  ]
}

Якщо ми отформатуэмо отримаэмо зрозумілий json Header

{
  "results": [
    {
      "id": 157336,
      "title": "Интерстеллар"
    },
    {
      "id": 336592,
      "title": "Изучение «Интерстеллар»"
    }
  ]
}
