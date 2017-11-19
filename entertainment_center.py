import media
import fresh_tomatoes

# make Toy Story movie class
toy_story_trailer = "https://www.youtube.com/watch?v=KYz2wyBy3kc"
toy_story_art = "https://lumiere-a.akamaihd.net/v1/images" \
                "/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450"
toy_story = media.Movie("Toy Story", toy_story_art, toy_story_trailer)

# make Avatar movie class
avatar_story_trailer = "https://www.youtube.com/watch?v=5PSNL1qE6VY"
avatar_story_art = "https://resizing.flixster.com/86CQQH9RKDumbcyHqzMQGixO_XI=" \
                   "/206x305/v1.bTsxMTE3Njc5MjtqOzE3NTQ0OzEyMDA7ODAwOzEyMDA"
avatar = media.Movie("avatar", avatar_story_art, avatar_story_trailer)

# make Avatar movie class
starship_troopers_story_trailer = "https://www.youtube.com/watch?v=Y07I_KER5fE"
starship_troopers_story_art = "https://upload.wikimedia.org/wikipedia/en/d/df/Starship_Troopers_-_movie_poster.jpg"
starship_troopers = media.Movie("Starship Troopers", starship_troopers_story_art, starship_troopers_story_trailer)
movies = [toy_story, avatar, starship_troopers]

fresh_tomatoes.open_movies_page(movies)
