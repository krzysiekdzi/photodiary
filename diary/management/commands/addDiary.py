from django.core.management.base import BaseCommand
from diary.models import Diary

class Command(BaseCommand):
    help = 'This adds new diary'

    def handle(self, *args, **kwargs):
        name = input("Provide diary name: ")
        desc = input("Provide diary description: ")
        d = Diary(name = name, description = desc)
        d.save()
        print('Diary:',name,'saved!')
