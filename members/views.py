import json
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpRequest
from django.template import loader
from django.urls import reverse
from .models import Members
from django.conf import settings
import os
from wsgiref.util import FileWrapper
import mimetypes

PATH = '/mnt/0C587C1F587C0A2A/Server/djangoProj/learnDjango/members/static/COG/'
FILE_LIST = sorted(os.listdir(PATH))
VPATH = '/mnt/0C587C1F587C0A2A/Server/djangoProj/learnDjango/members/static/Vids'
VIDEO_LIST = sorted(os.listdir(VPATH))

def getNameList(lm, path1, path2):
  ls = []
  for i in range(1,lm):
    tempOb = {
      'img' : path1 + '/' + str(i) + '.JPG',
      'cimg' : path2 + '/' + str(i) + '.JPG'
    }
    ls.append(tempOb)
  return ls

# def getIndexArr(lm):
#   ls = []
#   for i in range(1,lm):
#     ls.append(i)

# globalContext = {
#   'imgList' : getNameList(13, '/images/event1/'),
#   'cimgList' : getNameList(13, '/cimages/event1/'),
#   'indexArr' : [i for i in range(1,13)],
#   'file_list' : os.listdir(r'/home/msc2/DevTimez/djangoProj/learnDjango/members/static/OG'),
#   'imgLim' : 13
# }

# def index(request):
#   members = Members.objects.all().values()
#   template = loader.get_template('index1.html')
#   # nmList = os.listdir('./static/images')
#   return HttpResponse(template.render(globalContext, request))

# def loadmore(request, id):
#   print('in loadmore, send help')
#   tempLimit = id + 12
#   globalContext['imgList'] = getNameList(tempLimit, '/images/event1/')
#   globalContext['cimgList'] = getNameList(tempLimit, '/cimages/event1/')
#   globalContext['imgLim'] = tempLimit
#   globalContext['indexArr'] = getIndexArr(tempLimit)
#   return HttpResponseRedirect(reverse('index'))

def getHomeContext():
  ls = []
  for i in FILE_LIST:
    tempOB = {
      'eventName' : i,
      'thumbnail' : './COG/' + i + '/1.JPG'
    }
    ls.append(tempOB)
  return ls

def getVideoContext():
  ls = []
  for i in VIDEO_LIST:
    tempOB = {
      'eventName' : i,
      'thumbnail' : './COG/' + i.replace(".zip","") + '/1.JPG',
      'file' : "./Vids/"+i
    }
    ls.append(tempOB)
  return ls

def home(request):
  context={
    'list' : getHomeContext()
  }
  template = loader.get_template('home.html')
  return HttpResponse(template.render(context, request))

def images(request, eventName):
  print("hello worlkd")
  limit = len(os.listdir(PATH+eventName))
  path1 = 'OG/' + eventName
  path2 = 'COG/' + eventName
  context = {
    'list' : getHomeContext(),
    'imageList' : getNameList(limit, path1, path2),
    'eventName' : eventName
  }
  template = loader.get_template('index1.html')
  # nmList = os.listdir('./static/images')
  return HttpResponse(template.render(context, request))

def info(request):
  template = loader.get_template('info.html')
  return HttpResponse(template.render({}, request))  

def videos(request):
  print("hello worlkd")
  context={
    'list' : getVideoContext()
  }
  template = loader.get_template('videos.html')
  return HttpResponse(template.render(context, request))

def preview(request,fileName):
  print(fileName)
  fileName = fileName.replace('preview','')
  template = loader.get_template('preview.html')
  return HttpResponse(template.render(fileName, request))  

def download(request):
  print("\n\n\njkill me pls")
  myBody = request.POST
  print(myBody.get('filename'))
  filename = myBody.get('filename')
  # return HttpResponseRedirect(reverse('home'))
  file_path = '/mnt/0C587C1F587C0A2A/Server/djangoProj/learnDjango/members' + filename
  print("\n\nsend help\n", file_path)
  wrapper      = FileWrapper(open(file_path))
  content_type = mimetypes.guess_type(filename)[0]  # Use mimetypes to get file type
  response     = HttpResponse(wrapper,content_type=content_type)  
  response['Content-Length']      = os.path.getsize(file_path)    
  response['Content-Disposition'] = "attachment; filename=%s" %  file_path
  return response