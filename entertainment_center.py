# Import media for the movie class
import media
import fresh_tomatoes

# Create movie objects
movie_spirited_away = media.Movie(
    "Spirited Away",
    "During her family's move to the suburbs, a sullen 10-year-old girl \
    wanders into a world ruled by gods, witches, and spirits, and where\
    humans are changed into beasts.",
    "http://tinyurl.com/opl62zh",
    "https://www.youtube.com/watch?v=ByXuk9QqQkk")

movie_up = media.Movie(
    "Up",
    "Seventy-eight year old Carl Fredricksen travels to Paradise Falls in his\
     home equipped with balloons, inadvertently taking a young stowaway.",
    "http://tinyurl.com/pappn4y",
    "https://www.youtube.com/watch?v=X9g2ZEvVUVc")

movie_totoro = media.Movie(
    "My Neighbor Totoro",
    "When two girls move to the country to be near their ailing mother, they\
    have adventures with the wonderous forest spirits who live nearby.",
    "http://tinyurl.com/nv5tesf",
    "https://www.youtube.com/watch?v=92a7Hj0ijLs")

movie_guardians = media.Movie(
    "Guardians of the Galaxy",
    "A group of intergalactic criminals are forced to work together to stop a\
     fanatical warrior from taking control of the universe.",
    "http://tinyurl.com/nbpoevh",
    "https://www.youtube.com/watch?v=d96cjJhvlMA")

movie_300 = media.Movie(
    "300",
    "King Leonidas and a force of 300 men fight the Persians at Thermopylae i\
    n 480 B.C.",
    "http://tinyurl.com/pqkpjff",
    "https://www.youtube.com/watch?v=ZJ6yq-oVKPc")

# Add the movie objectes into a list
movies = [movie_spirited_away, movie_up, movie_totoro, movie_guardians,
          movie_300]
# Pass the list into fresh_tomatoes.open_movies_page
fresh_tomatoes.open_movies_page(movies)
