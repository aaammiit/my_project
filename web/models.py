
# Create your models here.
from django.db import models

# class Contact(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     subject = models.CharField(max_length=100, null=True, blank=True)
#     message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         managed = True
#         db_table = 'contact'

# from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'contact'
