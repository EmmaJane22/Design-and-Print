# Design and Print Website - Emma Scott
## Milestone Project 4 - Full Stack Development

![mockup image](/documentation/wireframes/mockup.png)

## Introduction
Design and Print is a full stack e-commerce website built using Django, Python, HTML, CSS and JavaScript. The website utilises Stripe to process payments.
This project was created as my fourth milestone project for my Level 5 Diploma in Web Application Development with Code Institute.

[Visit Design and Print here.](https://design-and-print-39b5c7712e63.herokuapp.com/)

___

## Table of Contents

* [User Experience (UX)](#user-experience)
  * [Strategy Plane](#strategy-plane)
    * [Project Goals](#project-goals)
  * [Scope Plane](#scope-plane)
    * [Feature Planning](#feature-planning)
  * [Structure Plane](#structure-plane)
    * [User Stories](#user-stories)
    * [Database](#database)
  * [Skeleton Plane](#skeleton-plane)
    * [Wireframes](#wireframes)
  * [Surface Plane](#surface-plane)
    * [Colour Scheme](#colour-scheme)
    * [Typography](#typography)
    * [Imagery](#imagery)
* [Features](#features)
    * [Features](#features)
    * [Future Features](#future-features)
* [Technologies Used](#technologies-used)   
* [Testing](#testing)
  * [Manual Testing](#manual-testing)
  * [Validator Testing](#validator-testing)
  * [Bugs](#bugs)
* [Deployment](#deployment)
  * [Cloning](#cloning)
  * [Django](#Django)
  * [ElephantSQL](#elephantsql)
  * [Deployment to Heroku](#deployment-to-heroku)
  * [Stripe](#stripe)
  * [AWS](#aws)
  * [Email](#email)
* [Credits](#credits)
  * [Code Used](#code-used)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

___

## User Experience

### Strategy Plane

#### **Project Goals**

Design and Print is an e-commerce site (for educational purposes only) that allows customers to order products to be printed, place bespoke orders for printing and for the site owners to run a print business. The timing of this project fortunately occured at the same time that I had a to prepare a presentation for a job interview where, by a happy co-incidence, I was required to provide a business solution for a print service! Hence, Design and Print was born! 

### Scope Plane

#### **Feature Planning**

The main features for production are:
* Home Page
* Product page
* Product search
* Bag/Basket page
* Checkout system
* Payment system via Stripe
* Sign In page
* Sign Out page
* Register page
* Profile page
* Product Management - Admin only
* Bespoke Order page
* Bespoke Quote page - Admin Only
* Bespoke acceptance page
* Submit Review page
* View Reviews page
* Review management - Admin Only

### Structure Plane

#### **User Stories**

| User Story | As a | I want to be able to ... | so that I can... |
| :--- | :--- | :--- | :---|
| 1 | Customer | easily navigate the site | find products easily and find the page that I want quickly. |
| 2 | Customer | register for an account | have a personal account and view my profile. |
| 3 | Customer | receive an email after registration | know my registration was successful.  |
| 4 | Customer | login and logout of my account | access my personal information everytime I visit the site. |
| 5 | Customer | view my profile page  | see my order history and edit my delivery information.  |
| 6 | Customer | view all products on the site  | find the product I am interested in ordering and compare products. |
| 7 | Customer | filter products by categories  | find the specific products I am interested in and compare products in order.  |
| 8 | Customer | view detailed information about a product  | see the specific details of price, size, description and image.  |
| 9 | Customer | view items in my basket  | see the items I want to purchase and the cost.  |
| 10 | Customer | edit the quantity of items in my basket  | increase or decrease quantities.  |
| 11 | Customer | enter my payment details easily  | purchase products with minimal fuss.  |
| 12 | Customer | receive confirmation of my purchases  | track my orders and be assured the order has been processed.  |
| 13 | Customer | place a unique, bespoke order  | purchase a product unique to me.  |
| 14 | Customer | receive a quoted price for my bespoke order  | accept or decline the price before being commmited to purchasing it.  |
| 15 | Customer | leave a review of the service  | provide feedback for the business.  |
| 16 | Customer | read other customer's reviews  | in order to decide if I want to use the service.  |

| User Story | As a | I want to be able to ... | so that I can... |
| :--- | :--- | :--- | :---|
| 1 | Site Admin | easily add products to the site | advertise my products quickly and easily. |
| 2 | Site Admin | easily edit products | update my products quickly and easily. |
| 3 | Site Admin | easily delete products | remove unwanted products quickly and easily. |
| 4 | Site Admin | view the orders being made | assess the work that needs completing. |
| 5 | Site Admin | manage bespoke requests | provide a custom service. |
| 6 | Site Admin | manage customer reviews | remove inappropriate reviews. |

#### **Database **

The relational database ElephantSQL was used for this project. The following data models were used:
* Category - stores information about the product categories.
* Products - stores information about the products.
* Order - stores order infomation.
* User Profile - stores user information.
* Review - stores customer reviews.
* Bespoke orders - stores unique custom orders.

The following schema was created with DbSchema: Database Diagram Designer & Management Tool.

![Database Schema](documentation/images/database.png)

[Back to top](#table-of-contents)
___

### Skeleton Plane

#### **Wireframes**

The wireframes for the project were created using Balsamiq.

* Base Template - this contains a header and a footer which are displayed throughout the site.
![Base Template Wireframe](documentation/wireframes/base_template.png)

* Home Page - The home page features an eye-catching image and a link to go directly to the bespoke order page. The nav bars are responsive on different size devices. The search feature searches through the title and the description of the products in the database and returns any products that match. There is a top nav bar that features drop-down menus to enable the user to navigate the different pages of the site, and to display only certain categories of product from the database. The site title enables the user to redirect to the Home page so they never have to use the browser's back button to navigate. 

![Home Page Wireframe](documentation/wireframes/home_page.png)

* Register Page - This enables users to sign up for an account using their email address. Once they have complete this, a confirmation email is sent to their registration email address which they need to click on to complete registration.

![Register Page Wireframe](documentation/wireframes/register.png)

* Login Page - The login page enables users to sign into their account with their username and password. A toast message displays that the action was successful.

![Login Page Wireframe](documentation/wireframes/log_in.png)

* Logout Page - The logout page enables the user to logout. When the user clicks the logout button, they will be directed to a confirmation page and then logged out of their account and redirected to the home page. A toast message displays that the action was successful.

![Log out Page Wireframe](documentation/wireframes/log_out.png)


* Profile Page - The profile page enables a user to view their default delivery information. It also displays their order history. The user can click on the order for a detailed view of the order. 

![Profile Page Wireframe](documentation/wireframes/profile.png)

* Products - The products page shows all images in the category. It includes an item image and the product details: title, price, category and rating. The page is responsive on different device sizes.

![Products Page Wireframe](documentation/wireframes/products_page.png)

* Product Information - This takes the user to a detailed view of a product. The page includes an image of the product and the product details: title, price, category, and rating. It also includes a quantity selector for the user to choose how many of the product they would like to purchase, and 'Add to bag' button and 'back' to products buttons. This ensures that the user does not need to use the browser ‘back’ button.
![Product Detail Page Wireframe](documentation/wireframes/product_info.png)

* Product Detail (Admin View) - This page is the same as the product detail page, but is only displayed to logged in Admin users. It features edit and delete buttons to allow the admin to edit and delete a product from the database.

![Product Detail Page Admin View Wireframe](documentation/wireframes/product_edit_admin.png)

* Bag Page – This page displays an image of the item, and the product details. The user is then able to select the ‘checkout’ button to complete their purchase or to ‘keeping shopping’ if they would prefer to make further additions. This ensures they do not need to use the browser’s back button to navigate the site. 

![Bag Page Wireframe](documentation/wireframes/shopping_bag.png)

* Checkout Page – This displays the items the user has added to their bag. When the user clicks on the checkout button, they are presented with a form to fill in their details, along with their delivery address. They are given the option to save the information they enter to their profile via a checkbox. The form is pre-populated with this information if they are signed in.
Below this is the payment input section. The user will be required to enter their card information. If there are errors with the information they enter, an error message will be displayed under the input. Once the user clicks on the 'complete order' button, an overlay showing the purchase is in progress is displayed, then a small toast message confirms the purchase has been successful. The user is also redirected to a page that confirms their order number.

![Checkout Page Wireframe](documentation/wireframes/checkout.png)

![Processing Overlay Wireframe](documentation/wireframes/checkout_process.png)

![Checkout Success Wireframe](documentation/wireframes/confirmation.png)


* Bespoke Orders Page – This enables users to request a custom order. The form enables them to select a product category, enter a title, description and colour. They are also able to upload an image to be included on the custom order. Once they have submitted this, the admin is able to provide a quoted price for the order.

![Bespoke Order Page Wireframe](documentation/wireframes/add_bespoke.png)

* Bespoke Orders Admin Page – Due to the nature of a custom order being unique, the Admin user is able to provide a quote for the price of the purchase.

![Bespoke Quote Page Wireframe](documentation/wireframes/quote_page.png)

* All Bespoke Orders Admin Page – The Admin user is able to view all requests for Bespoke orders.

![All Bespoke Orders Page Wireframe](documentation/wireframes/all_user_bespoke.png)


* Bespoke Orders Accept Page – Once the Admin user has provided a quote, the user can accept or decline the quote before the order is processed. 

![Bespoke Accept Page Wireframe](documentation/wireframes/bespoke_accept_quote.png)

* Reviews Page – Users can post a review of the service they have received. This page displays all customer reviews. 

![Reviews Page Wireframe](documentation/wireframes/customer_reviews.png)

* Reviews Page (Admin View) – Admin users can delete a review if they feel it is inappropriate, duplicated, offensive, etc.  

![Reviews Admin View Page Wireframe](documentation/wireframes/admin_customer_reviews.png)

* Add a Review Page – Users can post a review of the service they have received using the form on this page. This form features a title input, a description text area and a rating which is set to a maximum of 5 and a minimum of 1.  

![Add Review Page Wireframe](documentation/wireframes/add_review.png)

[Back to top](#table-of-contents)

### Surface Plane

#### **Colour Scheme**

The colour scheme for the site is very neutral, in order to not disrtact from the products and page content. A dark blue is used on a white background for good contrast and accessibility. The blue background and bright image on the home page are intended to convey the clarity and quality of the business' products. White text is used on this page for high contrast to provide good accessibility. 

#### **Typography**
All fonts are from Google Fonts. I chose 'Righteous' for the logo font and headings as it is crispy and clear and has a profesional look. This has a fall-back font of cursive.
All other text on the site uses 'Raleway' with sans-serif as a fall-back, for accessibility purposes as it is easy to read.

#### **Imagery**
The hero image on the site was chosen to convey a professional, high-quality impression due to it's vivid colours.

[Back to top](#table-of-contents)
___

## Features

### General Features

* Nav Bar - The mav bar consists of two parts: the top header which contains the account icon, the basket icon, the search bar and the site name and the main nav which inclues links to the product categories, reviews and bespoke orders. The nav bar is fully responsive on all screen sizes. On mobile view, a hamburger menu provides ease of access to the nav bar links.

* Footer - The footer contains social media links and contact information, such as phone number, address and email address for ease of access. The footer is responsive on all screen sizes, with the footer headings being hidden on small devices.

* Toasts - These are used to provide feedback to the user, telling them if their action has been successful or if an error has occured. This is conveyed to the user via text and colour. Toasts have a small cross for the user to dismiss them. I deliberately chose not to have them automatically dismiss so a user does not miss the message. 

### Future Features

Ideas for future implementation include:
* Defensive programming -  I had hoped to have time to implement defensive programming to prevent a user accidentally deleting an order.

* Admin approval of reviews - at present customers can post a review without an admin user being able to validate it. This could lead to offensive reviews, which can be removed by admin but would be beneficial to be able to prevent them being displayed at all.  

* Order views on mobile devices - at present, due to time constraints the order summary involves the user needing to do a lot of scrolling to view it. In future I would change this to be more responsive.

* Social Media Logins - The ability for users to log in using a social media account.

[Back to top](#table-of-contents)
___

## Technologies Used

HTML5 - to create the structure of the website.
CSS3 - to style the website.
Bootstrap - to style the website content.
JavaScript - to add interactivity to the website.
Python - to build the backend of the website.
Django - to build the website.
Django Allauth - account management.
Git - version control to commit and push to GitHub.
GitPod - development environment.
Chrome DevTools - to test responsiveness and fix bugs.
Heroku - to deploy the website.
Elephant SQL - the database.
Stripe - to process the card payment functionality.
Amazon AWS - to store the static and media files.
Google Mail - to generate emails.
Font Awesome - website icons.
Google Fonts - website fonts.
Balsamiq - for designing the wireframes.

[Back to top](#table-of-contents)
___

## Testing
### Manual Testing
### Validator Testing

#### HTML
W3C was used to validate the HTML on all pages of the site. It was also used to validate the CSS.

![HTML validator](documentation/testing/html_validator.jpg)
#### CSS

#### Flake8
Flake8 was used to validate the Python code. This showed several over/under indentations, some trailing whitespace, some missing empty lines and several lines that are too long. These issues were all adressed apart from the lines that are too long from migrations, and some of the other lines that are too long, which would need to be addressed in future.


#### Lighthouse Testing

I used Lighthouse in Chrome Dev Tools to run three typical reports on the website:

* Mobile View

Mobile Home page
![Mobile Home page](documentation/testing/mobile_home.jpg)

Mobile Sign In page
![Mobile Sign In page](documentation/testing/mobile_sign_in.jpg)

Mobile Products page
![Mobile products page](documentation/testing/mobile_products.jpg)


* Desktop View

Desktop Home page
![Desktop Home page](documentation/testing/desktop_home.jpg)

Desktop Sign In page
![Desktop Sign In page](documentation/testing/desktop_sign_in.jpg)

Desktop Products page
![Desktop products page](documentation/testing/desktop_products.jpg)

There are a few improvments to be made on the performance on mobile and desktop views which would need to be addressed at a later date.

### Bugs
* The Secret Key was accidentally exposed during a commit. This was recitified by generating a new Secret Key.

* When trying to connect to AWS, the connection was failing when trying to collect the static files and upload them into AWS. Eventually I discovered two typos in custom_storage.py. 

* The footer was not displaying at the bottom of the page when there was no body content. Making the body content 100% resolved this.

* The nav bar wouldn't display towards the beginning of the project. I discovered a typo in the word class. 

#### Unresolved Bugs
* The star rating is set to a maximum value of 5 and a minimum of 1 however the rating incrementor can go beyond 5 and below 0.


[Back to top](#table-of-contents)
___

## Deployment
### Cloning
### Django
### ElephantSQL
### Deployment to Heroku
### Stripe
### AWS
### Email

[Back to top](#table-of-contents)
___

## Credits

### Code Used
* The code for the gradient 'Bespoke' button on the Home page came from https://gradientbuttons.colorion.co/?utm_content=cmp-true
 
### Media
* Tiny PNG was used to compress images. https://tinypng.com/
* Website Mockup Generator: https://websitemockupgenerator.com/

* Images are all royalty free and taken from:

https://www.vecteezy.com/vector-art/1950048-realistic-yellow-notebook-with-a4-paper-set notepad
Business card https://www.vecteezy.com/vector-art/8254460-business-card-design-template
https://www.vecteezy.com/vector-art/692110-circle-cutout-blue-business-card-template business card
https://www.vecteezy.com/vector-art/1893372-vector-modern-creative-and-clean-business-card-template
https://www.vecteezy.com/vector-art/250628-abstract-stylish-wave-business-card-template-design

https://www.canva.com/templates/EAFLhgVjZDo-black-white-simple-real-estate-listing-business-card/
https://www.canva.com/templates/EAFgbWSHdks-red-black-dynamic-gym-trainer-business-card/
https://www.canva.com/templates/EAFQHkE0bec-red-black-creative-modern-business-card/
https://www.canva.com/templates/EAFGMTVbLYU-professional-business-card/

Notepads: 
https://www.vecteezy.com/vector-art/23165690-spiral-binder-notebook-vector-mockup-template
https://www.vecteezy.com/vector-art/1977680-set-of-realistic-notebooks-and-pencil-vector-illustration
https://www.vecteezy.com/vector-art/3231641-notepads-with-empty-lined-and-checkered-paper

Calendars
https://www.vecteezy.com/vector-art/4609884-one-page-2022-calendar-design-template-editable-file
https://www.vecteezy.com/vector-art/3044536-set-desk-calendar-2022-template-design-set-of-12-months
https://www.vecteezy.com/vector-art/94968-2016-calendar
https://www.vecteezy.com/vector-art/16363072-2023-calendar-design-with-holiday-2023-calendar-design-template-calendar-2023-calendar-design

https://www.canva.com/templates/EADahxMOCWc-colorful-illustrated-weekly-calendar/
https://www.canva.com/templates/EAFLbdj0EXc-pink-simple-customizable-october-2022-calendar/
https://www.canva.com/templates/EAFRhP7wQQw-green-creative-weekly-calendar/

Stickers
https://www.canva.com/templates/EAFcYwotyqU-black-and-white-neutral-hand-made-circle-sticker/
https://www.canva.com/templates/EAFVbMJdIso-white-minimalist-aesthetic-thank-you-circle-sticker/
https://www.canva.com/templates/EAFXOUNUcPA-teal-and-white-simple-cupcake-business-circle-sticker-label/
https://www.canva.com/templates/EAFYHoaxixU-pink-simple-product-label-rectangle-sticker/
https://www.canva.com/templates/EAFcfLMbwBM-pink-playful-illustration-shampoo-label/

Flyers
https://www.canva.com/templates/EAFbRy3hG0Y-project-status-report-professional-doc-in-dark-blue-light-blue-playful-abstract-style/
https://www.canva.com/templates/EAFTecJCu-E-project-overview-doc-in-light-green-blue-vibrant-professional-style/
https://www.canva.com/templates/EAFW3qlv8qo-press-release-doc-in-blue-pink-bold-style/

Posters
https://www.canva.com/templates/EAFGG0-jWsc-blue-futuristic-technology-poster/
https://www.canva.com/templates/EAFMo02Phxk-blue-gradient-technology-poster/
https://www.canva.com/templates/EAFH2p69h4g-purple-modern-future-destiny-movie-poster/
https://www.canva.com/templates/EAFNA4Z8qps-red-beige-modern-illustration-blood-donation-poster/
https://www.canva.com/templates/EAFb80T7RhM-grey-black-and-yellow-modern-professional-business-conference-poster/

Brochures
https://www.canva.com/templates/EAFDLsUlh6Q-yellow-modern-geometric-trifold-brochure/
https://www.canva.com/templates/EAFa6775kjs-blue-orange-minimalist-abstract-corporate-business-trifold-brochure/
https://www.canva.com/templates/EADajBG9Ybc-green-and-blue-banking-corporate-trifold-brochure/


### Acknowledgments

[Back to top](#table-of-contents)
___