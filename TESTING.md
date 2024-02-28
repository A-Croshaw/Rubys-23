# _Test Menu_

- [Test Menu](#test-menu)
- [Functional Testing](#functional-testing)
    - [Authentication](#authentication)
    - [Profile](#profiles)
    - [Books](#books)
    - [Book Management](#book-management)
    - [Shooping Cart](#shopping-cart)
    - [Checkout](#checkout)
    - [About](#about)
    - [Contact](#contact)
    - [Newsletters](#newsletters)
    - [Subscribe](#subscribe)
    - [Navigation](#navigation)
    - [Footer](#footer)
- [Bugs](#structure-plane)
- [Validation](#features)
    - [PEP8 Valadator](#implemented-features)
    - [W3 Valadator](#site-features)
    - [Lighthouse Report](#home-page)
- [Responsiveness](#header)
## _Functional Testing_

### _Authentication_
#### Registration
**Description**:

    a user can sign up to the website

**Steps**:
1. Navigate to [_Ruby's_](https://rubys-97a7171770c1.herokuapp.com/) go to  the account menu and click Register.
2. Enter email, username and password 

3. Click Sign Up Button

**Expected**:

    After clicking on the "Sign Up" button registration is successful, User is redirected to the home page

**Actual**: 

    clicking on the "Sign Up" button registration is successful, User is redirected to the home page
<hr>

#### Sign In
**Description**:

    a user can sign in to the website

**Steps**:
1. Navigate to [_Ruby's_](https://rubys-97a7171770c1.herokuapp.com/) go to  the account menu and click Login.

2. Enter email or username and password 

3. Click Sign In button

**Expected**:

    After clicking on the "Sign In" button user is signed in and redirected to the home page

**Actual**: 

    clicking on the "Sign In" button user is signed in and redirected to the home page
<hr>

#### Sign In
**Description**:

    a user can sign out of the website

**Steps**:
1. Navigate to [_Ruby's_](https://rubys-97a7171770c1.herokuapp.com/) go to the account menu and click Sign Out.

2. Click confirm on the confirm logout page

**Expected**:

    After clicking on the "Sign Out" Link user is redirected to confirm logout page, Click the Confirm button and the user is logged out and redirected to the home page

**Actual**: 

    Clicking on the "Sign Out" Link user is redirected to confirm logout page, Clicking the Confirm button and the user is logged out and redirected to the home page
<hr>

### _Profile_

#### 
**Description**:

**Steps**:
1. Navigate to [_Ruby's_](https://rubys-97a7171770c1.herokuapp.com/) go to the account menu and click Signin.

**Expected**:

**Actual**: 

<hr>



### _Books_
#### 
**Description**:

**Steps**:
1. Navigate to [_Ruby's_](https://rubys-97a7171770c1.herokuapp.com/) go to the account menu and click Signin.

**Expected**:

**Actual**: 

<hr>

### _Book Management_
#### 
**Description**:

**Steps**:
1. Navigate to [_Ruby's_](https://rubys-97a7171770c1.herokuapp.com/) go to the account menu and click Signin.

**Expected**:

**Actual**: 

<hr>

### _Shooping Cart_
#### 
**Description**:

**Steps**:
1. Navigate to [_Ruby's_](https://rubys-97a7171770c1.herokuapp.com/) go to the account menu and click Signin.

**Expected**:

**Actual**: 

<hr>

### _Checkout_
#### 
**Description**:

**Steps**:
1. Navigate to [_Ruby's_](https://rubys-97a7171770c1.herokuapp.com/) go to the account menu and click Signin.

**Expected**:

**Actual**: 

<hr>

### _About_
#### 
**Description**:

**Steps**:
1. Navigate to [_Ruby's_](https://rubys-97a7171770c1.herokuapp.com/) go to the account menu and click Signin.

**Expected**:

**Actual**: 

<hr>

### _Contact_
#### 
**Description**:

**Steps**:
1. Navigate to [_Ruby's_](https://rubys-97a7171770c1.herokuapp.com/) go to the account menu and click Signin.

**Expected**:

**Actual**: 

<hr>

### _Newsletters_
#### 
**Description**:

**Steps**:
1. Navigate to [_Ruby's_](https://rubys-97a7171770c1.herokuapp.com/) go to the account menu and click Signin.

**Expected**:

**Actual**: 

<hr>

### _Subscribe_
#### 
**Description**:

**Steps**:
1. Navigate to [_Ruby's_](https://rubys-97a7171770c1.herokuapp.com/) go to the account menu and click Signin.

**Expected**:

**Actual**: 

<hr>

### _Footer_

Testing was performed on the footer link and Button

* When Clicking the Facebook icon and ensuring that the link opens Ruby's Facebookp page in a new tab. This behaved as expected.
* When Clicking the Subscribe button ensuring it opens up the subscription page.

## _Bugs_
    After Testing the site there does not appeart to be any faults with the functions of the site main features.
    whit that in mind the only minor bug that can be seen at pressent is the messages outputed to the user after updating items with out redirecting are only shown when the page is reloaded.
    
## _Validation_

### PEP8 Valadator
    All file passed through the [Code Institute PEP8](https://pep8ci.herokuapp.com/) Validator after removing a few white spaces and Shortening a few line lenghts.

![PEP8 Validation](docs/testing/pep8-validation.png)

### W3 Valadator
    The site passed through W3 Valadator with just a few minor errors on carousel ids as they had same name, so after remaning them it passed.

![W3 Validation](docs/testing/w3-validation.png)

### Lighthouse Report

    Lighthouse report has shown areas to be improved. with the over all scores are 90 and above. 

![Lighthouse](docs/testing/lighthouse.png)

## Responsiveness

All pages have been tested to ensure responsiveness on screen sizes from 320px and upwards for responsive design on Chrome, Edge, browsers.

Steps to test:

- Open Chrome and navigate to [_Ruby's_](https://rubys-97a7171770c1.herokuapp.com/)
- Open the developer tools 
- Set to responsive
- Click and drag the responsive window to from 320px to maximum width

Expected:

Website is responsive on all screen sizes.

Actual:

Website behaved as expected.

Website was also opened on the following devices and no responsive issues were seen:

Samsung S23
IPhone 13