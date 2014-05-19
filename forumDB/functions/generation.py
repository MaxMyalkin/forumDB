import MySQLdb

__author__ = 'maxim'
from time import strftime, gmtime
from random import randrange


def time_gen():
    result = strftime('%Y-%m-%d %H:%M', gmtime())
    return result


host = 'localhost'
user = 'maxim'
password = '12345'
database = 'forumDB'

db = MySQLdb.connect(host, user, password, database, init_command='SET NAMES UTF8')
cursor = db.cursor()

#for i in xrange(1, 1000):
#    cursor.execute("insert into Users (email, about, name, username) values (%s, %s, %s, %s)",
#                   ("email" + format(i), "about me", "user" + format(i), "username" + format(i)))
#    db.commit()
#print "users done"

#for i in xrange(10, 10):
#    forum = "short_name" + format(i)
#    user = "email" + format(randrange(1, 1000))
#    cursor.execute("insert into Forums (name, short_name, user) values (%s, %s, %s)",
#                   ("forum" + format(i), forum, user))
#    db.commit()
#    for j in xrange(1, 10):
#        thread_id = 10 * (i - 1) + j
#        thread_slug = "slug" + format(10 * (i - 1) + j)
#        cursor.execute("insert into Threads (id, date, message, slug, title, user, forum) "
#                       "values (%s, %s, %s, %s, %s, %s, %s)",
#                       (thread_id, time_gen(), "message" + format(j), thread_slug, "title" + format(j),
#                        "email" + format(randrange(1, 1000)), forum))
#        user_post = "email" + format(randrange(1, 1000))
#        for k in xrange(1, 100):
#            post_id = 100 * (thread_id - 1) + k
#            cursor.execute("insert into Posts (date, user, message, thread, forum) "
#                           "values (%s, %s, %s, %s, %s)",
#                           (time_gen(), user_post, "message_", thread_id, forum))
#    print "forum 1"
#
#for i in xrange(1, 10000):
#    cursor.execute("insert into Followers (follower, followee) values(%s, %s)",
#    ( "email" + format(randrange(1, 100)), "email" + format(randrange(1, 100))))
#    db.commit()

for i in xrange(1, 10000):
    cursor.execute("insert into Subscriptions (thread, user) values(%s, %s)",
    (int(randrange(1, 50)), "email" + format(randrange(100, 1000))))
    db.commit()

cursor.close()
db.close()
