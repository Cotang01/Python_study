# Generated by Django 5.0.3 on 2024-04-12 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='image567770.png', upload_to='images/'),
        ),
    ]