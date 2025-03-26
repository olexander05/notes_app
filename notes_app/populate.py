import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notes_app.settings')
django.setup()

from notes.models import Category, Note
from datetime import datetime

cat1 = Category.objects.create(title="Робота")
cat2 = Category.objects.create(title="Особисте")

Note.objects.create(
    title="Зустріч з клієнтом",
    text="Обговорити деталі проєкту",
    reminder=datetime(2025, 3, 27, 10, 0),
    category=cat1
)
Note.objects.create(
    title="Купити подарунок",
    text="День народження друга",
    reminder=datetime(2025, 3, 28, 15, 30),
    category=cat2
)

print(Category.objects.all())
print(Note.objects.all())