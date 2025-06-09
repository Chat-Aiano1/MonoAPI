from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
import uuid
from starlette.responses import FileResponse
import uvicorn

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

API_KEY = "0c0f77464db6ebde01c597c123b0445c"
BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE = "https://image.tmdb.org/t/p/w500"
YOUTUBE_BASE = "https://www.youtube.com/embed/"
YOUTUBE_API_KEY = "AIzaSyBojew3-80CSCk2cz0IbKOEwScV9NiF3Kw"

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    popular_url = f"{BASE_URL}/movie/popular?api_key={API_KEY}&language=ru-RU"
    popular_response = requests.get(popular_url)
    popular_movies = popular_response.json().get("results", [])

    top_rated_url = f"{BASE_URL}/movie/top_rated?api_key={API_KEY}&language=ru-RU"
    top_rated_response = requests.get(top_rated_url)
    top_rated_movies = top_rated_response.json().get("results", [])

    return templates.TemplateResponse("index.html",
                                     {"request": request,
                                      "popular_movies": popular_movies,
                                      "top_rated_movies": top_rated_movies,
                                      "image_base": IMAGE_BASE,
                                      "search_result": None,
                                      "search_error": None,
                                      "title_search_results": None,
                                      "title_search_error": None})

@app.post("/search", response_class=HTMLResponse)
async def search(request: Request, movie_id: str = Form(...)):
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
            return templates.TemplateResponse("index.html",
                                             {"request": request,
                                              "popular_movies": popular_movies,
                                              "top_rated_movies": top_rated_movies,
                                              "image_base": IMAGE_BASE,
                                              "search_result": movie,
                                              "search_error": None,
                                              "title_search_results": None,
                                              "title_search_error": None})
        else:
            return templates.TemplateResponse("index.html",
                                             {"request": request,
                                              "popular_movies": popular_movies,
                                              "top_rated_movies": top_rated_movies,
                                              "image_base": IMAGE_BASE,
                                              "search_result": None,
                                              "search_error": "Фільм с таким ID не був знайдений",
                                              "title_search_results": None,
                                              "title_search_error": None})
    except (ValueError, TypeError):
        return templates.TemplateResponse("index.html",
                                         {"request": request,
                                          "popular_movies": popular_movies,
                                          "top_rated_movies": top_rated_movies,
                                          "image_base": IMAGE_BASE,
                                          "search_result": None,
                                          "search_error": "Введіть правильний ID фильму (число)",
                                          "title_search_results": None,
                                          "title_search_error": None})

@app.post("/search_by_title", response_class=HTMLResponse)
async def search_by_title(request: Request, movie_title: str = Form(...)):
    popular_url = f"{BASE_URL}/movie/popular?api_key={API_KEY}&language=ru-RU"
    popular_response = requests.get(popular_url)
    popular_movies = popular_response.json().get("results", [])

    top_rated_url = f"{BASE_URL}/movie/top_rated?api_key={API_KEY}&language=ru-RU"
    top_rated_response = requests.get(top_rated_url)
    top_rated_movies = top_rated_response.json().get("results", [])

    if not movie_title or movie_title.strip() == "":
        return templates.TemplateResponse("index.html",
                                         {"request": request,
                                          "popular_movies": popular_movies,
                                          "top_rated_movies": top_rated_movies,
                                          "image_base": IMAGE_BASE,
                                          "search_result": None,
                                          "search_error": None,
                                          "title_search_results": None,
                                          "title_search_error": "Введіть назву фільму"})

    search_url = f"{BASE_URL}/search/movie?api_key={API_KEY}&language=ru-RU&query={movie_title}"
    response = requests.get(search_url)
    if response.status_code == 200:
        results = response.json().get("results", [])
        if results:
            return templates.TemplateResponse("index.html",
                                             {"request": request,
                                              "popular_movies": popular_movies,
                                              "top_rated_movies": top_rated_movies,
                                              "image_base": IMAGE_BASE,
                                              "search_result": None,
                                              "search_error": None,
                                              "title_search_results": results,
                                              "title_search_error": None})
        else:
            return templates.TemplateResponse("index.html",
                                             {"request": request,
                                              "popular_movies": popular_movies,
                                              "top_rated_movies": top_rated_movies,
                                              "image_base": IMAGE_BASE,
                                              "search_result": None,
                                              "search_error": None,
                                              "title_search_results": None,
                                              "title_search_error": "Фільм з такою назвою не знайдений."})
    else:
        return templates.TemplateResponse("index.html",
                                         {"request": request,
                                          "popular_movies": popular_movies,
                                          "top_rated_movies": top_rated_movies,
                                          "image_base": IMAGE_BASE,
                                          "search_result": None,
                                          "search_error": None,
                                          "title_search_results": None,
                                          "title_search_error": "Помилка при пошуку фільмів."})

@app.get("/movie/{movie_id}", response_class=HTMLResponse)
async def movie_detail(request: Request, movie_id: int):
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

    return templates.TemplateResponse("movie.html",
                                     {"request": request,
                                      "movie": movie,
                                      "trailer_key": trailer_key,
                                      "youtube_base": YOUTUBE_BASE,
                                      "image_base": IMAGE_BASE})

@app.get("/api/movie/{lang}/{list_type}")
async def api_movies(lang: str, list_type: str):
    if list_type not in ["popular", "top_rated"]:
        return JSONResponse(content={"error": "Недоступній тип із списку. Застосовуйте 'popular' или 'top_rated'"}, status_code=400)

    url = f"{BASE_URL}/movie/{list_type}?api_key={API_KEY}&language={lang}"
    data = requests.get(url).json()
    return JSONResponse(content=data)

@app.get("/api/movie/{lang}/videos/{movie_id}")
async def api_video(lang: str, movie_id: int):
    url = f"{BASE_URL}/movie/{movie_id}/videos?api_key={API_KEY}&language={lang}"
    data = requests.get(url).json()

    if not data.get("results"):
        movie_url = f"{BASE_URL}/movie/{movie_id}?api_key={API_KEY}&language={lang}"
        movie = requests.get(movie_url).json()
        youtube_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={movie['title']}+official+trailer&key={YOUTUBE_API_KEY}&type=video"
        youtube_response = requests.get(youtube_url)
        youtube_data = youtube_response.json()
        if youtube_data.get("items"):
            data["results"] = [{
                "type": "Trailer",
                "site": "YouTube",
                "key": youtube_data["items"][0]["id"]["videoId"]
            }]

    return JSONResponse(content=data)

@app.get("/api/search/{lang}/{query}")
async def api_search(lang: str, query: str):
    if not query or query.strip() == "":
        return JSONResponse(content={"error": "Запит не може бути порожнім"}, status_code=400)

    search_url = f"{BASE_URL}/search/movieocial media group icon movie?api_key={API_KEY}&language={lang}&query={query}"
    response = requests.get(search_url)
    if response.status_code == 200:
        results = response.json().get("results", [])
        titles = [{"id": movie["id"], "title": movie["title"]} for movie in results]
        return JSONResponse(content={"results": titles})
    else:
        return JSONResponse(content={"error": "Помилка при пошуку фільмів"}, status_code=500)

@app.get('/favicon.ico')
async def favicon():
    return FileResponse('static/favicon.ico')

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
