from flask import Flask, render_template, request, jsonify, send_from_directory
import requests
import uuid

app = Flask(__name__)

API_KEY = "0c0f77464db6ebde01c597c123b0445c"
BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE = "https://image.tmdb.org/t/p/w500"
YOUTUBE_BASE = "https://www.youtube.com/embed/"
YOUTUBE_API_KEY = "AIzaSyBojew3-80CSCk2cz0IbKOEwScV9NiF3Kw"

@app.route("/")
def index():
    
    popular_url = f"{BASE_URL}/movie/popular?api_key={API_KEY}&language=ru-RU"
    popular_response = requests.get(popular_url)
    popular_movies = popular_response.json().get("results", [])
    
    
    top_rated_url = f"{BASE_URL}/movie/top_rated?api_key={API_KEY}&language=ru-RU"
    top_rated_response = requests.get(top_rated_url)
    top_rated_movies = top_rated_response.json().get("results", [])
    
    return render_template("index.html", 
                         popular_movies=popular_movies,
                         top_rated_movies=top_rated_movies,
                         image_base=IMAGE_BASE,
                         search_result=None,
                         search_error=None,
                         title_search_results=None,
                         title_search_error=None)

@app.route("/search", methods=["POST"])
def search():
    movie_id = request.form.get("movie_id")
    popular_url = f"{BASE_URL}/movie/popular?api_key={API_KEY}&language=ru-RU"
    popular_response = requests.get(popular_url)
    popular_movies = popular_response.json().get("results", [])
    
    top_rated_url = f"{BASE_URL}/movie/top_rated?api_key={API_KEY}&language=ru-RU"
    top_rated_response = requests.get(top_rated_url)
    top_rated_movies = top_rated_response.json().get("results", [])
    
    try:
        movie_id = int(movie_id)
        movie_url = f"{BASE_URL}/movie/{movie_id}?api_key={API_KEY}&language=ru-RU"
        response = requests.get(movie_url)
        if response.status_code == 200:
            movie = response.json()
            return render_template("index.html",
                                popular_movies=popular_movies,
                                top_rated_movies=top_rated_movies,
                                image_base=IMAGE_BASE,
                                search_result=movie,
                                search_error=None,
                                title_search_results=None,
                                title_search_error=None)
        else:
            return render_template("index.html",
                                popular_movies=popular_movies,
                                top_rated_movies=top_rated_movies,
                                image_base=IMAGE_BASE,
                                search_result=None,
                                search_error="Фильм с таким ID не найден",
                                title_search_results=None,
                                title_search_error=None)
    except (ValueError, TypeError):
        return render_template("index.html",
                            popular_movies=popular_movies,
                            top_rated_movies=top_rated_movies,
                            image_base=IMAGE_BASE,
                            search_result=None,
                            search_error="Введите корректный ID фильма (число)",
                            title_search_results=None,
                            title_search_error=None)

@app.route("/search_by_title", methods=["POST"])
def search_by_title():
    query = request.form.get("movie_title")
    popular_url = f"{BASE_URL}/movie/popular?api_key={API_KEY}&language=ru-RU"
    popular_response = requests.get(popular_url)
    popular_movies = popular_response.json().get("results", [])
    
    top_rated_url = f"{BASE_URL}/movie/top_rated?api_key={API_KEY}&language=ru-RU"
    top_rated_response = requests.get(top_rated_url)
    top_rated_movies = top_rated_response.json().get("results", [])
    
    if not query or query.strip() == "":
        return render_template("index.html",
                            popular_movies=popular_movies,
                            top_rated_movies=top_rated_movies,
                            image_base=IMAGE_BASE,
                            search_result=None,
                            search_error=None,
                            title_search_results=None,
                            title_search_error="Введите название фильма")
    
    search_url = f"{BASE_URL}/search/movie?api_key={API_KEY}&language=ru-RU&query={query}"
    response = requests.get(search_url)
    if response.status_code == 200:
        results = response.json().get("results", [])
        if results:
            return render_template("index.html",
                                popular_movies=popular_movies,
                                top_rated_movies=top_rated_movies,
                                image_base=IMAGE_BASE,
                                search_result=None,
                                search_error=None,
                                title_search_results=results,
                                title_search_error=None)
        else:
            return render_template("index.html",
                                popular_movies=popular_movies,
                                top_rated_movies=top_rated_movies,
                                image_base=IMAGE_BASE,
                                search_result=None,
                                search_error=None,
                                title_search_results=None,
                                title_search_error="Фильмы с таким названием не найдены")
    else:
        return render_template("index.html",
                            popular_movies=popular_movies,
                            top_rated_movies=top_rated_movies,
                            image_base=IMAGE_BASE,
                            search_result=None,
                            search_error=None,
                            title_search_results=None,
                            title_search_error="Ошибка при поиске фильмов")

