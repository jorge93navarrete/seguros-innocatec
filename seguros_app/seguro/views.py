from .models import Seguro
from .serializers import SeguroSerializer
from rest_framework.views import Http404, APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

class SeguroList(APIView):
    def get(self, request, format=None):
        seguros = Seguro.objects.all()
        serializer = SeguroSerializer(seguros, many=True)
        return Response(serializer.data)

class SeguroCreate(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def post(self, request, format=None):
        serializer = SeguroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SeguroDetail(APIView):
    def get_seguro(self, pk):
        try:
            return Seguro.objects.get(pk=pk)
        except Seguro.DoesNotExist:
            raise Http404
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk, format=None):
        seguro = self.get_seguro(pk)
        serializer = SeguroSerializer(seguro)
        return Response(serializer.data)

    def put(self, request, pk , format=None):
        seguro = self.get_seguro(pk)
        serializer = SeguroSerializer(seguro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        seguro = self.get_seguro(pk)
        seguro.delete()
        return Response({"response":"seguro borrado"} , status=204)
