from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100);
    color = models.CharField(max_length=100, choices=(
        ('bg-blue-dark', 'Azul Escuro'),
        ('bg-blue-light', 'Azul Claro'),
        ('bg-secondary', 'Cinza'),
        ('bg-green', 'Verde'),
        ('bg-red', 'Vermelho'),
        ('bg-yellow-300', 'Amarelo'),
        ('bg-indigo-400', 'Indigo'),
        ('bg-purple-400', 'Roxo'),
        ('bg-pink', 'Rosa'),
    ));
    url = models.CharField(max_length=100, default='');
    
    def __str__(self):
        return self.title
