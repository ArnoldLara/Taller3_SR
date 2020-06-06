from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rating.models import movies,ratings


#from .models import reviews

from django.contrib.auth.models import User

# Create your views here.

def RatingSearch(request):
    template = loader.get_template('rating/rating.html')
    if not request.user.is_anonymous:
        Usuario=request.user.username
        print("Usuario: " + Usuario)
        #Se hace el query y tenemos como resultado un listado de objetos
        #por cada registro encontrado
        rating = ratings.objects.filter(user_id=Usuario)[:10]
        count = ratings.objects.filter(user_id=Usuario).count()
        movieid_list=[]
        rating_list=[]
        moviename_list=[]
        info = []
        keys = ['movie','rating']
        for x in rating:
            movieid_list.append(int(x.movie_id))
            rating_list.append(int(x.rating))
            film = movies.objects.get(movie_id = movieid_list[-1])
            moviename_list.append(film)
            new_dict = dict(zip(keys,[moviename_list[-1].title,rating_list[-1]]))
            info.append(new_dict)
        # print("movieID: ", movieid_list)
        # print("rating_list: ", rating_list)
        # print("moviename_list: ", moviename_list)
        #print("Info: ", info)


        context = {
            'count': count,
            'info':info,
        }
        #print("Contexto: ",context)

    return HttpResponse(template.render(context,request))
