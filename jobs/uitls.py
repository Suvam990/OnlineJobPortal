from django.utils.text import slugify
import uuid
from .models import Category

def generate_slug(title: str, category) -> str:
    # Generate the base slug from the title
    slug = slugify(title)
    
    # Check if the slug already exists and make it unique
    while Category.objects.filter(slug=slug).exists():
        slug = f'{slug}-{str(uuid.uuid4())[:5]}'  # Append random string to ensure uniqueness

    return slug