from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
    #nazwa naszego QuerySetu
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    data_aktualna = timezone.now()
    post_number = Post.objects.count()
    #przekazujemy dane w słowniku, nadajemy nazwe klucza taka sama jaka 
    #wywolujemy w pliku html (przechodzimy tam po kluczu 'posts')
    return render(
        request, 'blog/post_list.html', {
            'posts': posts, 'data_teraz': data_aktualna, 'p':post_number
        })

def post_detail(request, pk):
    #tworzenie widoku do url'ow
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
