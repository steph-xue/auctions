# Auctions Project
The auctions project allows the user to view and create new auction listings, as well as bid for auctions in a web-based auction application. The user can login, logout, or register for a new user account for more functionality with the application.
<br></br>


## Auctions App
**Login**
- Allows the user to login to their account
&nbsp;

![Login](/auctions/static/auctions/images/login.png?raw=true "Login")
<br></br>

**Register for a New Account**
- Allows the user to register for a new account
&nbsp;

![Register](/auctions/static/auctions/images/register.png?raw=true "Register")
<br></br>

## Features where login authentication is not needed:
**1. Viewing active auction listings (homepage)**  
   - The user can view a list of all active auction listings (sorted alphabetically by title)
     - This can be accessed via the 'Active Listings' tab 
     - Each auction listing card on the homepage displays the following:
       - Title
        - Image
        - Description
        - The starting price
        - The highest bidding price (and the user who made the bid)
        - A 'more details' button to view more detailed information in the the auction listing page
&nbsp;

![Active Listings](/auctions/static/auctions/images/active_listings.png?raw=true "Active Listings")
<br></br>

**2. Viewing more detailed information in the the auction listing page**
   - The user can view more details about the selected auction listing item, add or delete items to their watchlist, add a bid greater than the starting price and last highest bid price, and leave or delete comments listed in reverse chronological order.
    - This can be accessed by clicking into viewing 'More Details' about a particular listing item
    - Information on the auction listing pages includes the following:
      - Title
        - Image
        - Description
        - Category
        - Listing Owner
        - The starting price
        - The highest bidding price (and the user who made the bid)
        - Comments made with regards to the listing item
&nbsp;
       
![Listing Page](/auctions/static/auctions/images/listing_page.png?raw=true "Listing Page")
<br></br>

**2. Searching auction listings by category**
   - The user can search the list of active listings by category based on the listed categories available
    - This can be accessed via the 'Categories' tab 
    - Listings in each category are sorted alphabetically by title
&nbsp;

![View by Category](/auctions/static/auctions/images/view_category.png?raw=true "View by Category")
<br></br>

## Features where login authentication is needed:
**1. Creating new auction listings**
   - Can be accessed via the 'Create Listing' tab 
   - Users can create a new auction listing by providing the following information:
      - Title
        - Description
        - Image URL (optional)
        - Starting price
        - Category
      - The new auction listing will specify the user as the owner of the listing
&nbsp;

![Create a New Listing](/auctions/static/auctions/images/create_listing.png?raw=true "Create a New Listing")
<br></br>

**2. Using the watchlist**
   - The watchlist can be used to help users keep track of listing items they are interested in
   - Users can add/remove listing items to/from their own watchlist
   - The function to add and remove watchlist items can be found on the auction's listing pages as a button:
      - 'Add to Watchlist'
         - 'Remove from Watchlist'
      - Users can then view listing items in their own watchlist in the 'Watchlist' tab
&nbsp;

![Watchlist](/auctions/static/auctions/images/watchlist.png?raw=true "Watchlist")
<br></br>

**3. Commenting on auction listings**
   - Users can add and delete their own comments to an auction item's listing page
   - Comments include:
      - The comment being made
        - The user who commented
        - Date and time stamp
      - The log of comments is displayed on the auction item's listing page in reverse chronological order
<br></br>

**4. Bidding for auctions**
   - Users can bid for their desired auction listing items
   - The function to add a bid can be found on the auction's listing pages as an input and then clicking:
      - 'Add Bid'
      - The bid amount must be greater than the starting price and the current highest bidding price (if bids have been placed)
      - The user can view their current highest bids in the 'Bidding List' tab
        - Only the active listings where you currently hold the highest bids are listed
      - Bidded items are also automatically added to the watchlist
      - The user can aksee which auction listings they currently hold the highest bid for
&nbsp;

![List of Your Highest Bids](/auctions/static/auctions/images/bidding_list.png?raw=true "List of Your Highest Bids")
<br></br>

**5. Closing auctions and declaring a winner of the bid**
   - Owners of a listing item can close the auction by clicking the red 'Close Listing' button at the bottom of the item's listing page
   - Once the listing is closed, a winner is declared to be the highest bidder (if there is one)
<br></br>

**6. Viewing auctions that you have won**
   - The winner can see all auctions they have won in the 'Auction's Won' tab after the owner of the listing closes the bid and listing item page
   - It will display all listings they have won with their name listed as the winner
&nbsp;

![Auctions Won](/auctions/static/auctions/images/auctions_won.png?raw=true "Auctions Won")
<br></br> 

**7. Viewing your own listings**
   - The user can see which listings they currently own and select to view from all, active, or inactive listings
&nbsp;

![Your Listings](/auctions/static/auctions/images/your_listings.png?raw=true "Your Listings")
<br></br> 

## Languages & Frameworks
- The auctions project was created using Django, a Python-based web framework
- JavaScript was utilized for the front end to create a mix of possible user interactions

## How to Run Locally
- Install the latest version of python
    - Check the version using the command
        - ```python --version```
- Clone the repository from github by typing in the command line
    - HTTPS: ```git clone https://github.com/steph-xue/auctions.git```
    - SSH: ```git clone git@github.com:steph-xue/auctions.git```
- Install any dependencies by using the command
    - ```pip install -r requirements.txt```
- Apply database migrations by typing in the command line
    - ```python3 manage.py makemigrations```
    - ```python3 manage.py migrate```
- The web application can be run on your local server by typing the command
    - ```python3 manage.py runserver```
