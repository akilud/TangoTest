from django.contrib import admin
from rango.models import Category, Page, UserProfile


admin.site.register(Category)


# Register your models here.

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')


admin.site.register(Page, PageAdmin)

admin.site.register(UserProfile)