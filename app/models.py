from django.db import models

class Signup(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    Age = models.CharField(max_length=3)
    id = models.CharField(max_length=6, primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=10)
    confirm_password = models.CharField(max_length=10)
    image = models.ImageField(upload_to="profile", default="")

    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = 'Signup'