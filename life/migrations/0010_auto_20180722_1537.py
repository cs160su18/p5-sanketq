# Generated by Django 2.0.7 on 2018-07-22 22:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('life', '0009_auto_20180722_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shopper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history', models.ManyToManyField(related_name='history_requests_created', to='life.Item')),
                ('shopping_list', models.ManyToManyField(related_name='shoppinglist_requests_created', to='life.Item')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='history',
            name='items',
        ),
        migrations.RemoveField(
            model_name='history',
            name='user',
        ),
        migrations.RemoveField(
            model_name='shopping_list',
            name='items',
        ),
        migrations.RemoveField(
            model_name='shopping_list',
            name='user',
        ),
        migrations.DeleteModel(
            name='History',
        ),
        migrations.DeleteModel(
            name='Shopping_List',
        ),
    ]
