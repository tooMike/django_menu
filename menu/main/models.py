from django.db import models


class Menu(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название"
    )

    class Meta:
        verbose_name = "меню"
        verbose_name_plural = "Список меню"

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu,
        related_name='items',
        on_delete=models.CASCADE,
        verbose_name="Меню"
    )
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Slug")
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='children',
        on_delete=models.CASCADE,
        verbose_name="Родительский пункт меню"
    )

    class Meta:
        verbose_name = "пункт меню"
        verbose_name_plural = "Пункты меню"

    def __str__(self):
        return self.name

    def get_url(self):
        return "/%s" % self.slug
