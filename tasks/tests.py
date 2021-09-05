
from django.http import response
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from tasks.models import Task


class TaskCreateTestCase(APITestCase):

    def test_create_task(self):
        url = reverse('create')
        initial_task_count = Task.objects.count()
        task_attrs = {
            'title': 'New title',
            'complete': False,
            # 'created': '2021-09-02'
        }
        response = self.client.post(url, task_attrs)
        if response.status_code != 201:
            print(response.data)
        self.assertEqual(
            Task.objects.count(),
            initial_task_count +1,
        )
        for attr, expected_value in task_attrs.items():
            self.assertEqual(response.data[attr], expected_value)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TaskListTestCase(APITestCase):
    
    def test_list_tasks(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
      


class TaskDestroyTestCase(APITestCase):
    
    def setUp(self):
        self.task = Task.objects.create(
            title = 'task 1',
            complete = False,
        )
        return super().setUp()

    def test_delete_task(self):
        initial_task_count = Task.objects.count()
        task_id = Task.objects.first().id
        self.client.delete('/api/update/{}/'.format(task_id))
        self.assertEqual(
            Task.objects.count(),
            initial_task_count - 1,
        )
        self.assertRaises(
            Task.DoesNotExist,
            Task.objects.get, id=task_id
        )


class TaskUpdateTestCase(APITestCase):

    def setUp(self):
        self.task = Task.objects.create(
            title = 'task 1',
            complete = False,
        )
        return super().setUp()

    def test_update_task(self):
        task = Task.objects.first()
        response = self.client.patch(
            '/api/update/{}/'.format(task.id),
            {
                'title': 'Updated title',
                'complete': True,
            },
            format = 'json',
        )
        updated = Task.objects.get(id=task.id)
        self.assertEqual(updated.title, 'Updated title')
