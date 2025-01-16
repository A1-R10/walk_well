from django.shortcuts import render

def home(request):
    posts = Post.objects.all().order_by('-created_at')

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/home.html', {'page_obj': page_obj})

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

    return render(request, 'blog/add_post.html', {'form':form})