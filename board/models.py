from django.db import models


class Category(models.Model):
    category_name = models.CharField(verbose_name='카테고리', max_length=20)
    created = models.DateTimeField(auto_now_add=True)


class Board(models.Model):
    class Meta:
        ordering = ('-created',)
    board_category = models.OneToOneField(Category, on_delete=models.CASCADE)
    board_title = models.CharField(verbose_name='제목', max_length=20)
    board_content = models.TextField(verbose_name='내용')
    # board_user = models.CharField(verbose_name='글쓴이', max_length=20)
    # board_password = models.CharField(verbose_name='패스워드', max_length=20)
    board_count = models.IntegerField(verbose_name='조회수')
    created = models.DateTimeField(auto_now_add=True)
