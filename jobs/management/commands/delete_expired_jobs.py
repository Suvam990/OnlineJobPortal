from django.core.management.base import BaseCommand
from jobs.models import Job
from django.utils import timezone

class Command(BaseCommand):
    help = 'Delete expired jobs from the database'

    def handle(self, *args, **kwargs):
        expired_jobs = Job.objects.filter(expire_date__lt=timezone.now(), status='active')
        deleted_count, _ = expired_jobs.delete()  # Delete expired jobs
        self.stdout.write(f"{deleted_count} expired job(s) deleted.")
