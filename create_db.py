from app import db
from app.models import *

from datetime import date
import csv

db.create_all()

with open('attractions_csv.csv') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    count = 0
    for row in csv_reader:
        if count == 0:
            count += 1
            continue
        attraction = Attraction(name=row[0],
                               description=row[1],
                               location=row[2],
                               link=row[3],
                               date_posted=date.today().strftime('%m/%d/%Y'),
                               image_link=row[4])
        db.session.add(attraction)
        db.session.commit()
        count += count