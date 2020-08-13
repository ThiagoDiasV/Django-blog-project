from django.contrib import admin
from blog.models import Blogpost, Author, Comments


class CommentsInline(admin.TabularInline):
    model = Comments
    extra = False


@admin.register(Blogpost)
class BlogpostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author')
    list_filter = ('date',)
    inlines = [CommentsInline]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('author', 'blog_post', 'date_time')
    list_filter = ('date_time',)
