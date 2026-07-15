# Auctions

A full stack online auction web application where users can create and manage listings, place competitive bids, browse listings by category, and track items of interest through a personal watchlist. Every listing page supports comments from other users, and closing an auction automatically declares the highest bidder the winner.

<br>

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [How It Works](#how-it-works)
- [Getting Started](#getting-started)
- [Future Improvements](#future-improvements)

<br>

## Overview

This project recreates the core experience of an online auction platform. The frontend is built with JavaScript, HTML, CSS, and Bootstrap, presenting listings, bidding, and account information through a clean, responsive interface. The backend is built with Django and Python, and handles user accounts, listings, categories, bids, comments, and watchlists, storing all of it in a SQLite database. Each listing tracks its own current highest bid and owner, so bidding, closing an auction, and declaring a winner are all handled consistently as listings move from active to closed. Beyond the core buying and selling flow, the application also supports category browsing, a personal watchlist, and comment threads on every listing.

<br>

## Features

### Authentication
Users can log in with an existing account or register for a new one. Browsing active listings is available to everyone, while creating listings, bidding, commenting, and using the watchlist all require an account.

<p align="center"><b>Login</b></p>
<p align="center"><img src="/auctions/static/auctions/images/login.png?raw=true" alt="Login" width="700"></p>

<p align="center"><b>Register</b></p>
<p align="center"><img src="/auctions/static/auctions/images/register.png?raw=true" alt="Register" width="700"></p>

<br>

### Active Listings
The homepage displays every active auction listing, sorted alphabetically by title, and can be reached at any time from the Active Listings tab. Each listing card shows its image, title, description, starting price, and current highest bid along with the bidder who made it, plus a "More Details" button that links through to the full listing page. A navigation bar gives users access to every part of the application, with Active Listings and Categories available to all visitors, while Create Listing, Watchlist, Bidding List, Auctions Won, and the user's own listings and username only appear once they are logged in.

<p align="center"><img src="/auctions/static/auctions/images/active_listings.png?raw=true" alt="Active Listings" width="700"></p>

<br>

### Listing Page
Each listing has its own detail page showing the title, image, description, category, listing owner, starting price, and current highest bid along with the bidder who made it. From here, users can add a bid, add or remove the listing from their watchlist, and leave or delete comments. Comments can be left and deleted by their own author, and each one records its text, the user who made it, and the date and time it was posted, with the full log displayed on the listing page in reverse chronological order.

<p align="center"><img src="/auctions/static/auctions/images/listing_page.png?raw=true" alt="Listing Page" width="700"></p>

<br>

### Browse by Category
Listings can be filtered by category from the Categories tab, with each category showing its listings sorted alphabetically by title. This makes it easy for users to find items in the type of auction they are interested in without scrolling through every active listing.

<p align="center"><img src="/auctions/static/auctions/images/view_category.png?raw=true" alt="View by Category" width="700"></p>

<br>

### Create Listing
Logged in users can create a new auction listing from the Create Listing tab by providing a title, description, starting price, category, and an optional image URL. The listing is saved with the current user as its owner and immediately appears among the active listings.

<p align="center"><img src="/auctions/static/auctions/images/create_listing.png?raw=true" alt="Create a New Listing" width="700"></p>

<br>

### Watchlist
Users can add or remove listings from a personal watchlist to keep track of items they are interested in, using the "Add to Watchlist" or "Remove from Watchlist" button on each listing's page. All watchlisted items can be reviewed together from the Watchlist tab.

<p align="center"><img src="/auctions/static/auctions/images/watchlist.png?raw=true" alt="Watchlist" width="700"></p>

<br>

### Bidding
Users can place a bid on any active listing by entering an amount and clicking "Add Bid," provided the amount is higher than both the starting price and the current highest bid, if one exists. Placing a bid automatically adds the listing to the user's watchlist, and the Bidding List tab shows every active listing where the user currently holds the highest bid.

<p align="center"><img src="/auctions/static/auctions/images/bidding_list.png?raw=true" alt="List of Your Highest Bids" width="700"></p>

<br>

### Closing Listings and Winning Auctions
The owner of a listing can close the auction at any time by clicking the "Close Listing" button at the bottom of the listing page. Once closed, a winner is declared as the highest bidder, if one exists, and the listing then appears in that winner's Auctions Won tab, where they can review every auction they have won.

<p align="center"><img src="/auctions/static/auctions/images/auctions_won.png?raw=true" alt="Auctions Won" width="700"></p>

<br>

### Your Listings
Users can view all the listings they own from a dedicated tab, and filter between all, active, or inactive listings to keep track of what they have created and their current status.

<p align="center"><img src="/auctions/static/auctions/images/your_listings.png?raw=true" alt="Your Listings" width="700"></p>

<br>

## Tech Stack

| Layer | Technologies |
|---|---|
| Frontend | JavaScript, HTML, CSS, Bootstrap |
| Backend | Django, Python |
| Database | SQLite |

<br>

## How It Works

Bootstrap provides the consistent structure and navigation bar seen throughout the application, with its built in JavaScript components powering small interactive elements like collapsible menus. On the backend, listings, bids, comments, categories, and watchlist relationships are each represented as their own model in Django, connected so that a listing can reference its current highest bid, category, and owner directly. The core functionality of the application, including bidding, commenting, and updating a watchlist, is handled through standard forms that are submitted and processed entirely on the backend before the page reloads with the updated result. All of this data is stored in a SQLite database, so a listing's status, current highest bid, and comments stay accurate as users interact with it.

<br>

## Getting Started

Follow the steps below to set up and run the application on your own machine.

**Prerequisites**

Make sure Python 3 is installed before you begin. You can check by running the command below, which should print a version number.
```bash
python --version
```

**1. Clone the repository**

This downloads a copy of the project to your computer and moves you into the project folder.
```bash
git clone https://github.com/steph-xue/auctions.git
cd auctions
```

**2. Create and activate a virtual environment (recommended)**

This keeps the project's dependencies separate from other Python projects on your machine.
```bash
python3 -m venv venv
source venv/bin/activate      # On Windows use: venv\Scripts\activate
```

**3. Install the dependencies**

This installs Django and everything else the project needs to run.
```bash
pip install -r requirements.txt
```

**4. Set up the database**

This creates the local database and the tables the application relies on.
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

**5. Start the development server**

This runs the application locally.
```bash
python3 manage.py runserver
```

Once the server is running, open `http://127.0.0.1:8000/` in your browser to start using the application.

<br>

## Future Improvements
Several enhancements are planned to extend the functionality of the application:
- Automatic notifications when a user is outbid
- Search functionality across listing titles and descriptions
- Image uploads in addition to image URLs
- A live hosted demo to allow users to try the application without a local setup
