from django.contrib import admin
from django import forms

from api.models import TestBlog, News, Emails
from ckeditor.widgets import CKEditorWidget

# Cosutmize Admin Interface
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title","id", "top_of_the_week","editors_pick","category", "date_posted"]

admin.site.site_header = 'Logiclude News Admin Panel'
admin.site.site_url = 'http://192.168.254.168:3000'
admin.site.register(TestBlog)
admin.site.register(News, NewsAdmin)
admin.site.register(Emails)
