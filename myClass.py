import webbrowser

class Movie():
    def __init__ (self , movieTitle , movieStory , posterImage , trailarYoutube):
        self.movieTitle=movieTitle
        self.movieStory=movieStory
        self.posterImage=posterImage
        self.trailarYoutube=trailarYoutube
    
    def showTrailar(self):
        webbrowser.open(self.trailarYoutube)

