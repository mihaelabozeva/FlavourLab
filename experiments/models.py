from django.db import models

# Create your models here.
class Experiment(models.Model):
    title=models.CharField(max_length=80)
    ingredients=models.ManyToManyField('ingredients.Ingredient', related_name='experiments')
    observations=models.TextField()
    result=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title