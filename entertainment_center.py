"""This module contains the instances of the media.Movie module,
as well each instances' unique characteristics, to be displayed
on an HTML page once the fresh_tomatoes module is ran.

Author: Jonathan Alvarado
Filename: entertainment_center.py
Last Date Modified: 2/10/16
"""

import fresh_tomatoes
import media


# Issue 1: Had a indentation error because I...
# ...added a colon after the media.Movie parenthesis.
# Issue 2: When creating my own Class, I kept putting in 4 arguments...
# ...when calling the Media class, but it only takes in 3 arguments. I was...
# ...mistakenly coutning the 'self' inside the __init__ parenthesis as a
# ...function but it doesn't count
toy_story = media.Movie("Toy Story",
                        "A movie about a boy and toys.",
                        "https://tinyurl.com/toy-story-image",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
star_wars_vii = media.Movie("Star Wars VII: The Force Awakens",
                            "A movie about the jedi and a new order.",
                            "https://tinyurl.com/star-wars-image",
                            "https://www.youtube.com/watch?v=sGbxmsDFVnE")
tombstone = media.Movie("Tombstone",
                        "A movie about masrshalls and cowboys.",
                        "https://tinyurl.com/tombstone-image",
                        "https://www.youtube.com/watch?v=XTWYKf5hXIg")
big_fish = media.Movie('Big Fish',
                       'A movie about a imaginative father and his tales.',
                       'https://tinyurl.com/bigfish-image',
                       'https://www.youtube.com/watch?v=lfW8qaJL1Fs')
winter_soldier = media.Movie('Captain America: Winter Solider',
                             'A movie about Captain America and company.',
                             'https://tinyurl.com/soldier-image',
                             'https://www.youtube.com/watch?v=82RKQPgeYRs')
running_scared = media.Movie('Running Scared',
                             'A movie about a family in constant peril.',
                             'https://tinyurl.com/hp9aedt',
                             'https://www.youtube.com/watch?v=bBboyvN3s-o')

# Needed to create the array 'movies' because the open_movies_page()...
# ...Method only takes in arrays/lists as its arguments
movies = [toy_story, big_fish, winter_soldier, running_scared, tombstone,
          star_wars_vii]
fresh_tomatoes.open_movies_page(movies)
