from django.contrib.auth.models import User


for x in range(1,101):
    user = User.objects.create_user(x, 'user@andes.com', 'pass')
    u = "Name"+str(x)
    l = "Lastname"+str(x)
    user.first_name = u
    user.last_name = l
    user.save()
    print(x,u,l)
