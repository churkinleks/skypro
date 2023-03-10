import pytest
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def api_auth_staff_user(api_client, user_factory):
    new_superuser = user_factory(is_staff=True)
    api_client.force_login(new_superuser)
    return new_superuser
