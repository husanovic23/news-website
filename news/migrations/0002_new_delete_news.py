# Generated by Django 4.1.3 on 2022-11-29 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sana', models.DateField(auto_created=True, verbose_name='T_sanasi ')),
                ('name', models.CharField(max_length=255, verbose_name='Nomi ')),
                ('lang', models.CharField(choices=[("O'zbek", 'Uzbek'), ('Qozoq', 'Qozoq'), ('Rus', 'Rus'), ('Boshqa', 'Boshqa'), ('-', '-----')], default='-', max_length=255, verbose_name='Tili ')),
                ('news', models.TextField(max_length=1024, verbose_name='Yangilik matni')),
                ('img', models.ImageField(max_length=255, upload_to='', verbose_name='Yangilik rasmi ')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.position')),
            ],
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]