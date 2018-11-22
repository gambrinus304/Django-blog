from django.shortcuts import render




# Create your views here.
def posts_list(request):
    n = ['Vasily.sk', 'Kris', 'Ksu']
    return render(request, 'blog/index.html', context={'names': n})