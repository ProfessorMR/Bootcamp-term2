# Generated by Django 5.0.7 on 2024-08-06 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_transactions_transaction'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'حساب', 'verbose_name_plural': 'حساب ها'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.AlterModelOptions(
            name='transaction',
            options={'verbose_name': 'تراکنش', 'verbose_name_plural': 'تراکنش ها'},
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('1', 'واریزی'), ('2', 'برداشتی')], default='1', max_length=1, verbose_name='نوع'),
            preserve_default=False,
        ),
    ]
