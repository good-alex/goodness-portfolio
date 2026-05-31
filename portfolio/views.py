from rest_framework import generics
from .models import Skill, Qualification, Project, Contact, Resume, ContactMessage, SiteSettings, AboutSection
from .serializers import (
    SkillSerializer,
    QualificationSerializer,
    ProjectSerializer,
    ContactSerializer
)

from django.contrib import messages
from django.http import FileResponse, Http404
from django.shortcuts import redirect, render


# API Views

class SkillList(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class QualificationList(generics.ListAPIView):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer


class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ContactList(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# Frontend View

def home(request):
    skills = list(Skill.objects.all())
    if not skills:
        skills = [
            Skill(name='Django'),
            Skill(name='Bootstrap'),
            Skill(name='JavaScript'),
        ]

    projects = list(Project.objects.all())
    if not projects:
        projects = [
            Project(title='Portfolio Website', description='A modern, responsive portfolio website built with Django and Bootstrap.', technology='React'),
            Project(title='E-Commerce Platform', description='Full-stack e-commerce application with payment integration and admin dashboard.', technology='Next.js'),
            Project(title='Task Management App', description='Real-time task management application with user authentication and team collaboration.', technology='Node.js'),
        ]

    qualifications = Qualification.objects.all()
    contacts = Contact.objects.all()
    site_settings = SiteSettings.objects.order_by('-updated_at').first()
    about_section = AboutSection.objects.order_by('-updated_at').first()

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message_text = request.POST.get('message', '').strip()

        if not name or not email or not subject or not message_text:
            messages.error(request, 'Please fill in all contact fields before sending.')
        else:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message_text,
            )
            messages.success(request, 'Your message has been sent successfully.')
            return redirect('home')

    about_tags = []
    if about_section and about_section.tags:
        about_tags = [tag.strip() for tag in about_section.tags.split(',') if tag.strip()]

    return render(request, 'portfolio/index.html', {
        'skills': skills,
        'projects': projects,
        'qualifications': qualifications,
        'contacts': contacts,
        'site_settings': site_settings,
        'about_section': about_section,
        'about_tags': about_tags,
    })


def download_resume(request):
    resume = Resume.objects.filter(active=True).order_by('-uploaded_at').first()
    if not resume:
        resume = Resume.objects.order_by('-uploaded_at').first()

    if not resume:
        raise Http404('No resume has been uploaded yet.')

    filename = resume.file.name.split('/')[-1]
    return FileResponse(resume.file.open('rb'), as_attachment=True, filename=filename)
