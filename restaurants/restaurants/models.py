from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название")
    address = models.CharField(max_length=128, blank=True, verbose_name="Адрес")
    
    class Meta:
        verbose_name = "Ресторан"
        verbose_name_plural = "Рестораны"

    def __str__(self):
        return f"{self.name}"

class Pizza(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название")
    cheese = models.CharField(max_length=128, blank=True, verbose_name="Сыр")
    pastry = models.CharField(max_length=128, blank=True, verbose_name="Тесто")
    secret_ingredient = models.CharField(max_length=128, blank=True, verbose_name="Секретный ингридиент")
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='restaurant',
        verbose_name="Ресторан"
    )
     
    class Meta:
        verbose_name = "Пицца"
        verbose_name_plural = "Пиццы"

    def __str__(self):
        return f"{self.name}"