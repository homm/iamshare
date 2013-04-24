from django.views.generic.edit import CreateView

from .models import Image


class UploadView(CreateView):
    model = Image
