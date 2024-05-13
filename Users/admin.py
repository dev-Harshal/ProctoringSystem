from django.contrib import admin
from Users.models import User

# Register your models here.



# class UserAdmin(admin.ModelAdmin):
#     list_display = ['id','full_name','email','role']

admin.site.register(User)