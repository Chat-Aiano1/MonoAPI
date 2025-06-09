# Install Project API-Trailer films YouTube

1.Інсталювати мову программування Python3 на сайті : https://www.python.org/downloads/
2.Інсталювати модулі для программи : Flask_Server [main.py]
  * pip install flask 
  * pip install requests
  * pip install jsonify

# АБО

1.Інсталювати модулі для программи : FastAPI [fast.py]
  * pip install -r requirements.txt


# Отримання API : YouTube v3 Data API

Для того щоб отримати подивіться відео-інструкцію тут : https://www.youtube.com/watch?v=TE66McLMMEw

# Отримання API : TMDB API

Для того щоб отримати подивіться відео-інструкцію тут : https://www.youtube.com/watch?v=FlFyrOEz2S4&pp=ygUOI3RlbWFrZXJldGFhcGk%3D

# Як звернутись до API ?

Для того щоб звернутись до API потрібно в полі прописати відносний шлях : http://127.0.0.1:8000/api/search/us-US/Назва Фільму 


*Наприклад Flask_Server Endpoint* 

http://127.0.0.1:8000/api/search/us-US/Интерстеллар

Воно нам виведе результат в хедерах :

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


*Наприклад FastAPI Endpoint*

Пииклади Ендпоінтів API 


127.0.0.1:8000/api/movie/us-US/videos/550

{
  "id": 550,
  "results": [
    {
      "iso_639_1": "en",
      "iso_3166_1": "US",
      "name": "Yeah... no wonder this movie never won an Oscar",
      "key": "V0Fqdb-smqo",
      "site": "YouTube",
      "size": 1080,
      "type": "Featurette",
      "official": false,
      "published_at": "2025-02-14T14:25:16.000Z",
      "id": "67c90f7a3dd7da394f24957b"
    },
    {
      "iso_639_1": "en",
      "iso_3166_1": "US",
      "name": "20th Anniversary Trailer",
      "key": "dfeUzm6KF4g",
      "site": "YouTube",
      "size": 1080,
      "type": "Trailer",
      "official": true,
      "published_at": "2019-10-15T18:59:47.000Z",
      "id": "64fb16fbdb4ed610343d72c3"
    },
    {
      "iso_639_1": "en",
      "iso_3166_1": "US",
      "name": "Mark Kermode introduces Fight Club | Film4 Interview",
      "key": "tiWCNtGDGEY",
      "site": "YouTube",
      "size": 1080,
      "type": "Featurette",
      "official": true,
      "published_at": "2015-05-08T15:59:05.000Z",
      "id": "65d00d0c57176f017b8fc73d"
    },
    {
      "iso_639_1": "en",
      "iso_3166_1": "US",
      "name": "Theatrical Trailer (HD Fan Remaster)",
      "key": "6JnN1DmbqoU",
      "site": "YouTube",
      "size": 1080,
      "type": "Trailer",
      "official": false,
      "published_at": "2015-02-26T03:19:25.000Z",
      "id": "653b36ba5907de00c4953699"
    },
    {
      "iso_639_1": "en",
      "iso_3166_1": "US",
      "name": "#TBT Trailer",
      "key": "BdJKm16Co6M",
      "site": "YouTube",
      "size": 1080,
      "type": "Trailer",
      "official": true,
      "published_at": "2014-10-02T19:20:22.000Z",
      "id": "5c9294240e0a267cd516835f"
    }
  ]
}



127.0.0.1:8000/api/movie/popular

