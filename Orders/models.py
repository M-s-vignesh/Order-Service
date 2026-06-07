from django.db import models
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL
status_choices = [
    ('PG', 'Pending'),
    ('CD', 'Confirmed'),
    ('DD', 'Delivered')]


class Orders(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    items = models.IntegerField()

    status = models.CharField(
        max_length=2,
        choices=status_choices,
        default='PG'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} order"
