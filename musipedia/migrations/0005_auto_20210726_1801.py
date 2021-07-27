# Generated by Django 3.2.5 on 2021-07-26 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musipedia', '0004_alter_album_artist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='image/')),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='album', to='musipedia.image'),
        ),
        migrations.AddField(
            model_name='album',
            name='info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='album', to='musipedia.info'),
        ),
        migrations.AddField(
            model_name='artist',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='artist', to='musipedia.image'),
        ),
        migrations.AddField(
            model_name='artist',
            name='info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='artist', to='musipedia.info'),
        ),
        migrations.AddField(
            model_name='song',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='song', to='musipedia.image'),
        ),
        migrations.AddField(
            model_name='song',
            name='info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='song', to='musipedia.info'),
        ),
    ]