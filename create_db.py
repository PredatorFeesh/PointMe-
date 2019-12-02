from app import db
from app.models import *

from datetime import date

db.create_all()

statue_of_liberty = Attraction(name='Statue of Liberty',
                               description='The Statue of Liberty is a colossal neoclassical sculpture on Liberty Island in New York Harbor in New York, in the United States.',
                               location='Liberty Island',
                               link='https://www.nycgo.com/articles/guide-to-the-statue-of-liberty',
                               date_posted=date.today().strftime('%m/%d/%Y'),
                               image_link='https://assets.libertyellisfoundation.org/cms/editor/About_the_Statue_Header_[Resized_826_x_300].jpg')
db.session.add(statue_of_liberty)
db.session.commit()