@app.route("/movie/<int:movie_id>")
def movie_detail(movie_id):
    movie_url = f"{BASE_URL}/movie/{movie_id}?api_key={API_KEY}&language=ru-RU"
    video_url = f"{BASE_URL}/movie/{movie_id}/videos?api_key={API_KEY}&language=ru-RU"
    
    movie = requests.get(movie_url).json()
    video = requests.get(video_url).json()

    trailer_key = ""
    for v in video.get("results", []):
        if v["type"] == "Trailer" and v["site"] == "YouTube":
            trailer_key = v["key"]
            break
    
    if not trailer_key:
        youtube_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={movie['title']}+official+trailer&key={YOUTUBE_API_KEY}&type=video"
        youtube_response = requests.get(youtube_url)
        youtube_data = youtube_response.json()
        if youtube_data.get("items"):
            trailer_key = youtube_data["items"][0]["id"]["videoId"]

    return render_template("movie.html", 
                         movie=movie, 
                         trailer_key=trailer_key, 
                         youtube_base=YOUTUBE_BASE, 
                         image_base=IMAGE_BASE)

@app.route("/api/movie/<lang>/<list_type>")
def api_movies(lang, list_type):
    if list_type not in ["popular", "top_rated"]:
        return jsonify({"error": "Недопустимый тип списка. Используйте 'popular' или 'top_rated'"}), 400
    
    url = f"{BASE_URL}/movie/{list_type}?api_key={API_KEY}&language={lang}"
    data = requests.get(url).json()
    return jsonify(data)

@app.route("/api/movie/<lang>/videos/<int:movie_id>")
def api_video(lang, movie_id):
    url = f"{BASE_URL}/movie/{movie_id}/videos?api_key={API_KEY}&language={lang}"
    data = requests.get(url).json()
    
    if not data.get("results"):
        movie_url = f"{BASE_URL}/movie/{movie_id}?api_key={API_KEY}&language={lang}"
        movie = requests.get(movie_url).json()
        youtube_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={movie['title']}+official+trailer&key={YOUTUBE_API_KEY}&type=video"
        youtube_data = requests.get(youtube_url).json()
        if youtube_data.get("items"):
            data["results"] = [{
                "type": "Trailer",
                "site": "YouTube",
                "key": youtube_data["items"][0]["id"]["videoId"]
            }]
    
    return jsonify(data)

@app.route("/api/search/<lang>/<query>")
def api_search(lang, query):
    if not query or query.strip() == "":
        return jsonify({"error": "Запрос не может быть пустым"}), 400
    
    search_url = f"{BASE_URL}/search/movie?api_key={API_KEY}&language={lang}&query={query}"
    response = requests.get(search_url)
    if response.status_code == 200:
        results = response.json().get("results", [])
        
        titles = [{"id": movie["id"], "title": movie["title"]} for movie in results]
        return jsonify({"results": titles})
    else:
        return jsonify({"error": "Ошибка при поиске фильмов"}), 500

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
