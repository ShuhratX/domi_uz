from distutils.command.upload import upload
from django.db import models
from django.utils.text import slugify


class Manufacturer(models.Model):

    class Meta:
        verbose_name = "Ishlab chiqaruvchi"
        verbose_name_plural = "Ishlab chiqaruvchilar"

        db_table = "manufacturers"

    title = models.CharField(max_length=255, verbose_name="Nomi")
    address = models.CharField(max_length=255, verbose_name="Manzili")

    def __str__(self):
        return self.title


class Category(models.Model):

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
        db_table = "categories"
        ordering = ['-id']

    title = models.CharField(max_length=50, verbose_name="Nomi")
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class SubCategory(models.Model):

    class Meta:
        verbose_name = "Subkategoriya"
        verbose_name_plural = "Subkategoriyalar"

        db_table = "subcategories"

    category = models.ForeignKey(Category, verbose_name="Kategoriya", on_delete=models.CASCADE)
    title = models.CharField(max_length=150, verbose_name="Nomi")

    def __str__(self):
        return self.title


class Product(models.Model):

    class Meta:
        verbose_name = "Maxsulot"
        verbose_name_plural = "Maxsulotlar"

        db_table = "products"

    subcategory = models.ForeignKey(SubCategory, verbose_name='Subkategoriya', on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, verbose_name="Ishlab chiqaruvchi", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Nomi')
    image = models.ImageField(verbose_name='Rasm', upload_to="img")
    description = models.TextField(verbose_name='Tafsilotlar', null=True)
    price = models.PositiveIntegerField(verbose_name='Narxi')


class Notebook(Product):

    class Meta:
        verbose_name = "Noutbuk"
        verbose_name_plural = "Noutbuklar"

        db_table = "notebooks"

    diagonal = models.CharField(max_length=255, verbose_name="Diagonal")
    display_type = models.CharField(max_length=255, verbose_name="Displey turi")
    processor_freq = models.CharField(max_length=255, verbose_name="Chastotasi")
    ram = models.CharField(max_length=255, verbose_name="Tezkor xotira")
    rom = models.CharField(max_length=255, null=True, verbose_name="Asosiy xotira")
    videokart = models.CharField(max_length=255, verbose_name="Videokarta")
    time_without_charge = models.CharField(max_length=255, verbose_name="Akkumulyator ishlash vaqti")

    def __str__(self):
        return self.title


class Smartphone(Product):

    class Meta:
        verbose_name = "Smartfon"
        verbose_name_plural = "Smartfonlar"

        db_table = "smartphones"

    diagonal = models.CharField(max_length=255, verbose_name="Diagonal")
    display_type = models.CharField(max_length=255, verbose_name="Displey turi")
    resolution = models.CharField(max_length=255, verbose_name="Ekran o'lchamlari")
    accum_volume = models.CharField(max_length=255, verbose_name="Akkumulyator hajmi")
    ram = models.CharField(max_length=255, verbose_name="Tezkor xotira")
    rom = models.CharField(max_length=255, null=True, verbose_name="Asosiy xotira")
    count_main_cam = models.PositiveIntegerField(verbose_name="Asosiy kameralar soni")
    main_cam_mp = models.CharField(max_length=255, verbose_name="Asosiy kamera")
    front_cam_mp = models.CharField(max_length=255, verbose_name="Frontal kamera")

    def __str__(self):
        return self.title


class Planshet(Product):

    class Meta:
        verbose_name = "Planshet"
        verbose_name_plural = "Planshetlar"

        db_table = "planshets"

    diagonal = models.CharField(max_length=255, verbose_name="Diagonal")
    display_type = models.CharField(max_length=255, verbose_name="Displey turi")
    resolution = models.CharField(max_length=255, verbose_name="Ekran o'lchamlari")
    accum_volume = models.CharField(max_length=255, verbose_name="Akkumulyator hajmi")
    ram = models.CharField(max_length=255, verbose_name="Tezkor xotira")
    rom = models.CharField(max_length=255, null=True, verbose_name="Asosiy xotira")
    main_cam_mp = models.CharField(max_length=255, verbose_name="Asosiy kamera")
    front_cam_mp = models.CharField(max_length=255, verbose_name="Frontal kamera")


class TV_product(Product):
    YEAR_CHOICES = (
        ('2010', '2010'),
        ('2011', '2011'),
        ('2012', '2012'),
        ('2013', '2013'),
        ('2014', '2014'),
        ('2015', '2015'),
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021'),
        ('2022', '2022'),
    )
    diagonal = models.CharField(max_length=50, verbose_name="Diagonal")
    display_type = models.CharField(max_length=50, verbose_name="Displey turi")
    tv_type = models.CharField(max_length=50, verbose_name="Televizor turi")
    wifi = models.BooleanField(default=False, verbose_name="Wifi mavjudligi")
    on_smart = models.BooleanField(default=False, verbose_name="Smart TV")
    on_stereo = models.BooleanField(default=False, verbose_name="Stereo ovoz")
    created_year = models.CharField(max_length=10, verbose_name="Ishlab chiqarilgan yili", choices=YEAR_CHOICES)