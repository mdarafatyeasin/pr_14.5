from django.db import models

# Create your models here.
class MyModel(models.Model) :
    name = models.CharField(max_length=100)
    comment = models.CharField(widget=models.Textarea)
    comment = models.CharField(widget=models.Textarea(attrs={'rows':3}))
    email = models.EmailField()
    agree = models.BooleanField()
    date = models.DateField()
    value = models.DecimalField()
    # birth_date = models.DateField(widget=NumberInput(attrs={'type': 'date'}))
    
    def __str__ (self) :
        return f'{self.title} - ({self.author})'