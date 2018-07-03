from django.db import models
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    text = models.TextField()
    timestamp = models.DateField(
        default=timezone.now)
    draft = models.BooleanField()
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        view_name = "detail"
        return reverse(view_name, kwargs={"pk": self.pk})

    def __str__(self):
        return self.text[:150]
