# Generated by Django 2.0.7 on 2018-07-22 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0008_history_shopping_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='items',
            field=models.ManyToManyField(to='life.Item'),
        ),
    ]