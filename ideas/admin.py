from django.contrib import admin
from .models import Idea, remarks
# Register your models here.

class IdeaAdmin(admin.ModelAdmin):
    readonly_fields = ('created','edited')#admin will be able to see when the idea was created and when it was edited

admin.site.register(Idea, IdeaAdmin)
admin.site.register(remarks)