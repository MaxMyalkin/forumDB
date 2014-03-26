from django.conf.urls import patterns,  url

urlpatterns = patterns('',
    url(r"^user/create/$", 'forumDB.views.user.create', name='user_create'),
    url(r"^user/follow/$", 'forumDB.views.user.follow', name='follow'),
    url(r"^user/unfollow/$", 'forumDB.views.user.unfollow', name='unfollow'),
    url(r"^user/details/$", 'forumDB.views.user.details', name='user_details'),
    url(r"^user/updateProfile/$", 'forumDB.views.user.update', name='user_update'),
    url(r"^user/listFollowers/$", 'forumDB.views.user.list_followers', name='list_followers'),
    url(r"^user/listFollowing/$", 'forumDB.views.user.list_following', name='list_following'),
    url(r"^user/listPosts/$", 'forumDB.views.user.list_posts', name='list_posts'),

    url(r"^forum/create/$", 'forumDB.views.forum.create', name='forum_create'),
    url(r"^forum/details/$", 'forumDB.views.forum.details', name='forum_details'),
    url(r"^forum/listThreads/$", 'forumDB.views.forum.listThreads', name='forum_list_threads'),
    url(r"^forum/listPosts/$", 'forumDB.views.forum.list_posts', name='forum_list_posts'),
    url(r"^forum/listUsers/$", 'forumDB.views.forum.list_users', name='forum_list_users'),

    url(r"^thread/create/$", 'forumDB.views.thread.create', name='thread_create'),
    url(r"^thread/subscribe/$", 'forumDB.views.thread.subscribe', name='subscribe'),
    url(r"^thread/unsubscribe/$", 'forumDB.views.thread.unsubscribe', name='unsubscribe'),
    url(r"^thread/details/$", 'forumDB.views.thread.details', name='thread_details'),
    url(r"^thread/vote/$", 'forumDB.views.thread.vote', name='thread_vote'),
    url(r"^thread/open/$", 'forumDB.views.thread.open', name='thread_open'),
    url(r"^thread/close/$", 'forumDB.views.thread.close', name='thread_close'),
    url(r"^thread/list/$", 'forumDB.views.thread.list', name='thread_list'),
    url(r"^thread/update/$", 'forumDB.views.thread.update', name='thread_update'),
    url(r"^thread/listPosts/$", 'forumDB.views.thread.list_posts', name='thread_list_post'),

    url(r"^post/create/$", 'forumDB.views.post.create', name='post_create'),
    url(r"^post/details/$", 'forumDB.views.post.details', name='post_details'),
    url(r"^post/update/$", 'forumDB.views.post.update', name='post_update'),
    url(r"^post/remove/$", 'forumDB.views.post.remove', name='post_remove'),
    url(r"^post/restore/$", 'forumDB.views.post.restore', name='post_restore'),
    url(r"^post/vote/$", 'forumDB.views.post.vote', name='post_vote'),
    url(r"^post/list/$", 'forumDB.views.post.list', name='post_list'),

)
