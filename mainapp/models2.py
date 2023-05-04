from django.db import models


class Company(models.Model):
    name_company = models.CharField(max_length=127)
    logo = models.ImageField(upload_to='company/', blank=True)
    description = models.TextField(verbose_name='Описание', blank=True) 
    telegram = models.URLField(verbose_name='Telegram')
    whatsapp = models.URLField(verbose_name='Whatsapp')

    @property
    def event_amount(self):
        return self.events.count()
    
    @property
    def job_amount(self):
        return self.jobs.count()
    
    @property
    def video_amount(self):
        return self.video.count()


class Jobs(models.Model):
    position = models.CharField(max_length=127)
    salary = models.CharField(max_length=127)
    type = models.CharField(max_length=127)
    name_company = models.ForeignKey(
        Company, on_delete=models.CASCADE,
        related_name='jobs'
    )

class Events(models.Model):
    location = models.CharField(max_length=127)
    date = models.DateTimeField(verbose_name='Дата и время')
    website = models.URLField(verbose_name='Ссылка к сайту')
    registration = models.URLField(verbose_name='Регистрация')
    description = models.TextField(verbose_name='Описание')
    name = models.CharField(max_length=127)
    image = models.ImageField(upload_to='events/') 
    name_company = models.ForeignKey(
        Company, on_delete=models.CASCADE,
        related_name='events'
    )

class Video(models.Model):
    video = models.URLField(verbose_name='Ссыллка на видео')
    date = models.DateTimeField(verbose_name='Дата и время')
    name = models.CharField(max_length=127)
    preview = models.ImageField(max_length=127)
    description = models.TextField(verbose_name='Описание')
    name_company = models.ForeignKey(
        Company, on_delete=models.CASCADE,
        related_name='video'
    )