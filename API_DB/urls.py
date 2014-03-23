from django.conf.urls import patterns,  url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r"^user/create/$", 'forumDB.views.user.create', name='user_create'),
    url(r"^user/follow/$", 'forumDB.views.user.follow', name='follow'),
    url(r"^user/unfollow/$", 'forumDB.views.user.unfollow', name='unfollow'),
    url(r"^user/details/$", 'forumDB.views.user.details', name='user_details'),
    url(r"^user/updateProfile/$", 'forumDB.views.user.update', name='user_update'),
    url(r"^user/listFollowers/$", 'forumDB.views.user.list_followers', name='list_followers'),
    url(r"^user/listFollowing/$", 'forumDB.views.user.list_following', name='list_following'),
    url(r"^forum/create/$", 'forumDB.views.forum.create', name='forum_create'),
    url(r"^forum/details/$", 'forumDB.views.forum.details', name='forum_details'),
    url(r"^thread/create/$", 'forumDB.views.thread.create', name='thread_create'),
    url(r"^thread/subscribe/$", 'forumDB.views.thread.subscribe', name='subscribe'),
    url(r"^thread/unsubscribe/$", 'forumDB.views.thread.unsubscribe', name='unsubscribe'),
    # url(r'^API_DB/', include('API_DB.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
