from django.contrib import admin

from .models import Member,User_List

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname","phone","create_date")
    prepopulated_fields = {"slug": ("firstname", "lastname")}
admin.site.register(Member,MemberAdmin)


class UserListAdmin(admin.ModelAdmin):
    list_display = ("Factory","username","TeamID","FullName","LastUpdate")
    list_filter  = ["LastUpdate"]
    search_fields= ["username"]
admin.site.register(User_List,UserListAdmin)

