# Generated by Django 2.1.5 on 2019-01-23 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jewelry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jew_name', models.CharField(max_length=10)),
                ('description', models.TextField(max_length=100)),
                ('artist_name', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JewelryType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Necklace'), (2, 'Ring'), (3, 'Piercing'), (4, 'Other')])),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('jew_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_app.JewelryType')),
                ('jewelry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_app.Jewelry')),
            ],
        ),
    ]