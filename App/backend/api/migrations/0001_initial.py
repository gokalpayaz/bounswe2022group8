# Generated by Django 4.1.2 on 2022-12-24 10:43

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_level2', models.BooleanField(default=False, verbose_name='Level2 user (active)')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('surname', models.CharField(blank=True, max_length=100)),
                ('about', models.TextField(blank=True)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('username', models.CharField(error_messages={'unique': 'User with this username already exists.'}, max_length=100, unique=True)),
                ('email', models.EmailField(error_messages={'unique': 'User with this email already exists.'}, max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile_image', models.ImageField(default='avatar/default.png', upload_to='avatar/')),
                ('profile_path', models.TextField(default='avatar/default.png')),
                ('otp', models.CharField(blank=True, max_length=256, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ArtItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('category', models.CharField(choices=[('AR', 'Architecture'), ('SC', 'Sculpture'), ('SK', 'Sketch'), ('DR', 'Drawing'), ('PT', 'Poster'), ('PH', 'Photography'), ('PR', 'Prints'), ('PA', 'Painting/Acrylic'), ('PO', 'Painting Oilpaint'), ('PW', 'Painting Watercolour'), ('PD', 'Painting Digital'), ('PM', 'Painting Mural'), ('PG', 'Painting Gouache'), ('PP', 'Painting Pastel'), ('PE', 'Painting Encaustic'), ('PF', 'Painting Fresco'), ('PS', 'Painting Spray'), ('OP', 'Painting Other'), ('OT', 'Other')], default='OT', max_length=2)),
                ('artitem_image', models.ImageField(default='artitem/defaultart.jpg', upload_to='artitem/')),
                ('artitem_path', models.TextField(default='artitem/defaultart.jpg')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('number_of_views', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('commented_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('commented_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.artitem')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='api.comment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagname', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='VirtualExhibition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('artitems_gallery', models.ManyToManyField(blank=True, related_name='gallery', to='api.artitem')),
                ('collaborators', models.ManyToManyField(blank=True, related_name='virtualCollaborators', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('poster', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.artitem')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='OfflineExhibition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('collaborators', models.ManyToManyField(blank=True, related_name='offlineCollaborators', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('poster', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.artitem')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='LikeComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_at', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-liked_at'],
            },
        ),
        migrations.CreateModel(
            name='LikeArtItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_at', models.DateTimeField(auto_now_add=True)),
                ('artitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api.artitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-liked_at'],
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='artitem',
            name='tags',
            field=models.ManyToManyField(blank=True, to='api.tag'),
        ),
        migrations.AddField(
            model_name='artitem',
            name='virtualExhibition',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.virtualexhibition'),
        ),
        migrations.AddConstraint(
            model_name='virtualexhibition',
            constraint=models.CheckConstraint(check=models.Q(('end_date__gt', models.F('start_date'))), name='api_virtualexhibition has valid start-end dates.'),
        ),
        migrations.AddConstraint(
            model_name='offlineexhibition',
            constraint=models.CheckConstraint(check=models.Q(('end_date__gt', models.F('start_date'))), name='api_offlineexhibition has valid start-end dates.'),
        ),
        migrations.AddConstraint(
            model_name='likecomment',
            constraint=models.UniqueConstraint(fields=('user', 'comment'), name='api_likecomment_unique_relationships'),
        ),
        migrations.AddConstraint(
            model_name='likeartitem',
            constraint=models.UniqueConstraint(fields=('user', 'artitem'), name='api_likeartitem_unique_relationships'),
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('from_user', 'to_user'), name='api_follow_unique_relationships'),
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.CheckConstraint(check=models.Q(('from_user', models.F('to_user')), _negated=True), name='api_follow_prevent_self_follow'),
        ),
    ]
