from rating.models import movies
import csv


with open('../datasets/movies.csv', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    mov = list(reader)

y=0
for x in mov:
    # movie=movies(movie_id=x[0],title=x[1],genre=x[2])
    # movie.save()
    print(y,"\n")
    y=y+1
