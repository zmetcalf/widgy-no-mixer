from django.conf import settings
from django.db import models

from widgy.db.fields import VersionedWidgyField

class TestModel(models.Model):
    
    def __unicode__(self):
        return self.title
    
    title = VersionedWidgyField (
        site=settings.WIDGY_MEZZANINE_SITE,
        verbose_name='Title',
        related_name='+' ,
    )
    
    form_field = VersionedWidgyField (
        site=settings.WIDGY_MEZZANINE_SITE,
        verbose_name='Test Field',
        related_name='+' ,
    )
