from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r"^user/create/$", 'forumDB.views.user.create', name='user_create'),
    url(r"^forum/create/$", 'forumDB.views.forum.create', name='forum_create'),
    url(r"^user/follow/$", 'forumDB.views.user.follow', name='follow'),
    url(r"^user/unfollow/$", 'forumDB.views.user.unfollow', name='unfollow'),
    url(r"^user/details/$", 'forumDB.views.user.details', name='user_details'),

    # url(r'^API_DB/', include('API_DB.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
