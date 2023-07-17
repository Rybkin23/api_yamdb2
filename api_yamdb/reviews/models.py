from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


MIN_SCORE = 1
MAX_SCORE = 10


class UserRole(models.TextChoices):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'


class User(AbstractUser):
    username = models.CharField(
        verbose_name='Имя пользователя',
        help_text='Введите имя',
        max_length=150,
        unique=True,
        validators=(UnicodeUsernameValidator(),)
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
        help_text='Введите почту',
        max_length=254,
        unique=True, blank=False)
    role = models.CharField(
        verbose_name='Роль',
        help_text='Выберите роль',
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.USER)
    bio = models.TextField(
        verbose_name='Биография',
        help_text='Напиши биографию',
        blank=True,
        null=True,
    )

    @property
    def is_moderator(self):
        return self.role == UserRole.MODERATOR.value

    @property
    def is_admin(self):
        return self.is_superuser or self.role == UserRole.ADMIN.value

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'


class Category(models.Model):
    name = models.CharField(max_length=256,
                            verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True,
                            verbose_name='Идентификатор категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=256,
                            verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True,
                            verbose_name='Идентификатор жанра')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['name']

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=256,
                            verbose_name='Название')
    year = models.PositiveSmallIntegerField(db_index=True,
                                            verbose_name='Год выхода')
    genre = models.ManyToManyField(
        Genre, related_name='titles', blank=True,
        verbose_name='Жанр'
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        related_name='titles', blank=True, null=True,
        verbose_name='Категория'
    )
    description = models.TextField(null=True, blank=True,
                                   verbose_name='Описание')

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        ordering = ['name']

    def __str__(self):
        return self.name


class Review(models.Model):

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(MIN_SCORE),
                    MaxValueValidator(MAX_SCORE)])
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        unique_together = ('author', 'title',)
        ordering = ('pub_date',)
        verbose_name_plural = 'Отзыв'
        verbose_name = 'Отзывы'


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('pub_date',)
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'
