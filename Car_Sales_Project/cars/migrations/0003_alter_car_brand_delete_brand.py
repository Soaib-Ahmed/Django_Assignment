# Generated by Django 4.2.7 on 2023-12-17 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_rename_category_brand'),
        ('cars', '0002_remove_car_quantity_alter_car_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.brand'),
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
    ]
