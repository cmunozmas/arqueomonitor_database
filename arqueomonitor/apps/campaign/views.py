
from django.shortcuts import render
from models import Cruise, Station, Deployment, Instrument
from arqueomonitor.apps.laboratory.models import Sample, TankTrial
from arqueomonitor.apps.products.models import Product, Publication, Staff
from forms import CruiseForm, StationForm
from django.db.models import Count


def start(request):
    count_cruises = str(Cruise.objects.all().count())
    count_stations = str(Station.objects.all().count())
    count_deployments = str(Deployment.objects.all().count())
    count_instruments = str(Instrument.objects.all().count())
    count_samples = str(Sample.objects.all().count())
    count_tank_trials = str(TankTrial.objects.all().count())
    count_products = str(Product.objects.all().count())
    count_publications = str(Publication.objects.all().count())
    count_staff = str(Staff.objects.all().count())
    context= {'cruise_count': count_cruises, 'station_count': count_stations, 'deployment_count': count_deployments, 'instrument_count': count_instruments, 'sample_count': count_samples, 'tank_trial_count': count_tank_trials, 'product_count': count_products, 'publication_count': count_publications, 'staff_count': count_staff}
    return render(request, 'index.html', context)

def byThePlots(request):
    count_materials_copper = str(Sample.objects.filter(sample_material__contains='copper').count())
    count_materials_brass = str(Sample.objects.filter(sample_material__contains='brass').count())
    count_materials_forged = str(Sample.objects.filter(sample_material__contains='forged_steel').count())
    count_materials_steel = str(Sample.objects.filter(sample_material__contains='steel').count())
    count_h1 = str(Sample.objects.filter(sample_height__contains='h1').count())
    count_h2 = str(Sample.objects.filter(sample_height__contains='h2').count())
    count_h3 = str(Sample.objects.filter(sample_height__contains='h3').count())
    count_samples_station_buc = str(Sample.objects.filter(sample_station_id__exact=1).count())
    count_samples_station_foug = str(Sample.objects.filter(sample_station_id__exact=2).count())
    count_deployments_station_buc = str(Deployment.objects.filter(deployment_station_id__exact=1).count())
    count_deployments_station_foug = str(Deployment.objects.filter(deployment_station_id__exact=2).count())

    context= {'material_count_copper': count_materials_copper, 'material_count_brass': count_materials_brass,
              'material_count_forged': count_materials_forged, 'material_count_steel': count_materials_steel,
              'h1_count': count_h1, 'h2_count': count_h2, 'h3_count': count_h3,
              'sample_station_buc_count': count_samples_station_buc, 'sample_station_foug_count': count_samples_station_foug,
              'deployment_station_buc_count': count_deployments_station_buc, 'deployment_station_foug_count': count_deployments_station_foug}



    return render(request, 'widgets_by_the_plots.html', context)

def logIn(request):
    return render(request, 'login.html')

def tablesDynamic(request):
    return render(request, 'tables_dynamic.html')

def getCruises(request):
    template_name = 'tables_cruise.html'
    cruises = Cruise.objects.all()
    context = {'cruises':cruises}
    return render(request, template_name, context)

def addCruise(request):
    form = CruiseForm(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        cruise_name_view = form_data.get("cruise_name")
        cruise_description_view = form_data.get("cruise_description")
        created_by_id_view = request.user.id
        updated_by_id_view = created_by_id_view
        obj = Cruise.objects.create(cruise_name = cruise_name_view, cruise_description = cruise_description_view, updated_by_id = updated_by_id_view, created_by_id = created_by_id_view)
        print cruise_name_view
        print cruise_description_view
        print updated_by_id_view
        print created_by_id_view

    context = {'form':form,}
    return render(request, 'form_cruise.html', context)

def getDeployments(request):
    template_name = 'tables_deployment.html'
    deployments = Deployment.objects.all()
    context = {'deployments':deployments}
    return render(request, template_name, context)

def getStations(request):
    template_name = 'tables_station.html'
    stations = Station.objects.all()
    context = {'stations':stations}
    return render(request, template_name, context)

def addStation(request):
    form = StationForm(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        station_name_view = form_data.get("station_name")
        station_description_view = form_data.get("station_description")
        station_geospatial_lat_view = form_data.get("station_geospatial_lat")
        created_by_id_view = request.user.id
        updated_by_id_view = created_by_id_view
        obj = Station.objects.create(station_name = station_name_view, station_description = station_description_view, station_geospatial_lat = station_geospatial_lat_view, updated_by_id = updated_by_id_view, created_by_id = created_by_id_view)
        print station_name_view
        print station_description_view
        print updated_by_id_view
        print created_by_id_view

    context = {'form':form,}
    return render(request, 'form_station.html', context)

def getInstruments(request):
    template_name = 'tables_instrument.html'
    instruments = Instrument.objects.all()
    context = {'instruments':instruments}
    return render(request, template_name, context)

def getSamples(request):
    template_name = 'tables_sample.html'
    samples = Sample.objects.all()
    context = {'samples':samples}
    return render(request, template_name, context)

def getTankTrials(request):
    template_name = 'tables_tank_trial.html'
    tank_trials = TankTrial.objects.all()
    context = {'tank_trials':tank_trials}
    return render(request, template_name, context)
