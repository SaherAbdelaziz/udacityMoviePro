import Movies
import myClass

the_prestige=myClass.Movie("The Prestige" , "story" , "https://upload.wikimedia.org/wikipedia/en/d/d2/Prestige_poster.jpg" , "https://www.youtube.com/watch?v=a1AqrIkD7vU")
Matrix=myClass.Movie("The Matrix" , "story" , "https://s-media-cache-ak0.pinimg.com/736x/a8/3b/96/a83b969804d214ddb0f1f38924edce65--the-matrix-film-music-books.jpg" , "https://www.youtube.com/watch?v=m8e-FF8MsqU")
FightClub=myClass.Movie("Fight Club" , "story" , "http://www.flore-maquin.com/wp-content/uploads/Fight_club_RVB_72.jpg" , "https://www.youtube.com/watch?v=J8FRBYOFu2w")
Inception=myClass.Movie("Inception" , "story" , "http://p7.storage.canalblog.com/76/61/660219/52517006.jpg" , "https://www.youtube.com/watch?v=8hP9D6kZseM")
V_for_vendetta=myClass.Movie("v for vendetta" , "story" , "https://media.culturalist.com/media/8456f0ed9c2cd7a863aae0e4749a66a9.jpg" , "https://www.youtube.com/watch?v=k_13fFIrhPk")
the_dark_knight=myClass.Movie("The Dark Knight" , "story" , "https://img.csfd.cz/files/images/user/profile/158/838/158838814_278231.jpg" , "https://www.youtube.com/watch?v=yQ5U8suTUw0")

Moviess=[the_prestige , Matrix , FightClub , Inception , V_for_vendetta , the_dark_knight]

Movies.open_movies_page(Moviess)
