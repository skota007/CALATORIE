# Generated by Django 3.1.5 on 2021-03-17 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buna', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='gara',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod', models.CharField(max_length=3)),
                ('oras', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='calatorie',
            name='destinatie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vine', to='buna.gara'),
        ),
        migrations.AlterField(
            model_name='calatorie',
            name='origine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plecari', to='buna.gara'),
        ),
    ]
