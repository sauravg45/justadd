# Generated by Django 2.0.9 on 2018-12-20 06:20

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('duration', models.IntegerField()),
                ('start_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Car_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_model', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_name', models.CharField(max_length=50)),
                ('car_no', models.CharField(max_length=20)),
                ('phone_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='oda.Brand')),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='oda.Car_model')),
            ],
        ),
        migrations.CreateModel(
            name='Pos_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latpos', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lonpos', models.DecimalField(decimal_places=6, max_digits=9)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='oda.Brand')),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='oda.Driver')),
            ],
        ),
        migrations.CreateModel(
            name='Wraptype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wrap_type', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='brand',
            name='wrap_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='oda.Wraptype'),
        ),
    ]
