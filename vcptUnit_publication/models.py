from django.db import models
import uuid
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class VcptuPublications(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    description = RichTextField()
    posted_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='publcation_content_posted_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'VCPTU-Publications'

    def __str__(self):
        return f'{str(self.description[3:-4])} '