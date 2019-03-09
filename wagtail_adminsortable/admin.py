from .views import SortableIndexView
from . import defaults

__all__ = ['SortableAdminMixin']


class SortableAdminBase(object):

    view_extra_css = []
    view_extra_js = [
        'js/adminsortable/jquery.ui.touch-punch.min.js',
    ]

    def get_index_view_extra_css(self):
        css = super().get_index_view_extra_css()
        return css + self.view_extra_css

    def get_index_view_extra_js(self):
        js = super().get_index_view_extra_js()
        return js + self.view_extra_js


class SortableAdminMixin(SortableAdminBase):
    sortable = True
    ordering_field = defaults.ORDERING_FIELD

    admin_order_field = ordering_field
    sortable_by = (ordering_field,)

    index_template_name = 'adminsortable/index.html'
    index_view_class = SortableIndexView
