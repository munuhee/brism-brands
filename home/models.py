from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from PIL import Image
from autoslug import AutoSlugField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django_file_validator.validators import MaxSizeValidator




class Fashion(models.Model):
    title = models.CharField(max_length=100)
    overview = models.CharField(max_length=100,default='Be trendy for every Mood at Braams Fashion Hub')
    description = models.TextField(default='Be trendy for every Mood at Braams Fashion Hub', null=True,blank=True)
    slug = AutoSlugField(unique=True, populate_from='title')
    cover_image = ProcessedImageField(default='2.jpg', upload_to='post_pics', format='JPEG',
                                processors = [ResizeToFill(410,380)],
                                options={ 'quality': 100})
    photo_one =  ProcessedImageField(default='2.jpg', upload_to='post_pics', format='JPEG',
                                processors = [ResizeToFill(500,354)],
                                options={ 'quality': 100})
    photo_two =  ProcessedImageField(default='2.jpg', upload_to='post_pics', format='JPEG',
                                processors = [ResizeToFill(500,354)],
                                options={ 'quality': 100})
    photo_three =  ProcessedImageField(default='2.jpg', upload_to='post_pics', format='JPEG',
                                processors = [ResizeToFill(500,354)],
                                options={ 'quality': 100})
    photo_four =  ProcessedImageField(default='2.jpg', upload_to='post_pics', format='JPEG',
                                processors = [ResizeToFill(500,354)],
                                options={ 'quality': 100})
    
    class Meta:
        verbose_name_plural = "All fashions"


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('fashion-detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Fashion, self).save(*args, **kwargs)

class Graphic(models.Model):
    title = models.CharField(max_length=100)
    overview = models.CharField(max_length=100,default='Be trendy for every Mood at BraamsGraphics')
    description = models.TextField(default='Be trendy for every Mood at Braams Graphics', null=True, blank=True)
    slug = AutoSlugField(unique=True, populate_from='title')
    cover_image = ProcessedImageField(default='2.jpg', upload_to='post_pics', format='JPEG',
                                processors = [ResizeToFill(394,298)],
                                options={ 'quality': 100})
    photo_one =  ProcessedImageField(default='2.jpg', upload_to='post_pics', format='JPEG',
                                processors = [ResizeToFill(300,300)],
                                options={ 'quality': 100})
    photo_two =  ProcessedImageField(default='2.jpg', upload_to='post_pics', format='JPEG',
                                processors = [ResizeToFill(300,300)],
                                options={ 'quality': 100})
    
    class Meta:
        verbose_name_plural = "Graphics"


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('graphic-detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Graphic, self).save(*args, **kwargs)