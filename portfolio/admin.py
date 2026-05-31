from django.contrib import admin
from django.utils.html import format_html
from .models import Skill, Qualification, Project, Contact, Resume, ContactMessage, SiteSettings, AboutSection


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'thumbnail')
    readonly_fields = ('thumbnail',)
    fieldsets = (
        (None, {
            'fields': ('name', 'image', 'description', 'tags', 'thumbnail')
        }),
    )

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width:64px;height:auto;object-fit:cover;"/>', obj.image.url)
        return '-'

    thumbnail.short_description = 'Image'


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail', 'technology')
    readonly_fields = ('thumbnail',)
    fieldsets = (
        (None, {
            'fields': ('title', 'image', 'description', 'technology', 'tags', 'thumbnail')
        }),
    )

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width:64px;height:auto;object-fit:cover;"/>', obj.image.url)
        return '-'

    thumbnail.short_description = 'Image'


admin.site.register(Qualification)
admin.site.register(Contact)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'updated_at')
    readonly_fields = ('updated_at',)
    fields = (
        'site_name',
        'navbar_logo',
        'hero_image',
        'hero_name',
        'hero_subtitle',
        'hero_description',
        'updated_at',
    )
    search_fields = ('site_name', 'hero_name')


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    readonly_fields = ('updated_at',)
    fields = (
        'title',
        'description',
        'image',
        'tags',
        'updated_at',
    )
    search_fields = ('title',)


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at', 'active')
    list_editable = ('active',)
    ordering = ('-uploaded_at',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submitted_at')
    readonly_fields = ('submitted_at',)
    search_fields = ('name', 'email', 'subject', 'message')
    ordering = ('-submitted_at',)
