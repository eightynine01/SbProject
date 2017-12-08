from django.db import models


class Board(models.Model):
    # board_category = models.
    board_user = models.CharField(max_length=20)
    board_password = models.CharField(max_length=20)
    board_count = models.IntegerField()
