from django.shortcuts import get_object_or_404

# Create your views here.

from django.http import JsonResponse, HttpResponse
from tasks.models import Task
from django.core import serializers
from django.views.generic import View
import datetime
import json


class TasksView(View):
    def get(self, request):
        return JsonResponse(serializers.serialize('json', Task.objects.all()), safe=False)

    def post(self, request):
        print(request.POST.get('task_title'))
        Task.objects.create(task_text=request.POST.get("task_text", ""), due_date=request.POST.get("due_date", datetime.datetime.now()), complete=False)
        return HttpResponse('OK')

    def put(self, request):
        # body_unicode = request.body.replace("\'", "\"")
        # body = json.loads(body_unicode.decode('utf-8'))
        # print(body_data)
        # body = json.loads(request.body.replace("\'", "\""))
        for task in serializers.deserialize('json', request.body):
            task.save()
        # task = Task.objects.get(body.id)
        # task.task_text=body.task_text
        # task.save()
        return HttpResponse("OK")

    def delete(self,request, pk):
        task=get_object_or_404(Task, pk=pk)
        task.delete()
        return HttpResponse("OK")


