from django.core.management.base import BaseCommand
from diary.models import PhotoObject, Diary
import os

class Command(BaseCommand):
    help = 'This adds new photo to diary'

    def handle(self, *args, **kwargs):
        name = input("Provide diary name: ")
        title = input("Provide photo title: ")
        filePath = input("Provide file name: ")
        #print(os.path.abspath(os.getcwd()))
        filePath = os.path.abspath(os.getcwd())+'\\diary\\photos\\'+filePath
        diary = Diary.objects.get(name = name)
        p = PhotoObject(title = title, filePath = filePath,\
            diary = diary)
        p.save()
        print('Photo:',title,'filepath:',filePath,'saved!')
