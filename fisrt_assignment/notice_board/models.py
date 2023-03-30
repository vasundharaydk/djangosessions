from django.db import models

# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=245)
    text = models.TextField(max_length=500)
    contact_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.text} - {self.contact_number} - {self.created_at}'

