from django.db import models

class Player(models.Model):
    nick = models.CharField(max_length=55)

    def __str__(self):
        return self.nick
