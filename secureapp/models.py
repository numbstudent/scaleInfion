from email.policy import default
from django.db import models
from django.contrib.auth.models import User, Group

class AccessList(models.Model):
    feature_alias = models.CharField(max_length=30, unique=True)
    feature_name = models.CharField(max_length=50)
    allowed_groups = models.ManyToManyField(Group)
    def __str__(self):
        return self.feature_name