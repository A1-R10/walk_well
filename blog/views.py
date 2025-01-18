from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import PostForm,  UserUpdateForm, ProfileUpdateForm,  CommentForm
from .models import Post
from django.core.paginator import Paginator


def home(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 3)  # 5 posts per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {'page_obj': page_obj})


# Get Specific Post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  # Ensure post exists
    comments = post.comments.all()

    # Handle comment form submission
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            if request.user.is_authenticated:
                comment.name = request.user.username  # Set name as the username
                comment.email = request.user.email
                comment.author = request.user  # Associate logged-in user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=pk)
    else:
        form = CommentForm()

    # Pass the necessary context
    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })


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


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('home')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html', context)