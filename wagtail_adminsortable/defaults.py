"""
Default WagtailAdminSortable configs
"""

from django.conf import settings

DEFAULT_ORDERING_FIELD = 'order'
ORDERING_FIELD = getattr(settings, 'ORDERING_FIELD', DEFAULT_ORDERING_FIELD)
