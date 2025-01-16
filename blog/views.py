from django.shortcuts import render
from .forms import PostForm

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # Basically get the Post form
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'add_post.html', {'form':form})