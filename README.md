# wagtail-admin-sortable

Generic drag-and-drop ordering for objects in the Wagtail admin interface

### Quick Start

Install **wagtail_adminsortable** via PyPi

```bash
$ pip install wagtail_adminsortable
```

or via Github for latest version

```bash
$ pip install git+https://github.com/Lh4cKg/wagtail-admin-sortable

```

Add `wagtail_adminsortable` and `wagtail.contrib.modeladmin,` to `INSTALLED_APPS` in `settings.py` for your Django project:

```python
INSTALLED_APPS = [
  ...
  'wagtail.contrib.modeladmin',
  'wagtail_adminsortable',
]

```

##### Integrate your models

```python
from django.db import models
from modelcluster.models import ClusterableModel
from wagtail_adminsortable.models import AdminSortable


class Category(AdminSortable, ClusterableModel):
    title = models.CharField('Title', max_length=255, null=True, blank=True)

    class Meta(AdminSortable.Meta):
        verbose_name = "Category"
        verbose_name_plural = "Categories"
```

##### or

```python
from django.db import models
from modelcluster.models import ClusterableModel


class Category(ClusterableModel):
    title = models.CharField('Title', max_length=255, null=True, blank=True)
    my_order = models.IntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ['my_order']
        verbose_name = "Category"
        verbose_name_plural = "Categories"
```

##### and define ORDERING_FIELD in settings.py

```python
ORDERING_FIELD = 'my_order'
```

##### Integrate into a list view

###### In wagtail_hooks.py (in your app directory), add a mixin class to augment the functionality for sorting (be sure to put the mixin class before ModelAdmin):

```python
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail_adminsortable.admin import SortableAdminMixin


class CategoryAdmin(SortableAdminMixin, ModelAdmin):
    model = YourModel

modeladmin_register(CategoryAdmin)
```

##### License

Copyright &copy; 2019 Lasha Gogua.

MIT licensed.
