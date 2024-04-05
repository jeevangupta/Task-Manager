
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from .models import Tasks
import pdb

class CreateTaskTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_task_success(self):
        # Prepare POST data
        data = {
            'taskTitle': 'Test Task',
            'taskDescription': 'This is a test task',
            'taskStatus': 'To Do'
        }

        # Send POST request to create_task view
        response = self.client.post(reverse('create-task'), data)

        # Check if task was created successfully
        #self.assertEqual(response.status_code, 302)
        #self.assertTrue(Tasks.objects.filter(title='Test Task').exists())
        
        # Access success message after request (since redirect happens)
        messages = get_messages(response.wsgi_request)
        #pdb.set_trace()
        self.assertEqual(len(messages), 1) 
        self.assertEqual(messages[0].status, 302)
        print(f"Messages: {messages}")


    def test_create_task_empty_title(self):
        # Prepare POST data with empty task title
        data = {
            'taskTitle': '',
            'taskDescription': 'This is a test task',
            'taskStatus': 'To Do'
        }

        # Send POST request to create_task view
        response = self.client.post(reverse('create-task'), data)

        # Check if task creation failed due to empty title
        self.assertEqual(response.status_code, 200)  # Assuming it renders the same page again
        self.assertContains(response, 'Failed to create Task! Title cannot be empty')

    def test_create_task_invalid_status(self):
        # Prepare POST data with invalid task status
        data = {
            'taskTitle': 'Test Task',
            'taskDescription': 'This is a test task',
            'taskStatus': 'Invalid Status'
        }

        # Send POST request to create_task view
        response = self.client.post(reverse('create-task'), data)

        # Check if task creation failed due to invalid status
        self.assertEqual(response.status_code, 200)  # Assuming it renders the same page again
        self.assertContains(response, 'Failed to create Task! Invalid task status')

    def test_create_task_invalid_method(self):
        # Send GET request to create_task view (invalid method)
        response = self.client.get(reverse('create-task'))

        # Check if it returns an error message for invalid method
        self.assertEqual(response.status_code, 200)  # Assuming it renders the same page again
        self.assertContains(response, 'Invalid method')
