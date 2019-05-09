# Generated by Django 2.2.1 on 2019-05-08 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storeproject', '0003_auto_20190507_2142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caritme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, verbose_name='数量')),
                ('sum_price', models.FloatField(default=0.0, verbose_name='小计')),
                ('clothing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storeproject.Goods', verbose_name='购物车中产品条目')),
            ],
            options={
                'verbose_name': '购物车条目',
                'verbose_name_plural': '购物车条目',
            },
        ),
    ]
