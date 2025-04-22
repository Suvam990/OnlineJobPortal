
from django.contrib import admin
from .models import Category, Job, Application
from django.contrib.auth.models import User


admin.site.register(Category)
# admin.site.register(Job)
# admin.site.register(Application)
# admin.site.register(User)



@admin.register(Job)
class JobAmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'category', 'posted_at','slug']
    prepopulated_fields = {'slug': ('title',)}


# @admin.register(Application)
# class ApplicationAdmin(admin.ModelAdmin):
#    list_display = ['job', 'user', 'full_name', 'email', 'phone', 'resume', 'applied_at',' status']
#    list_filter = ['status']
#    search_fields = ['full_name', 'email', 'job']


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['job', 'user', 'full_name', 'email', 'phone', 'resume', 'applied_at', 'status_display']

    def status_display(self, obj):
        return obj.get_status_display()  # This will return the human-readable status name
    status_display.admin_order_field = 'status'  # Allows sorting by status
    status_display.short_description = 'Status'




# admin.site.register(User, UserAdmin)
