# list, tuple, set, map

# SET
bhakt = {"Ramesh", "Suresh", "Mahesh", "Ramesh", "Hitesh", "Mahesh"}

print(bhakt)

winners = {"Mahesh", "Mahesh", "Mahesh"}

all_movies = {"Pushpa", "Bahubali", "The mask", "Tom n Jerry", "Superman", "Bahubali"}
watched_movies = {"Tom n Jerry", "The mask", "Tom n Jerry"}

print("All: ", all_movies)
print("Watched: ", watched_movies)
print("Pending: ",all_movies.difference(watched_movies))