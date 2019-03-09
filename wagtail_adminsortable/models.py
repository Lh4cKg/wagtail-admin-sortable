from django.db import models


class AdminSortable(models.Model):
    order = models.IntegerField(null=True, blank=True, editable=False)
    sortable_field = 'order'

    class Meta:
        abstract = True
        ordering = ['order']
