from django.contrib import admin
from . models import Course, Category


#admin.site.register(Course)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'available') #kursları adı ve  başka özelliğine göre listeleme
    list_filter = ('available',) #listeleme
    search_fields = ('name','date') #tarihe göre arama


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}