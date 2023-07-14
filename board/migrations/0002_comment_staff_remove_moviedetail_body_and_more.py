# Generated by Django 4.2.1 on 2023-07-14 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('role', models.CharField(max_length=100, null=True)),
                ('image_url', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='moviedetail',
            name='body',
        ),
        migrations.RemoveField(
            model_name='moviedetail',
            name='date',
        ),
        migrations.RemoveField(
            model_name='moviedetail',
            name='title',
        ),
        migrations.AddField(
            model_name='moviedetail',
            name='genre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='moviedetail',
            name='poster_url',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='moviedetail',
            name='rate',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='moviedetail',
            name='rating_aud',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='moviedetail',
            name='rating_cri',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='moviedetail',
            name='rating_net',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='moviedetail',
            name='release_date',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='moviedetail',
            name='showtimes',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='moviedetail',
            name='summary',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='moviedetail',
            name='title_eng',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='moviedetail',
            name='title_kor',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
