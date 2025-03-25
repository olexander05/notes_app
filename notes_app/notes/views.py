from django.shortcuts import render
from datetime import datetime

def index(request):

    notes = [
        {
            'title': 'Note 1',
            'content': 'This is the text of my first note.',
            'created_at': datetime(2025, 3, 25, 12, 0)
        },
        {
            'title': 'Note 2',
            'content': 'This is the text of the second note, a bit longer.',
            'created_at': datetime(2025, 3, 24, 15, 30)
        },
        {
            'title': 'Note 3',
            'content': 'The third note for testing.',
            'created_at': datetime(2025, 3, 23, 9, 15)
        },
    ]
    return render(request, 'notes/index.html', {'notes': notes})