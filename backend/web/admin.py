from django.contrib import admin
from web.models.user import UserProfile

@admin.register(UserProfile)
class UserProflieAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
# Register your models here.
