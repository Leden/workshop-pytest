from shorts.models import ShortUrl
import random

import pytest
import factory
import pytest_factoryboy
from django.contrib.auth import get_user_model


@pytest_factoryboy.register
class ShortUrlFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ShortUrl

    code = factory.LazyFunction(lambda: ''.join(random.choice('012345678') for _ in range(4)))


@pytest.fixture()
def short_url_factory():
    return ShortUrlFactory


@pytest.fixture()
def short_url__code():
    return '1245'


@pytest.fixture()
def short_url(short_url__code, short_url_factory):
    return short_url_factory(code=short_url__code)


@pytest.fixture()
def url(short_url):
    return short_url


@pytest.mark.django_db
@pytest.mark.parametrize('short_url__code', ['1234'])
def test_create_short_url(url):
    assert url.code == '1234'


@pytest.mark.django_db
def test_short_url_code_autogenerates(url):
    assert url.code is not None
    assert url.code != ''


@pytest.mark.django_db
def test_url_codes_differ(short_url_factory):
    url_1 = short_url_factory()
    url_2 = short_url_factory()
    assert url_1.code != url_2.code
