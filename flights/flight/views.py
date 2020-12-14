### PACKAGES ###
from django.shortcuts import render   # function to render the html..
from .forms import FlightForm         # class for forms.
from django.views import View         # View class to inherit.
from .scraper import *                # Contains web scraping functions.


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

