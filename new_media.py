"""Defines the Movie class that contains the movie details."""
import webbrowser

class Movie():
    """ This class provides a way to store movie related information """

    VALID_RATINGS =["G", "PG", "PG-13", "R"]

    """ title: A string to keep the title of the movie.
        storyline: A string  to keep brief movie synopsis.
        poster_image_url: A string  to keep URL of movie poster.
        trailer_youtube_url: A string to keep URL of movie trailer.
        release_date: A string to keep movie release date.
        imdb_rating: A string to keep movie rating
    """

    # Pyton to tell programmers is reserved in Pyton. Create memory for data (__init__)
        
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_release_date, movie_imdb_rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = movie_release_date
        self.imdb_rating = movie_imdb_rating

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    
