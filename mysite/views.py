from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from manage import send_msg
from django.core.exceptions import ValidationError
<<<<<<< HEAD
import sys
import pdb
sys.path.append('/home/kavinubuntu/Desktop/GUI/Django_GUI')
=======

import sys
sys.path.append('/home/kavinubuntu/django-apps/Django2')
>>>>>>> 2eaea023202bb669c51d7d26bcfe9c73b43affad
# from django.template import RequestContext
@csrf_exempt
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html', {'output': ''})
    elif request.method == 'POST':
        # print("Value Rxed")
        # raise ValidationError(request.POST)
<<<<<<< HEAD
        # direction=request.POST['action']
        # pdb.set_trace()
        # print(direction)
        # send_msg(direction)
        if 'dataX' in request.POST:
            dataX = request.POST['dataX']
            print(dataX)
=======
        direction=request.POST['action']
        print(direction)
        send_msg(direction)
>>>>>>> 2eaea023202bb669c51d7d26bcfe9c73b43affad
        # execute_file("handler")
        return render(request,'index.html',{'output': "Success"})
        # return render(request, 'output.html', )

<<<<<<< HEAD

# def my_view(request):
#     if request.method == 'POST':
#         if 'dataX' in request.POST:
#             dataX = request.POST['dataX']
#             print(dataX)
#             # doSomething with pieFact here...
#             # return HttpResponse('success') # if everything is OK
#     # nothing went well
#     # return HttpRepsonse('FAIL!!!!!')

=======
>>>>>>> 2eaea023202bb669c51d7d26bcfe9c73b43affad
        