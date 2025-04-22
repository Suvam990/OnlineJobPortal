from .models import Category


def global_data(request):
    category = Category.objects.all()

    data={
        'categories':category
    }
    return data