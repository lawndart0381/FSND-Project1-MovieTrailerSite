import fresh_tomatoes
import media

# Movie data for Fresh Tomatoes Movie Trailers
full_metal_jacket = media.Movie("Full Metal Jacket",
                        "https://dl.dropboxusercontent.com/u/29108866/full_metal_jacket.jpg",  # NOQA
                        "https://dl.dropboxusercontent.com/u/29108866/ratings/rating_r.PNG",  # NOQA
                        "https://www.youtube.com/watch?v=x9f6JaaX7Wg")

platoon = media.Movie("Platoon",
                     "https://dl.dropboxusercontent.com/u/29108866/platoon.jpg",
                     "https://dl.dropboxusercontent.com/u/29108866/ratings/rating_r.PNG",  #NOQA
                     "https://www.youtube.com/watch?v=KztP7SKe0uk")

heartbreak_ridge = media.Movie("Heartbreak Ridge",
                              "https://dl.dropboxusercontent.com/u/29108866/heartbreak_ridge_ver2.jpg",  # NOQA
                              "https://dl.dropboxusercontent.com/u/29108866/ratings/rating_r.PNG",  # NOQA
                              "https://www.youtube.com/watch?v=ZOo4ir1MtoI")

tropic_thunder = media.Movie("Tropic Thunder",
                             "https://dl.dropboxusercontent.com/u/29108866/tropic_thunder_ver4.jpg",  # NOQA
                             "https://dl.dropboxusercontent.com/u/29108866/ratings/rating_r.PNG",  # NOQA
                             "https://www.youtube.com/watch?v=utPTtw0sNbA")

top_gun = media.Movie("Top Gun",
                      "https://dl.dropboxusercontent.com/u/29108866/original.jpg",  # NOQA
                      "https://dl.dropboxusercontent.com/u/29108866/ratings/rating_pg.PNG",  # NOQA
                      "https://www.youtube.com/watch?v=qAfbp3YX9F0")

days_of_thunder = media.Movie("Days of Thunder",
                              "https://dl.dropboxusercontent.com/u/29108866/days_of_thunder.jpg",  # NOQA
                              "https://dl.dropboxusercontent.com/u/29108866/ratings/rating_pg13.PNG",  # NOQA
                              "https://www.youtube.com/watch?v=hrjkdQWF4gk")

meet_the_parents = media.Movie("Meet the Parents",
                               "https://dl.dropboxusercontent.com/u/29108866/meet-the-parents.jpg",  # NOQA
                               "https://dl.dropboxusercontent.com/u/29108866/ratings/rating_pg13.PNG",  # NOQA  
                               "https://www.youtube.com/watch?v=CXqxP-bUC7I")

central_intelligence = media.Movie("Central Intelligence",
                                   "https://dl.dropboxusercontent.com/u/29108866/central_intelligence.jpg",  # NOQA
                                   "https://dl.dropboxusercontent.com/u/29108866/ratings/rating_pg13.PNG",  # NOQA
                                   "https://www.youtube.com/watch?v=MxEw3elSJ8M")
ice_age = media.Movie("Ice Age",
                      "https://dl.dropboxusercontent.com/u/29108866/Ice_Age_Original_Poster.jpg",  #NOQA
                      "https://dl.dropboxusercontent.com/u/29108866/ratings/rating_pg.PNG",  # NOQA
                      "https://www.youtube.com/watch?v=5utbt2Ycenw")

dispicable_me = media.Movie("Dispicable Me",
                            "https://dl.dropboxusercontent.com/u/29108866/dispicable_me.jpg",  # NOQA
                            "https://dl.dropboxusercontent.com/u/29108866/ratings/rating_pg.PNG",  # NOQA
                            "https://www.youtube.com/watch?v=TZkAcKCFIVo")
dumb_and_dumber = media.Movie("Dumb and Dumber",
                              "https://dl.dropboxusercontent.com/u/29108866/dumb_and_dumber.jpg",  # NOQA
                              "https://dl.dropboxusercontent.com/u/29108866/ratings/rating_pg13.PNG",  # NOQA
                              "https://www.youtube.com/watch?v=gqHe6UcaCXI")
liar_liar = media.Movie("Liar Liar",
                        "https://dl.dropboxusercontent.com/u/29108866/liar_liar.jpg",  # NOQA
                        "https://dl.dropboxusercontent.com/u/29108866/ratings/rating_pg13.PNG",  # NOQA
                        "https://www.youtube.com/watch?v=DGpS0XgKuLk")

# List of movies for create_movie_tiles_content function in fresh_tomatoes   
movies = [full_metal_jacket, platoon, heartbreak_ridge, tropic_thunder, top_gun,
          days_of_thunder, meet_the_parents, central_intelligence, ice_age,
          dispicable_me, dumb_and_dumber, liar_liar]
            

# Call to open_movies_page function in fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)

                     
