from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from rest_framework import status, response, views

import statistics

def Dashboard_Main_Page(request):
    user = request.user
    if user.is_authenticated == False:
        return HttpResponse("Sorry, but 'You Shall Not Pass',untill you Login first ;)")

    context = {
        'user': user,
    }
    return render(request,'dashboard/dashboard.html',context)


class Dashboard_API_View(views.APIView):
    def get(self, request):

        return response.Response(
            status=status.HTTP_200_OK,

            data = {
                "Average_Temperature": Get_Average_Temperature(),
                "Average_Pressure": Get_Average_Pressure(),
                "Average_CO2": Get_Average_CO2(),
                "Average_TVCO": Get_Average_TVOC(),
                "Average_Humidity": Get_Average_Humidity(),
                })


def Get_Average_Temperature():
    sum = 0
    data = TimeSeriesDatum.objects.filter(sensor = "Temperature")

    for  datum in data:
        try:
            AVG=statistics.averages(datum.value)
            return AVG
    except Exception as e:
        return None

def Get_Average_Pressure():
    sum = 0
    data = TimeSeriesDatum.objects.filter(sensor = "Pressure")

    for  datum in data:
        try:
            AVG=statistics.averages(datum.value)
            return AVG
    except Exception as e:
        return None



def Get_Average_CO2():
    sum = 0
    data = TimeSeriesDatum.objects.filter(sensor = "CO2")

    for  datum in data:
        try:
            AVG=statistics.averages(datum.value)
            return AVG
    except Exception as e:
        return None


def Get_Average_TVOC():
    sum = 0
    data = TimeSeriesDatum.objects.filter(sensor = "TVOC")

    for  datum in data:
        try:
            AVG=statistics.averages(datum.value)
            return AVG
    except Exception as e:
        return None



def Get_Average_Humidity():
    sum = 0
    data = TimeSeriesDatum.objects.filter(sensor = "Humidity")

    for  datum in data:
        try:
            AVG=statistics.averages(datum.value)
            return AVG
    except Exception as e:
        return None


class Instruments_List_API_View(views.APIView):
    def get(self, request):

        if request.user.is_authenticated:
            try:
                Instrument.objects.get(id=1)
                instruments = Insturment.objects.values('name')
                return response.Response(

                 status=status.HTTP_200_OK,

                 data={
                       'result': instruments,
                       'count':Instrument.objects.all().count()
                       })

            except Exception as e:
                return response.Response(

                status=status.HTTP_404_NOT_FOUND,

                data = {
                     'message': 'You had not add an instrument; Please add at least one insturment.',
                     })


        else:

            return response.Response(
            status=status.HTTP_401_UNAUTHORIZED,
            data = {
                'message':"Sorry, but 'You Shall Not Pass',untill you Login first ;)",
            })



class Instruments_statisticsList_API_View(views.APIView):
    def get(self, request):
        if request.user.is_authenticated:
            try:
                Temperature_Values = TimeSeriesDatum.objects.filter(sensor = "Temperature").values_list('value', flat=True)
                Pressure_Values = TimeSeriesDatum.objects.filter(sensor = "Pressure").values_list('value', flat=True)
                CO2_Values = TimeSeriesDatum.objects.filter(sensor = "CO2").values_list('value', flat=True)
                TVCO_Values = TimeSeriesDatum.objects.filter(sensor = "TVOC").values_list('value', flat=True)
                Humidity_Values = TimeSeriesDatum.objects.filter(sensor = "Humidity").values_list('value', flat=True)


                return response.Response(
                    status=status.HTTP_200_OK,

                    data = {
                        #mean
                        'Temperature Mean':statistics.mean(Temperature_Values),
                        'Pressure Mean':statistics.mean(Pressure_Values),
                        'CO2 Mean':statistics.mean(CO2_Values),
                        'TVCO Mean':statistics.mean(TVCO_Values),
                        'Humidity Mean':statistics.mean(Humidity_Values),
                        #media
                        'Temperature Median':statistics.median(Temperature_Values),
                        'Pressure Median':statistics.median(Pressure_Values),
                        'CO2 Median':statistics.median(CO2_Values),
                        'TVCO Median':statistics.median(TVCO_Values),
                        'Humidity Median':statistics.median(Humidity_Values),
                        #mode
                        'Temperature Mode':statistics.mode(Temperature_Values),
                        'Pressure Mode':statistics.mode(Pressure_Values),
                        'CO2 Mode':statistics.mode(CO2_Values),
                        'TVCO Mode':statistics.mode(TVCO_Values),
                        'Humidity Mode':statistics.mode(Humidity_Values),
                        #stdv
                        'Temperature Mean':statistics.stdv(Temperature_Values),
                        'Pressure Mean':statistics.stdv(Pressure_Values),
                        'CO2 Mean':statistics.stdv(CO2_Values),
                        'TVCO Mean':statistics.stdv(TVCO_Values),
                        'Humidity Mean':statistics.stdv(Humidity_Values),

                        })

            except Exception as e:
                return response.Response(

                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    data = {
                        'error':str(e)
                        })
        else:
            return response.Response(

            status=status.HTTP_401_UNAUTHORIZED,

            data = {
                'message': "Sorry, but 'You Shall Not Pass',untill you Login first ;)",
                })
