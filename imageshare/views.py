from pyuploadcare import InvalidRequestError
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.http import Http404

from .models import Image


class UploadView(CreateView):
    model = Image


class ImageView(DetailView):
    model = Image

    def get_object(self):
        obj = super(ImageView, self).get_object()
        try:
            if obj.image.is_removed():
                raise ValueError('File was deleted.')
        except (InvalidRequestError, ValueError):
            obj.delete()
            raise Http404

        return obj
