from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Kategoriya nomi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

class NewsImage(models.Model):
    image = models.ImageField(upload_to='news_images/', verbose_name="Rasm")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")

    def __str__(self):
        return f"Rasm {self.id}"

    class Meta:
        verbose_name = "Yangilik rasmi"
        verbose_name_plural = "Yangilik rasmlari"

class News(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='news', verbose_name="Kategoriya")

    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    body = models.TextField(verbose_name="Tavsif")

    image = models.ImageField(upload_to='news_images/', verbose_name="Bosh rasm")
    images = models.ManyToManyField(NewsImage, related_name='news', blank=True, verbose_name="Qo‘shimcha rasmlar")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqt")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"

    def __str__(self):
        return self.title
