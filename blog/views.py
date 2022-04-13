from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models.functions import Lower

from .models import Post
from .forms import PostForm


""" Gets all blog posts """
def posts(request):

    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)


@login_required
def add_post(request):
    """ Adds blog posts """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry only site admins can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST' and request.user.is_superuser:
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.user = request.user
            post.save()
            messages.success(request, "Your post has" +
                             "been submitted for this blog")
            return redirect('reviews')
        else:
            messages.error(request, 'Sorry, we couldn''t' +
                           'submit you post right now')    
    else:
        form = PostForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_post(request, post_id):
    """ Edits a blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can edit a review.')
        return redirect(reverse('posts'))

    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your blog post has been updated!')
            return redirect('posts')
        else:
            messages.error(request, 'Your post failed to update. Please check the form is filled out correctly.')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.id}')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_post(request, post_id):
    """ Deletes blog posts """

    post = get_object_or_404(Post, pk=post_id)
    if request.user.is_superuser:
        post.delete()
        messages.success(request, "Post has been successfully deleted"
                         )
    else:
        messages.error(request, 'Sorry, we could not' +
                       'delete you post right now')

    return redirect(reverse('posts'))
