class Video():
    """
    Class: Video
    Parent: None
    Description: Stores all info about a video 
    Attributes: title - name of video
                youtube_url - url to video
    """
    def __init__(self, title, video):
        self.title = title
        self.youtube_url = video


class Movie(Video):
    """
    Class: Move
    Parent: Video
    Description: Stores all info about a movie
    Attributes: poster_image_url - url to movie poster image 
    """
    def __init__(self, title, art, trailer):
        Video.__init__(self, title, trailer)
        self.poster_image_url = art

