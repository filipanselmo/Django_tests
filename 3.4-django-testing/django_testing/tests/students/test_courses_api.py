import pytest
from django.urls import reverse
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
    course = course_factory(_quantity=4)
    id_course = course[1].id
    url = reverse('courses-list')
    resp = api_client.get(url)
    resp_json = resp.json()
    resp_ids = {r['id'] for r in resp_json}
    assert resp.status_code == HTTP_200_OK
    assert id_course in resp_ids

@pytest.mark.django_db
def test_name_course(api_client, course_factory):
    course = course_factory(_quantity=4)
    name_course = course[1].name
    url = reverse('courses-list')
    resp = api_client.get(url)
    resp_json = resp.json()
    resp_ids = {r['name'] for r in resp_json}
    assert resp.status_code == HTTP_200_OK
    assert name_course in resp_ids

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