from django.contrib import admin

# Register your models here.

from .models import Language,Code

class LanguageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':    ('name',)}

class CodeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':    ('title',)}

admin.site.register(Language,LanguageAdmin)
admin.site.register(Code,CodeAdmin)