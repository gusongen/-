from django.forms import modelformset_factory, BaseModelFormSet

from .models import Image


class BaseMultiImageFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queryset = Image.objects.none()


MultiImageForm = modelformset_factory(Image, fields=('file',), formset=BaseMultiImageFormSet)
