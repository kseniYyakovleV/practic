# Generated by Django 4.2.3 on 2023-07-04 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_alter_element_sap_number_alter_element_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='name',
            field=models.TextField(null=True),
        ),
    ]
