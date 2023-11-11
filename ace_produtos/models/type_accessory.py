from django.db import models

class TypeAccessory(models.Model):
    title = models.CharField(max_length=100);
    color = models.CharField(max_length=100, choices=(
        ('bg-blue-dark', 'Azul Escuro'),
        ('bg-blue-light', 'Azul Claro'),
        ('bg-secondary', 'Cinza'),
        ('bg-green', 'Verde'),
        ('bg-red', 'Vermelho'),
        ('bg-yellow', 'Amarelo'),
        ('bg-indigo', 'Indigo'),
        ('bg-purple', 'Roxo'),
        ('bg-pink', 'Rosa'),
        ('bg-purple-escuro', 'Roxo Escuro'),
        ('bg-indigo-blue', 'Indigo Azul'),
        ('bg-pink-dark', 'Rosa Escuro'),
        ('bg-orange', 'Laranja'),
        ('bg-orange-dark', 'Laranja Escuro'),
        ('bg-orange-light', 'Laranja Claro'),
        ('bg-green-light', 'Verde Claro'),
        ('bg-green-dark', 'Verde Escuro'),
        ('bg-green-blue', 'Verde Azul'),
    ));
    url = models.CharField(max_length=100, default='');
    
    
    def __str__(self):
        return self.title
