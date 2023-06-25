# Design and Print Website - Emma Scott
## Milestone Project 4 - Full Stack Development

![mockup image](/documentation/mockup.jpg)

## Introduction
Design and Print is a full stack e-commerce website built using Django, Python, HTML, CSS and JavaScript. The website utilises Stripe to process payments.
This project was created as my fourth milestone project for my Level 5 Diploma in Web Application Development with Code Institute.

[View the live project here.](https:/ "View the live project here")

___

## Table of Contents

1. [User Experience (UX)](#ux)
    - [User Stories](#user-stories)
        - [Target Audience](#target-audience)
        - [First Time User Goals](#first-time-user-goals)
        - [Frequent User Goals](#frequent-user-goals)
    - [Design](#design)
        - [Colour Scheme](#colour-scheme)
        - [Typography](#typography)
2. [Features](#features)
    - [Wireframes](#wireframes)
    - [Features](#features)
    - [Future Features](#future-features)
3. [Technologies](#technologies)
    - [Languages](#languages)
    - [Frameworks & Libraries](#frameworks-and-libraries)
    - [Storage & Hosting](#storage-and-hosting)
4. [Testing](#testing)
5. [Deployment](#deployment)
    - [Heroku](#heroku)
6. [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)

___

## 1. User Experience (UX)

## User Stories

### Target Audience

### First Time User Goals

As a first time user, I want to be able :
* 

### Frequent User Goals

As a returning user, I want to be able to:
* 

### Administrator Goals

As an administrator of the site, I want to be able to:
* 

## Design
### Colour Scheme

### Typography

[Back to top](#table-of-contents)
___

## 2. Features

### Wireframes

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





### Features

#### Nav Bar

#### Footer
___

### Pages

The website consists of X pages that run from a base page:

* pages list

#### Page

#### Page

#### Page

#### 404 Error Page
___

### Future Features
Ideas for future implementation include:

 - 

[Back to top](#table-of-contents)
___

## 3. Technologies

### Languages

*

### Frameworks & Libraries

* 

### Storage & Hosting

* 

[Back to top](#table-of-contents)
___

## 4. Testing

A separate [TEST.md](TEST.md) file has been created for the documentation of testing.

[Back to top](#table-of-contents)
___

## 5. Deployment
### Heroku

To deploy 

### Cloning the Git Hub Repository

[Back to top](#table-of-contents)
___

## 6. Credits
### Content

* 

### Media

### Acknowledgements

* Thank yous

[Back to top](#table-of-contents)
___