"""This class displays attributes defined by its constructor, and
its method uses the webbrowser module to open YouTube links to
display video, along with the attributes, on an HTML page.

Author: Jonathan Alvarado
Filename: media.py
Last Date Modified: 2/10/16
"""

import webbrowser
# import of this module is essential for show_trailer


class Movie():
    """This method creates the class variables title, storyline,
    poster_image_url and trailer_youtube_url. These class variables
    are set equal to the constructor __init__'s arguments. These
    arguments are explicitly defined by any module that calls this
    class."""
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        # instance names can be same as the constructor's arguments

    """This method is used to open the webpage for each class instance
    containing the trailer_youtube argument"""
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
