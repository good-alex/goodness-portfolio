from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='skills/', blank=True, null=True)
    description = models.TextField(blank=True, default='')
    tags = models.CharField(max_length=200, blank=True, default='')

    def __str__(self):
        return self.name


class Qualification(models.Model):
    title = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    year = models.IntegerField()

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True, default='')

    def __str__(self):
        return self.title


class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.email


class Resume(models.Model):
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.file.name.split('/')[-1]


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f'{self.name} - {self.subject}'


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100, default='Muhindi')
    navbar_logo = models.ImageField(upload_to='navbar/', blank=True, null=True)
    hero_image = models.ImageField(upload_to='hero/', blank=True, null=True)
    hero_name = models.CharField(max_length=100, blank=True, default='Muhindi John')
    hero_subtitle = models.CharField(max_length=200, blank=True, default='Data Science')
    hero_description = models.TextField(
        blank=True,
        default='I’m a passionate front-end developer with one year of professional experience building modern, responsive web applications. I specialize in React.js, Next.js, HTML5, CSS3, Bootstrap, and GitHub.'
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Site Setting'
        verbose_name_plural = 'Site Settings'
        ordering = ['-updated_at']

    def __str__(self):
        return self.site_name or 'Site Setting'


class AboutSection(models.Model):
    title = models.CharField(max_length=200, blank=True, default='Data Science with 1 Year of Experience')
    description = models.TextField(
        blank=True,
        default='I’m a dedicated front-end developer with one year of experience creating professional, responsive web applications. My work focuses on delivering polished user interfaces and seamless user experiences using modern web technologies.'
    )
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    tags = models.CharField(max_length=400, blank=True, default='React.js,Next.js,Bootstrap,JavaScript,CSS3,HTML5')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'About Section'
        verbose_name_plural = 'About Sections'
        ordering = ['-updated_at']

    def __str__(self):
        return self.title or 'About Section'
