from django.shortcuts import render, get_object_or_404
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.core.mail import send_mail
from taggit.models import Tag
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Blog, Comment
from .forms import EmailPostForm, CommentForm, SearchForm



def post_share(request, post_id):
    post = get_object_or_404(Blog, id=post_id, active=True)
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{}'.format(post.title[:30])
            message = f'сообщение от -  {cd["name"]}  : {cd["comments"]}\n\n' \
                      f'Email отправителя  -  {cd["you_email"]}\n\n' \
                      f'Узнать подробнее по ссылке : {post_url}'
            to = '{}'.format(cd['to'])
            send_mail(subject, message, 'vinogradovpavel32@gmail.com', [to])
            sent = True
    else:
        form = EmailPostForm()
    context = {
        'form': form,
        'post': post,
        'sent': sent,
    }
    return render(request, 'blog/post_share.html', context)

@login_required
def home(request, type_news=None):
    # Views home page
    object_list = Blog.published.all()
    tag = None
    if type_news:
        tag = get_object_or_404(Tag, slug=type_news)
        object_list = object_list.filter(tags__in=[tag])
    paginator = Paginator(object_list, 6)
    page = request.GET.get('page')

    # Pagination home page
    try:
        blog = paginator.page(page)
    except EmptyPage:
        blog = paginator.page(1)
    except PageNotAnInteger:
        blog = paginator.page(paginator.num_pages)

    context = {
        'blog': blog,
        'page': page,
        'tag': tag,
        'comments': object_list,
    }
    return render(request, 'blog/home.html', context)


def detail(request, year, month, day, slug):
    post = get_object_or_404(Blog, slug=slug,
                             created__year=year,
                             created__month=month,
                             created__day=day, )
    new_comment = None
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comment_form': comment_form,
        'comments': comments,
        'new_comment': new_comment,
    }
    return render(request, 'blog/details.html', context)

