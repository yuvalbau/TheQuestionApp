from django.http import HttpResponse 
from MyApp.models import Question
import json
from django.contrib.auth.models import User

response_data = {}
response_data['result'] = ''
response_data['message'] = ''

def read(request): 
    data = {}
    data['questions'] = []
    if request.method == 'GET': 
        try:       
            questions = Question.objects.all()
            for question in questions:
                q_as_json = question.as_json()
                data['questions'].append(q_as_json)
                   
            response_data['result'] = json.dumps(data)  
            return HttpResponse(response_data['result'])
        
        except Exception as e:
            response_data['message'] = ('You get an Error:',e)
            return HttpResponse(response_data['message'])
        
    else:       
        response_data['message'] = ('You get an Error: Wrong http method')
        return HttpResponse(response_data['message'])  
    
def delete(request):
    if request.method == 'PUT':
        try:
            jsonObj = json.loads(request.body.decode('utf-8'))
            p= Question.objects.get(pk=jsonObj["question_id"])
            p.delete()
            response_data['result']='/Question Deleted'
            return HttpResponse(response_data['result'])
        
        except Exception as e:
            response_data['message'] = ('You get an Error:',e)
            return HttpResponse(response_data['message'])
        
    else:       
        response_data['message'] = ('You get an Error: Wrong http method')
        return HttpResponse(response_data['message'])
            
def create(request):
    if request.method == 'POST':
        try:
            jsonObj = json.loads(request.body.decode('utf-8'))
            u = User.objects.get(id=jsonObj["author_id"])    
            q = Question(title=jsonObj["title"],description=jsonObj["description"],author= u)   
            q.save()
            response_data['result']='/Question Created'
            return HttpResponse(response_data['result'])
        
        except Exception as e:
            response_data['message'] = ('You get an Error:',e)
            return HttpResponse(response_data['message'])
        
    else:       
        response_data['message'] = ('You get an Error: Wrong http method')
        return HttpResponse(response_data['message'])
        
def edit(request):
    if request.method == 'PUT':
        try:
            jsonObj = json.loads(request.body.decode('utf-8'))
            p= Question.objects.get(pk=jsonObj["question_id"])
            p.title = jsonObj["title"]
            p.description = jsonObj["description"] 
            p.save()
            response_data['result']='/Question updated'
            return HttpResponse(response_data['result'])
        
        except Exception as e:
            response_data['message'] = ('You get an Error:',e)
            return HttpResponse(response_data['message'])
        
    else:       
        response_data['message'] = ('You get an Error: Wrong http method')
        return HttpResponse(response_data['message'])
        
        