import email
from tokenize import group
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Categories(models.Model):
    categoryname = models.CharField(max_length=255)

    def __str__(self):
        return self.categoryname


class Post(models.Model):
    GENDERS = (
    ('m', 'Boy'),
    ('f', 'Girl'),
    )

    # GARDENS = (
    #     ('7a', '7a'),
    #     ('7b', '7b'),
    #     ('8a', '8a'),
    #     ('8b', '8b'),
    #     ('9a', '9a'),
    #     ('9b', '9b'),
    #     ('10a', '10a'),
    #     ('10b', '10b'),
    #     ('11a', '11a'),
    #     ('11b', '11b'),
    # )

    title = models.CharField('Username', max_length=255, default='Lionel Messi')
    email = models.EmailField(max_length=225)
    birth_date = models.DateField('Born', default='2007-09-12')
    gender = models.CharField('Sex', max_length=1, choices=GENDERS, default='')
    location = models.CharField('Address', max_length=120, default='Panfilov 188')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # garden = models.CharField('Class', max_length=4, choices=GARDENS, default='')
    category = models.ForeignKey(Categories, null=True, on_delete=models.PROTECT, related_name='category_set')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

