# Generated by Django 4.1.7 on 2023-03-20 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('van', '0002_rename_customer_id_van_customer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='img_tracking',
            old_name='van_id',
            new_name='van',
        ),
    ]
