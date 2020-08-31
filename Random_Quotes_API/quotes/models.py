from django.db import models

# Create your models here.
class Language(models.Model):
    language_name = models.CharField(max_length=30)

    def __str__(self):
        return self.language_name
    
    class Meta:
        verbose_name_plural = "Languages"

class Quotes(models.Model):
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.CharField(max_length= 100)
    source = models.CharField(max_length= 100, blank= True)
    rating = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = "Quotes"