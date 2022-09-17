# Generated by Django 4.1.1 on 2022-09-16 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Course_reg', '0007_remove_course_users_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course_enroll',
            field=models.ManyToManyField(to='Course_reg.date'),
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course_reg.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course_reg.student')),
            ],
        ),
    ]