{
  "page": 1,
  "results": [
    {
      "adult": false,
      "backdrop_path": "/a3F9cXjRH488qcOqFmFZwqawBMU.jpg",
      "genre_ids": [16, 878, 28],
      "id": 1376434,
      "original_language": "en",
      "original_title": "Predator: Killer of Killers",
      "overview": "This original animated anthology follows three of the fiercest warriors in human history: a Viking raider guiding her young son on a bloody quest for revenge, a ninja in feudal Japan who turns against his Samurai brother in a brutal battle for succession, and a WWII pilot who takes to the sky to investigate an otherworldly threat to the Allied cause.",
      "popularity": 792.9766,
      "poster_path": "/lbimIPTVsSlnmqSW5ngEsUxtHLM.jpg",
      "release_date": "2025-06-05",
      "title": "Predator: Killer of Killers",
      "video": false,
      "vote_average": 8,
      "vote_count": 235
    },
    {
      "adult": false,
      "backdrop_path": "/yBDvgpyynDsbMyK21FoQu1c2wYR.jpg",
      "genre_ids": [9648, 80, 53],
      "id": 870028,
      "original_language": "en",
      "original_title": "The Accountant²",
      "overview": "When an old acquaintance is murdered, Wolff is compelled to solve the case. Realizing more extreme measures are necessary, Wolff recruits his estranged and highly lethal brother, Brax, to help. In partnership with Marybeth Medina, they uncover a deadly conspiracy, becoming targets of a ruthless network of killers who will stop at nothing to keep their secrets buried.",
      "popularity": 711.6688,
      "poster_path": "/ieYaJz2nzs4wcqpWaofagzGoGPi.jpg",
      "release_date": "2025-04-23",
      "title": "The Accountant²",
      "video": false,
      "vote_average": 7.2,
      "vote_count": 502
    },
    {
      "adult": false,
      "backdrop_path": "/7Zx3wDG5bBtcfk8lcnCWDOLM4Y4.jpg",
      "genre_ids": [10751, 35, 878, 12],
      "id": 552524,
      "original_language": "en",
      "original_title": "Lilo & Stitch",
      "overview": "The wildly funny and touching story of a lonely Hawaiian girl and the fugitive alien who helps to mend her broken family.",
      "popularity": 571.1231,
      "poster_path": "/tUae3mefrDVTgm5mRzqWnZK6fOP.jpg",
      "release_date": "2025-05-17",
      "title": "Lilo & Stitch",
      "video": false,
      "vote_average": 7.116,
      "vote_count": 546
    },
    {
      "adult": false,
      "backdrop_path": "/nAxGnGHOsfzufThz20zgmRwKur3.jpg",
      "genre_ids": [27, 28, 53],
      "id": 1233413,
      "original_language": "en",
      "original_title": "Sinners",
      "overview": "Trying to leave their troubled lives behind, twin brothers return to their hometown to start again, only to discover that an even greater evil is waiting to welcome them back.",
      "popularity": 553.0692,
      "poster_path": "/jYfMTSiFFK7ffbY2lay4zyvTkEk.jpg",
      "release_date": "2025-04-16",
      "title": "Sinners",
      "video": false,
      "vote_average": 7.5,
      "vote_count": 1288
    },
    {
      "adult": false,
      "backdrop_path": "/v67tbCB03CMcJRWit8CS7JdJp6.jpg",
      "genre_ids": [28, 53, 18],
      "id": 757725,
      "original_language": "en",
      "original_title": "Shadow Force",
      "overview": "Kyrah and Isaac were once the leaders of a multinational special forces group called Shadow Force. They broke the rules by falling in love, and in order to protect their son, they go underground. With a large bounty on their heads, and the vengeful Shadow Force hot on their trail, one family's fight becomes all-out war.",
      "popularity": 349.5856,
      "poster_path": "/7IEW24vBiZerZrDlgLVSUU3oT1C.jpg",
      "release_date": "2025-05-01",
      "title": "Shadow Force",
      "video": false,
      "vote_average": 6.307,
      "vote_count": 57
    },
    {
      "adult": false,
      "backdrop_path": "/2Nti3gYAX513wvhp8IiLL6ZDyOm.jpg",
      "genre_ids": [10751, 35, 12, 14],
      "id": 950387,
      "original_language": "en",
      "original_title": "A Minecraft Movie",
      "overview": "Four misfits find themselves struggling with ordinary problems when they are suddenly pulled through a mysterious portal into the Overworld: a bizarre, cubic wonderland that thrives on imagination. To get back home, they'll have to master this world while embarking on a magical quest with an unexpected, expert crafter, Steve.",
      "popularity": 311.5447,
      "poster_path": "/yFHHfHcUgGAxziP1C3lLt0q2T4s.jpg",
      "release_date": "2025-03-31",
      "title": "A Minecraft Movie",
      "video": false,
      "vote_average": 6.512,
      "vote_count": 1718
    },
    {
      "adult": false,
      "backdrop_path": "/uIpJPDNFoeX0TVml9smPrs9KUVx.jpg",
      "genre_ids": [27, 9648],
      "id": 574475,
      "original_language": "en",
      "original_title": "Final Destination Bloodlines",
      "overview": "Plagued by a violent recurring nightmare, college student Stefanie heads home to track down the one person who might be able to break the cycle and save her family from the grisly demise that inevitably awaits them all.",
      "popularity": 278.9729,
      "poster_path": "/6WxhEvFsauuACfv8HyoVX6mZKFj.jpg",
      "release_date": "2025-05-14",
      "title": "Final Destination Bloodlines",
      "video": false,
      "vote_average": 6.985,
      "vote_count": 605
    },
    {
      "adult": false,
      "backdrop_path": "/fTrQsdMS2MUw00RnzH0r3JWHhts.jpg",
      "genre_ids": [28, 80, 53],
      "id": 1197306,
      "original_language": "en",
      "original_title": "A Working Man",
      "overview": "Levon Cade left behind a decorated military career in the black ops to live a simple life working construction. But when his boss's daughter, who is like family to him, is taken by human traffickers, his search to bring her home uncovers a world of corruption far greater than he ever could have imagined.",
      "popularity": 249.9285,
      "poster_path": "/6FRFIogh3zFnVWn7Z6zcYnIbRcX.jpg",
      "release_date": "2025-03-26",
      "title": "A Working Man",
      "video": false,
      "vote_average": 6.684,
      "vote_count": 1186
    },
    {
      "adult": false,
      "backdrop_path": "/rRIz3KweJDjnJ4GtCZJT3JPEYgL.jpg",
      "genre_ids": [28, 12],
      "id": 1411773,
      "original_language": "en",
      "original_title": "The Last Stand of Ellen Cole",
      "overview": "When an evil contractor goes to extreme measures to evict a testy tenant who is standing in the way of his new project, he fails to take into account that this seemingly harmless old woman is a trained killer and will do anything to protect her beloved home.",
      "popularity": 244.9839,
      "poster_path": "/oq1pGVQ2t3Cy4v7sA4LRhNjtZuJ.jpg",
      "release_date": "2024-10-18",
      "title": "The Last Stand of Ellen Cole",
      "video": false,
      "vote_average": 8.417,
      "vote_count": 18
    },
    {
      "adult": false,
      "backdrop_path": "/4MNRH73XmwBK2ycv3qvLpa07O5F.jpg",
      "genre_ids": [28, 18],
      "id": 1257960,
      "original_language": "hi",
      "original_title": "सिकंदर",
      "overview": "A tragic accident pushes the powerful Sikandar to protect the less fortunate by standing up to corruption and greed — using any means necessary.",
      "popularity": 192.0116,
      "poster_path": "/t48miSSfe7COqgbgMyRIyPVTBoM.jpg",
      "release_date": "2025-03-29",
      "title": "Sikandar",
      "video": false,
      "vote_average": 5.125,
      "vote_count": 48
    },
    {
      "adult": false,
      "backdrop_path": "/eQV9rSQ6S1ja4lGTwHTnQuVhoG.jpg",
      "genre_ids": [27, 35, 14, 18],
      "id": 1284120,
      "original_language": "no",
      "original_title": "Den stygge stesøsteren",
      "overview": "In a fairy-tale kingdom where beauty is a brutal business, Elvira battles to compete with her incredibly beautiful stepsister, and she will go to any length to catch the prince’s eye.",
      "popularity": 231.6285,
      "poster_path": "/crX9rSg9EohybhkEe8iTQUCe55y.jpg",
      "release_date": "2025-03-07",
      "title": "The Ugly Stepsister",
      "video": false,
      "vote_average": 7,
      "vote_count": 139
    },
    {
      "adult": false,
      "backdrop_path": "/xOuhhbQ3Nzznt5MjRdLBJb0CmDE.jpg",
      "genre_ids": [28, 12, 53],
      "id": 575265,
      "original_language": "en",
      "original_title": "Mission: Impossible - The Final Reckoning",
      "overview": "Ethan Hunt and team continue their search for the terrifying AI known as the Entity — which has infiltrated intelligence networks all over the globe — with the world's governments and a mysterious ghost from Hunt's past on their trail. Joined by new allies and armed with the means to shut the Entity down for good, Hunt is in a race against time to prevent the world as we know it from changing forever.",
      "popularity": 212.233,
      "poster_path": "/z53D72EAOxGRqdr7KXXWp9dJiDe.jpg",
      "release_date": "2025-05-17",
      "title": "Mission: Impossible - The Final Reckoning",
      "video": false,
      "vote_average": 7.164,
      "vote_count": 691
    },
    {
      "adult": false,
      "backdrop_path": "/oPgXVSdGR9dGwbmvIToOCMmsdc2.jpg",
      "genre_ids": [28, 53, 80],
      "id": 541671,
      "original_language": "en",
      "original_title": "Ballerina",
      "overview": "Taking place during the events of John Wick: Chapter 3 – Parabellum, Eve Macarro begins her training in the assassin traditions of the Ruska Roma.",
      "popularity": 206.7834,
      "poster_path": "/mKp4euM5Cv3m2U1Vmby3OGwcD5y.jpg",
      "release_date": "2025-06-04",
      "title": "Ballerina",
      "video": false,
      "vote_average": 7.115,
      "vote_count": 126
    },
    {
      "adult": false,
      "backdrop_path": "/mDfJG3LC3Dqb67AZ52x3Z0jU0uB.jpg",
      "genre_ids": [12, 28, 878],
      "id": 299536,
      "original_language": "en",
      "original_title": "Avengers: Infinity War",
      "overview": "As the Avengers and their allies have continued to protect the world from threats too large for any one hero to handle, a new danger has emerged from the cosmic shadows: Thanos. A despot of intergalactic infamy, his goal is to collect all six Infinity Stones, artifacts of unimaginable power, and use them to inflict his twisted will on all of reality. Everything the Avengers have fought for has led up to this moment - the fate of Earth and existence itself has never been more uncertain.",
      "popularity": 155.8577,
      "poster_path": "/7WsyChQLEftFiDOVTGkv3hFpyyt.jpg",
      "release_date": "2018-04-25",
      "title": "Avengers: Infinity War",
      "video": false,
      "vote_average": 8.236,
      "vote_count": 30599
    },
    {
      "adult": false,
      "backdrop_path": "/dTGECn8He16tZeBHQTLf6rVydE8.jpg",
      "genre_ids": [80, 53, 18],
      "id": 302946,
      "original_language": "en",
      "original_title": "The Accountant",
      "overview": "As a math savant uncooks the books for a new client, the Treasury Department closes in on his activities and the body count starts to rise.",
      "popularity": 166.1359,
      "poster_path": "/fceheXB5fC4WrLVuWJ6OZv9FXYr.jpg",
      "release_date": "2016-10-13",
      "title": "The Accountant",
      "video": false,
      "vote_average": 7.116,
      "vote_count": 6660
    },
    {
      "adult": false,
      "backdrop_path": "/d53MM15mO9EEiHzNlfvJK0otaaM.jpg",
      "genre_ids": [10751, 14],
      "id": 1241894,
      "original_language": "de",
      "original_title": "Woodwalkers",
      "overview": "Humans who can shapeshift into animals struggle to integrate with others without giving away their special abilities. As a group, they strive to inform and institute change in the world perspective of deforestation and the importance of natural habitats. However, when that can’t happen, they are forced to take matters into their own hands.",
      "popularity": 179.8867,
      "poster_path": "/bC1r04ohuxv5feaGDzQ0lXz7Bbl.jpg",
      "release_date": "2024-10-17",
      "title": "Woodwalkers",
      "video": false,
      "vote_average": 6.25,
      "vote_count": 24
    },
    {
      "adult": false,
      "backdrop_path": "/8SaEH4kYCy7JlviyhKtSVsMkt4r.jpg",
      "genre_ids": [28, 53],
      "id": 1315988,
      "original_language": "es",
      "original_title": "Mikaela",
      "overview": "During the eve of the 6th of January, a record-breaking snowstorm sweeps across Spain. In the midst of its chaos, a group of robbers seizes the opportunity to hijack an armoured van. A few meters away is Leo, a finished policeman who has nothing to lose. With the unexpected aid of a young woman, he will try to stop the band from running away with their loot.",
      "popularity": 431.9591,
      "poster_path": "/xG8olkWOmoW78GbozKbS2UxYGEo.jpg",
      "release_date": "2025-01-31",
      "title": "Mikaela",
      "video": false,
      "vote_average": 5.78,
      "vote_count": 25
    },
    {
      "adult": false,
      "backdrop_path": "/uU1Mt4JWhDvl4vKb3AfxNsorkoM.jpg",
      "genre_ids": [10751, 14, 10749],
      "id": 321612,
      "original_language": "en",
      "original_title": "Beauty and the Beast",
      "overview": "A live-action adaptation of Disney's version of the classic tale of a cursed prince and a beautiful young woman who helps him break the spell.",
      "popularity": 130.3583,
      "poster_path": "/hKegSKIDep2ewJWPUQD7u0KqFIp.jpg",
      "release_date": "2017-03-16",
      "title": "Beauty and the Beast",
      "video": false,
      "vote_average": 6.972,
      "vote_count": 15651
    },
    {
      "adult": false,
      "backdrop_path": "/tPpYGm2mVecue7Bk3gNVoSPA5qn.jpg",
      "genre_ids": [28, 12, 878, 18],
      "id": 315635,
      "original_language": "en",
      "original_title": "Spider-Man: Homecoming",
      "overview": "Following the events of Captain America: Civil War, Peter Parker, with the help of his mentor Tony Stark, tries to balance his life as an ordinary high school student in Queens, New York City, with fighting crime as his superhero alter ego Spider-Man as a new threat, the Vulture, emerges.",
      "popularity": 130.6558,
      "poster_path": "/c24sv2weTHPsmDa7jEMN0m2P3RT.jpg",
      "release_date": "2017-07-05",
      "title": "Spider-Man: Homecoming",
      "video": false,
      "vote_average": 7.331,
      "vote_count": 22238
    },
    {
      "adult": false,
      "backdrop_path": "/rAgsOIhqRS6tUthmHoqnqh9PIAE.jpg",
      "genre_ids": [28, 35, 12],
      "id": 436969,
      "original_language": "en",
      "original_title": "The Suicide Squad",
      "overview": "Supervillains Harley Quinn, Bloodsport, Peacemaker and a collection of nutty cons at Belle Reve prison join the super-secret, super-shady Task Force X as they are dropped off at the remote, enemy-infused island of Corto Maltese.",
      "popularity": 127.7109,
      "poster_path": "/q61qEyssk2ku3okWICKArlAdhBn.jpg",
      "release_date": "2021-07-28",
      "title": "The Suicide Squad",
      "video": false,
      "vote_average": 7.486,
      "vote_count": 8925
    }
  ],
  "total_pages": 50813,
  "total_results": 1016252
}


