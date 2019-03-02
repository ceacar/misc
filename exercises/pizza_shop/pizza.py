
"""
Here's the scenario: We have a pizza shop, and customers place orders for pizzas. We need to figure out how much of each ingredient we need for our pizzas to fill all of the orders. Here's our ingredients table to define it:

# We use a multiplier to ensure consistent ingredient quantities.

# A medium pizza will always gets exactly 1.25 times as many

# ingredients as a small, across all ingredients
"""

mult = {

    'Small': 1.0,

    'Medium': 1.25,

    'Large': 1.5,

    'Extra-Large': 2.0,

}


# We specify the amounts we would use for each ingredient in

# grams for a small pizza.

quantities = {

    'dough': 100,

    'sauce': 75,

    'cheese': 100,

    'pepperoni': 75,

    'sausage': 66,

    'peppers': 100,

    'onions': 50,

}


# We list out the ingredients for each pizza here

recipes = {

    'meaty': ['pepperoni', 'sausage', 'dough', 'cheese', 'sauce'],

    'vegetarian': ['peppers', 'onions', 'dough', 'cheese', 'sauce'],

    'custom': ['dough', 'cheese', 'sauce']

}

"""
For example, if we needed to make a small meaty pizza, we would need 100g of dough, 75g of sauce, 100g of cheese, 75g of pepperoni, and 66g of sausage. If we needed an extra-large version, we would need 200g of dough, 150g of sauce, 200g of cheese, 150g of pepperoni, and 132g of sausage.

When a customer places an order, they can add additional toppings. They can even double up, so they include double pepperoni for instance. We don't allow removal though. Our technology just doesn't support it right.
Our shop has just received a bunch of orders. They were received in an avro encoded format. Here's the exact message we received:
"""

orders = b'Obj\x01\x04\x14avro.codec\x08null\x16avro.schema\xb0\x0c[{"type": "enum", "name": "Type", "symbols": ["Custom", "Meaty", "Vegetarian"]}, {"type": "enum", "name": "Size", "symbols": ["Small", "Medium", "Large", "Extra-Large"]}, {"type": "enum", "name": "AdditionalToppings", "symbols": ["Pepperoni", "Sausage", "Peppers", "Onions"]}, {"type": "record", "name": "Pizza", "fields": [{"type": ".Type", "name": "type"}, {"type": ".Size", "name": "size"}, {"type": {"type": "array", "items": ".AdditionalToppings"}, "name": "toppings"}]}, {"type": "record", "name": "PizzaOrder", "fields": [{"type": "string", "name": "customer_name"}, {"type": "string", "name": "address"}, {"type": "string", "name": "city"}, {"type": "string", "name": "state"}, {"type": "string", "name": "zipcode"}, {"type": {"type": "array", "items": ".Pizza"}, "name": "pizzas"}]}]\x00\\3\x8d\x0ev\x96\xd5\x99?\xa1[[\xa9\x90\x0e\xfd\x14\x96\n\x08\x1cHerman Munster*1313 Mockingbird Lane&Mockingbird Heights\x14California\n13131\x02\x00\x00\x06\x00\x02\x06\x00\x00\x08\x18US President*1600 Pennsylvania Ave\x14Washington\x04DC\n02020\x04\x02\x06\x00\x04\x02\x00\x00\x08\x10John Doe\x1442 Main St\x18Ruby Heights\x04IL\n12345\x08\x02\x02\x06\x00\x04\x06\x00\x02\x06\x06\x06\x00\x02\x00\x04\x00\x02\x00\x00\x00\x06\x06\x02\x00\x06\x00\x00\x08\x10Jane Doe\x1c347 Alpine Ave\x0cOrlowe\x04FL\n45712\x02\x04\x04\x02\x04\x00\x00\x08\x16Richard Doe 86 Restaurant Rd\x0eMadison\x04WI\n90577\x08\x00\x04\x00\x00\x02\x06\x06\x00\x02\x00\x02\x06\x06\x04\x06\x00\x00\x00\x04\x00\x00\x08\x1cHoward T. Duck$901 Washington Ave\x10Portland\x04PA\n18301\x04\x00\x00\x06\x00\x04\x02\x00\x00\x04\x02\x04\x00\x00\x08\x16Bruce Wayne 38 Springtown Rd\x0cGotham\x04NY\n21112\n\x00\x02\x04\x00\x06\x00\x04\x04\x02\x06\x00\x04\x00\x04\x00\x02\x00\x02\x02\x00\x02\x06\x06\x04\x00\x02\x00\x00\x08\x14Clark Kent\x16492 83rd St\x14Metropolis\x04NY\n12121\x02\x04\x04\x00\x00\x08\x1aHarold Jordan 314 Simon Circle\x14Fort Wyatt\x04ND\n87561\x02\x00\x06\x06\x00\x02\x04\x00\x00\x08\x16Barry Allen\x1625 Oak Lane\x18North Platte\x04NE\n66581\x04\x02\x06\x06\x04\x02\x00\x00\x04\x00\x06\x00\x02\x06\x00\x00\\3\x8d\x0ev\x96\xd5\x99?\xa1[[\xa9\x90\x0e\xfd'
"""
We need to read these orders, and figure out our total ingredients we need to consume. Once we know our totals, we need to encode them into an avro record that we can send up to our supplier to make sure we keep in stock. The schema that our supplier expects is as follows:
"""

ingredient_schema_str = """
{

   "type": "record",

   "name": "ingredients",

   "fields": [

       {"name": "name", "type": "string"},

       {"name": "quantity", "type": "float"}

   ]

}
"""
Show here how you would go about turning the data stream we get into what we need to send to our supplier. We have supplied an environment.yml file that will get you a Python3 environment with avro support already put together for this.
"""

from io import BytesIO

from avro.datafile import DataFileReader, DataFileWriter

from avro.io import DatumReader, DatumWriter

from avro.schema import Parse

avro.schema.Parse(ingredient_schema_str)





