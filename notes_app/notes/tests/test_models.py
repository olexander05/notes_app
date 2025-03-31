from django.test import TestCase
from notes.models import Category, Note



class NoteModelTest(TestCase):
    def setUp(self):

        self.category = Category.objects.create(title="Personal")
        self.note = Note.objects.create(
            title="Buy milk",
            text="Don't forget to buy milk",
            category=self.category
        )

    def test_note_creation(self):

        note = Note.objects.get(id=self.note.id)
        self.assertEqual(note.title, "Buy milk")
        self.assertEqual(note.text, "Don't forget to buy milk")
        self.assertEqual(note.category.title, "Personal")

    def test_note_update(self):

        self.note.title = "Buy coffee"
        self.note.text = "Remember to buy coffee instead"
        self.note.save()

        updated_note = Note.objects.get(id=self.note.id)
        self.assertEqual(updated_note.title, "Buy coffee")
        self.assertEqual(updated_note.text, "Remember to buy coffee instead")