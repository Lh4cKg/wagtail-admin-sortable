from django.views.generic import FormView
from wagtail.contrib.modeladmin.views import IndexView

from .forms import SortableForm
from .mixins import AjaxableResponseMixin


class SortableIndexView(AjaxableResponseMixin, FormView, IndexView):
    form_class = SortableForm

    def get_success_url(self):
        return self.index_url
