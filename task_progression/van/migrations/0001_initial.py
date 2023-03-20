# Generated by Django 4.1.7 on 2023-03-20 09:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Van',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('work_requested', models.TextField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Work_tracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_id', models.UUIDField(default=uuid.uuid4)),
                ('work_progress_percentage', models.IntegerField()),
                ('work_progress_done', models.TextField()),
                ('finish', models.BooleanField(default=False)),
                ('van_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='van.van')),
            ],
        ),
        migrations.CreateModel(
            name='Img_tracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='images/van/')),
                ('van_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='van.van')),
            ],
        ),
    ]
