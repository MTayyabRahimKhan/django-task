from django.contrib import admin
from .models import *
# Register your models here.


class IssueTicketsView(admin.ModelAdmin):
    list_display = ('id', 'summary', 'creator')


admin.site.register(IssueTickets, IssueTicketsView)