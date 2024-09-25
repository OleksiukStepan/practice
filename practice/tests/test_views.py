from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from practice.models import Task, Tag


class TaskListViewTest(TestCase):
    def setUp(self):
        self.task1 = Task.objects.create(content="Task 1", is_done=False)
        self.task2 = Task.objects.create(content="Task 2", is_done=True)

    def test_task_list_view(self):
        response = self.client.get(reverse("practice:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/home.html")
        self.assertContains(response, self.task1.content)
        self.assertContains(response, self.task2.content)

    def test_task_complete(self):
        response = self.client.post(
            reverse("practice:home"),
            {"task_id": self.task1.id, "Complete": ""}
        )
        self.task1.refresh_from_db()
        self.assertTrue(self.task1.is_done)
        self.assertRedirects(response, reverse("practice:home"))

    def test_task_undo(self):
        response = self.client.post(
            reverse("practice:home"), {"task_id": self.task2.id, "Undo": ""}
        )
        self.task2.refresh_from_db()
        self.assertFalse(self.task2.is_done)
        self.assertRedirects(response, reverse("practice:home"))


class TaskCreateViewTest(TestCase):
    def test_create_task(self):
        response = self.client.post(
            reverse("practice:task_create"),
            {
                "content": "New Task",
                "created_at": timezone.now(),
                "is_done": False,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(content="New Task").exists())


class TaskUpdateViewTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(content="Update Test", is_done=False)

    def test_update_task(self):
        response = self.client.post(
            reverse("practice:task_update", args=[self.task.id]),
            {
                "content": "Updated Task",
                "is_done": True,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.content, "Updated Task")
        self.assertTrue(self.task.is_done)


class TaskDeleteViewTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(content="Delete Test")

    def test_delete_task(self):
        response = self.client.post(
            reverse("practice:task_delete", args=[self.task.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())


class TagListViewTest(TestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(name="Tag 1")
        self.tag2 = Tag.objects.create(name="Tag 2")

    def test_tag_list_view(self):
        response = self.client.get(reverse("practice:tag_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/tag_list.html")
        self.assertContains(response, self.tag1.name)
        self.assertContains(response, self.tag2.name)


class TagCreateViewTest(TestCase):
    def test_create_tag(self):
        response = self.client.post(
            reverse("practice:tag_create"), {"name": "New Tag"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Tag.objects.filter(name="New Tag").exists())


class TagUpdateViewTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Update Tag")

    def test_update_tag(self):
        response = self.client.post(
            reverse(
                "practice:tag_update",
                args=[self.tag.id]
            ),
            {"name": "Updated Tag"}
        )
        self.assertEqual(response.status_code, 302)
        self.tag.refresh_from_db()
        self.assertEqual(self.tag.name, "Updated Tag")


class TagDeleteViewTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Delete Tag")

    def test_delete_tag(self):
        response = self.client.post(
            reverse("practice:tag_delete", args=[self.tag.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Tag.objects.filter(id=self.tag.id).exists())
