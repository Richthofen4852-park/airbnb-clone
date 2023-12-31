# Generated by Django 4.2.3 on 2023-08-07 07:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_alter_room_amenities_alter_room_category_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('experiences', '0003_alter_experience_category_alter_experience_host_and_more'),
        ('wishlists', '0002_alter_wishlists_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlists',
            name='experiences',
            field=models.ManyToManyField(related_name='wishlists', to='experiences.experience'),
        ),
        migrations.AlterField(
            model_name='wishlists',
            name='rooms',
            field=models.ManyToManyField(related_name='wishlists', to='rooms.room'),
        ),
        migrations.AlterField(
            model_name='wishlists',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlists', to=settings.AUTH_USER_MODEL),
        ),
    ]
