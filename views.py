from django.shortcuts import render
from .models import covid_data
from django.http import HttpResponse
from .resources import dataResource
from tablib import Dataset
from .forms import covidData
# Create your views here.

def index(request):
    items = covid_data.objects.all
    return render(request,'index.html', {'all':items})


def input(request):
    if request.method=='POST':
        form=covidData(request.POST)
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/index')  
            except:  
                pass
            
          
    else:  
        form = covidData()  
    return render(request,'index.html',{'form':form})  

def update(request, id):  
    prod = covid_data.objects.get(id=id)  
    form = covidData(request.POST, instance = prod)  
    if form.is_valid():  
        form.save()  
        return redirect("/index")  
    return render(request, 'edit.html', {'prod': prod})  
def destroy(request, id):  
    prod = covid_data.objects.get(id=id)  
    prod.delete()  
    return redirect("/index")  

def export(request):
    data_resource = dataResource()
    dataset = data_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response




def simple_upload(request):
    if request.method == 'POST':
        data_resource = dataResource()
        dataset = Dataset()
        new_data = request.FILES['myfile']

        imported_data = dataset.load(new_data.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
        	print(data[1])
        	value = covid_data(
        		data[0],
        		data[1],
        		data[2],
        		data[3],
                data[4],
                data[5],
                data[6],
                data[7]
               
        		)
        	value.save()       
        
        #result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        #if not result.has_errors():
        #    person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'input.html')
