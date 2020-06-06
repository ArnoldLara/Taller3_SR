from rating.models import ratings
import csv


with open('../datasets/ratings100.csv', newline='') as f:
    reader = csv.reader(f, delimiter=';')
    rat = list(reader)

y=0
for x in rat:
    rating=ratings(user_id=x[0],movie_id=x[1],rating=float(x[2]))
    rating.save()
    print(y,"\n")
    y=y+1
