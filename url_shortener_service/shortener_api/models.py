from django.db import models
from django.utils.translation import ugettext_lazy
from django.utils import timezone
import random
import string
from django.db.models.signals import pre_save


# Table for url detail.
class UrlDetail(models.Model):
    objects = None
    token = models.CharField(ugettext_lazy('URL Token'), max_length=6, db_column='token')
    url = models.TextField(ugettext_lazy('Long URL'), help_text='This is actual URL', db_column='url')
    created_at = models.DateTimeField(ugettext_lazy('Created Date'), default=timezone.now, db_column='created_at')

    def __str__(self):
        return self.token  # Return value from this model.

    class Meta:
        verbose_name_plural = 'Url Detail'  # Table name display in superuser/admin.
        db_table = 'UrlDetail'  # Table name display in database.


def random_string_generator(size=6, chars=string.ascii_uppercase + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_token_generator(instance):
    string_code = random_string_generator()
    token = string_code

    old_record = instance.__class__

    qs_exists = old_record.objects.filter(token=token).exists()
    if qs_exists:
        return unique_token_generator(instance)
    return token


def pre_save_create_token(sender, instance, *args, **kwargs):
    if not instance.token:
        instance.token = unique_token_generator(instance)


pre_save.connect(pre_save_create_token, sender=UrlDetail)
