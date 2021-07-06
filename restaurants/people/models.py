from django.db import models

class Person(models.Model):
    iin = models.CharField(max_length=14, verbose_name="ИИН")

    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Люди"

    def __str__(self):
        return f"{self.name}"
