from django.contrib import admin
from insta.models import Post, Like, InstaUser, UserConnection

# Register your models here.

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(InstaUser)
admin.site.register(UserConnection)