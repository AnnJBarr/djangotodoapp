from django.test import TestCase
import datetime
import json
from django.core import serializers
from django.urls import reverse
from tasks.models import Task


def create_task(task_title, due_date):
    return Task.objects.create(task_text=task_title, due_date=due_date, complete=False)

# Create your tests here.
class TaskTests (TestCase):
    def test_we_can_get_a_task (self):
        create_task("walk the dog", datetime.datetime.now())
        response = self.client.get(reverse("tasks:crud"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "walk the dog")

    def test_we_can_create_a_task (self):
        # post task
        self.client.post(reverse("tasks:crud"), {"task_text":"task no1", "due_date":datetime.datetime.now()})
        # copy get from test above but change text and then try to implement functionality
        response = self.client.get(reverse("tasks:crud"))
        print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "task no1")

    def test_we_can_update_a_task (self):
        task = create_task("test update", datetime.datetime.now())
        task.task_text="walk the cat"
        task.due_date=datetime.datetime(2020, 12, 25)
        serialized_task=serializers.serialize('json', [task])
        self.client.put(reverse("tasks:crud"), serialized_task)
        response = self.client.get(reverse("tasks:crud"))
        print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "walk the cat")
        self.assertContains(response, datetime.datetime(2020, 12, 25).strftime('%Y-%m-%dT%H:%M:%SZ'))
        self.assertNotContains(response, "test update")


    def test_we_can_delete_a_task(self):
        task = create_task("test delete", datetime.datetime.now())
        self.client.delete(reverse("tasks:crud_pk", kwargs={"pk":task.id}))
        response = self.client.get(reverse("tasks:crud"))
        self.assertNotContains(response, task.id)
        self.assertNotContains(response, task.task_text)
        




