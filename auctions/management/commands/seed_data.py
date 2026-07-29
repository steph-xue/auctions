from django.core.management.base import BaseCommand

from auctions.models import Bid, Category, Listing, User

# Usernames and emails for all demo accounts
DEMO_USERS = {
    "Steph": "steph@example.com",
    "Seykafu": "seykafu@example.com",
    "Totorosteph": "totorosteph@example.com",
}

# Shared login password for all the demo accounts above
DEMO_PASSWORD = "password123"

# Names for all demo categories
DEMO_CATEGORIES = ["Furniture", "Clothing", "Electronics", "Books"]

# Each entry mirrors what the create listing view does, creating one listing row
# with an owner and category, plus an optional bid and winner for a listing whose
# auction has already closed
DEMO_LISTINGS = [
    {
        "title": "Wooden Chair",
        "description": "A cute wooden chair. Great to sit on and very comfortable. Good quality oak wood.",
        "image_url": "https://www.ikea.com/ca/en/images/products/nordviken-chair-antique-stain__0832454_pe777681_s5.jpg?f=s",
        "initial_price": 25.0,
        "category": "Furniture",
        "owner": "Steph",
        "is_active": True,
    },
    {
        "title": "Leather Sofa",
        "description": "A cute brown leather sofa. Soft leather is smooth to the touch and of good quality",
        "image_url": "https://ca.valenciatheaterseating.com/cdn/shop/products/Artisan_Leather_3_Seater_Front.png?v=1712882586&width=1000",
        "initial_price": 600.0,
        "category": "Furniture",
        "owner": "Totorosteph",
        "is_active": True,
        "bid": {"amount": 700.0, "user": "Seykafu"},
    },
    {
        "title": "Apple iPad",
        "description": "Newest edition iPad, useful for taking notes, drawing, taking pictures, etc.",
        "image_url": "https://www.shutterstock.com/image-photo/kiev-ukraine-march-10-2014apple-600nw-181599737.jpg",
        "initial_price": 500.0,
        "category": "Electronics",
        "owner": "Steph",
        "is_active": True,
    },
    {
        "title": "COS Bag",
        "description": "A cozy and versatile beige COS bag. Very comfortable to carry and can hold a lot of items. Functional yet fashionable.",
        "image_url": "https://i.ebayimg.com/images/g/WwoAAOSwnexlhIEA/s-l1200.webp",
        "initial_price": 100.0,
        "category": "Clothing",
        "owner": "Steph",
        "is_active": True,
        "bid": {"amount": 200.0, "user": "Seykafu"},
    },
]


class Command(BaseCommand):
    help = "Seeds the database with demo users, categories, and listings for local development and testing."

    # Adds the --flush flag for clearing existing demo listings before reseeding
    def add_arguments(self, parser):
        parser.add_argument(
            "--flush",
            action="store_true",
            help="Delete existing demo listings (from the demo users) before reseeding.",
        )

    # Creates the demo users and categories, then seeds the listings unless they already exist
    def handle(self, *args, **options):
        users = {}
        for username, email in DEMO_USERS.items():
            user, created = User.objects.get_or_create(
                username=username, defaults={"email": email}
            )
            if created:
                user.set_password(DEMO_PASSWORD)
                user.save()
                self.stdout.write(f"Created user {username}")
            users[username] = user

        categories = {}
        for name in DEMO_CATEGORIES:
            category, _ = Category.objects.get_or_create(category_name=name)
            categories[name] = category

        if options["flush"]:
            deleted, _ = Listing.objects.filter(owner__in=users.values()).delete()
            self.stdout.write(f"Deleted {deleted} existing demo listing row(s)")

        if Listing.objects.filter(owner__in=users.values()).exists():
            self.stdout.write(
                self.style.WARNING(
                    "Demo listings already exist, skipping. Re-run with --flush to reseed."
                )
            )
        else:
            for entry in DEMO_LISTINGS:
                listing = Listing(
                    title=entry["title"],
                    description=entry["description"],
                    image_url=entry["image_url"],
                    initial_price=entry["initial_price"],
                    category=categories[entry["category"]],
                    owner=users[entry["owner"]],
                    is_active=entry["is_active"],
                )
                listing.save()

                bid_info = entry.get("bid")
                if bid_info:
                    bid = Bid.objects.create(
                        highest_bid=bid_info["amount"], user=users[bid_info["user"]]
                    )
                    listing.current_highest_bid = bid

                winner = entry.get("winner")
                if winner:
                    listing.winner = users[winner]

                listing.save()

            self.stdout.write(f"Created {len(DEMO_LISTINGS)} demo listing(s)")

        self.stdout.write(self.style.SUCCESS("Done."))
        self.stdout.write(f"Demo accounts (password: {DEMO_PASSWORD}):")
        for username in DEMO_USERS:
            self.stdout.write(f"  {username}")
