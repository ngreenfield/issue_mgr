from django.contrib import admin
from .models import Issue

class IssueAdmin(admin.ModelAdmin):
    list_display = [
        "name", "summary", "reporter",
        "assignee", "status", "created_on"
    ]

    admin.site.register(Issue,)
