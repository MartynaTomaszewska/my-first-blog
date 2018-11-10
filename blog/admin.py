from django.contrib import admin
from .models import Post
from .models import User
from .models import Group

# Register your models here.

admin.site.register(Post)
admin.site.register(User)
admin.site.register(Group)