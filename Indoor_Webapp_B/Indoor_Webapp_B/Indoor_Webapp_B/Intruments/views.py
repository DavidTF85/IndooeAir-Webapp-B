#django
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
#rest_framework
from rest_framework import status, views, response
#mie code
from foundation.models import Instrument
from instrument.serializers import InstrumentSerializer


def Intruments_lists_page(request):
    return render(request, "instrument/list.html", {})

def Instruments_create_page(request):
    return render(request, "instruments/create.html", {})


class Instruments_List_API_View(views.APIView):
    def get(self,request):
        instruments = Instrument.objects.filter(user=request.user).values('name','location','serial_number')

        return response.Response(
            status=status.HTTP_200_OK,
            data={
                'instrument list: ': instruments,
            }
    )

class Instrument_Create_API(views.APIView):
    def post(self ,request):
        serializer = InstrumentSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


        return response.Response(
            status = status.HTTP_201_CREATED,
            data = serializer.data,
        )


def Instrment_Retrieve_Page(request, id):
    return render(request, "instrument/retrieve.html", {
        "instrument_id": int(id),
    })


def Instrument_Update_Page(request, id):
    return render(request, "instrument/update.html", {
        "instrument_id": int(id),
    })


class Instrument_Retrieve_Update_API(views.APIView):
    def get_object(self,id):
        return get_object_or_404(Instrument, id=id)


    def get(self, request, id):
        object = self.get_object(id)
        serializer = InstrumentSerializer(object, many=False)
        return response.Response(
            status = status.HTTP_200_OK,
            data = serializer.data,
        )


    def put(self, request, id):
        object = self.get_object(id)
        serializer = InstrumentSerializer(object, data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()


        return response.Response(
            status = status.HTTP_200_OK,
            data = serializer.data,
        )
