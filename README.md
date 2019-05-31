# Deli Builder Client

We want to build a sandwich (Turkey, Roast Beef or Veggie) with additional ingredients.  The Sandwich will have a name, the type,
a description, and toppings.


Requirements
============

Please build a client that will cover these stories. You can use any technology
you feel comfortable with. 

  * As a builder, I should be able to list existing Sandwiches
  * As a builder, I should be able to create a new Sandwich
  * As a builder, I should be able to create toppings that can be added to a Sandwich
  * As a builder, I should be able to list the toppings I can to add to a Sandwich
  * As a builder, I should be able to add a topping to a Sandwich
  * As a builder, I should be able to list toppings on a Sandwich

**Once you have a client built, please push it to your (a) repository location so we can clone it.  Deploy it some where and send the url. If it is a SPA and can be run locally in development mode, please add those instruction in your README.md and no URL is needed. 
[speardevsubmission@speareducation.com](speardevsubmission@speareducation.com).**

Resources
=========
Use these resources to build your client.  The server with these resources can
be accessed at *http://deli.chaddio.com*

```
GET  /api/v1/toppings                   # List toppings
POST /api/v1/toppings                   # Create a topping
GET  /api/v1/sandwiches                 # List sandwiches
GET  /api/v1/sandwiches/:id             # List a sandwich
POST /api/v1/sandwiches                 # Create a sandwich
GET  /api/v1/sandwiches/:id/topping     # List toppings associated with a sandwich
POST /api/v1/sandwiches/:id/topping     # Add a topping to an existing sandwich
```

*Example curl command to create a sandwich:*
```
curl -H "Content-Type: application/json" -H "Accept: application/json" http://deli.chaddio.com/api/v1/sandwiches --data '{"name": "My Favorite Veggie Sandwich", "description": "All Veggies possible and Avacado","base" : 3, "price" : 6.99}'
```

Sandwich
---------
A sandwich is a food typically consisting of meat, sliced cheese and veggies, placed on or between slices of bread (base: 1 = Turkey, 2 = Roast Beef, 3 = Veggie)

#### Examples:
```
POST /api/v1/sandwiches, {"name": "My Favorite Veggie Sandwich", "description": "All Veggies possible and Avacado","base" : 3, "price" : 6.99}
```

```
GET  /api/v1/sandwiches
```

Topping
-------
Raw ingredients that can be added to a sandwich

#### Examples:
```
POST /api/v1/toppings, {"name": "Pepperoni", "description" : "Pork made meat thang","extra" 2.00}
```
```
GET  /api/v1/toppings
```

Sandwich Toppings
--------------
Sandwich Toppings are Toppings that have been added to a Sandwich

#### Examples:

Get a list of all the toppings added to a sandwich
```
GET  /api/v1/sandwiches/:id/toppings
```

Add toppings to a sandwich *(must be sent as PATCH all at once, if you patch one then another individually, it will update to just the last list value(s), this is intentional)*
```
PATCH /api/v1/sandwiches/:id/toppings, {toppings: [1]}
```
or
```
PATCH /api/v1/sandwiches/:id/toppings, {toppings: [1,2,3]}
```

