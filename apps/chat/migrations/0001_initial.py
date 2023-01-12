# Generated by Django 4.1.5 on 2023-01-11 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'chat',
                'verbose_name_plural': 'Chats',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=500)),
                ('files', models.FileField(blank=True, upload_to='')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('chat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_id', to='chat.chat')),
            ],
            options={
                'verbose_name': 'message',
                'verbose_name_plural': 'Messages',
                'ordering': ('-timestamp',),
            },
        ),
    ]
