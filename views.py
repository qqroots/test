from django.http import HttpRequest,HttpResponse
from django.shortcuts import redirect, render
from django.contrib.messages.storage import session
# from django.conf import settings

# todos = []
# def task(request):
#     return render(request, 'task.html',{'test_context':todos})
    
# def add(request):
#     if request.method == "GET":
#         return render(request,'add.html')
#     else:
#         todoitem = request.POST['view_task']
#         todos.append(todoitem)
#         return redirect("/")


def task(request):
    if 'todos' not in request.session:
        request.session['todos'] = []
    return render(request, 'task.html',{'test_context':request.session['todos']})
    # return render(request, 'task.html',{'test_context':request.session['todos']})

def add(request):
    if request.method == "GET":
        return render(request,'add.html')
    else:
        todoitem = request.POST['view_task']
        request.session['todos'].append(todoitem)
        return redirect("/")





        # return render(request,'task.html') 不可這樣寫 這樣資料即流失 重新request一次