# Generated by Django 3.2.12 on 2022-05-04 10:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0013_auto_20220503_1739'),
        ('services', '0009_auto_20220504_0118'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecommendedProductPack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='recommended-product-pack')),
                ('title', models.CharField(max_length=100)),
                ('sub_title', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('price', models.IntegerField()),
                ('last_price', models.IntegerField()),
                ('priority', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RecommendedShopPack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='recommended-shop-pack')),
                ('title', models.CharField(max_length=100)),
                ('sub_title', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('price', models.IntegerField()),
                ('last_price', models.IntegerField()),
                ('priority', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='bannerpack',
            name='image',
            field=models.ImageField(upload_to='banner-pack'),
        ),
        migrations.AlterField(
            model_name='smspack',
            name='image',
            field=models.ImageField(upload_to='sms-pack'),
        ),
        migrations.CreateModel(
            name='UsedRecommendedShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('text', models.TextField()),
                ('priority', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('image', models.ImageField(upload_to='banner')),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.shop')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UsedRecommendedProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('text', models.TextField()),
                ('priority', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('image', models.ImageField(upload_to='banner')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartRecommendedShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('recommended_shop_pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.recommendedshoppack')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartRecommendedProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('recommended_product_pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.recommendedproductpack')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='recommended_product_pack',
            field=models.ManyToManyField(blank=True, to='services.CartRecommendedProduct'),
        ),
        migrations.AddField(
            model_name='order',
            name='recommended_shop_pack',
            field=models.ManyToManyField(blank=True, to='services.CartRecommendedShop'),
        ),
    ]
