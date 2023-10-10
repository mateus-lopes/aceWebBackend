from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100);
    color = models.CharField(max_length=100, choices=(
        ('bg-primary', 'Azul'),
        ('bg-secondary', 'Cinza'),
        ('bg-green-500', 'Verde'),
        ('bg-red-500', 'Vermelho'),
        ('bg-yellow-500', 'Amarelo'),
        ('bg-indigo-500', 'Indigo'),
        ('bg-purple-500', 'Roxo'),
        ('bg-pink-500', 'Rosa'),
    ));
    url = models.CharField(max_length=100, default='');
    
    def __str__(self):
        return self.title
