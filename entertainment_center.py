# Importing needed files
import media
import fresh_tomatoes


# Creating multiple instances of Class Movie
the_pursuit_of_happyness = media.Movie(
    "The Pursuit of Happyness",
    "http://bit.ly/2jBwuUk",
    "https://www.youtube.com/watch?v=DMOBlEcRuw8"
    )

bilal = media.Movie(
    "Bilal",
    "http://bit.ly/2ftUeFD",
    "https://www.youtube.com/watch?v=Wp_7Gdf2blE"
    )

mission_impossible = media.Movie(
    "Mission: Impossible - Rogue Nation",
    "http://bit.ly/2jDQK82",
    "https://www.youtube.com/watch?v=EIsauUFIguE"
    )

# Making a list to pass to the open_movies_page function
movies = [the_pursuit_of_happyness, bilal, mission_impossible]

# Calling open_movies_page function for making the HTML page
fresh_tomatoes.open_movies_page(movies)
