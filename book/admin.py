from django.contrib import admin

# Register your models here.
from .models import Book, Novel, News
admin.site.site_header = "Dose of Voice Admin Panel"
class BookAdmin(admin.ModelAdmin):
	list_display = ['name', 'author', 'category', 'book', 'audio', 'uploaded_time']
class NovelAdmin(admin.ModelAdmin):
	list_display = ['novelname', 'novelauthor', 'novelcategory', 'novelbook', 'novelaudio', 'noveluploaded_time']
class NewsAdmin(admin.ModelAdmin):
	list_display = ['newsname', 'newsauthor', 'newscategory', 'newsbook', 'newsaudio', 'newsuploaded_time']

admin.site.register(Book, BookAdmin)
admin.site.register(Novel, NovelAdmin)
admin.site.register(News, NewsAdmin)