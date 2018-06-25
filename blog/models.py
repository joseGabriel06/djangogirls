from django.db import models
from django.utils import timezone


class Post(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    timestamp = models.DateField(
        default=timezone.now)
    draft = models.BooleanField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #def get_absolute_url(self):
    #    view_name = "detail"
    #    return reverse(view_name, kwargs={"pk": self.id})
    


    def __str__(self):
        return self.title
