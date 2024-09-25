from django.test import TestCase
from django.utils import timezone
from practice.models import Task, Tag


class TagModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Urgent")

    def test_tag_creation(self):
        self.assertEqual(self.tag.name, "Urgent")
        self.assertTrue(Tag.objects.filter(name="Urgent").exists())

    def test_tag_unique_name(self):
        with self.assertRaises(Exception):
            Tag.objects.create(name="Urgent")

    def test_tag_str_method(self):
        self.assertEqual(str(self.tag), "Urgent")


class TaskModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Home")
        self.task = Task.objects.create(
            content="Test Task",
            created_at=timezone.now(),
            deadline=timezone.now() + timezone.timedelta(days=1),
            is_done=False,
        )
        self.task.tags.add(self.tag)

    def test_task_creation(self):
        self.assertEqual(self.task.content, "Test Task")
        self.assertFalse(self.task.is_done)
        self.assertTrue(Task.objects.filter(content="Test Task").exists())

    def test_task_str_method(self):
        self.assertEqual(str(self.task), "Test Task")

    def test_task_tags(self):
        self.assertIn(self.tag, self.task.tags.all())
        self.assertEqual(self.task.tags.count(), 1)

    def test_task_deadline_optional(self):
        task_without_deadline = Task.objects.create(
            content="Test Task 2",
            created_at=timezone.now(),
            is_done=False,
        )
        self.assertIsNone(task_without_deadline.deadline)

    def test_task_mark_done(self):
        self.task.is_done = True
        self.task.save()
        self.assertTrue(Task.objects.get(id=self.task.id).is_done)
