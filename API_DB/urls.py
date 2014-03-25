from django.conf.urls import patterns,  url

urlpatterns = patterns('',
    url(r"^user/create/$", 'forumDB.views.user.create', name='user_create'),
    url(r"^user/follow/$", 'forumDB.views.user.follow', name='follow'),
    url(r"^user/unfollow/$", 'forumDB.views.user.unfollow', name='unfollow'),
    url(r"^user/details/$", 'forumDB.views.user.details', name='user_details'),
    url(r"^user/updateProfile/$", 'forumDB.views.user.update', name='user_update'),
    url(r"^user/listFollowers/$", 'forumDB.views.user.list_followers', name='list_followers'),
    url(r"^user/listFollowing/$", 'forumDB.views.user.list_following', name='list_following'),

    url(r"^forum/create/$", 'forumDB.views.forum.create', name='forum_create'),
    url(r"^forum/details/$", 'forumDB.views.forum.details', name='forum_details'),
    url(r"^forum/listThreads/$", 'forumDB.views.forum.listThreads', name='forum_list_threads'),

    url(r"^thread/create/$", 'forumDB.views.thread.create', name='thread_create'),
    url(r"^thread/subscribe/$", 'forumDB.views.thread.subscribe', name='subscribe'),
    url(r"^thread/unsubscribe/$", 'forumDB.views.thread.unsubscribe', name='unsubscribe'),
    url(r"^thread/details/$", 'forumDB.views.thread.details', name='thread_details'),
    url(r"^thread/vote/$", 'forumDB.views.thread.vote', name='thread_vote'),
    url(r"^thread/open/$", 'forumDB.views.thread.open', name='thread_open'),
    url(r"^thread/close/$", 'forumDB.views.thread.close', name='thread_close'),
    url(r"^thread/list/$", 'forumDB.views.thread.list', name='thread_list'),
    url(r"^thread/update/$", 'forumDB.views.thread.update', name='thread_update'),

    url(r"^post/create/$", 'forumDB.views.post.create', name='post_create'),


)
