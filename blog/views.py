from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    #nazwa naszego QuerySetu
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    #przekazujemy dane w słowniku, nadajemy nazwe klucza taka sama jaka 
    #wywolujemy w pliku html (przechodzimy tam po kluczu 'posts')
    return render(request, 'blog/post_list.html', {'posts': posts})
