from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, verbose_name='Автор')
    ratingAuthor = models.SmallIntegerField(default=0, verbose_name='Рейтинг автора')

    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('rating', verbose_name='Рейтинг публикации'))
        pRat = 0
        pRat += postRat.get('postRating')

        commentRat = self.authorUser.comment_set.appregate(commentRating=Sum('rating', verbose_name='Рейтинг комментария'))
        cRat = 0
        cRat += commentRat.get('commentRating')

        self.ratingAuthor = pRat * 3 + cRat
        self.save()

        #  функция, которая говорит, как лучше вывести объект в админ панель
    def __str__(self):
        return f'{self.authorUser}'

    class Meta:
        verbose_name_plural = 'Авторы'
        verbose_name = 'Автор'


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Категория')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')

    class Meta:
        verbose_name_plural = 'Публикации'
        verbose_name = 'Публикация'

    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    )
    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE, verbose_name='Категория')
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    postCategory = models.ManyToManyField(Category, through='PostCategory', verbose_name='Категория публикации')
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    rating = models.SmallIntegerField(default=0, verbose_name='Рейтинг')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:123] + '...'

    def __str__(self):
        return f'{self.title}'


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Выбрать публикацию')
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Выбрать категорию')

    class Meta:
        verbose_name_plural = 'Категории публикаций'
        verbose_name = 'Категория публикации'


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Комменарий к публикации')
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Комментарий пользователя')
    text = models.TextField(verbose_name='Текст')
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    rating = models.SmallIntegerField(default=0, verbose_name='Рейтинг')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return f'{self.commentUser}: {self.text[:20]}'

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'