# Generated by Django 4.2.5 on 2023-09-20 13:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("ace_produtos", "0002_marca_produto"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="produto",
            options={"verbose_name": "Produto", "verbose_name_plural": "Produtos-Teste"},
        ),
    ]