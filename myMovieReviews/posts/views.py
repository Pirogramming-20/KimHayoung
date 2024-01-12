from django.shortcuts import render, HttpResponse, redirect 
from .models import *

def post_list(request) : 
    posts = Post.objects.all()
    context = {
        "posts" : posts 
    }
    return render(request, 'posts_list.html', context)

def posts_detail(request, pk):
    post = Post.objects.get(id = pk)

    


    context = {
        "post" : post,

       
        

    }
    return render(request, "posts_detail.html", context)

def posts_create(request) :
    if request.method == "POST" :
        Post.objects.create(
            movie_title = request.POST["movie_title"],
            created_year = request.POST["created_year"],
            genre = request.POST["genre"],
            score = request.POST["score"],
            review_content = request.POST["review_content"],

            #새로 추가
            director = request.POST["director"],
            actor= request.POST["actor"],
            running_time = request.POST["running_time"],

        )
        return redirect("/posts")
    return render(request, "posts_create.html")

def posts_update (request, pk):  
    post = Post.objects.get(id=pk)

    if request.method == "POST" :
        post.movie_title = request.POST["movie_title"]
        post.created_year = request.POST["created_year"]
        post.genre = request.POST["genre"]
        post.score = request.POST["score"]
        post.review_content = request.POST["review_content"]

        #새로 추가
        post.director = request.POST["director"]
        post.actor= request.POST["actor"]
        post.running_time = request.POST["running_time"]
        
        post.save()
        return redirect(f"/posts/{pk}")
    

    context = {
        "post" : post 
    }
    return render(request, "posts_update.html", context)

def posts_delete (request, pk) : 
    if request.method == "POST" : 
        post = Post.objects.get(id=pk)
        post.delete()
    return redirect("/posts")

# def comments_create(request, post_id) :
#     Comment.objects.create(
#         post_id = post_id,
#         review_content = request.POST["review_content"]
#     )

#     return redirect(f"/posts/{post_id}")



