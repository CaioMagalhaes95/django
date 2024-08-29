# todo_app/tests.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task

class TaskAPITests(APITestCase):
    
    def setUp(self):
        # Cria tarefas iniciais para os testes
        self.task1 = Task.objects.create(title='Task 1', description='Description 1', completed=False, category='6601', test_count=1)
        self.task2 = Task.objects.create(title='Task 2', description='Initial Description', completed=True, category='7051', test_count=2)
        self.task3 = Task.objects.create(title='Initial Task 3', description='Description 3', completed=False, category='8849', test_count=3)
    
    def test_create_task(self):
        url = reverse('task-list')
        data = {'title': 'New Task', 'description': 'New Description', 'completed': False, 'category': '6601', 'test_count': 1}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 4)
        self.assertEqual(Task.objects.get(id=response.data['id']).title, 'New Task')
    
    def test_read_task_list(self):
        url = reverse('task-list')
        response = self.client.get(url, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['title'], 'Task 1')
    
    def test_read_single_task(self):
        url = reverse('task-detail', args=[self.task1.id])
        response = self.client.get(url, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Task 1')
    
    def test_update_task(self):
        url = reverse('task-detail', args=[self.task1.id])
        data = {'title': 'Updated Task', 'description': 'Updated Description', 'completed': True, 'category': '6601', 'test_count': 2}
        response = self.client.put(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.title, 'Updated Task')
        self.assertTrue(self.task1.completed)
    
    def test_delete_task(self):
        url = reverse('task-detail', args=[self.task1.id])
        response = self.client.delete(url, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 2)
    
    def test_filter_tasks_by_completed(self):
        url = reverse('task-list')
        response = self.client.get(url, {'completed': True}, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Task 2')
    
    def test_search_tasks_by_word(self):
        url = reverse('task-list')
        response = self.client.get(url, {'search': 'Initial'}, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], 'Task 2')
        self.assertEqual(response.data[1]['title'], 'Initial Task 3')
    
    def test_filter_tasks_by_category(self):
        url = reverse('task-list')
        response = self.client.get(url, {'category': '6601'}, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Task 1')
    
    def test_filter_tasks_by_test_count(self):
        url = reverse('task-list')
        response = self.client.get(url, {'test_count': 2}, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Task 2')
