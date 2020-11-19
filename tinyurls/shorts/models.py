from django.db import models
import random

import string

from django.contrib.auth import get_user_model


alphabet = string.digits + string.ascii_letters

def generate_code():
    return ''.join(random.choice(alphabet) for _ in range(8))


class ShortUrl(models.Model):
    code = models.CharField(max_length=8, default=generate_code)
    full = models.URLField()

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)

