# Forno Italiano Pizzeria - Project 3

The link to live project can be found here - https://forno-italiano-pizzeria-ee821493ba58.herokuapp.com/

The link to github repository can be found here - https://github.com/declanwatts97/forno_italiano_pizzeria_project

### Introduction

Welcome to Forno Italiano Pizzeria! We are a small family run pizzeria located in the heart of Newcastle. Explore our site for information about our restaurant, view our vast award winning menu, and why not book a table to come visit us and see for yourself why we are considered the number 1 pizzeria in Newcastle.

## Table of Contents

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

1. As a user I require a clean single design, emphasising the main features of the website so I can access the information I need easily.

2. As a user I require easy clear navigation, so that I can make my way to which ever page is required for my visit. 

3. As a user I require the website to be responsive, so that I can access it on any device I may have. I require ease of access to book up at any time.

4. As a user I require a book table option, so I can reserve a table online and not have to call during busy hours.

5. As a user I require contact information for the restaurant, so I know the address for my visit and the phone number/email for any queries not answered by the website.

6. As a user I require an expansive menu with prices, so that I can decide if I want to visit, and plan my meal prior to arrival.

### Acceptance Criteria

1. The user should load into the page being clean, uncluttered using consistent typography and colour scheme. All main features should be visable and images load quickly.

2. The user should be able to view the navbar on all pages, with it visable at the top on desktop and as a hamburger menu on mobile and tablet. All navigation links should be clearly labeled and take you to the correct page on click.

3. When the user accesses the website with a tablet, phone or on desktop the layout should adapt with no horizontal scrolling. The book table button should be accessible and working from the navbar and homepage. All interactive elements should remain funtional across browsers. 

4. When the user is on the book table page, they should be prompted to fill in Full Name, Email, Phone Number, Date, Time and Party Size. A confirmation message should show up when submitted or an error if there is a double booking. The booking should be stored in the database. All required fields should be validated before submission.

5. When the user is on the our restaurant page, the full address, email, phone number and opening times should be clearly listed. The opening hours should be clearly listed by day.

6. When the user navigates to the menu section, the items should be grouped into main categories and each item has a price. Prices should be aligned directly to the right for easy scanning.

### Goals of Site Developers

1. As a developer I require clean code which follows the standard for readability. This ensures any changes can be easily made and the code understood by other contributors.

2. As a developer I require a database model relevant to the project and entity relationship diagram to outline the reason for the model.

3. As a developer I require the site to be responsive on all devices and browsers, allowing the customer base the best possible experience when viewing the site.

4. As a developer I require a detailed Readme document which outlines the planning, development and deployment procedure.

5. As a developer I require customers to be able to book tables, and if a double booking occurs that they are notified and the booking returns an error message.

### Acceptance Criteria

1. In the finished project, all HTML should follow semantic structure, all indentation is consistent, and the pages should pass through validation without error.

2. In the project repository, there should be a models.py file with the designed model for the database and also an entity relationship diagram shown in the readme.

3. When the site is deployed and tested on Mobile, Tablet and Desktop then no layout breaks should occur, and all content should resize nicely to fit chosen device.

4. If a new contributor clones the repository and opens the readme, they should have a full description of the purpose of the project, design choices made and the deployment procedure.

5. If a table is already booked for a specific date or time and a second user tries to book, the system should check availability in real time and return an eror message if double booked.

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

![home](static/readme-images/home.png)

### Menu Page

![menu](static/readme-images/menu.png)

### Our Restaurant Page

![our restaurant](static/readme-images/our-restaurants.png)

### Book Table Page

![alt text](static/readme-images/book-table.png)


### Book Table Success Page

![alt text](static/readme-images/booking-success.png)


## Design

### Wireframes

The below wireframes were created at the beginning of the design process, these were to be the layout followed for the creation of the site:

![wireframe-1](static/readme-images/wireframe-1.png)

![wireframe-2](static/readme-images/wireframe-2.png)

![wireframe-3](static/readme-images/wireframe-3.png)

### Entity Relationship Diagram

![ERD](static/readme-images/ERD.png)

The entity relationship diagram for this project is a single entity, meaning there are no one to many or many to many relationships. This entity stands alone.

This shows the chosen model behind the database for the table booking system which has been put in place for the website.


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

- Github: For hosting code through repositories and deployment.
- Heroku: For hosting and deploying the final site.
- VS Code: Used for writing and testing local code prior to sending to github.
- HTML5: The standard language of a web page.
- CSS3: For styling the website.
- Javascript - For creating the interactive trivia quiz.
- Python - Used through the Django framework for the models, views, url's of the site.
- Django - the django framework was used for the building of this site.
- Taiwind: To create responsive design and also page styling through the use of classes.
- Favicon.io: For adding the favicon on the title bar of webpage.
- Gemini AI - for troubleshooting as well as producing logos and ideas for the menu.
- PostgreSQL - for hosting the site database.

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

- Images: images taken from Unsplash free as uploaded by other users.
- Content: content inspired by Gemini AI for Menu and Logo.

### Acknowledgements 

- Tailwind: for most of the styling used on the website.
- Code Institute: for ideas, assistance and the LMS, which was referred back to while designing this project.
- Favicon.io - for the favicon used in browser title.
- Unsplash - for all images used on the webpage.
- Gemini AI - for the logo and some menu ideas, as well as occasional assistance troubleshooting.



## Contact Information
- For any queries or feedback, please contact declan.watts97@gmail.com

