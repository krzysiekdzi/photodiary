from django.shortcuts import render
from diary.models import Diary, Comment, PhotoObject
from django.core.files.storage import FileSystemStorage
import os
import datetime
from threading import Thread
from PIL import Image
from diary.forms import CommentForm

FILE_PATH = ''
DIARY_NAME = ''
NOW = ''

# Create your views here.
def diariesView(request):
    diaries = Diary.objects.all()
    data = []
    for i in diaries:
        data.append({'name' : i.name, 'description' : i.description })
    context = {}
    context['data'] = data
    context['imghost'] = 'http://'+os.environ['IMAGES_HOST']+':'+os.environ['IMAGES_PORT']+'/'
    return render(request, "diary/index.html", context)

def photosView(request, diaryName):
    photos = PhotoObject.objects.all()
    context = {}
    data = []
    for i in photos:
        if i.diary.name == diaryName:
            path = i.filePath.split('/')
            data.append({'title' : i.title,\
                'date' : str(i.date)[:16],\
                'filePath' : path[-1]})
    context['data'] = data
    context['diaryName'] = diaryName
    context['imageshost'] = 'http://'+os.environ['IMAGES_HOST']+':'+os.environ['IMAGES_PORT']+'/'
    return render(request, 'diary/photosView.html',context)

def postView(request, diaryName, postName):
    pass

def uploadPhoto(request, diaryName):
    if request.method == 'POST':
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        now = str(datetime.datetime.now())[11:]
        now = now.replace(':','_')
        now = now.replace('.','_')
        global NOW
        NOW = now
        global FILE_PATH
        global DIARY_NAME
        DIARY_NAME = diaryName
        filepath = os.path.abspath(os.getcwd())+'/diary/templates/diary/photos/'+now+'.jpg'
        FILE_PATH = filepath
        saved = fs.save(filepath, myfile)
        uploadedUrl = fs.url(saved)
        th = Thread(target = savePhoto)
        th.start()
        return render(request, 'diary/upload.html',
        {'uploadedUrl' : uploadedUrl})
    return render(request,'diary/upload.html',{'imghost':'http://'+os.environ['IMAGES_HOST']+\
    ':'+os.environ['IMAGES_PORT']+'/'})

def savePhoto():
    resize(FILE_PATH)
    diary = Diary.objects.get(name = DIARY_NAME)
    po = PhotoObject(title = NOW, filePath = FILE_PATH,\
            diary = diary)
    po.save()

def resize(FILE_PATH):
    basewidth = 800
    img = Image.open(FILE_PATH)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save(FILE_PATH)

def postComment(request,diaryName, photoTitle):
    if request.method =='POST':
        form = CommentForm(request.POST)
        if(form.is_valid()):
            text = form.cleaned_data.get('text')
            author = form.cleaned_data.get('author')
            po = PhotoObject.objects.get(title = photoTitle)
            com = Comment(author = author, text = text , photo = po)
            com.save()

            #return diariesView(request)
    else:
        form = CommentForm()
    return render(request, 'diary/comment.html',{'form':form})
