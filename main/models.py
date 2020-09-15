from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class Settings(models.Model):
    about_content = RichTextField()
    about_video = models.FileField(upload_to ='document/video')
    contact_fax = models.TextField()
    contact_phone = models.TextField()
    contact_email = models.TextField()
    contact_address = models.CharField(max_length = 300)
    document_title = models.CharField(max_length = 200)
    document_content = RichTextField()
    document_image = models.ImageField(upload_to ='document/images')

    class Meta:
        verbose_name        = 'settings'
        verbose_name_plural = 'settings'

    def __str__(self):
        return self.document_title

class News(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images', default="")
    image_blur = models.ImageField(upload_to='images_blur', default='')
    thumbnail = models.ImageField(upload_to='news/thumbnail', default='')
    show = models.BooleanField(default=True)
    content = RichTextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Magazine(models.Model):
    title = models.CharField(max_length=50)
    pdf_file = models.FileField(upload_to='magazines/pdf_files')
    thumbnail = models.ImageField(upload_to='magazines/thumbnail')
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'magazine'
        verbose_name_plural = 'magazines'

    def __str__(self):
        return self.title

class Gallery(models.Model):
    image = models.ImageField(upload_to ='images')
    image_crop = models.ImageField(upload_to='images_crop', null = True, blank = True)
    thumbnail = models.ImageField(upload_to='thumbnail', null = True, blank = True)
    date = models.DateTimeField(default = timezone.now)
    created_date = models.DateTimeField(default = timezone.now)

    class Meta:
        verbose_name        = 'gallery'
        verbose_name_plural = 'gallery'

    def __str__(self):
        return self.image.name

class Tender(models.Model):
    title = models.CharField(max_length=900)
    content = RichTextField()
    show = models.BooleanField(default=True)
    image = models.ImageField(upload_to='tender/images')
    image_crop = models.ImageField(upload_to='tender/images_crop')
    thumbnail = models.ImageField(upload_to='tender/thumbnail')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'tender'
        verbose_name_plural = 'tenders'

    def __str__(self):
        return self.title

class Factory(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField(default='')
    thumbnail = models.ImageField(upload_to='factory/thumbnail')
    video = models.FileField(upload_to='factory/video', null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'factory'
        verbose_name_plural = 'factory'

    def __str__(self):
        return self.title

class AssocationContacts(models.Model):
    name        = models.CharField(max_length = 200)
    address     = models.CharField(max_length = 200)
    phone       = models.TextField()
    fax         = models.TextField()
    date        = models.DateTimeField(default = timezone.now)
    create_ts   = models.DateTimeField(default = timezone.now)

    class Meta:
        verbose_name        = 'associations contact'
        verbose_name_plural = 'associations contacts'

    def __str__(self):
        return self.name

class Contact_us(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return self.fullname