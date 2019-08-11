from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activation',
            name='code',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]