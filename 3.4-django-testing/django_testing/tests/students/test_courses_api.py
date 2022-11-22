import pytest
from django.urls import reverse
import random
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_one_course(api_client, course_factory):
    course = course_factory()
    url = reverse('courses-detail', args=(course.id, ))
    resp = api_client.get(url)
    assert resp.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_list_course(api_client, course_factory):
    url = reverse('courses-list')
    course = course_factory(_quantity=4)
    resp = api_client.get(url)
    assert resp.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_id_course(api_client, course_factory):
    courses = course_factory(_quantity=4)
    random_course = random.choice(courses)
    url = reverse('courses-list')
    response = api_client.get(f'{url}?id={random_course.id}')
    assert response.status_code == HTTP_200_OK
    data = response.json()
    assert len(data) == 1
    assert random_course.name == data[0]['name']


@pytest.mark.django_db
def test_name_course(api_client):
    url = reverse('courses-list')
    course = api_client.post(url, data={'name': 'test_course'})
    data = course.json()
    response = api_client.get('/api/v1/courses/?name=test_course')
    assert response.status_code == HTTP_200_OK
    assert data['name'] == 'test_course'


@pytest.mark.django_db
def test_create_course(api_client, course_factory):
    url = reverse('courses-list')
    course = {'name': 'test',
              'students': [],
    }
    resp = api_client.post(url, course, format='json',)
    assert resp.status_code == HTTP_201_CREATED


@pytest.mark.django_db
def test_path_course(api_client, course_factory):
    course = course_factory()
    url = reverse('courses-detail', args=(course.id, ))
    course = {'name': 'test',
              }
    resp = api_client.patch(url, content_type='application/json')
    assert resp.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_delete_course(api_client, course_factory):
    course = course_factory()
    url = reverse('courses-detail', args=(course.id, ))
    resp = api_client.delete(url, course, content_type='application/json')
    assert resp.status_code == HTTP_204_NO_CONTENT


