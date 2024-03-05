from django.template import Library
from django.forms.utils import flatatt
from django.utils.safestring import mark_safe
from django.contrib.admin.templatetags.admin_list import result_headers
from wagtail_modeladmin.templatetags.modeladmin_tags import results

register = Library()


@register.inclusion_tag("adminsortable/includes/result_list.html",
                        takes_context=True)
def sortable_result_list(context):
    """
    Displays the headers and data list together
    """
    request = context['request']
    view = context['view']
    object_list = context['object_list']
    headers = list(result_headers(view))
    num_sorted_fields = 0
    for h in headers:
        if h['sortable'] and h['sorted']:
            num_sorted_fields += 1
    context.update({
        'result_headers': headers,
        'num_sorted_fields': num_sorted_fields,
        'results': list(results(view, object_list, request))})
    return context


@register.inclusion_tag(
    "modeladmin/includes/result_row.html", takes_context=True)
def sortable_result_row_display(context, index):
    obj = context['object_list'][index]
    view = context['view']
    row_attrs_dict = view.model_admin.get_extra_attrs_for_row(obj, context)
    row_attrs_dict['data-object-pk'] = obj.pk
    row_attrs_dict['class'] = 'wagtail-admin-sortable'
    odd_or_even = 'odd' if (index % 2 == 0) else 'even'
    if 'class' in row_attrs_dict:
        row_attrs_dict['class'] += ' %s' % odd_or_even
    else:
        row_attrs_dict['class'] = odd_or_even

    context.update({
        'obj': obj,
        'row_attrs': mark_safe(flatatt(row_attrs_dict)),
        'action_buttons': view.get_buttons_for_obj(obj),
    })
    return context
