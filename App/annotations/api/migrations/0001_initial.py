# Generated by Django 4.1.2 on 2022-12-25 10:05

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FragmentSelector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('conformsTo', models.TextField(blank=True, default='http://www.w3.org/TR/media-frags/')),
            ],
        ),
        migrations.CreateModel(
            name='Motivation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivation', models.TextField(choices=[('assessing', 'Assessing'), ('bookmarking', 'Bookmarking'), ('classifying', 'Classifying'), ('commenting', 'Commenting'), ('describing', 'Describing'), ('editing', 'Editing'), ('highlighting', 'Highlighting'), ('identifying', 'Identifying'), ('linking', 'Linking'), ('moderating', 'Moderating'), ('questioning', 'Questioning'), ('replying', 'Replying'), ('tagging', 'Tagging')], unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Selector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fragmentSelector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.fragmentselector')),
            ],
        ),
        migrations.CreateModel(
            name='TextPositionSelector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.BigIntegerField()),
                ('end', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TextQuoteSelector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exact', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(choices=[('Annotation', 'Annotation'), ('Image', 'Image'), ('Text', 'Text'), ('Dataset', 'Dataset'), ('Sound', 'Sound'), ('Video', 'Vidoe'), ('TextualBody', 'Textualbody')], unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.TextField()),
                ('format', models.TextField(blank=True)),
                ('language', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), blank=True, null=True, size=None)),
                ('selector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.selector')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.type', to_field='type')),
            ],
        ),
        migrations.AddField(
            model_name='selector',
            name='textPositionSelector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.textpositionselector'),
        ),
        migrations.AddField(
            model_name='selector',
            name='textQuoteSelector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.textquoteselector'),
        ),
        migrations.CreateModel(
            name='Body',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('format', models.TextField(default='text/plain')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.creator')),
                ('purpose', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.motivation', to_field='motivation')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.type', to_field='type')),
            ],
        ),
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('context', models.TextField(default='http://www.w3.org/ns/anno.jsonld')),
                ('creator', models.BigIntegerField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('body', models.ManyToManyField(to='api.body')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.target')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.type', to_field='type')),
            ],
        ),
    ]
