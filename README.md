# Forno Italiano Pizzeria - Project 3


## Table of Contents

 

The link to live project can be found here - https://forno-italiano-pizzeria-ee821493ba58.herokuapp.com/

The link to github repository can be found here - https://github.com/declanwatts97/forno_italiano_pizzeria_project

### Introduction

Welcome to Forno Italiano Pizzeria! We are a small family run pizzeria located in the heart of Newcastle. Explore our site for information about our restaurant, view our vast award winning menu, and why not book a table to come visit us and see for yourself why we are considered the number 1 pizzeria in Newcastle.

## User Experience

### User Requirements

The website has been created with the below goals in mind:

1. Accessability - The website needs to be as accessible as possible so all users can view the site as it was intended.

2. Device Friendly - The website needs to be able to be viewed on devices of all sizes, and on all browsers to ensure our full customer base can access all content.

3. Menu - The website needs to include our Menu, so that our customers can make an informed decision on whether or not they would like to book a table with us.

4. Table Booking - The website needs to include a table booking system so that customers can reserve a table on their chosen dates.

5. Admin access for database - The website needs to have access to the database so that the restaurant manager can view table bookings and arrange service.

## User Stories
### Website Visitors

1. 

### Acceptance Criteria

### Goals of Site Developers

1. 

### Acceptance Criteria

## Structure

The site has 5 active pages:
- A home landing page
- An our restaurants page so customers can view our contact information
- A menu page, so customers can view our menu online with prices.
- A table booking page, so customers can book a table online.
- A table booking success page, so customers are made aware that their booking has been accepted.

### Navbar



### Footer



### Home Page



### Menu Page



### Our Restaurant Page

### Book Table Page


### Book Table Success Page




## Design

### Wireframes



### Colour Scheme

 - The main colour scheme was red for the header and footer, and a light yellow colour for the background of the pages.
 - On multiple web pages theres an additonal white background which sits on top of the yellow background.
 - The button colours on this website are Green.
 - The heading colours on each page are the same red as the header and footer.

### Font

- The font used in this project are just the standard global font for HTML pages.

## Imagery

All images used on this project were taken from unsplash.

Unsplash was used for the hero image, as well as the image on the our restaurant page.

Gemini AI was used to create the business logo.

## Technologies Used

### Development Tools

Github: For hosting code through repositories and deployment.
Heroku: For hosting and deploying the final site.
VS Code: Used for writing and testing local code prior to sending to github.
HTML5: The standard language of a web page.
CSS3: For styling the website.
Javascript - For creating the interactive trivia quiz.
Python - Used through the Django framework for the models, views, url's of the site.
Django - the django framework was used for the building of this site.
Taiwind: To create responsive design and also page styling through the use of classes.
Favicon.io: For adding the favicon on the title bar of webpage.
Gemini AI - for troubleshooting as well as producing logos and ideas for the menu.
PostgreSQL - for hosting the site database.

## Deployment

### Deployment to Heroku

This site has been deployed to Heroku. To view, please see below:

1. View the GitHub repository. This project is found at title (https://github.com/declanwatts97/forno_italiano_pizzeria_project)
2. You can view the deployment on Heroku by visiting https://forno-italiano-pizzeria-ee821493ba58.herokuapp.com/

### Deployment Procedure

See below step by step instructions for how to deploy to Heroku:

1. Create a new app on Heroku with a unique name.
2. Click on the settings tab and reveal the config vars. Add a key of DISABLE_COLLECTSTATIC and add a value of 1.
3. Install a production ready web server to your project with pip3 install gunicorn~=20.1.
4. Add your web server to requirements.txt with pip3 freeze --local > requirements.txt
5. Create a file named Procfile at the root directory of the project.
6. In the Procfile add web: gunicorn my_project.wsgi.
7. In your settings.py file add '.herokuapp.com' to your allowed hosts list.
8. Return to heroku and click on the deploy tab.
9. Connect and log in to github after clicking the connect to github box.
10. Scroll to the bottom of the page and manually deploy your site on the main branch.
11. Open the resources tab and choose an Eco Dyno.
12. Click open app to view your deployed project!

### Deployment to Heroku

## Testing

### User Stories Testing

1. 

### Manual Testing

1.

### Testing Summary



### Browser Compatibility



## Credits
### Content and Inspiration

Images: images taken from Unsplash free as uploaded by other users.
Content: content inspired by Gemini AI for Menu and Logo.

### Acknowledgements 

Tailwind: for most of the styling used on the website.
Code Institute: for ideas, assistance and the LMS, which was referred back to while designing this project.
Favicon.io - for the favicon used in browser title.
Unsplash - for all images used on the webpage.
Gemini AI - for the logo and some menu ideas, as well as occasional assistance troubleshooting.



## Contact Information
- For any queries or feedback, please contact declan.watts97@gmail.com

