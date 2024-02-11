# Generated by Django 4.0.2 on 2024-02-11 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('P/D', '기획/디자인'), ('FE', '프론트엔드'), ('BE', '벡엔드')], default='P/D', max_length=10)),
                ('study_url', models.CharField(max_length=2100, null=True, verbose_name='깃헙/블로그 링크')),
                ('first_q', models.TextField(verbose_name='질문 1')),
                ('second_q', models.TextField(verbose_name='질문 2')),
                ('third_q', models.TextField(verbose_name='질문 3')),
                ('fourth_q', models.TextField(verbose_name='질문 4')),
                ('is_submitted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'apply',
                'managed': False,
            },
        ),
    ]
