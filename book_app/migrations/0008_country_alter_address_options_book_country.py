# Generated by Django 4.0.1 on 2022-08-31 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0007_address_alter_book_slug_author_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=3)),
            ],
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'author addresses'},
        ),
        migrations.AddField(
            model_name='book',
            name='country',
            field=models.ManyToManyField(to='book_app.Country'),
        ),
    ]
