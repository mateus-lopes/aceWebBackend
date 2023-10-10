from django.db import models

class Gender(models.Model):
    title = models.CharField(max_length=100);
    color = models.CharField(max_length=100, default='Branco', choices=(
        ('bg-primary', 'Azul'),
        ('bg-cinza', 'Cinza'),
        ('bg-verde', 'Verde'),
        ('bg-vermelho', 'Vermelho'),
        ('bg-amarelo', 'Amarelo'),
        ('bg-azul-claro', 'Azul Claro'),
        ('bg-white', 'Branco'),
        ('bg-dark', 'Preto'),
    ));
    url = models.CharField(max_length=100, default='');
    
    
    def __str__(self):
        return self.title
