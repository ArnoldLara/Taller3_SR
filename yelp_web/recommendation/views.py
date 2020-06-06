from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import svd_db,neo4j_db
from rating.models import movies

from py2neo import Graph
from py2neo import Node, Relationship





#from .models import reviews

from django.contrib.auth.models import User

# Create your views here.
def svdRecommendation(request):
    template = loader.get_template('recommendation/rec_svd.html')
    if not request.user.is_anonymous:
        Usuario=request.user.username
        print("Usuario: " + Usuario)

        #Se hace el query y tenemos como resultado un listado de objetos
        #por cada registro encontrado
        rating = svd_db.objects.filter(user_id=Usuario).order_by('-rating')[:10]
        count = svd_db.objects.filter(user_id=Usuario).count()
        #print(rating.count())
        movieid_list=[]
        rating_list=[]
        moviename_list=[]
        info = []
        keys = ['movie','rating']
        for x in rating:
            movieid_list.append(int(x.movie_id))
            rating_list.append(float(x.rating))
            film = movies.objects.get(movie_id = movieid_list[-1])
            moviename_list.append(film)
            new_dict = dict(zip(keys,[moviename_list[-1].title,rating_list[-1]]))
            info.append(new_dict)
        # print("movieID: ", movieid_list)
        #print("rating_list: ", rating_list)
        # print("moviename_list: ", moviename_list)
        #print("Info: ", info)


        context = {
            'info':info,
            'count':count,
        }
        #print("Contexto: ",context)

    return HttpResponse(template.render(context,request))

def neo4jRecommendation(request):
    graph = Graph("bolt://localhost:7687", auth=("neo4j", "neo4j"))
    template = loader.get_template('recommendation/rec_neo4j.html')
    if not request.user.is_anonymous:
        Usuario=request.user.username

        #SACAR LISTADO PELICULAS
        rating = svd_db.objects.filter(user_id=Usuario).order_by('-rating')[:10]
        print(rating.count())
        movieid_list=[]
        moviename_list=[]
        #keys = ['movie','rating']
        for x in rating:
            movieid_list.append(int(x.movie_id))
            film = movies.objects.get(movie_id = movieid_list[-1])
            moviename_list.append(film.title)

        print("Lista peliculas: ", moviename_list)
        data=[]
        info=[]
        for movie in movieid_list:
            print(movie)
            ############neo4j###########################
            query = """
            MATCH (p1:Movie {id: '%s'})<-[:ACTOR|DIRECTOR|GENERO]->(info1)
            WITH p1, collect(id(info1)) AS p1Info
            MATCH (p2:Movie)<-[:ACTOR|DIRECTOR|GENERO]->(info2) WHERE p1 <> p2
            WITH p1, p1Info, p2, collect(id(info2)) AS p2Info
            RETURN p1.title AS from,
                p2.title AS to,
                gds.alpha.similarity.jaccard(p1Info, p2Info) AS similarity
            ORDER BY similarity DESC
            LIMIT 5;
            """ % movie


            info = graph.run(query).data()
            print(info)
            data.extend(info)
            ####################################################
        # using sorted and lambda to print list sorted
        # by similaridad
        print("The list printed sorting by similaridad: ")
        print()
        data=sorted(data, key = lambda i: i['similarity'],reverse=True)
        count = len(data)
        #print("Resultado:",data)
        context = {
            'data':data,
            'count':count,
        }
        #print("Contexto: ",context)

    return HttpResponse(template.render(context,request))
