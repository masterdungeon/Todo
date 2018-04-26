from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect

from todo.models import Todo

def main(request):
	if request.method == "POST":
		topic = request.POST["topic"]
		content = request.POST["content"]
		p = Todo(topic = topic, content = content)
		p.save()
	return render(request, 'todo/index.html')

def fetch_todo(request):
	p = Todo.objects.all()
	return render(request, 'todo/todo.html', {'p': p})

def delete(request):
	if request.method == "GET":
		iid = request.GET.get('item_id')
		Todo.objects.filter(id=iid).delete()
		return HttpResponseRedirect("/todo")
	else:
		return HttpResponse("FUCK YOU")

	# url = request.META.get('PATH_INFO', '')[35:]
	# unique_id = url[:len(url)-1]
	# Paste.objects.filter(id=unique_id).delete()
	# return render(request, 'todo/todo.html')
	# if request.method == "POST":
	# 	unique_id = request.POST.get("id")
	# 	Paste.objects.filter(id=unique_id).delete()
	# 	return render(request, 'todo/todo.html')

# def delete(request, oid): 
#     unique_id = Object.objects.filter(id=oid)
#     Paste.objects.filter(id=unique_id).delete()
#     return render(request, 'todo/todo.html')



