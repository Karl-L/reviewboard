import datetime

from django.core.cache import cache
from django.db.models import signals
from djblets.util.misc import make_cache_key

from reviewboard.admin.widgets import CACHED_WIDGETS


def _delete_widget_cache(*args, **kwargs):
    """Clear the cache to keep the admin dashboard up to date."""
    timestamp = str(datetime.date.today())

    cache.delete_many([make_cache_key('%s-%s' % (widget, timestamp))
                       for widget in CACHED_WIDGETS])


signals.post_save.connect(_delete_widget_cache)
signals.post_delete.connect(_delete_widget_cache)
