from py2neo import Graph
from py2neo import Node, Relationship
import csv

graph = Graph("bolt://localhost:7687", auth=("neo4j", "1qasde32!SR"))
#*************CREACION DE ACTORES***********************
# with open('actors.csv', newline='') as f:
#     reader = csv.reader(f, delimiter=';')
#     actors = list(reader)
# #print(actors[0][0])
# tx = graph.begin()
# for x in actors:
#     # Persons
#     actor = Node("Person", name=x[0])
#     tx.create(actor)
#     print(x[0])
# tx.commit()
#*******************************************************
#*************CREACION DE DIRECTORES***********************

# with open('directors.csv', newline='') as f:
#     reader = csv.reader(f, delimiter=';')
#     director = list(reader)
#
# tx = graph.begin()
# for x in director:
#     #Persons
#     dir = Node("Person", name=x[0])
#     tx.create(dir)
#     print(x[0])
# tx.commit()
#*******************************************************
#*************CREACION DE PELICULAS***********************

# with open('movies.csv', newline='') as f:
#     reader = csv.reader(f, delimiter=';')
#     movies = list(reader)
#
# tx = graph.begin()
# for x in movies:
#     #Persons
#     movie = Node("Movie",id=x[0], title=x[1], genre=x[2])
#     tx.create(movie)
#     print(x[0], x[1], x[2])
# tx.commit()
#*******************************************************

#*************CREACION DE RELACION ACTORES***************
# with open('r_actors.csv', newline='') as f:
#     reader = csv.reader(f, delimiter=';')
#     r_actors = list(reader)
#
# tx = graph.begin()
# for x in r_actors:
#     try:
#         #Persons
#         movie = graph.nodes.match(id=x[0]).first()
#         actor = graph.nodes.match(name=x[1]).first()
#         relacion = Relationship(actor, "ACTOR", movie)
#         tx.create(relacion)
#         print(x[0], x[1])
#     except Exception as e:
#         print('Error ')
#
# tx.commit()
#*******************************************************

#*************CREACION DE RELACION DIRECTORES***************
with open('r_director.csv', newline='') as f:
    reader = csv.reader(f, delimiter=';')
    r_directors = list(reader)

tx = graph.begin()
for x in r_directors:
    try:
        #Persons
        movie = graph.nodes.match(id=x[0]).first()
        director = graph.nodes.match(name=x[1]).first()
        relacion = Relationship(director, "DIRECTOR", movie)
        tx.create(relacion)
        print(x[0], x[1])
    except Exception as e:
        print('Error ')

tx.commit()
#*******************************************************
