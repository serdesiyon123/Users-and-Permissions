from django.shortcuts import render, redirect
from .forms import RegisterUser, PostForm
from django.contrib.auth import login,logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, permission_required
from .models import Post
@login_required(login_url='/login')
def home(request):
    posts = Post.objects.all()

    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        user_id = request.POST.get('user_id')

        if post_id:
            post = Post.objects.filter(id=post_id).first()
            if post and post.author == (request.user or request.user.has_perms('website.delete_post')):
                post.delete()
        elif user_id:
            user = User.objects.filter(id=user_id).first()
            if request.user.is_staff:
                try:
                    group = Group.objects.get(name='default')
                    group.user_set.remove(user)
                except :
                    pass
                try:
                    group = Group.objects.get(name='mods')
                    group.user_set.remove(user)
                except :
                    pass

    return render(request, 'website/home.html', {'posts': posts})

def out(request):
    return redirect('/login')


def sign_up(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/home')
    elif request.method == 'GET':
        form = RegisterUser()

    return render(request, 'registration/sign_up.html' , {'form': form})


@login_required(login_url='/login')
@permission_required('website.add_post', login_url='/login', raise_exception=True)
def post(request):
    if request.method == 'POST':
       form = PostForm(request.POST)
       if form.is_valid():
           post = form.save(commit=False)
           post.author = request.user
           post.save()
           return redirect('/home')

    else:
      form = PostForm()

      return render(request,'website/post_form.html', {'form': form})



def log_out(request):
    logout(request)
    return redirect('/login')