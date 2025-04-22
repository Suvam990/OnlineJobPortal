from django.shortcuts import render, get_object_or_404, redirect
from .models import Job, Application,Category
from .forms import ApplicationForm
from django.http import HttpResponse
from django.db.models import Q

# adding



def index(request):
    search = request.GET.get('search')  # Use get() to safely retrieve the 'search' parameter

    if search:
        jobs = Job.objects.filter(
            Q(title__icontains=search) |  # Search for matching title (case-insensitive)
            Q(description__icontains=search)  # Or search for matching description (case-insensitive)
        )
        return render(request, 'index.html', {'jobs': jobs})
    else:
        jobs = Job.objects.all()
        return render(request, 'index.html', {'jobs': jobs})

def apply_for_job(request,slug):
    job = get_object_or_404(Job, slug=slug)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.user = request.user 
            application.save()
            return redirect('job_list')  
    else:
        form = ApplicationForm()
    
    return render(request, 'apply_for_job.html', {'form': form, 'job': job})


def category_jobs(request, slug):
    category = Category.objects.get(slug=slug)
    job = Job.objects.filter(category=category)
    return render(request, 'category_jobs.html', {'jobs': job, 'category': category})

def home(request):
    job = Job.objects.all()
    return render(request, 'index.html', {'jobs': job})


    