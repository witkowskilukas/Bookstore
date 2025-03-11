from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth import get_user_model

# Create your models here.
class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    title = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to="covers/", blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["id"], name="id_index"),
        ]
        permissions = [("special_status","Can read all books"),]
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])


class Review(models.Model):
    book = models.ForeignKey(Book,
                             on_delete=models.CASCADE,
                             related_name="reviews") # equivalent to name in urls.py, reference to which you refer e.g. in DTL
    
    review = models.CharField(max_length=250)
    author = models.ForeignKey(get_user_model(),
                               on_delete=models.CASCADE)
    
    def __str__(self):
        return self.review
