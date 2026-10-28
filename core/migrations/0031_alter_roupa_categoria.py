from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_roupa_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roupa',
            name='categoria',
            field=models.ManyToManyField(blank=True, related_name='roupas', to='core.categoria'),
        ),
    ]
