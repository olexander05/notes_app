from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Note(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    reminder = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Поле, яке викликає проблему

    def __str__(self):
        return self.title