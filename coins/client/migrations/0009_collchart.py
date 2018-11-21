# Generated by Django 2.1.2 on 2018-10-26 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0008_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collchart',
            fields=[
                ('collchartid', models.AutoField(db_column='CollChartID', primary_key=True, serialize=False)),
                ('collchartdesc', models.CharField(db_column='CollChartDesc', max_length=45)),
                ('collchartremarks', models.TextField(blank=True, db_column='CollChartRemarks', null=True)),
            ],
            options={
                'db_table': 'collchart',
                'managed': False,
            },
        ),
    ]
