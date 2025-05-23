# Generated by Django 5.2 on 2025-05-08 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("curriculum", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cv",
            options={
                "ordering": ["created"],
                "verbose_name": "Entrada",
                "verbose_name_plural": "Entradas",
            },
        ),
        migrations.AddField(
            model_name="cv",
            name="image_position",
            field=models.CharField(
                choices=[
                    ("25% 25%", "25% 25%"),
                    ("top center", "Arriba-Centro"),
                    ("center center", "Centro"),
                ],
                default="center center",
                max_length=50,
                verbose_name="Posición de la imagen",
            ),
        ),
        migrations.AddField(
            model_name="cv",
            name="texto_boton",
            field=models.CharField(
                default="Ver más", max_length=100, verbose_name="Texto del botón"
            ),
        ),
    ]
