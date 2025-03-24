from django.contrib import admin
from companywebsite.models import Category, Page

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

# Register Category with CategoryAdmin
admin.site.register(Category, CategoryAdmin)

# Register Page model
admin.site.register(Page)
