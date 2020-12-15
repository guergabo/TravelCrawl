### PACKAGES ###
from django.shortcuts import render   # function to render the html..
from .forms import FlightForm         # class for forms.
from django.views import View         # View class to inherit.
from .scraper import *                # Contains web scraping functions.
from .models import Airport           # model for iata_codes of airports.

### HomeSearchView ###
class HomeSearchView(View):
    template_name_get = 'flight/main.html'
    template_name_post = 'flight/list.html'

    # GET METHOD.
    def get(self, request):
        form = FlightForm()
        context = {
            'form': form
        }
        return render(request, self.template_name_get, context)

    # POST METHOD.
    def post(self, request):
        form = FlightForm(request.POST) # allows form data coming through

        # ASSIGN QUERY PARAMETERS.
        origin = form['origin'].value()
        destination = form['destination'].value()
        startdate = form['startdate'].value()
        enddate = form['enddate'].value()

        # MAPPING CITY TO IATA CODE
        d1_origin = Airport.objects.filter(city_name=origin)
        d1_destination = Airport.objects.filter(city_name=destination)
        print(d1_origin)
        print(d1_destination)

        if len(d1_origin) > 1:
            origin = d1_origin[0].iata_code
        else:
            origin = d1_origin.iata_code
        if len(d1_destination) > 1:
            destination = d1_destination[0].iata_code
        else:
            destination = d1_destination.iata_code

        # CREATE URL.
        url = kayak_url_structure(origin, destination, startdate, enddate)
        print(url)

        # GET PANDAS DATAFRAME OF FLIGHTS.
        data_frame = kayak_scraping(url)
        data_frame['check_out'] = data_frame['check_out'].apply(lambda x: "<a href='{}' target='_blank'>Buy Now</a>".format(x))
        context = {
            'df': data_frame.to_html(render_links=True, escape=False),
            'form': form
        }
        return render(request, self.template_name_post, context)

