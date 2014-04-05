from django.conf.urls import patterns,  url

urlpatterns = patterns('',
    url(r"^myalkin/user/create/$", 'forumDB.views.user.create', name='user_create'),
    url(r"^myalkin/user/follow/$", 'forumDB.views.user.follow', name='follow'),
    url(r"^myalkin/user/unfollow/$", 'forumDB.views.user.unfollow', name='unfollow'),
    url(r"^myalkin/user/details/$", 'forumDB.views.user.details', name='user_details'),
    url(r"^myalkin/user/updateProfile/$", 'forumDB.views.user.update', name='user_update'),
    url(r"^myalkin/user/listFollowers/$", 'forumDB.views.user.list_followers', name='list_followers'),
    url(r"^myalkin/user/listFollowing/$", 'forumDB.views.user.list_following', name='list_following'),
    url(r"^myalkin/user/listPosts/$", 'forumDB.views.user.list_posts', name='list_posts'),

    url(r"^myalkin/forum/create/$", 'forumDB.views.forum.create', name='forum_create'),
    url(r"^myalkin/forum/details/$", 'forumDB.views.forum.details', name='forum_details'),
    url(r"^myalkin/forum/listThreads/$", 'forumDB.views.forum.listThreads', name='forum_list_threads'),
    url(r"^myalkin/forum/listPosts/$", 'forumDB.views.forum.list_posts', name='forum_list_posts'),
    url(r"^myalkin/forum/listUsers/$", 'forumDB.views.forum.list_users', name='forum_list_users'),

    url(r"^myalkin/thread/create/$", 'forumDB.views.thread.create', name='thread_create'),
    url(r"^myalkin/thread/subscribe/$", 'forumDB.views.thread.subscribe', name='subscribe'),
    url(r"^myalkin/thread/unsubscribe/$", 'forumDB.views.thread.unsubscribe', name='unsubscribe'),
    url(r"^myalkin/thread/details/$", 'forumDB.views.thread.details', name='thread_details'),
    url(r"^myalkin/thread/vote/$", 'forumDB.views.thread.vote', name='thread_vote'),
    url(r"^myalkin/thread/open/$", 'forumDB.views.thread.open', name='thread_open'),
    url(r"^myalkin/thread/close/$", 'forumDB.views.thread.close', name='thread_close'),
    url(r"^myalkin/thread/list/$", 'forumDB.views.thread.list', name='thread_list'),
    url(r"^myalkin/thread/update/$", 'forumDB.views.thread.update', name='thread_update'),
    url(r"^myalkin/thread/listPosts/$", 'forumDB.views.thread.list_posts', name='thread_list_post'),
    url(r"^myalkin/thread/remove/$", 'forumDB.views.thread.remove', name='thread_remove'),
    url(r"^myalkin/thread/restore/$", 'forumDB.views.thread.restore', name='thread_restore'),

    url(r"^myalkin/post/create/$", 'forumDB.views.post.create', name='post_create'),
    url(r"^myalkin/post/details/$", 'forumDB.views.post.details', name='post_details'),
    url(r"^myalkin/post/update/$", 'forumDB.views.post.update', name='post_update'),
    url(r"^myalkin/post/remove/$", 'forumDB.views.post.remove', name='post_remove'),
    url(r"^myalkin/post/restore/$", 'forumDB.views.post.restore', name='post_restore'),
    url(r"^myalkin/post/vote/$", 'forumDB.views.post.vote', name='post_vote'),
    url(r"^myalkin/post/list/$", 'forumDB.views.post.list', name='post_list'),

)
