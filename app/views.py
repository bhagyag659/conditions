from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':2000,'b':300}
    return render(request,'if_condition.html',d)

def if_else_condition(request):
    d={'a':200,'b':300}
    return render(request,'if_else_condition.html',d)
def if_else_if_condition(request):
    d={'a':200,'b':300,'c':400}
    return render(request,'if_else_if_condition.html',d)
def nested(request):
    d={'a':200,'b':250,'c':300}
    return render(request,'nested.html',d)
