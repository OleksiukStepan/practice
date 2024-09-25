from django.test import TestCase
from django.utils import timezone
from practice.forms import TaskForm, TagForm
from practice.models import Tag


class TaskFormTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Urgent")

    def test_task_form_valid_data(self):
        form = TaskForm(
            data={
                "content": "Complete the assignment",
                "deadline": timezone.now() + timezone.timedelta(days=1),
                "is_done": False,
                "tags": [self.tag.id],
            }
        )
        self.assertTrue(form.is_valid())
        task = form.save()
        self.assertEqual(task.content, "Complete the assignment")
        self.assertEqual(task.is_done, False)
        self.assertIn(self.tag, task.tags.all())

    def test_task_form_no_deadline(self):
        form = TaskForm(
            data={
                "content": "Read a book",
                "is_done": False,
                "tags": [self.tag.id],
            }
        )
        self.assertTrue(form.is_valid())
        task = form.save()
        self.assertEqual(task.deadline, None)

    def test_task_form_invalid_data(self):
        form = TaskForm(
            data={
                "deadline": timezone.now() + timezone.timedelta(days=1),
                "is_done": False,
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("content", form.errors)


class TagFormTest(TestCase):
    def test_tag_form_valid_data(self):
        form = TagForm(data={"name": "Home"})
        self.assertTrue(form.is_valid())
        tag = form.save()
        self.assertEqual(tag.name, "Home")

    def test_tag_form_invalid_data(self):
        form = TagForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)

    def test_tag_form_unique_name(self):
        Tag.objects.create(name="Work")
        form = TagForm(data={"name": "Work"})
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)
