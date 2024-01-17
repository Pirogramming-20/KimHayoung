from django.shortcuts import render, redirect 
from .forms import PostForm
from .models import Post 

def main(request):
    #필터링을 위한 부분 
    #쿼리스트링 가져오기 / 필터링을 만들어보자!
    sort_name = request.GET.get('sort_name') #이름순
    sort_recent = request.GET.get('sort_recent') #최신순  최신것부터 
    sort_order = request.GET.get('sort_order') #등록순 오래된항목부터
    #찜하기순 
    
    

    posts = Post.objects.all()

    if sort_name:
        posts = posts.filter(title_gt=sort_name) #알파벳 순은 gt인가 lt인가?
    if sort_order:
        posts = posts.filter(created_date__gt=sort_order)
    if sort_recent:
        posts = posts.filter(created_date__lt=sort_recent)


    ctx = {'posts': posts} 
    return render(request, 'posts/post_list.html', ctx) 

def create(request):
    if request.method == 'GET': 
        form = PostForm()
        ctx = {'form': form}
        return render(request, 'posts/post_create.html', ctx)
    
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        post = form.save()
        return redirect('posts:detail', pk=post.pk) # Redirect to the detail view
    else:
        return render(request, 'posts/post_create.html', {'form': form}) # Display form errors


def detail(request, pk):
    post = Post.objects.get(id=pk)
    devtool = post.devtool  
    related_posts = Post.objects.filter(devtool=devtool)  
    ctx = {'post': post, 'related_posts': related_posts}
    return render(request, 'posts/post_detail.html', ctx)

def delete(request, pk):
    if request.method == 'POST':
        #pk에 해당하는 post 객체 조회하기 
        posts = Post.objects.get(id=pk)
        posts.delete() 
        #Post.objects.get(id=pk).posts.delete() 위 두줄을 합친 똑같은 코드임.
    return redirect('posts:main')

def update(request, pk):
    post=Post.objects.get(id=pk)

    if request.method == 'GET':
        #수정하기 폼에서 내용 보여지도록 저장된값 불러오기
        
        form = PostForm(instance=post)
        
        ctx = {'form': form, 'pk': pk}
        return render(request, 'posts/post_update.html', ctx)
    form = PostForm(request.POST, request.FILES, instance=post)
    if form.is_valid():
        form.save()
    return redirect('posts:detail', pk) 
#urls.py에 있는 posts 안에 detail안에 pk를 말함.
    
