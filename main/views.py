from django.shortcuts import render
from .models import Classes, Tasks
from .forms import ClassForm, TaskForm
from django.shortcuts import redirect
from django.contrib import messages
import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.
#@login_required(login_url='login')
def home(request):
    classes = Classes.objects.all()
    tasks = Tasks.objects.all()
    current_user = request.user
    current_datetime = datetime.date.today()  
    filterClass = []
    filterTask = []

    gradePoint = 0
    completed = 0
    count = 0
    currClass = 0
    currClassList = []

    for c in classes:
        if current_user.id == c.user_id:
            filterClass.append(c)
            if c.completed == True:
                gradePoint += c.GPA
                completed+= 1
                count+=3
            else:
                currClass += 1
                currClassList.append(c);
            
    for t in tasks:
        if current_user.id == t.classes.user_id:
            filterTask.append(t)

    if (count > 0):
        GPA = round(gradePoint/count, 1)
    else: 
        GPA=0

    pieChartData = [completed, 33 - completed]
    pieChartLabel = ['Completed', 'Uncompleted']

    datas = []
    labels = []
    for c in filterClass:
        if c.completed == True:
            datas.append(float(c.GPA))
            labels.append(c.course_code)

    lateTask = 0
    compeletedTask = 0
    inProgressTask = 0

    lateTaskList = []
    compeletedTaskList = []
    inProgressTaskList = []

    for t in filterTask:
        if t.completed == True: 
            compeletedTask += 1 
            compeletedTaskList.append(t)
        elif t.due_date < current_datetime:
            lateTask += 1   
            lateTaskList.append(t)
        else: 
            inProgressTask += 1
            inProgressTaskList.append(t)

    compeletedPercentage = int(completed/33*100)
    uncompleteTask = lateTask + inProgressTask;

    taskData = [lateTask, inProgressTask, compeletedTask]
    taskLabel = ['Late','In Progress','Complete']
    print(taskData)
    return render(request, 'main/home.html', {
        'classes': filterClass,
        'tasks': filterTask, 
        'current_user': current_user,
        'current_datetime': current_datetime,
        'GPA': GPA,
        'completed': completed,
        'currClass': currClass,
        'uncompleteTask': uncompleteTask,
        'pieChartData': pieChartData,
        'pieChartLabel': pieChartLabel,
        'filterClass': filterClass,
        'datas': datas,
        'labels': labels,
        'taskData': taskData,
        'taskLabel': taskLabel,
        'compeletedPercentage': compeletedPercentage,
        'lateTaskList': lateTaskList,
        'compeletedTaskList': compeletedTaskList,
        'inProgressTaskList': inProgressTaskList,
        'currClassList': currClassList,
        })

#@login_required(login_url='login')
def classes(request):
    classes = Classes.objects.all()
    current_user = request.user
    return render(request, 'main/classes.html', {'classes': classes, 'current_user': current_user})

#@login_required(login_url='login')
def display_class(request, class_id):
    display_class = Classes.objects.get(pk=class_id)
    return render(request, 'main/display_class.html', {'display_class': display_class})

#@login_required(login_url='login')
def add_class(request):
    class_form = ClassForm(request.POST or None)
    if request.method == "POST":
        if class_form.is_valid():
            form = class_form.save()
            form.user = request.user
            form.save()
            messages.success(request, 'Class has been added')
            return redirect('add_class')
    return render(request, 'main/add_class.html', {'form': class_form})


#@login_required(login_url='login')
def update_class(request, class_id):
    update_class = Classes.objects.get(pk=class_id)
    update_form = ClassForm(request.POST or None, instance=update_class)
    if update_form.is_valid():
            update_form.save()
            messages.success(request, 'Class has been updated')
            return redirect('classes')
    return render(request, 'main/update_class.html', {'update_class': update_class, 'update_form': update_form})

#@login_required(login_url='login')
def delete_class(request, class_id):
    delete_class = Classes.objects.get(pk=class_id)
    if request.method == 'POST':
        delete_class.delete()
        return redirect('classes')
    return render(request, 'main/delete_class.html', {'delete_class': delete_class})

#@login_required(login_url='login')
def tasks(request):
    tasks = Tasks.objects.all()
    current_user = request.user
    late_task = []
    ontime_task = []
    current_datetime = datetime.date.today()   
    for t in tasks:
        if t.due_date < current_datetime:
            late_task.append(t)
        else:
            ontime_task.append(t)
    return render(request, 'main/task.html', {'tasks': tasks,'late_task':  late_task, 'ontime_task':ontime_task, 'current_user': current_user})

#@login_required(login_url='login')
def add_task(request):
    form = TaskForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Task has been added')
            return redirect('add_task')
    return render(request, 'main/add_task.html', {'form': form})

#@login_required(login_url='login')
def update_task(request, task_id):
    update_task = Tasks.objects.get(pk=task_id)
    update_form = TaskForm(request.POST or None, instance=update_task)
    if update_form.is_valid():
            update_form.save()
            messages.success(request, 'Class has been updated')
            return redirect('tasks')
    return render(request, 'main/update_task.html', {'update_task': update_class, 'update_form': update_form})

#@login_required(login_url='login')
def delete_task(request, task_id):
    delete_task = Tasks.objects.get(pk=task_id)
    if request.method == 'POST':
        delete_task.delete()
        return redirect('tasks')
    return render(request, 'main/delete_task.html', {'delete_task': delete_task})

#@login_required(login_url='login')
def display_task(request, task_id):
    display_task = Tasks.objects.get(pk=task_id)
    return render(request, 'main/display_task.html', {'display_task': display_task})

#@login_required(login_url='login')
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        classes = Classes.objects.filter(name__icontains=searched)
        tasks = Tasks.objects.filter(name__icontains=searched)
        return render(request, 'main/search.html', {'searched': searched, 'classes': classes, 'tasks':tasks})
    else:
        return render(request, 'main/search.html', {})