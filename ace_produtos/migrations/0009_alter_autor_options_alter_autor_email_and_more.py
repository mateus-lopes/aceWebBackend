# Generated by Django 4.2.5 on 2023-09-22 04:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ace_produtos", "0008_alter_produto_autores"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="autor",
            options={"verbose_name_plural": "Autores"},
        ),
        migrations.AlterField(
            model_name="autor",
            name="email",
            field=models.EmailField(default="sem email", max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="autor",
            name="nome",
            field=models.CharField(max_length=255),
        ),
    ]