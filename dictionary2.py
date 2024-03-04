movies = [
    {'name': 'Matrix', 'Rating': '4', 'Release year': '2007'},
    {'name': 'Die hard', 'Rating': '5', 'Release year': '2020'},
    {'name': 'Marvel', 'Rating': '3', 'Release year': '2023'}
]
for movie in movies:
    print(movie['name'], movie['Rating'], movie['Release year'], sep = ',')