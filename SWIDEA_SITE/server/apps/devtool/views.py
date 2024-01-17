from django.shortcuts import render, redirect 
from .forms import DevtoolForm
from .models import Devtool
from apps.posts.models import Post
# from posts.models import Post


# Create your views here.
def devtool_list(request):
    devtools = Devtool.objects.all()
    ctx = {'devtools': devtools}
    return render(request, 'devtool/devtool_list.html', ctx)

def create(request):
    if request.method == 'GET':
        form = DevtoolForm()
        ctx = {'form': form}
        return render(request, 'devtool/devtool_create.html', ctx) 
    form = DevtoolForm(request.POST)
    if form.is_valid():
        devtool = form.save()
        return redirect('devtools:detail', pk=devtool.pk) # Redirect to the detail view
    else:
        return render(request, 'devtool/devtool_create.html', {'form': form}) # Display form errors


def delete(request, pk):
    if request.method == 'POST':
        devtools = Devtool.objects.get(id=pk)
        devtools.delete()
        
    return redirect('devtools:list')

    
def update(request, pk):
    devtool = Devtool.objects.get(id=pk) 

    if request.method == 'GET':    
        # devtool = Devtool.objects.get(id=pk)
        form = DevtoolForm(instance=devtool)
        ctx = {'form': form, 'pk': pk}
        return render(request, 'devtool/devtool_update.html', ctx)
    
    form = DevtoolForm(request.POST, instance=devtool)
    if form.is_valid():
        form.save()
    return redirect('devtools:detail', pk)

def detail(request, pk):
    devtool = Devtool.objects.get(id=pk)
    related_posts = Post.objects.filter(devtool=devtool)
    return render(request, 'devtool/devtool_detail.html', {
        'devtool': devtool,
        'related_posts': related_posts
    })
