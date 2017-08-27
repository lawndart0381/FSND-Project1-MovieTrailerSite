import webbrowser
       
class Movie():
    
    """A movie that will appear on Fresh Tomoatoes Movie Trailers HTML page.
    Movies have the following properties:

    Attributes:
        title: The movie title
        poster_image_url: The poster image url for the movie
        movie_rating_url: The MPAA rating of the movie for the USA
        trailer_youtube_url: The youtube trailer url for the movie
    """
             
    def __init__(self, movie_title, poster_image, movie_rating, trailer_youtube):
        """Return Movie objects whose title is *movie_title*, poster image url
        is *poster_image*, movie rating url is *movie_rating*, and trailer
        youtube url is *trailer_youtube*."""
        self.title = movie_title
        self.poster_image_url = poster_image
        self.movie_rating_url = movie_rating
        self.trailer_youtube_url = trailer_youtube
               
