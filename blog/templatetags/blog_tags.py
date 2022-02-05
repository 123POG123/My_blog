from django import template

from ..models import Blog

register = template.Library()


@register.simple_tag()
def total_post():
    return Blog.published.count()


@register.inclusion_tag('blog/components/latest_post.html')
def show_latest(count=5):
    latest_posts = Blog.published.order_by('-created')[:count]
    return {'latest_posts': latest_posts}
