from django.urls import reverse

import pytest
from rest_framework import status

from ..serializers import ResumeSerializer


@pytest.mark.django_db
class TestResumeAPI:
    def test_get_list_anonymous_user(self, api_client, resume_factory):
        resume_1, resume_2 = resume_factory(), resume_factory()

        response = api_client.get(reverse('job:resume-list'))
        serialized_data = ResumeSerializer([resume_1, resume_2], many=True).data

        assert response.status_code == status.HTTP_200_OK
        assert response.data == serialized_data

    def test_patch_staff_user(self, api_client, api_auth_staff_user, resume):
        payload = {
            'grade': 0,
            'education': 'Доктор наук',
        }
        response = api_client.patch(reverse('job:resume-detail', args=(resume.id,)), payload)
        resume.refresh_from_db()

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {'status': 'OK'}
        assert resume.grade == payload['grade']
        assert resume.education == payload['education']

    def test_patch_anonymous_user(self, api_client, resume):
        response = api_client.patch(reverse('job:resume-detail', args=(resume.id,)))
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_get_detail_staff_user(self, api_client, api_auth_staff_user, resume):
        response = api_client.get(reverse('job:resume-detail', args=(resume.id,)))
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_post_staff_user(self, api_client, api_auth_staff_user):
        response = api_client.post(reverse('job:resume-list'))
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
