# The Inovance Lab


The Inovance Lab is an e-commerce store derived from a French Laboratory Ysonut.fr that produces nutraceutical and dietary products. With a strong focus on office health it attempts to start a new office norm through proper support of the Circadian Rythm. In addition to basic products it has started to sell a Phyto brand which is 100% plant based. 

The current deployment has been made for functionality purposes, the store will in the future comprise 100 of products making its functionalities such as price order, categories and searching relevant. In the long term, the idea is to provide office nutritional products enabling health and boosting the productivity of employees through subsidised micro-nutrition by the employer.

You can access the site here: theinovancelab.herokuapp.com

## Table Of Contents

1. [**UX**](#ux)
    - [**Project Goals**](#project-goals)
    - [**User goals**](#user-goals)
    - [**Developer Goals**](#developer-goals)
    - [**User Stories**](#user-stories)
    - [**Design choices**](#design-choices)
    - [**Wireframes**](#wireframes)

2. [**Features**](#Features)
    - [**Main Features**](#main-features)
    - [**Important Apps**](#important-apps)
    - [**Allauth Templates**](#allauth-templates)
    - [**Future Features**](#future-features)
    - [**Languages & Technologies Used**](#Languages-technologies-used)
    - [**Testing**](#testing)

3. [**Deployments**](#deployments)

4. [**Credits**](#credits)

5. [**Media**](#media)

6. [**Acknowledgements**](#acknowledgements)

# UX

## Project Goals

The project goal has been to develop a first version e-commerce site to sell Phyto and Inovance Brand products under the name of "The Inovance Lab". This being said, Inovance is the name of the Micro-nutrition products of Ysonut.fr. The idea is to start selling in both the United States and Europe. As this is a pilot project we would like to carry out in Miami, we have denominated the pricing in USD. The interesting, part of the website is the user profile, as later it would be the source of intelligent profiling for suggestion making based on past purchases and logical in-take plans when it comes to nutraceuticals.


### User Goals

* A site to purchase products of Ysonut.fr under "The Inovance Lab" brand name.
* An e-commerce store where I can find nutraceutical soltuion to specific problems/themes.
* A site where I can enquire about problems and receive advise concerning Nutraceutical product intakes,
* A user friendly, easy-to-use e-commerce experience with logical and fast-going processes from product browsing to checkout.
* To have a login functionality where a user can easily find its personal space and information with his current orders, order history and more.
* To have a secure checkout with a credit card payment gateway.

### Developer Goals

* To be able to sell Inovance and Ysonut products on a global basis, starting with the United States. 
* To help improve my users health and well-being through adequate information provision and product-problem association.
* To be able to keep track of my sales and manage my products through an admin portal.
* To be able to easily create, view, update, and delete my products available across the platform.

## User Stories

#### As a User:

1. I want to be able to access this e-commerce site and easily browse through products, classes and offers.
2. I want to be able to access this site on my computer, tablet and phone.
3. I want to be able to add and remove products from my shopping cart, and purchase them through my own account.
4. I want to be able to be able to see the product information and provide rating a rating upon purchase.
5. I want to receive notifications related to my actions.
6. I want to be able to see shipping cost information and what I still need to purchase in order to have free shipping.
7. I want to be able to save my billing details, and personal information for further purchases.
8. I want to be able to contact the site-owner/manager if I need to or if I have a question.

#### As a Developer:

1. I want to manage a UX driven ecommerce site where loyalty is boosted by ease of use and repeat product purchase.
2. I want to be able to manage my products and categories easily via my access. 
3. I want to be able to see users that have made purchases.
4. I want to be able to store the media and images related to my site on a relevant cloud service provider directly linked to my e-commerce site.
5. I want to be able to receive payments through stripe in order to approve shipping.

## Design Choices

* The design of this e-commerce was made with the Guidance of Boutique Ado demonstration of the Code Institute. I took the design over with slight alterations, as it fits the ambitions of my company to have a simple, straightforward and non-complex exposition of the products and brand. As a laboratory, the domination of the white color on the site is important for its users to perceive it as clinical. 

#### Fonts

* For the fonts, I used Lato obtained through google fonts for its cleanliness, which relates to the previous Design choice justification. 

#### Icons

* Icons were imported from Font Awesome and relate to ecommerce logic or health. (Credited at the end)

#### Colours 

* The colours used are focused on white, black green and a bit of yellow for notifications.

#### Background, Images & Audio

* All images used throughout the site are either property of Ysonut SL, or have been obtained through unsplash. There are no dense pictures or background images in the site, neither should there be. 
* Background used are white of nature.
* Product images originate from the product database of Inovance and should all be with white background colours. 
* Home page might change in the future, as it is complex to find the perfect background picture for an pharma/clinical site that matches perfectly with the theme at hand.


## Wireframes

# Features 

## Main Features

* HOME PAGE - The home page consists of the navbar and a mid-section occupying the totality of the page with a background image containing a button that leads to the shop. 

* NavBar - On each pagem, the NavBar is available and contains NavLinks, the branding, a search bar, login functionality, logout functionality, registration, account functionalities/access when logged in and the shopping cart. Functionality of a logged in admin reflects CRUD capacity on Navbar, which enables product management.

* Products pages - This page is dedicated to all products of the group and has alike all other product category pages functionalities such as filtering, rating and picture display and more. 

* Phyto pages - This page is similar to the all products page, but it contains the 3 core phyto products of the group, understood as one category.  

* Well-being pages -  This page is similar to the all products page, but it contains the all well-being products of the group, understood as one category.  

* Product details page - When navigating to the product details page, one finds all relevant information concerning the product, its rating, its purpose, title and purchasing call-to-action with quantity selection capacity. Whenever adding a product to cart from this page, a notification is triggered in the top right corner of the page, allowing the user to obtain confirmation, grand total etc. 

* Bag page - The bag page enables the user to see their order size, edit it by adding or removing products and allowing to proceed to secure checkout or continue shopping. 

* Checkout page - The Checkout page enables the user to proceed to their purchase by seing their order again, filling in their billing and shipping details and executing their purchase. If the user is already logged-in then their details will appear.

* Checkout success page - Once the checkout is successfully concluded, this would entail receiving a "success message" on the success page. It would automatically send an email with confirmation and allow the user to continue surfing the store with a button.

* Product Management - A page where admin users can add, review, edit and delete products. 


## Important Apps 

* Bag App - app enabling full bag process and the capacity to add products, sum them etc.
* Checkout App - Connects to psp, enables checkout, security oriented.
* Products App - All actions and code concerning products.
* Profiles App - All actions and code concerning profiles and user authentication.


## Allauth Templates
Allauth templates were used throughout the site for user creation, login, logout and handling forgotten passwords.

# Features left to Implement

1. KYC form for product suggestions. Detect if user is a woman or man, detect allergens and associate products based on detailed identification.
2. Implement all 120 products of the Inovance Brand into the store.
3. Add essential pages, such as about us, information concerning the lab and more. 

# Languages & Technologies Used

* [HTML](https://www.w3schools.com/html/)  - HTML is used as frontend language throughout the site.
* [CSS](https://www.w3schools.com/css/) - CSS is used in a main styling file for the site's design.
* [JavaScript](https://www.w3schools.com/js/) - JS has been used for notifications animations and more small effects through the site.
* [PYTHON](https://www.python.org/) - Python is the main language for this platform.
* [BOOTSTRAP](https://getbootstrap.com/) - Bootstrap elements have been used. Please note that v4 has been used in this code, not v5. 
* [Font Awesome](https://fontawesome.com/) - FA used to implement all the icons for improving UX and the website design.
* [Code Institute](https://codeinstitute.net/) - Learning institute that supported this project with knowledge and guidance, including tooling.
- [Gitpod](https://www.gitpod.io/) - IDE used to develop this project. (+ VS code, which is linked).
- [Github](https://github.com/) - Store and share all project code remotely. (with Github pages)
- [PIP](https://pypi.org/project/pip/) - Used to install tools needed for this project.
- [Stripe](https://stripe.com/en-gb) - PSP used for project.
- [Amazon AWS](https://s3.console.aws.amazon.com/s3/) - Used to store static and media files.
- [SQLite3](https://www.sqlite.org/index.html) - Used for the development database.
- [JQuery](https://jquery.com/) - DOM manipulation framework 
- [Google Fonts](https://fonts.google.com/) - Website fonts. 
- [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) - Django application addressing authentication, registration and account management.
- [Django](https://www.djangoproject.com/)  - Used to construct, build and render apps and pages. 
- [Django Crispy Forms](https://www.djangoproject.com/)  - Application to help to manage and render Django forms.
- [Heroku](https://www.heroku.com/what)  - Cloud platform used to host the website.

# Testing

## Testing the stories from the UX section

### As a User: 

1. I want to be able to access this e-commerce site and easily browse through products, classes and offers.

* There is a straightforward browsing, with call to actions, clear navbar and no hidden paths. Everything is self explanatory and within 3 clicks away.

2. I want to be able to access this site on my computer, tablet and phone.

* The website is device friendly thanks to frameworks like bootstrap and you can see that fonts and images adjust based on px dimensions. 

3. I want to be able to add and remove products from my shopping cart, and purchase them through my own account.

* You can easily add and remove products by selecting the quantity you wish to add to bag, clicking the add to bag button and navigating to the bag through clicking on the shopping bag icon on the top right corner of the screen, or by clicking on the go to secure checkout button on the toast that is issued upon adding iterms to bag. Once inside the bag, you can easily remove items or change the quantities. When logged in you will automatically find your details directly pasted onto the order forms.

4. I want to be able to be able to see the product information and provide rating a rating upon purchase.

* When clicking on a product, all information appears and you can provide a rating by email, which the staff with admin accounts can implement. 

5. I want to receive notifications related to my actions.

* Toasts are issued throughout the website and appear in boxes, mostly related to adding products to the cart. 

6. I want to be able to see shipping cost information and what I still need to purchase in order to have free shipping.

* Shipping cost information is always displayed as a standard below the navbar and within toasts notification and on the shopping bag page there is an indication of how much product value still needs to be purchased before the shipping costs are set to zero.

7. I want to be able to save my billing details, and personal information for further purchases.

* When logged in you can either input your information under the "My_profile" page or they are saved into the system upon first purchase. 

8. I want to be able to update my personal information.

* You can update your personal information unde the my profile page accessible through a dropdown menu issued by clicking on " My account"


#### As a Developer:

1. I want to manage a UX driven ecommerce site where loyalty is boosted by ease of use and repeat product purchase.

* All elements bolstering the User experience are present, ease of use, customer database, mailing system, future offers to be implemented but already existing, user profiles enabling speed purchases, fair shipping policy etc. 

2. I want to be able to manage my products and categories easily via my access. 

* Once logged in, the admin user can easily enter the product management by clicking "My Account". In there products can be added. Most important, once in the admin profile, products can be edited or removed throughout the website by simply clicking on the produts and choosing the "delete" or "edit" option.

3. I want to be able to see users that have made purchases.

* Within the django envrionment accessible through [here](https://theinovancelab.herokuapp.com/admin/) you can enter the full admin panel and retrieve all necessary information points. 

4. I want to be able to store the media and images related to my site on a relevant cloud service provider directly linked to my e-commerce site.

* By using AWS S3, the site has all its media, images and static data stored securely on their cloud platform. 

5. I want to be able to receive payments through stripe in order to approve shipping.

* A stripe account has been made and fully integrated and succesfully tested with the platform.


### ON THE GO TESTING / PROBLEMS

1. General

* Continuous testing has been performed on the code and the site throughout the development as this is a functionality-bound development. Many mistakes were founds including inconsistencies, which might have escaped the developer. On the overall the site is fully functional and pending some logical changes after this first version, such as footer and more information on the background of the company. However, the overall flow, speed and logic of the ecommerce store have passed the surface testing.

2. Authentication 

* Authentication, registration and profile management have been tested. Throughout the development and with the intial submission of the project, an error blocking the log in of the admin or customer was present. After thourough examination and code review, the issue was spotted in the global settings.py where in the LOGIN_REDIRECT_URL the value was set to '/succcess', whereas it should have been '/'. This bug has been resolved and now all users can succesfully log in into their account and access their functionalities. A thorough review of all URLS was conducted as well on global and app level.

3. HTML/CSS

* Errors linked to the Jinja templating language were found within the checkout app and profiles app, which affected the HTML and CSS rendering of these pages. These have since been corrected. The CSS connection to bootstrap works perfectly and all styles and media are properly linked. Within the workspace of the IDE, the images do not render anymore, this is due to the AWS storage, but on the herokuapp they render perfectly. 

4. Product Set Up

* All products render fine. For a further version and before official go live it is crucial to add information to these products, such as content, pharma licences, perscription requisits etc. However, for an initial version this is fine, as it allows for proper functionality demonstration.

5. Searching

* Searching works fine and all dependencies are well installed. Test worked from the get go.

6. Shopping Bag

* Shopping bag issues concerning rendering were met and solved, as mentioned previously. CSS issues were fixed in an earlier version after not properly rendering styles. 

7. Product Modification

* It is possible to modify products by clicking on edit/delete buttons, which comes to succesfully prove all CRUD functionalities.

8. Toasts

* In the beginning and due to JavaScript issues, the toasts did not render or render to the left side of the screen under the NavBard. This was fixed with proper JavaScript and reliance on both Stack Overflow and the Code Institute Slack Community. Toasts work perfectly fine now, when adding products or other actions, toasts succesfully render.

9. Checkout

* The checkout works fine and information is well received through stripe. The test was conducted with the "42424242" account details. Some isssues concerning locations were met during development, but these have since been solved.

10. Stripe Payments

* When tested with the "42424242" credit card from Stripe, payments succesfully enter the testing environment.

11. Profiles, admin and normal

* The main issue, which led to revising the full code of the profile app, was the login redirect mistake mentioned earlier. For the rest, the Admin profile works fine both in the Django Administration and the platform authentication. The Allauth environment is correctly set up, with confirmation mails working and loging/logout pages rendering correctly. Post and GET methods are operational.


12. AWS & Heroku

* Both AWS & Heroku are succesfully set up and the project is fully deployed to both. Hence the working of the project on the Heroku domain. 

### POST-CONTRUCTION TESTING

* The lighthouse testing was mostly successful with the following scores: Best Practices 100%, Performance 74%, Accessibility 88%, and SEO 91%.

* Pylint issues are still present.

* Code Refactoring was partly succesful, as some PEP8 issues still remain, with lines being too long.


# Deployments

You can access the site here: theinovancelab.herokuapp.com

## Heroku

I deployed this project through Heroku by following the steps below:

1. Generate a "requirements.txt" file using the terminal command "pip freeze > requirements.txt".

2. Generating a "Procfile" with the terminal command "python app.py > Procfile".

3. Publishing by: "git add . " and "git commit -m" committing the requiremnts.txt and Procfile", then "git push" to GitHub.

4. I created a new app on the [Heroku](https://www.heroku.com/) 

5. From The Inovance Lab dashboard, I clicked on "Deploy" > "Deployment method" and selected Github.

6. In the Heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

7. Remove DEVELOPMENT = True and DISABLE_COLLECTSTATIC = 1.

8. In the Heroku dashboard, click "Deploy".

9. The site is successfully deployed.


# Credits

* [Code Institute](https://learn.codeinstitute.net/courses) -  The Boutique Ado project.
* [BOOTSTRAP](https://getbootstrap.com/)

A lot of the website is based on the Boutique Ado Project, but will be used in real life. The functionalities, branding and all extra coding arround the project has been my original work.

# Font

* I used Lato throughout the website with through the google fonts library.

# Media

* Product images were sourced from [Ysonut](https://www.ysonut.fr/) & [Unsplash](https://unsplash.com/).

* All images within this website are the property of Ysonut.fr and I do not possess the rights to these, apart from the approval to use those.

* Icons were sourced from [Font Awesome](https://fontawesome.com)

# Acknowledgements

* [Code Institute](https://learn.codeinstitute.net/courses) 
* [W3Schools](https://www.w3schools.com/)
* [Stack Overflow](https://stackoverflow.com/).
* [Github Pages](https://pages.github.com/)
* [Font Awesome](https://fontawesome.com)
* [BOOTSTRAP](https://getbootstrap.com/)
* [Ysonut](Ysonut.fr)
