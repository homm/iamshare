from django.views.generic import DetailView
from django.views.generic.edit import CreateView

from .models import Image


class UploadView(CreateView):
    model = Image


class ImageView(DetailView):
    model = Image
