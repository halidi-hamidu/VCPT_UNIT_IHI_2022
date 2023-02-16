from django.db import models
import uuid
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class VcptuTeamModal(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    staff_image = models.ImageField(upload_to='media/')
    staff_name = models.CharField(max_length= 100, null=True, blank=True)
    professional_or_title = models.CharField(max_length=100,null=True, blank=True)
    profile_descriptions = RichTextField()
    posted_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='staff_profile_content_posted_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'VCPTU-Team'

    def __str__(self):
        return f'{str(self.staff_name)}'