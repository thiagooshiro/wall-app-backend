# wall-app-backend
wall-app-backend is a backend REST API utilizing Django and Django Rest Framework.
It's a socialmedia app where users can make posts can make posts in a wall.
The Front-End of this app its comming up soon =)

**Here are some of the business rules for this API:**

**1** - Users must be authenticated. On user registration they recieve and confirmation e-mail.

**2** - Users and Guests are able to see all posts.

**3** Users can only delete or edit their own posts.

# Installing
It is recommended to install the required packages for the project in a virtual enviroment.
This is the command to create the virtual enviroment:

**python3 -m venv .venv**

To activate it just run:

**source .venv/bin/activate**

To install the required packages run:

**pip install -r requirements.txt**

Then you should be good!

# Structure:

accounts: is the app tha manages user interations,
there is a custom User and a custom UserManager class implemented
because I wanted email to be the login field. 
Here you will find the classes that operate the CRUD for User, 
at the moment it is only possible to create and list users, but not edit or delete them.

postwall: is the app that manages the wall posting,
all the rules and classes necessary to create, edit, delete or read posts.

wallapp: is the main project folder, most important file here is the settings
that was altered in a lot of ways to use enviromental variables with dotenv, and 
the email settings necessary to send an email on user sucessful registration.

 # Enviromental Variables:
There are some env. variables that I needed to set, their names and functionalities are as follows:
 
SECRET : This one is to hide the django key that is in settings.py in a env variable so its not exposed.

EMAIL_HOST_USER: For the email sending the confirmation e-mails.

EMAIL_HOST_PASSWORD: It is required to provide a password to be able to sent e-mails.

SENDGRID_API_KEY: It is a generated unique key so you can use Sendgrid to sent emails.

DEFAULT_FROM_EMAIL: When no e-mail for sender is provided it takes this one as the sender email.

# Tests: 

I used coverage package to run tests and generate reports, the configuration for coverage is in the covergarerc file.
You can run:

**python3 manage.py test** 

Or if you and a report and see the test coverage for the app you run:

**coverage run manage.py test && coverage report && coverage html**

The HTML file that this report generates is really useful.

# Final Observations: 

It is not a finished project yet. I learned a lot while making it but its not optmized. I intend to change it a little more and make it better.
I wrote this readme in the intent that one can use this project as a basis to understand Django and Django Rest Framework and how powerful they can be.
There are a lot of good references in the web, and the documentation for Django and Django Rest Framework it is really good and I lot of what I learned
from theses sources to be able to do this project.

 
