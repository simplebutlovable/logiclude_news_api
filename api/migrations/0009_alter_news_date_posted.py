# Generated by Django 3.2 on 2021-04-21 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_news_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]