127.0.0.1:8000/api/movie/top_rated

{
  "page": 1,
  "results": [
    {
      "adult": false,
      "backdrop_path": "/zfbjgQE1uSd9wiPTX4VzsLi0rGG.jpg",
      "genre_ids": [18, 80],
      "id": 278,
      "original_language": "en",
      "original_title": "The Shawshank Redemption",
      "overview": "Imprisoned in the 1940s for the double murder of his wife and her lover, upstanding banker Andy Dufresne begins a new life at the Shawshank prison, where he puts his accounting skills to work for an amoral warden. During his long stretch in prison, Dufresne comes to be admired by the other inmates -- including an older prisoner named Red -- for his integrity and unquenchable sense of hope.",
      "popularity": 32.1779,
      "poster_path": "/9cqNxx0GxF0bflZmeSMuL5tnGzr.jpg",
      "release_date": "1994-09-23",
      "title": "The Shawshank Redemption",
      "video": false,
      "vote_average": 8.711,
      "vote_count": 28411
    },
    {
      "adult": false,
      "backdrop_path": "/tmU7GeKVybMWFButWEGl2M4GeiP.jpg",
      "genre_ids": [18, 80],
      "id": 238,
      "original_language": "en",
      "original_title": "The Godfather",
      "overview": "Spanning the years 1945 to 1955, a chronicle of the fictional Italian-American Corleone crime family. When organized crime family patriarch, Vito Corleone barely survives an attempt on his life, his youngest son, Michael steps in to take care of the would-be killers, launching a campaign of bloody revenge.",
      "popularity": 51.941,
      "poster_path": "/3bhkrj58Vtu7enYsRolD1fZdja1.jpg",
      "release_date": "1972-03-14",
      "title": "The Godfather",
      "video": false,
      "vote_average": 8.686,
      "vote_count": 21506
    },
    {
      "adult": false,
      "backdrop_path": "/kGzFbGhp99zva6oZODW5atUtnqi.jpg",
      "genre_ids": [18, 80],
      "id": 240,
      "original_language": "en",
      "original_title": "The Godfather Part II",
      "overview": "In the continuing saga of the Corleone crime family, a young Vito Corleone grows up in Sicily and in 1910s New York. In the 1950s, Michael Corleone attempts to expand the family business into Las Vegas, Hollywood and Cuba.",
      "popularity": 15.4716,
      "poster_path": "/hek3koDUyRQk7FIhPXsa6mT2Zc3.jpg",
      "release_date": "1974-12-20",
      "title": "The Godfather Part II",
      "video": false,
      "vote_average": 8.57,
      "vote_count": 12992
    },
    {
      "adult": false,
      "backdrop_path": "/zb6fM1CX41D9rF9hdgclu0peUmy.jpg",
      "genre_ids": [18, 36, 10752],
      "id": 424,
      "original_language": "en",
      "original_title": "Schindler's List",
      "overview": "The true story of how businessman Oskar Schindler saved over a thousand Jewish lives from the Nazis while they worked as slaves in his factory during World War II.",
      "popularity": 19.3612,
      "poster_path": "/sF1U4EUQS8YHUYjNl3pMGNIQyr0.jpg",
      "release_date": "1993-12-15",
      "title": "Schindler's List",
      "video": false,
      "vote_average": 8.564,
      "vote_count": 16466
    },
    {
      "adult": false,
      "backdrop_path": "/bxgTSUenZDHNFerQ1whRKplrMKF.jpg",
      "genre_ids": [18],
      "id": 389,
      "original_language": "en",
      "original_title": "12 Angry Men",
      "overview": "The defense and the prosecution have rested and the jury is filing into the jury room to decide if a young Spanish-American is guilty or innocent of murdering his father. What begins as an open and shut case soon becomes a mini-drama of each of the jurors' prejudices and preconceptions about the trial, the accused, and each other.",
      "popularity": 20.9212,
      "poster_path": "/ow3wq89wM8qd5X7hWKxiRfsFf9C.jpg",
      "release_date": "1957-04-10",
      "title": "12 Angry Men",
      "video": false,
      "vote_average": 8.548,
      "vote_count": 9159
    },
    {
      "adult": false,
      "backdrop_path": "/m4TUa2ciEWSlk37rOsjiSIvZDXE.jpg",
      "genre_ids": [16, 10751, 14],
      "id": 129,
      "original_language": "ja",
      "original_title": "千と千尋の神隠し",
      "overview": "A young girl, Chihiro, becomes trapped in a strange new world of spirits. When her parents undergo a mysterious transformation, she must call upon the courage she never knew she had to free her family.",
      "popularity": 19.4658,
      "poster_path": "/39wmItIWsg5sZMyRUHLkWBcuVCM.jpg",
      "release_date": "2001-07-20",
      "title": "Spirited Away",
      "video": false,
      "vote_average": 8.537,
      "vote_count": 17190
    },
    {
      "adult": false,
      "backdrop_path": "/enNubozHn9pXi0ycTVYUWfpHZm.jpg",
      "genre_ids": [18, 28, 80, 53],
      "id": 155,
      "original_language": "en",
      "original_title": "The Dark Knight",
      "overview": "Batman raises the stakes in his war on crime. With the help of Lt. Jim Gordon and District Attorney Harvey Dent, Batman sets out to dismantle the remaining criminal organizations that plague the streets. The partnership proves to be effective, but they soon find themselves prey to a reign of chaos unleashed by a rising criminal mastermind known to the terrified citizens of Gotham as the Joker.",
      "popularity": 26.643,
      "poster_path": "/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
      "release_date": "2008-07-16",
      "title": "The Dark Knight",
      "video": false,
      "vote_average": 8.52,
      "vote_count": 33929
    },
    {
      "adult": false,
      "backdrop_path": "/90ez6ArvpO8bvpyIngBuwXOqJm5.jpg",
      "genre_ids": [35, 18, 10749],
      "id": 19404,
      "original_language": "hi",
      "original_title": "दिलवाले दुल्हनिया ले जायेंगे",
      "overview": "Raj is a rich, carefree, happy-go-lucky second generation NRI. Simran is the daughter of Chaudhary Baldev Singh, who in spite of being an NRI is very strict about adherence to Indian values. Simran has left for India to be married to her childhood fiancé. Raj leaves for India with a mission at his hands, to claim his lady love under the noses of her whole family. Thus begins a saga.",
      "popularity": 8.3735,
      "poster_path": "/rfcy6Gd3PbFIqwZX5U8xnbv7jOc.jpg",
      "release_date": "1995-10-20",
      "title": "Dilwale Dulhania Le Jayenge",
      "video": false,
      "vote_average": 8.517,
      "vote_count": 4488
    },
    {
      "adult": false,
      "backdrop_path": "/amZavErrjrdgDwhsIdpWxHNenIx.jpg",
      "genre_ids": [14, 18, 80],
      "id": 497,
      "original_language": "en",
      "original_title": "The Green Mile",
      "overview": "A supernatural tale set on death row in a Southern prison, where gentle giant John Coffey possesses the mysterious power to heal people's ailments. When the cell block's head guard, Paul Edgecomb, recognizes Coffey's miraculous gift, he tries desperately to help stave off the condemned man's execution.",
      "popularity": 17.1908,
      "poster_path": "/8VG8fDNiy50H4FedGwdSVUPoaJe.jpg",
      "release_date": "1999-12-10",
      "title": "The Green Mile",
      "video": false,
      "vote_average": 8.505,
      "vote_count": 18127
    },
    {
      "adult": false,
      "backdrop_path": "/hiKmpZMGZsrkA3cdce8a7Dpos1j.jpg",
      "genre_ids": [35, 53, 18],
      "id": 496243,
      "original_language": "ko",
      "original_title": "기생충",
      "overview": "All unemployed, Ki-taek's family takes peculiar interest in the wealthy and glamorous Parks for their livelihood until they get entangled in an unexpected incident.",
      "popularity": 122.6036,
      "poster_path": "/7IiTTgloJzvGI1TAYymCfbfl3vT.jpg",
      "release_date": "2019-05-30",
      "title": "Parasite",
      "video": false,
      "vote_average": 8.499,
      "vote_count": 19103
    },
    {
      "adult": false,
      "backdrop_path": "/suaEOtk1N1sgg2MTM7oZd2cfVp3.jpg",
      "genre_ids": [53, 80],
      "id": 680,
      "original_language": "en",
      "original_title": "Pulp Fiction",
      "overview": "A burger-loving hit man, his philosophical partner, a drug-addled gangster's moll and a washed-up boxer converge in this sprawling, comedic crime caper. Their adventures unfurl in three stories that ingeniously trip back and forth in time.",
      "popularity": 102.7421,
      "poster_path": "/vQWk5YBFWF4bZaofAbv0tShwBvQ.jpg",
      "release_date": "1994-09-10",
      "title": "Pulp Fiction",
      "video": false,
      "vote_average": 8.489,
      "vote_count": 28728
    },
    {
      "adult": false,
      "backdrop_path": "/2u7zbn8EudG6kLlBzUYqP8RyFU4.jpg",
      "genre_ids": [12, 14, 28],
      "id": 122,
      "original_language": "en",
      "original_title": "The Lord of the Rings: The Return of the King",
      "overview": "As armies mass for a final battle that will decide the fate of the world--and powerful, ancient forces of Light and Dark compete to determine the outcome--one member of the Fellowship of the Ring is revealed as the noble heir to the throne of the Kings of Men. Yet, the sole hope for triumph over evil lies with a brave hobbit, Frodo, who, accompanied by his loyal friend Sam and the hideous, wretched Gollum, ventures deep into the very dark heart of Mordor on his seemingly impossible quest to destroy the Ring of Power.​",
      "popularity": 19.8345,
      "poster_path": "/rCzpDGLbOoPwLjy3OAm5NUPOTrC.jpg",
      "release_date": "2003-12-17",
      "title": "The Lord of the Rings: The Return of the King",
      "video": false,
      "vote_average": 8.485,
      "vote_count": 25131
    },
    {
      "adult": false,
      "backdrop_path": "/8x9iKH8kWA0zdkgNdpAew7OstYe.jpg",
      "genre_ids": [16, 10749, 18],
      "id": 372058,
      "original_language": "ja",
      "original_title": "君の名は。",
      "overview": "High schoolers Mitsuha and Taki are complete strangers living separate lives. But one night, they suddenly switch places. Mitsuha wakes up in Taki’s body, and he in hers. This bizarre occurrence continues to happen randomly, and the two must adjust their lives around each other.",
      "popularity": 37.8462,
      "poster_path": "/8GJsy7w7frGquw1cy9jasOGNNI1.jpg",
      "release_date": "2016-08-26",
      "title": "Your Name.",
      "video": false,
      "vote_average": 8.5,
      "vote_count": 11800
    },
    {
      "adult": false,
      "backdrop_path": "/tlEFuIlaxRPXIYVHXbOSAMCfWqk.jpg",
      "genre_ids": [35, 18, 10749],
      "id": 13,
      "original_language": "en",
      "original_title": "Forrest Gump",
      "overview": "A man with a low IQ has accomplished great things in his life and been present during significant historic events—in each case, far exceeding what anyone imagined he could do. But despite all he has achieved, his one true love eludes him.",
      "popularity": 19.129,
      "poster_path": "/arw2vcBveWOVZr6pxd9XTd1TdQa.jpg",
      "release_date": "1994-06-23",
      "title": "Forrest Gump",
      "video": false,
      "vote_average": 8.468,
      "vote_count": 28270
    },
    {
      "adult": false,
      "backdrop_path": "/x4biAVdPVCghBlsVIzB6NmbghIz.jpg",
      "genre_ids": [37],
      "id": 429,
      "original_language": "it",
      "original_title": "Il buono, il brutto, il cattivo",
      "overview": "While the Civil War rages on between the Union and the Confederacy, three men – a quiet loner, a ruthless hitman, and a Mexican bandit – comb the American Southwest in search of a strongbox containing $200,000 in stolen gold.",
      "popularity": 91.8321,
      "poster_path": "/bX2xnavhMYjWDoZp1VM6VnU1xwe.jpg",
      "release_date": "1966-12-22",
      "title": "The Good, the Bad and the Ugly",
      "video": false,
      "vote_average": 8.461,
      "vote_count": 9010
    },
    {
      "adult": false,
      "backdrop_path": "/l33oR0mnvf20avWyIMxW02EtQxn.jpg",
      "genre_ids": [12, 18, 878],
      "id": 157336,
      "original_language": "en",
      "original_title": "Interstellar",
      "overview": "The adventures of a group of explorers who make use of a newly discovered wormhole to surpass the limitations on human space travel and conquer the vast distances involved in an interstellar voyage.",
      "popularity": 37.6389,
      "poster_path": "/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg",
      "release_date": "2014-11-05",
      "title": "Interstellar",
      "video": false,
      "vote_average": 8.455,
      "vote_count": 37238
    },
    {
      "adult": false,
      "backdrop_path": "/7TF4p86ZafnxFuNqWdhpHXFO244.jpg",
      "genre_ids": [18, 80],
      "id": 769,
      "original_language": "en",
      "original_title": "GoodFellas",
      "overview": "The true story of Henry Hill, a half-Irish, half-Sicilian Brooklyn kid who is adopted by neighbourhood gangsters at an early age and climbs the ranks of a Mafia family under the guidance of Jimmy Conway.",
      "popularity": 13.4244,
      "poster_path": "/aKuFiU82s5ISJpGZp7YkIr3kCUd.jpg",
      "release_date": "1990-09-12",
      "title": "GoodFellas",
      "video": false,
      "vote_average": 8.455,
      "vote_count": 13409
    },
    {
      "adult": false,
      "backdrop_path": "/sJNNMCc6B7KZIY3LH3JMYJJNH5j.jpg",
      "genre_ids": [28, 18],
      "id": 346,
      "original_language": "ja",
      "original_title": "七人の侍",
      "overview": "A samurai answers a village's request for protection after he falls on hard times. The town needs protection from bandits, so the samurai gathers six others to help him teach the people how to defend themselves, and the villagers provide the soldiers with food.",
      "popularity": 8.0551,
      "poster_path": "/8OKmBV5BUFzmozIC3pPWKHy17kx.jpg",
      "release_date": "1954-04-26",
      "title": "Seven Samurai",
      "video": false,
      "vote_average": 8.5,
      "vote_count": 3901
    },
    {
      "adult": false,
      "backdrop_path": "/tDFvXn4tane9lUvFAFAUkMylwSr.jpg",
      "genre_ids": [16, 18, 10752],
      "id": 12477,
      "original_language": "ja",
      "original_title": "火垂るの墓",
      "overview": "In the final months of World War II, 14-year-old Seita and his sister Setsuko are orphaned when their mother is killed during an air raid in Kobe, Japan. After a falling out with their aunt, they move into an abandoned bomb shelter. With no surviving relatives and their emergency rations depleted, Seita and Setsuko struggle to survive.",
      "popularity": 0.0101,
      "poster_path": "/k9tv1rXZbOhH7eiCk378x61kNQ1.jpg",
      "release_date": "1988-04-16",
      "title": "Grave of the Fireflies",
      "video": false,
      "vote_average": 8.448,
      "vote_count": 5912
    },
    {
      "adult": false,
      "backdrop_path": "/6aNKD81RHR1DqUUa8kOZ1TBY1Lp.jpg",
      "genre_ids": [35, 18],
      "id": 637,
      "original_language": "it",
      "original_title": "La vita è bella",
      "overview": "A touching story of an Italian book seller of Jewish ancestry who lives in his own little fairy tale. His creative and happy life would come to an abrupt halt when his entire family is deported to a concentration camp during World War II. While locked up he tries to convince his son that the whole thing is just a game.",
      "popularity": 10.318,
      "poster_path": "/74hLDKjD5aGYOotO6esUVaeISa2.jpg",
      "release_date": "1997-12-20",
      "title": "Life Is Beautiful",
      "video": false,
      "vote_average": 8.4,
      "vote_count": 13392
    }
  ],
  "total_pages": 509,
  "total_results": 10178
}
