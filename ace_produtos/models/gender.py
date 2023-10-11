from django.db import models

class Gender(models.Model):
    title = models.CharField(max_length=100);
    color = models.CharField(max_length=100, choices=(
        ('bg-blue-900', 'Azul Escuro'),
        ('bg-blue-600', 'Azul Claro'),
        ('bg-green-600', 'Verde'),
        ('bg-red-600', 'Vermelho'),
        ('bg-yellow-600', 'Amarelo'),
        ('bg-indigo-600', 'Indigo'),
        ('bg-purple-600', 'Roxo'),
        ('bg-pink-600', 'Rosa'),
    ));
    url = models.CharField(max_length=100, default='');
    
    
    def __str__(self):
        return self.title
