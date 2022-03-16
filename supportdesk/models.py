from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


# Create your models here.


class IssueTickets(models.Model):
    summary = models.CharField(max_length=127, default=None, null=False)
    description = models.CharField(max_length=511, default=None, null=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='created_by_user')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None,
                                    related_name='assigned_to_user')
    is_high_priority = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
