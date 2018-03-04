from .models import Customer,Products
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
from django.views import View
import  json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from .serializers import CustomerSerializer, ProductSerializer

class CustomerList(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CustomerList, self).dispatch(request, *args, **kwargs)
    def get(self,request):
        customer_list = list(Customer.objects.values())
        return JsonResponse(customer_list,safe=False)
    def post(self,request):
        data = request.body.decode('utf8')
        data = json.loads(data)
        new_customer = Customer(first_name=data["first_name"],last_name=data["last_name"],address= data["address"])
        new_customer.save()
        return JsonResponse(data, safe=False)

class CustomerDetail(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CustomerDetail, self).dispatch(request, *args, **kwargs)
    def get(self,request,pk):
        customer_detail = list(Customer.objects.filter(pk = pk).values())
        return JsonResponse(customer_detail,safe=False)
    def put(self,request,pk):
        data = request.body.decode('utf-8')
        data = json.loads(data)
        customer_updated = Customer.objects.get(pk=pk)
        data_key = list(data.keys())
        for key in data_key:
            if key == "first_name":
                customer_updated.first_name = data[key]
            if key == "last_name":
                customer_updated.last_name = data[key]
            if key == "address":
                customer_updated.address = data[key]
        customer_updated.save()
        return JsonResponse(data,safe=False)
    def delete(self,request,pk):
        customer_removed = Customer.objects.get(pk=pk)
        customer_removed.delete()
        return JsonResponse({"deleted":'Yes'},safe=False)



class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer