import csv
from flight.models import Airport

def run():
    loader = open('scripts/iata_db.csv', 'r')   #
    reader = csv.reader(loader)    #
    next(reader)                   # advance past the header.

    Airport.objects.all().delete() # clean up the table.

    for row in reader:
        print(row)
        if len(row) == 3:
            a = Airport(city_name=row[0], country_name=row[2], iata_code=row[1])
            a.save()