import numpy as np

movies = [
    {"id": 1, "name": "superman", "imdb": 9.2},
    {"id": 2, "name": "bahubali", "imdb": 8.6},
    {"id": 3, "name": "bagheera", "imdb": 7.3},
    {"id": 4, "name": "bhedia", "imdb": 4.2}
]

movies_data = np.array(movies)
print("Movies:",movies_data)


# 2D array
tda = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(tda)