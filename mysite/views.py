from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from manage import send_msg
from django.core.exceptions import ValidationError
import sys
import pdb
sys.path.append('/home/kavinubuntu/Desktop/GUI/Django_GUI')
# from django.template import RequestContext
@csrf_exempt
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html', {'output': ''})
    elif request.method == 'POST':
        # print("Value Rxed")
        # raise ValidationError(request.POST)
        # direction=request.POST['action']
        # pdb.set_trace()
        # print(direction)
        # send_msg(direction)
        if 'dataX' in request.POST:
            dataX = request.POST['dataX']
            print(dataX)
        # execute_file("handler")
        return render(request,'index.html',{'output': "Success"})
        # return render(request, 'output.html', )


# def my_view(request):
#     if request.method == 'POST':
#         if 'dataX' in request.POST:
#             dataX = request.POST['dataX']
#             print(dataX)
#             # doSomething with pieFact here...
#             # return HttpResponse('success') # if everything is OK
#     # nothing went well
#     # return HttpRepsonse('FAIL!!!!!')

        