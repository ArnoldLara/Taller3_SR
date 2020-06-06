from recommendation.models import svd_db
import csv

with open('../datasets/SVD_global_rec.csv', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    svd_rec = list(reader)

y=0
for x in svd_rec:
    rating=svd_db(user_id=x[0],movie_id=x[1],rating=float(x[2]))
    rating.save()
    print(y,"\n")
    y=y+1
