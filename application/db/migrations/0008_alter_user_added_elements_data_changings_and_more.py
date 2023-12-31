# Generated by Django 4.2.3 on 2023-07-10 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0007_alter_data_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='added_elements',
            field=models.ManyToManyField(related_name='added_elements', through='db.Data', to='db.element'),
        ),
        migrations.CreateModel(
            name='Data_changings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('changed_element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.element')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db.user')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='data_changing_elements',
            field=models.ManyToManyField(related_name='data_changing_elements', through='db.Data_changings', to='db.element'),
        ),
    ]
