
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest

# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    ctx = {
        'posts': posts,
    }
    return render(request, 'main/post_list.html', ctx)


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:post_list')
        else:
            ctx = {
                'form': form,
            }
            return render(request, 'main/post_new.html', ctx)
    elif request.method == 'GET':
        form = PostForm()
        ctx = {
            'form': form,
        }
        return render(request, 'main/post_new.html', ctx)
    
### 서버 실습 ###
import json 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# {% csrf_token %} 
# 보안용코드, csrf를 해제 시켜준다.(@ 데코레이터 달아서.)

@csrf_exempt
def like_ajax(request):
    req = json.loads(request.body)
    post_id = req['id']
    button_type = req['type']

    post = get_object_or_404(Post, id=post_id)

    if button_type == 'like':
        post.like += 1
    elif button_type == 'dislike':
        post.dislike += 1
    elif button_type == 'heart':
        # 사용자 세션에서 좋아요 상태를 가져오기
        user_liked = request.session.get(f'post_{post_id}_liked', False)

        # 좋아요 상태 토글 처리
        if user_liked:
            post.heart_like = False
            request.session[f'post_{post_id}_liked'] = False
        else:
            post.heart_like = True
            request.session[f'post_{post_id}_liked'] = True

    post.save()

    return JsonResponse({'id': post_id, 'type': button_type})


### 새 댓글 제출 ###
from .models import Post, Comment
from django.http import HttpResponseRedirect
from django.urls import reverse

def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        author = request.POST.get('author')
        text = request.POST.get('text')
        Comment.objects.create(post=post, author=author, text=text)
    return HttpResponseRedirect(reverse('main:post_list'))



from django.views.decorators.http import require_http_methods

 

@require_http_methods(["POST"])
@csrf_exempt
def delete_comment(request, comment_id):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Authentication required'}, status=401)
    
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.author or request.user.is_staff:
        comment.delete()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'error': 'Permission denied'}, status=403)

