from django.conf.urls import url
from user import views

urlpatterns = [
    url(r'^$',views.AboutView.as_view(),name='about'),
    # url(r'^adduser/$',views.add_user,name='add_user'),
    url(r'^user/$',views.UserListView.as_view(),name='list'),
    url(r'^user/new/$', views.CreatePostView.as_view(), name='user_new'),
    url(r'^user/(?P<pk>\d+)$',views.UserDetailView.as_view(), name='user_detail'),
    url(r'^user/(?P<pk>\d+)/edit/$', views.UserUpdateView.as_view(), name='user_edit'),
    url(r'^user/(?P<pk>\d+)/remove/$', views.UserDeleteView.as_view(), name='user_remove'),
    url(r'^user/(?P<pk>\d+)/friend/$', views.add_friend_to_user, name='add_friend_to_user'),
    ]
