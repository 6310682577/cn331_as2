# Generated by Django 4.1.1 on 2022-09-16 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course_reg', '0011_enrollment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course_enroll',
            field=models.ManyToManyField(related_name='student', to='Course_reg.date'),
        ),
        migrations.DeleteModel(
            name='Enrollment',
        ),
    ]
