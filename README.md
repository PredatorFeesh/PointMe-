# PointMe!

## Description

We are building an application that will give users access to a database of points of interests in New York City. Users can also set up events and add them to the database to market it to other users. Posts will contain general information and a brief description about the event. The app will cater to a diverse range of interests, especially college students, as there aren’t quite many applications that cater specifically to the college going population of New York City. Other applications like EventBrite, and MeetUp aren’t necessarily for students. This app seeks to fill in the niche with more added functionality than offered by the other apps. <br />

This software is interesting because it allows users to have access to a vast collection of activities, events, and attractions that they may partake in. Users can provide criteria and filters to narrow down their searches when searching for activities, i.e. expensive and inexpensive; tourist and non-touristy attractions to narrow down their search. This will allow the users to find an activity tailored to them, based on existing activities. In addition to that, there is another functionality--users can participate in the listing of events. Users may categorize their posts to better market their events to desired audiences. Lastly, users can follow events for notifications, as the date of the event approaches. <br />
	
Our application is similar to NYCGO.com, New York City The Official Guide, sponsored by the City of New York. It’s a website that allows users to browse various attractions in New York City by category. In addition to that, the website shows current activities as well as future activities, and their location. The key difference between our application and NYCGO is that NYCGO has a curated list of events and attractions, while our application allows users to create and market their own events whereas. Our application is more flexible, and allows the better marketing of smaller events that may otherwise go unnoticed. <br />

## How we are building it

We are using Python3 Flask in order to actually render our website. To make it concurrent for more than 1 user, we are using gunicorn.

## Features

- Create local events and post them for other users to see
- View events posted by other users
- View a curated list of attractions that are in New York City
- Follow other users and see events they created and users they follow

## Proposed Schemas

- Users(userid,  name, passwordhash, emailaddress, dateofbirth, phonenumber)
- Events(eventid, datestart, dateend, name, description, location)
- Attractions(attractionid, location, name, description)
- UserFollows(userid, useridtarget, date)

## How to run

### Modules

First, install all the pip files. To do this, type pip3 install -r requirements.txt. Next, you need to set up the database.

If you get a database error, make sure mysqldb actually installed for Python3 (and make sure your sql server is active). Install with `pip3 install mysqlclient` <br />

### Database

First, make sure you are running a mysql server on your laptop. Then, make sure you configure a user called test with password 'password' and create a database pointme, <b> OR YOU WILL GET AN ERROR </b>.

Might later change to SQLLite instead of MYSQL, unless we migrate to a server
Now, you need to create all the tables we are using. To do this, run `python3 create_db.py` <br />


### Running

Now, you can run the server. To run the server, type `python3 run.py`