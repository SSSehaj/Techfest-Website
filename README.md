
# Ignite 6.0 website - A website for the 6th iteration of the annual Techfest of NMIMS Navi Mumbai

  ![booksphere](https://github.com/Progpr/BookSphere-Library-Management-System/assets/95381092/62b65334-49fa-4c27-ab84-615060cdc1b6)


This is a front end only project which acts a medium for students or participants to register for their desired events in the techfest. With the theme of this year's techfest being OTT, I decided to give it a primary theme of Netflix. Here, I created a UI similar to Netflix with the navbar becoming opaque on scrolling plus the events being displayed as a carousel slider. Each event would then lead to a google form so for our participants to proceed to the registration. Next theme is Amazon Prime where I took the time to introduce our team members and some highlights from our last iteration of the techfest. Lastly to promote our sponsors, I created a Disney plus Hotstar like theme. The website was deployed and hosted on Microsoft Azure where I also utilized its private DNS service to set a custom domain. The address of the website (Now Disabled) is https://nm-ignite.co.in/. **My website aided in receiving 366 event registrations**

+ [TechStack](#TechStack)
+ [Features](#Features)
+ [Run Locally](#Screenshots)


## TechStack

+ [Flask](https://flask.palletsprojects.com/en/3.0.x/): The website is created on a flask web application.

+ [Bootstrap 5.3.1](https://getbootstrap.com/docs/5.3/getting-started/introduction/): Front end framework used for creating the OTT-like UI
  
+ [Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=flask%2Cwindows%2Cazure-cli%2Cvscode-deploy%2Cdeploy-instructions-azportal%2Cterminal-bash%2Cdeploy-instructions-zip-azcli): To deploy the flask application to azure app service

+ [Azure CICD](https://learn.microsoft.com/en-us/azure/app-service/deploy-azure-pipelines?tabs=yaml): To setup automated deployment from github actions itself. On commiting to the github branch, changes are automatically reflected on the deployed website.

+ [Google Forms](https://www.google.com/forms/about/): To create Registration Forms for each event.
  
## Features
- **Interfaces:** Separate interfaces for different OTT themes (Adds to the look and feel of the website).
- **Event Registration:** Comprehensive and simple event registration with the help of netflix-like event cards.
- **Comprehensive look:** The overall UI design with the theme provides a comprehensive introduction to the techfest and its essence.

## Run Locally

Clone the project

```bash
  git clone https://github.com/Progpr/ignite5
```

Go to the project directory

```bash
  cd ignite5
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  flask run
```

