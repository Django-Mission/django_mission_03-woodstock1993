# Generated by Django 4.0.4 on 2022-05-03 15:21

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('A', 'category A'), ('B', 'category B'), ('C', 'category C'), ('D', 'category D')], default='others', max_length=256)),
                ('inquiry_status', models.CharField(choices=[('register', 'Register'), ('register_complete', 'Register Complete'), ('complete', 'Complete')], max_length=20)),
                ('question', models.CharField(max_length=80, verbose_name='문의 질문')),
                ('comment', models.TextField(verbose_name='문의 내용')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='작성자 이메일')),
                ('phone_number', models.CharField(blank=True, help_text='format: 010-1234-1234', max_length=13, null=True, validators=[django.core.validators.RegexValidator('^01([0|1|6|7|8|9]?)-([0-9]{3,4})-([0-9]{4})', message='Wrong format enter')], verbose_name='전화번호')),
                ('is_email', models.BooleanField(blank=True, default=False, null=True, verbose_name='이메일 수신 여부')),
                ('is_phone', models.BooleanField(blank=True, default=False, null=True, verbose_name='문자 메세지 수신 여부')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='최종 수정일')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='이미지')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inquiry_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inquiry_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='답변 내용')),
                ('created_at', models.DateTimeField(verbose_name='생성 일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='최종 수정 일시')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_created_by', to=settings.AUTH_USER_MODEL)),
                ('question_answer', models.ForeignKey(db_column='Inquiry_id', on_delete=django.db.models.deletion.CASCADE, to='support.inquiry')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_updated_by', to=settings.AUTH_USER_MODEL)),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]