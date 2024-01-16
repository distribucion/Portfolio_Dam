from django.shortcuts import render, get_object_or_404
# froma para importar los modelos
from .models import Post

# Esta funcion renderiza todas las publicaciones


def render_posts(request):
    # esta es la forma de proyectar desde models
    # la estructura de publicacion para verla en la pagina
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

# Vista para renderizar una vista de detalle


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {"post": post})
