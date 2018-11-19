# Generated by Django 2.1.3 on 2018-11-19 14:12

from django.db import migrations, models
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=tagging.fields.TagField(blank=True, help_text='tag', max_length=255, verbose_name='Test'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='post_images', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(upload_to='post_images', verbose_name='Image'),
        ),
    ]