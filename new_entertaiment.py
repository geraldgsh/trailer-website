"""Keeps movie detail and shows them on a website."""

import fresh_tomatoes
import new_media

toy_story = new_media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                            "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                            "Release Date: November 22, 1995", "IMDB Rating:8.3/10")
print (toy_story.storyline)

dunkirk = new_media.Movie("Dunkirk", "Allied troops surrounded on the beach of Dunkirk",
                     "https://upload.wikimedia.org/wikipedia/en/1/15/Dunkirk_Film_poster.jpg",
                     "https://www.youtube.com/watch?v=F-eMt3SrfFU",
                          "Release Date: 21 July 2017", "IMDB Rating: 8.5/10")
print(dunkirk.storyline)
print(dunkirk.release_date)

Spiderman_Homecoming = new_media.Movie("Spiderman Homecoming", "A boy bitten by a special spider",
                                   "https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg",
                                   "https://www.youtube.com/watch?v=39udgGPyYMg",
                                       "Release Date: 7 July 2017", "IMDB Rating: 8.0/10")
print(Spiderman_Homecoming.storyline)

Thor_Ragnarok = new_media.Movie("Thor: Ragnarok", "Imprisoned on the other side of the universe",
                            "https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg",
                            "https://www.youtube.com/watch?v=v7MGUNV8MxU",
                                "Release Date: November 3, 2017", "IMDB Rating: N/A")
print(Thor_Ragnarok.storyline)

Transformers_5 = new_media.Movie("Transformers 5", "Last Knight",
                             "https://upload.wikimedia.org/wikipedia/en/2/26/Transformers_The_Last_Knight_poster.jpg",
                             "https://www.youtube.com/watch?v=6Vtf0MszgP8",
                                 "Release Date: June 21, 2017", "IMDB Rating: 5.3/10")
print(Transformers_5.storyline)

Justice_League = new_media.Movie("Justice League","Unite the league",
                             "https://upload.wikimedia.org/wikipedia/en/3/31/Justice_League_film_poster.jpg",
                             "https://www.youtube.com/watch?v=3cxixDgHUYw",
                                 "Release Date: November 17, 2017", "IMDB Rating: N/A")
print(Justice_League.storyline)
print(new_media.Movie.VALID_RATINGS)
print(new_media.Movie.__doc__)

#Print output appears in module

#Store movie object in a list
movies = [toy_story,dunkirk,Spiderman_Homecoming,Thor_Ragnarok,Transformers_5,Justice_League]

#Open a page for movies above
fresh_tomatoes.open_movies_page(movies)
