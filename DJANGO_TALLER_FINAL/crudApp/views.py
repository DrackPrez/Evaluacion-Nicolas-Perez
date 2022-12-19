from django.shortcuts import render,redirect
from crudApp.models import Inscritos, Institucion
from crudApp.forms import FormInscritos
from .serializers import InscritosSerializer, InstitucionSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.decorators import api_view
from django.http import Http404
from django.http import JsonResponse

# Create your views here.
#-----------------Api View------------------------

def verinscritosDb(request):
    inscrito = Inscritos.objects.all()
    data = {'inscritos' : list(inscrito.values('id','nombre','telefono','fecha_inscripcion', 'institucion','hora_inscripcion','estado','observacion'))}

    return JsonResponse(data)

#----------------------Crud View-------------------
def index(request):
    return render(request, 'index.html')

def agregarInscrito(request):
    form = FormInscritos()
    if request.method == 'POST':
        form = FormInscritos(request.POST)
        if form.is_valid():
            form.save()
        return listarInscrito(request)
    data = {'form' : form}
    return render(request, 'agregarInscrito.html', data)

def eliminarInscrito(request, id):
    ins = Inscritos.objects.get(id = id)
    ins.delete()
    return redirect('/inscritos')

def listarInscrito(request):
    ins = Inscritos.objects.all()
    data = {'inscritos': ins}
    return render(request, 'listarInscrito.html', data)


def actualizarInscrito(request, id):
    ins = Inscritos.objects.get(id = id)
    form = FormInscritos(instance=ins)
    if request.method == 'POST':
        form = FormInscritos(request.POST, instance=ins)
        if form.is_valid():
            form.save()
        return listarInscrito(request)
    data = {'form': form}
    return render(request, 'agregarInscrito.html', data)
#-------------Class Base View------------------------------------------------------------------------------------
class ListarInscritos(APIView):

    def get(self, request):
        ins = Inscritos.objects.all()
        serial = InscritosSerializer(ins, many=True)
        return Response(serial.data)
    
    def post(self, request):
        serial = InscritosSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


class DetalleInscrito(APIView):
    def get_object(self, pk):
        try:
            return Inscritos.objects.get(pk=pk)
        except Inscritos.DoesNotExist:
            return Http404
    
    def get(self,request,pk):
        ins = self.get_object(pk)
        serial = InscritosSerializer(ins)
        return Response(serial.data)

    def put(self, request,pk):
        ins = self.get_object(pk)
        serial = InscritosSerializer(ins, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, rquest, pk):
        ins = self.get_object(pk)
        ins.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#----------------------Function Based View-----------------------------

@api_view(['GET', 'POST'])
def Lista_de_Instituciones(request):
    if request.method == 'GET':
        ins = Institucion.objects.all()
        serial = InstitucionSerializer(ins, many=True)
        return Response(serial.data)
    
    if request.method == 'POST':
        serial = InstitucionSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def institucion_detalle(request, pk):
    try:
        ins = Institucion.objects.get(id = pk)
    except Institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = InstitucionSerializer(ins)
        return Response(serial.data)

    if request.method == 'PUT':
        serial = InstitucionSerializer(ins, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        ins.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
