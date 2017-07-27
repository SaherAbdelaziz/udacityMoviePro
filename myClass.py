import webbrowser

class Movie():
    def __init__ (self , movieTitle , movieStory , posterImage , trailarYoutube):
        self.title=movieTitle
        self.storyline=movieStory
        self.poster_image_url=posterImage
        self.trailer_youtube_url=trailarYoutube
    
    def showTrailar(self):
        webbrowser.open(self.trailarYoutube)

