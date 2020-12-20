from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .froms import *

# Create your views here.

def home(request):
	
	tasks = Task.objects.all()

	form = TaskForm()

	if request.method == 'POST': 

		form = TaskForm(request.POST) # lo que se escriba en el textbox se mandara el form del admin

		if form.is_valid(): # esto lo validara y luego

			form.save() #Guardar en la base de datos

		return redirect('/') # redireccionar a la pagina principal 

	content = {'tasks': tasks, 'form': form}

	return render(request, 'principal/todo.html', content)


def updateTask(request, pk):

	task = Task.objects.get(id = pk)

	form = TaskForm(instance = task)

	if request.method == 'POST':

		form = TaskForm(request.POST, instance = task) # la informacion introducida se manda a task del admin y se modifica.

		if form.is_valid(): # se valida 

			form.save() # se guarda 

			return redirect('/') # regresa a la pagina principal


		
	content = {'form': form}
	
	return render(request, 'principal/update_task.html', content)


def deleteTask(request, pk):

	item = Task.objects.get(id = pk)

	if request.method == "POST":

		item.delete()

		return redirect('/')

	content = {'item': item}

	return render(request, 'principal/delete.html', content)