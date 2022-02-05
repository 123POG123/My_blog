from django.urls import path
from django.contrib.auth import views as auth_views


from . import views
from .feeds import LatestBlogFeed

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    # Registration
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('feed/', LatestBlogFeed(), name='post_feed'),
    path('<slug:type_news>/', views.home, name='home_tag_type'),
    path('share/<int:post_id>/', views.post_share, name='share_post'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.detail, name='detail'),

]
