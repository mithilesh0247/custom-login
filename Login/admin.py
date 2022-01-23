from django.contrib import admin
from Login.models import count_user
# Register your models here.
class count_user_admin(admin.ModelAdmin):
    list_display=["username","count","loginAt"]

admin.site.register(count_user,count_user_admin)