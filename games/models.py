from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=55)
    year = models.IntegerField(null=True, blank=True)
    genre = models.ForeignKey(
        to=Genre,
        null=True,
        on_delete=models.PROTECT,
        blank=True
    )
    studio = models.ForeignKey(
        to='Studio',
        null=True,
        on_delete=models.PROTECT,
        blank=True
    )


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Studio(models.Model):
    name = models.CharField(max_length=55)
    workers_count = models.PositiveIntegerField()
    games_count = models.IntegerField()


    def __str__(self):
        return self.name


