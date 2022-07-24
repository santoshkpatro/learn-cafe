from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    message = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'contacts'

    def __str__(self) -> str:
        return str(self.email)