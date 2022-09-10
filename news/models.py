from django.db import models

class Articles(models.Model):
    title = models.CharField('Title', max_length=50, default='21')
    anons = models.CharField('Anons', max_length=250)
    fullt_text = models.TextField('Article')
    date = models.DateTimeField('Date publication')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
