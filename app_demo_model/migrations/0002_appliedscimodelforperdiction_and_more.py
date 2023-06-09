# Generated by Django 4.1.6 on 2023-02-04 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_demo_model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppliedSciModelForPerdiction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.CharField(max_length=100)),
                ('admission_grade', models.CharField(max_length=5)),
                ('gpa_year_1', models.CharField(max_length=5)),
                ('thai', models.CharField(max_length=5)),
                ('math', models.CharField(max_length=5)),
                ('sci', models.CharField(max_length=5)),
                ('society', models.CharField(max_length=5)),
                ('hygiene', models.CharField(max_length=5)),
                ('art', models.CharField(max_length=5)),
                ('career', models.CharField(max_length=5)),
                ('langues', models.CharField(max_length=5)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='HealthSciModelForPerdiction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.CharField(max_length=100)),
                ('admission_grade', models.CharField(max_length=5)),
                ('gpa_year_1', models.CharField(max_length=5)),
                ('thai', models.CharField(max_length=5)),
                ('math', models.CharField(max_length=5)),
                ('sci', models.CharField(max_length=5)),
                ('society', models.CharField(max_length=5)),
                ('hygiene', models.CharField(max_length=5)),
                ('art', models.CharField(max_length=5)),
                ('career', models.CharField(max_length=5)),
                ('langues', models.CharField(max_length=5)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PureSciModelForPerdiction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.CharField(max_length=100)),
                ('admission_grade', models.CharField(max_length=5)),
                ('gpa_year_1', models.CharField(max_length=5)),
                ('thai', models.CharField(max_length=5)),
                ('math', models.CharField(max_length=5)),
                ('sci', models.CharField(max_length=5)),
                ('society', models.CharField(max_length=5)),
                ('hygiene', models.CharField(max_length=5)),
                ('art', models.CharField(max_length=5)),
                ('career', models.CharField(max_length=5)),
                ('langues', models.CharField(max_length=5)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='appliedscience',
            name='admission_grade',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='appliedscience',
            name='art',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='appliedscience',
            name='career',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='appliedscience',
            name='gpa_year_1',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='appliedscience',
            name='hygiene',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='appliedscience',
            name='langues',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='appliedscience',
            name='major',
            field=models.FloatField(max_length=100),
        ),
        migrations.AlterField(
            model_name='appliedscience',
            name='math',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='appliedscience',
            name='sci',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='appliedscience',
            name='society',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='appliedscience',
            name='status',
            field=models.FloatField(max_length=50),
        ),
        migrations.AlterField(
            model_name='appliedscience',
            name='thai',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='healthscience',
            name='admission_grade',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='healthscience',
            name='art',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='healthscience',
            name='career',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='healthscience',
            name='gpa_year_1',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='healthscience',
            name='hygiene',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='healthscience',
            name='langues',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='healthscience',
            name='major',
            field=models.FloatField(max_length=100),
        ),
        migrations.AlterField(
            model_name='healthscience',
            name='math',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='healthscience',
            name='sci',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='healthscience',
            name='society',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='healthscience',
            name='status',
            field=models.FloatField(max_length=50),
        ),
        migrations.AlterField(
            model_name='healthscience',
            name='thai',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='purescience',
            name='admission_grade',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='purescience',
            name='art',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='purescience',
            name='career',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='purescience',
            name='gpa_year_1',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='purescience',
            name='hygiene',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='purescience',
            name='langues',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='purescience',
            name='major',
            field=models.FloatField(max_length=100),
        ),
        migrations.AlterField(
            model_name='purescience',
            name='math',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='purescience',
            name='sci',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='purescience',
            name='society',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='purescience',
            name='status',
            field=models.FloatField(max_length=50),
        ),
        migrations.AlterField(
            model_name='purescience',
            name='thai',
            field=models.FloatField(max_length=5),
        ),
    ]
