from datetime import *
import random
vendors = ["Adonai Kitchen", "Hot and Spicy Kitchen", "Deli Buds Kitchen", "SOTA Kitchen", "Blossom"]
_menu = [
    {
        "slug": "noodles",
        "title": "Noodles",
        "image" : "images/Noodles.jpg",
        "price" : 1500,
        "cf" : 200,
        "total" : 1700
    },
    {
        "slug": "sharwarma",
        "title": "Sharwarma",
        "image" : "images/sharwarma.webp",
        "price" : 1500,
        "cf" : 200,
        "total" : 1700
    },
    {
        "slug": "chicken",
        "title": "Chicken",
        "image" : "images/friedchicken.jpg",
        "price" : 1500,
        "cf" : 200,
        "total" : 1700
    },
    {
        "slug": "noodles-and-eggs",
        "title": "Noodles and Eggs",
        "image" : "images/noodlesandeggs.jpg",
        "price" : 1500,
        "cf" : 200,
        "total" : 1700
    },
    {
        "slug": "chicken-and-chips",
        "title": "Chicken and Chips",
        "image" : "images/chicken_and_chips.jpg",
        "price" : 1500,
        "cf" : 200,
        "total" : 1700
    },
    {
        "slug": "bread-and-eggs",
        "title": "Bread and Eggs",
        "image" : "images/breadandegg.jpg",
        "price" : 1500,
        "cf" : 200,
        "total" : 1700
    }
]


vendors_menu = [
    {
        "slug": "pepsi",
        "title": "Pepsi",
        "image": "images/pepsi.jpg",
        "price": 150,
        "cf": 50,
        "total": 200,
        "description": "A refreshing, carbonated cola soft drink, perfect for quenching your thirst.",
        "kitchen": "Blossom Kitchen",
        "kitchen_slug": "blossom-kitchen",
        "category": "drink"
    },
    {
        "slug": "coke",
        "title": "Coca-Cola",
        "image": "images/coke.png",
        "price": 150,
        "cf": 50,
        "total": 200,
        "description": "The classic cola soft drink with a rich, bold flavor. Always refreshing.",
        "kitchen": "Adonai Kitchen",
        "kitchen_slug": "adonai-kitchen",
        "category": "drink"
    },
    {
        "slug": "fanta",
        "title": "Fanta",
        "image": "images/fanta.webp",
        "price": 150,
        "cf": 50,
        "total": 200,
        "description": "A fruity, orange-flavored soft drink that's sweet and bubbly.",
        "kitchen": "Hot and Spicy Kitchen",
        "kitchen_slug": "hot-and-spicy-kitchen",
        "category": "drink"
    },
    {
        "slug": "doughnut",
        "title": "Doughnut",
        "image": "images/doughnut.jpg",
        "price": 400,
        "cf": 100,
        "total": 500,
        "description": "A soft, sweet, and delicious doughnut, perfect for a quick snack.",
        "kitchen": "Deli Buds Kitchen",
        "kitchen_slug": "deli-buds-kitchen",
        "category": "Snack"
    },
    {
        "slug": "egg-roll",
        "title": "Egg Roll",
        "image": "images/egg_rolls.jpg",
        "price": 400,
        "cf": 50,
        "total": 450,
        "description": "A deep-fried snack with a boiled egg encased in a crispy, golden dough.",
        "kitchen": "SOTA Kitchen",
        "kitchen_slug": "sota-kitchen",
        "category": "Snack"
    },
    {
        "slug": "fish-roll",
        "title": "Fish Roll",
        "image": "images/fish_rolls.jpeg",
        "price": 150,
        "cf": 50,
        "total": 200,
        "description": "A tasty, deep-fried roll filled with seasoned fish, crispy on the outside and savory inside.",
        "kitchen": "Blossom Kitchen",
        "kitchen_slug": "blossom-kitchen",
        "category": "Snack"
    },
    {
        "slug": "akara",
        "title": "Akara",
        "image": "images/akara.jpg",
        "price": 100,
        "cf": 50,
        "total": 150,
        "description": "A popular Nigerian snack made from deep-fried bean cakes, crunchy and delicious.",
        "kitchen": "Adonai Kitchen",
        "kitchen_slug": "adonai-kitchen",
        "category": "Snack"
    },
    {
        "slug": "sharwarma",
        "title": "Sharwarma",
        "image": "images/sharwarma.webp",
        "price": 2000,
        "cf": 100,
        "total": 2100,
        "description": "A tasty wrap filled with grilled meat, veggies, and a mix of delicious sauces.",
        "kitchen": "Hot and Spicy Kitchen",
        "kitchen_slug": "hot-and-spicy-kitchen",
        "category": "Snack"
    },
    {
        "slug": "small-chops",
        "title": "Small Chops",
        "image": "images/smallchops.jpg",
        "price": 1700,
        "cf": 100,
        "total": 1800,
        "description": "A delightful assortment of mini snacks including puff-puff, samosas, and spring rolls.",
        "kitchen": "Deli Buds Kitchen",
        "kitchen_slug": "deli-buds-kitchen",
        "category": "Snack"
    },
    {
        "slug": "ewedu",
        "title": "Ewedu Soup",
        "image": "images/ewedu.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "description": "A traditional Nigerian soup made from jute leaves, perfect with Amala or any swallow.",
        "kitchen": "SOTA Kitchen",
        "kitchen_slug": "sota-kitchen",
        "category": "Soup"
    },
    {
        "slug": "egusi",
        "title": "Egusi Soup",
        "image": "images/egusi.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "description": "A hearty Nigerian soup made from ground melon seeds, rich in flavor and best enjoyed with any swallow.",
        "kitchen": "Blossom Kitchen",
        "kitchen_slug": "blossom-kitchen",
        "category": "Soup"
    },
    {
        "slug": "efo",
        "title": "Efo Soup",
        "image": "images/efo.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "description": "A vibrant vegetable soup made from spinach and other leafy greens, spiced to perfection.",
        "kitchen": "Adonai Kitchen",
        "kitchen_slug": "adonai-kitchen",
        "category": "Soup"
    },
    {
        "slug": "amala",
        "title": "Amala",
        "image": "images/amala.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "description": "A popular Nigerian swallow made from yam flour, pairs perfectly with Ewedu or any other soup.",
        "kitchen": "Hot and Spicy Kitchen",
        "kitchen_slug": "hot-and-spicy-kitchen",
        "category": "Swallow"
    },
    {
        "slug": "semolina-semovita",
        "title": "Semolina or Semovita",
        "image": "images/semolina.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "description": "A smooth, light swallow made from semolina flour, great with any Nigerian soup.",
        "kitchen": "Deli Buds Kitchen",
        "kitchen_slug": "deli-buds-kitchen",
        "category": "Swallow"
    },
    {
        "slug": "fufu",
        "title": "Fufu",
        "image": "images/fufu.webp",
        "price": 100,
        "cf": 50,
        "total": 150,
        "description": "A starchy, fermented swallow made from cassava, with a slightly sour taste. Enjoyed with various soups.",
        "kitchen": "SOTA Kitchen",
        "kitchen_slug": "sota-kitchen",
        "category": "Swallow"
    },
    {
        "slug": "eba",
        "title": "Eba",
        "image": "images/eba.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "description": "A popular Nigerian swallow made from garri, often paired with Egusi or any other soup.",
        "kitchen": "Blossom Kitchen",
        "kitchen_slug": "blossom-kitchen",
        "category": "Swallow"
    }
]


categories = []
for each in vendors_menu:
    cat = each["category"]
    if cat not in categories:
        categories.append(each["category"])

_menu2 = [
    {
        "slug": "jollof-rice",
        "title": "Jollof Rice",
        "image": "images/jollof.jpg",
        "price": 150,
        "cf": 50,
        "total": 200,
        "kitchen": "Adonai Kitchen",
        "description": "A classic West African dish made from long-grain rice cooked in a tomato-based sauce with spices.",
        "kitchen_slug": "adonai-kitchen",
    "category": "special"
    },
    {
        "slug": "fried-rice",
        "title": "Fried Rice",
        "image": "images/friedrice.jpg",
        "price": 150,
        "cf": 50,
        "total": 200,
        "kitchen": "Adonai Kitchen",
        "description": "Rice stir-fried with vegetables, eggs, and spices, often served with chicken or beef.",
        "kitchen_slug": "adonai-kitchen",
    "category": "special"
    },
    {
        "slug": "jollof-spaghetti",
        "title": "Jollof Spaghetti",
        "image": "images/jollofspag.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "kitchen": "Adonai Kitchen",
        "description": "Spaghetti cooked in a rich tomato sauce, similar to Jollof Rice but with a twist.",
        "kitchen_slug": "adonai-kitchen",
    "category": "special"
    },
    {
        "slug": "beans-and-corn",
        "title": "Beans and Corn",
        "image": "images/oloka.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "kitchen": "Adonai Kitchen",
        "description": "A nutritious and filling dish made from a mix of beans and corn, often seasoned with palm oil and spices.",
        "kitchen_slug": "adonai-kitchen",
    "category": "special"
    },
    {
        "slug": "white-spaghetti",
        "title": "White Spaghetti",
        "image": "images/white_spag.jpg",
        "price": 150,
        "cf": 50,
        "total": 200,
        "kitchen": "Adonai Kitchen",
        "description": "Simple boiled spaghetti served with a light sauce or as a base for other toppings.",
        "kitchen_slug": "adonai-kitchen",
    "category": "special"
    },
    {
        "slug": "white-rice",
        "title": "White Rice",
        "image": "images/white_rice.jpeg",
        "price": 150,
        "cf": 50,
        "total": 200,
        "kitchen": "Adonai Kitchen",
        "description": "Steamed white rice, a staple side dish perfect for pairing with stews and sauces.",
        "kitchen_slug": "adonai-kitchen",
    "category": "special"
    },
    {
        "slug": "beans",
        "title": "Beans",
        "image": "images/beans.png",
        "price": 200,
        "cf": 50,
        "total": 250,
        "kitchen": "Adonai Kitchen",
        "description": "Hearty and flavorful beans cooked to perfection, often enjoyed with rice or bread.",
        "kitchen_slug": "adonai-kitchen",
    "category": "special"
    },
    {
        "slug": "yam-and-egg",
        "title": "Yam and Egg",
        "image": "images/yam_eggs.webp",
        "price": 500,
        "cf": 100,
        "total": 600,
        "kitchen": "Adonai Kitchen",
        "description": "Boiled yam served with a tasty egg sauce, a popular breakfast or brunch option.",
        "kitchen_slug": "adonai-kitchen",
    "category": "special"
    },
    {
        "slug": "potato-and-egg",
        "title": "Potato and Egg",
        "image": "images/potato_eggs.jpg",
        "price": 500,
        "cf": 100,
        "total": 600,
        "kitchen": "Adonai Kitchen",
        "description": "A satisfying dish featuring boiled or fried potatoes paired with an egg sauce.",
        "kitchen_slug": "adonai-kitchen",
    "category": "special"
    },
    {
        "slug": "amala",
        "title": "Amala",
        "image": "images/amala.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "kitchen": "Adonai Kitchen",
        "description": "A traditional Yoruba dish made from yam flour, served with various soups.",
        "kitchen_slug": "adonai-kitchen",
    "category": "swallow"
    },
    {
        "slug": "semolina-semovita",
        "title": "Semolina or Semovita",
        "image": "images/semolina.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "kitchen": "Adonai Kitchen",
        "description": "Smooth and soft, Semolina or Semovita is a perfect accompaniment to rich, hearty soups.",
        "kitchen_slug": "adonai-kitchen",
    "category": "swallow"
    },
    {
        "slug": "fufu",
        "title": "Fufu",
        "image": "images/fufu.webp",
        "price": 100,
        "cf": 50,
        "total": 150,
        "kitchen": "Adonai Kitchen",
        "description": "A starchy side dish made from cassava, often served with a variety of African soups.",
        "kitchen_slug": "adonai-kitchen",
    "category": "swallow"
    },
    {
        "slug": "egg-sauce",
        "title": "Egg Sauce",
        "image": "images/egg_sauce.jpg",
        "price": 100,
        "cf": 50,
        "total": 150,
        "kitchen": "Adonai Kitchen",
        "description": "A savory sauce made with eggs, tomatoes, and onions, perfect for pairing with yams or potatoes.",
        "kitchen_slug": "adonai-kitchen",
    "category": "special"
    },
    {
        "slug": "fried-plantain",
        "title": "Fried Plantain",
        "image": "images/fried_plantain.jpg",
        "price": 50,
        "cf": 25,
        "total": 75,
        "kitchen": "Adonai Kitchen",
        "description": "Sweet, ripe plantains fried to a golden brown, a delicious side or snack.",
        "kitchen_slug": "adonai-kitchen",
    "category": "dessert"
    },
    {
        "slug": "porridge-yam",
        "title": "Porridge Yam",
        "image": "images/yam_porridge.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "kitchen": "Adonai Kitchen",
        "description": "Yam cooked in a rich sauce with palm oil, tomatoes, and spices, creating a thick porridge.",
        "kitchen_slug": "adonai-kitchen",
    "category": "special"
    },
    {
        "slug": "akara",
        "title": "Akara",
        "image": "images/akara.jpg",
        "price": 100,
        "cf": 50,
        "total": 150,
        "kitchen": "Adonai Kitchen",
        "description": "Deep-fried bean cakes made from ground black-eyed peas, a popular street food snack.",
        "kitchen_slug": "adonai-kitchen",
    "category": "snack"
    },
    {
        "slug": "doughnut",
        "title": "Doughnut",
        "image": "images/doughnut.jpg",
        "price": 400,
        "cf": 100,
        "total": 500,
        "kitchen": "Adonai Kitchen",
        "description": "Soft and fluffy doughnuts, sweetened and fried to perfection, a delightful treat.",
        "kitchen_slug": "adonai-kitchen",
    "category": "snack"
    },
    {
        "slug": "ice-cream",
        "title": "Ice Cream",
        "image": "images/icecream.jpg",
        "price": 1000,
        "cf": 100,
        "total": 1100,
        "kitchen": "Adonai Kitchen",
        "description": "Creamy and cold, this ice cream is the perfect dessert to cool off on a hot day.",
        "kitchen_slug": "adonai-kitchen",
    "category": "dessert"
    },
    {
        "slug": "meat",
        "title": "Meat",
        "image": "images/meat.jpg",
        "price": 100,
        "cf": 50,
        "total": 150,
        "kitchen": "Adonai Kitchen",
        "description": "Tender and flavorful meat, perfect as a side dish or main course.",
        "kitchen_slug": "adonai-kitchen",
    "category": "protein"
    },
    {
        "slug": "turkey",
        "title": "Turkey",
        "image": "images/turkey.jpeg",
        "price": 1500,
        "cf": 100,
        "total": 1600,
        "kitchen": "Adonai Kitchen",
        "description": "Juicy and well-seasoned turkey, roasted to perfection and served hot.",
        "kitchen_slug": "adonai-kitchen",
    "category": "protein"
    },
    {
        "slug": "chicken",
        "title": "Chicken",
        "image": "images/friedchicken.jpg",
        "price": 1500,
        "cf": 100,
        "total": 1600,
        "kitchen": "Adonai Kitchen",
        "description": "Succulent chicken, seasoned and cooked to a golden brown, a crowd favorite.",
        "kitchen_slug": "adonai-kitchen",
    "category": "protein"
    },
    {
        "slug": "fish",
        "title": "Fish",
        "image": "images/fish.jpg",
        "price": 800,
        "cf": 100,
        "total": 900,
        "kitchen": "Adonai Kitchen",
        "description": "Fresh fish, grilled or fried, served with a side of vegetables or rice.",
        "kitchen_slug": "adonai-kitchen",
    "category": "protein"
    },
    {
        "slug": "ewedu",
        "title": "Ewedu Soup",
        "image": "images/ewedu.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "kitchen": "Adonai Kitchen",
        "description": "A traditional Yoruba soup made from jute leaves, often served with Amala.",
        "kitchen_slug": "adonai-kitchen",
    "category": "drink"
    },
    {
        "slug": "efo",
        "title": "Efo Soup",
        "image": "images/efo.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "kitchen": "Adonai Kitchen",
        "description": "A nutritious and flavorful soup made from leafy greens, commonly served with pounded yam or fufu.",
        "kitchen_slug": "adonai-kitchen",
    "category": "soup"
    },
    {
        "slug": "ogbono",
        "title": "Ogbono Soup",
        "image": "images/ogbonosoup.jpeg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "kitchen": "Adonai Kitchen",
        "description": "A thick and hearty Nigerian soup made from ground ogbono seeds, known for its slimy texture.",
        "kitchen_slug": "adonai-kitchen",
    "category": "soup"
    },
    {
        "slug": "vegetable-soup",
        "title": "Vegetable Soup",
        "image": "images/vegetable_soup.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "kitchen": "Adonai Kitchen",
        "description": "A rich and savory soup made with various vegetables, often served with fufu or rice.",
        "kitchen_slug": "adonai-kitchen",
    "category": "soup"
    },
    {
        "slug": "egusi",
        "title": "Egusi Soup",
        "image": "images/egusi.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "kitchen": "Adonai Kitchen",
        "description": "A popular Nigerian soup made with ground melon seeds, often enjoyed with pounded yam.",
        "kitchen_slug": "adonai-kitchen",
    "category": "soup "
    },
    {
        "slug": "ogbono-and-egusi",
        "title": "Ogbono and Egusi Soup",
        "image": "images/egusi_ogbono.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "kitchen": "Adonai Kitchen",
        "description": "A combination of Ogbono and Egusi, creating a thick, flavorful soup.",
        "kitchen_slug": "adonai-kitchen",
    "category": "soup"
    },
    {
        "slug": "rice-and-beans",
        "title": "Rice and Beans",
        "image": "images/rice_beans.png",
        "price": 200,
        "cf": 50,
        "total": 250,
        "kitchen": "Adonai Kitchen",
        "description": "A hearty mix of rice and beans, often served with fried plantain or a side of meat.",
        "kitchen_slug": "adonai-kitchen",
    "category": "special"
    },
    {
        "slug": "bread",
        "title": "Bread",
        "image": "images/breadandegg.jpg",
        "price": 500,
        "cf": 100,
        "total": 600,
        "kitchen": "Hot and Spicy Kitchen",
        "description": "A freshly baked loaf of soft, fluffy bread, perfect for sandwiches or as a side to any meal.",
        "kitchen_slug": "hot-and-spicy-kitchen",
    "category": "special"
    },
    {
        "slug": "noodles",
        "title": "Noodles",
        "image": "images/noodles.jpg",
        "price": 400,
        "cf": 50,
        "total": 450,
        "kitchen": "Hot and Spicy Kitchen",
        "description": "A savory and spicy plate of stir-fried noodles, cooked to perfection with a blend of special seasonings.",
        "kitchen_slug": "hot-and-spicy-kitchen",
    "category": "special"
    },
    {
        "slug": "egg",
        "title": "Egg",
        "image": "images/egg.jpg",
        "price": 300,
        "cf": 50,
        "total": 350,
        "kitchen": "Hot and Spicy Kitchen",
        "description": "A perfectly boiled egg, a versatile side that complements any main dish.",
        "kitchen_slug": "hot-and-spicy-kitchen",
    "category": "snack"
    },
    {
        "slug": "sharwarma",
        "title": "Sharwarma",
        "image": "images/sharwarma.webp",
        "price": 2000,
        "cf": 100,
        "total": 2100,
        "kitchen": "Hot and Spicy Kitchen",
        "description": "A mouthwatering wrap filled with tender, marinated meat, fresh vegetables, and a rich, flavorful sauce.",
        "kitchen_slug": "hot-and-spicy-kitchen",
    "category": "snack"
    },
    {
        "slug": "chicken-and-chips",
        "title": "Chicken and Chips",
        "image": "images/chicken_and_chips.jpg",
        "price": 4000,
        "cf": 100,
        "total": 4100,
        "kitchen": "Hot and Spicy Kitchen",
        "description": "A generous portion of crispy fried chicken served with golden fries, a perfect comfort meal.",
        "kitchen_slug": "hot-and-spicy-kitchen",
    "category": "dessert"
    },
    {
        "slug": "egg-roll",
        "title": "Egg Roll",
        "image": "images/egg_roll.jpg",
        "price": 400,
        "cf": 50,
        "total": 450,
        "kitchen": "Hot and Spicy Kitchen",
        "description": "A soft, doughy roll filled with a savory boiled egg, ideal for a quick snack.",
        "kitchen_slug": "hot-and-spicy-kitchen",
    "category": "snack"
    },
    {
        "slug": "fish-roll",
        "title": "Fish Roll",
        "image": "images/fish_roll.jpg",
        "price": 150,
        "cf": 50,
        "total": 200,
        "kitchen": "Hot and Spicy Kitchen",
        "description": "A delightful pastry filled with seasoned fish, offering a tasty and convenient snack option.",
        "kitchen_slug": "hot-and-spicy-kitchen",
    "category": "snack"
    },
    {
        "slug": "smoothie",
        "title": "Smoothie",
        "image": "images/smoothie.jpg",
        "price": 1000,
        "cf": 100,
        "total": 1100,
        "kitchen": "Deli Buds Kitchen",
        "description": "A refreshing blend of fruits, providing a healthy and delicious drink to quench your thirst.",
        "kitchen_slug": "deli-buds-kitchen",
    "category": "dessert"
    },
    {
        "slug": "suya",
        "title": "Suya",
        "image": "images/suya.jpg",
        "price": 700,
        "cf": 50,
        "total": 750,
        "kitchen": "Deli Buds Kitchen",
        "description": "A spicy and succulent skewered meat, grilled to perfection and seasoned with traditional suya spices.",
        "kitchen_slug": "deli-buds-kitchen",
    "category": "dessert"
    },
    {
        "slug": "gizzards",
        "title": "Gizzards",
        "image": "images/gizzards.jpg",
        "price": 700,
        "cf": 50,
        "total": 750,
        "kitchen": "Deli Buds Kitchen",
        "description": "Tender and flavorful gizzards, cooked with a blend of spices, perfect for a quick snack or as a side dish.",
        "kitchen_slug": "deli-buds-kitchen",
    "category": "dessert"
    },
    {
        "slug": "shaki-suya",
        "title": "Shaki Suya",
        "image": "images/shaki_suya.jpg",
        "price": 700,
        "cf": 50,
        "total": 750,
        "kitchen": "Deli Buds Kitchen",
        "description": "Spicy and tender shaki (tripe) grilled with a unique blend of suya spices, offering a traditional taste experience.",
        "kitchen_slug": "deli-buds-kitchen",
    "category": "dessert"
    },
    {
        "slug": "goat-meat-suya",
        "title": "Goat Meat Suya",
        "image": "images/goat_meat_suya.jpg",
        "price": 700,
        "cf": 50,
        "total": 750,
        "kitchen": "Deli Buds Kitchen",
        "description": "Juicy goat meat grilled with suya spices, a must-try for lovers of spicy, flavorful meats.",
        "kitchen_slug": "deli-buds-kitchen",
    "category": "dessert"
    },
    {
        "slug": "small-chops",
        "title": "Small Chops",
        "image": "images/smallchops.jpg",
        "price": 1700,
        "cf": 100,
        "total": 1800,
        "kitchen": "Deli Buds Kitchen",
        "description": "A delightful mix of bite-sized snacks, perfect for sharing and enjoying with friends.",
        "kitchen_slug": "deli-buds-kitchen",
    "category": "dessert"
    },
    {
        "slug": "spaghetti-stir-fry",
        "title": "Spaghetti Stir Fry",
        "image": "images/spaghetti_stir_fry.jpg",
        "price": 3000,
        "cf": 100,
        "total": 3100,
        "kitchen": "Deli Buds Kitchen",
        "description": "A flavorful stir-fried spaghetti dish, packed with vegetables and protein, offering a satisfying meal.",
        "kitchen_slug": "deli-buds-kitchen",
    "category": "special"
    },
    {
        "slug": "asun",
        "title": "Asun",
        "image": "images/asun.jpg",
        "price": 1000,
        "cf": 100,
        "total": 1100,
        "kitchen": "Deli Buds Kitchen",
        "description": "Spicy roasted goat meat, a traditional Nigerian delicacy that packs a punch of flavor.",
        "kitchen_slug": "deli-buds-kitchen",
    "category": "dessert"
    },
    {
        "slug": "boli-and-turkey",
        "title": "Boli and Turkey",
        "image": "images/bole.jpg",
        "price": 2700,
        "cf": 100,
        "total": 2800,
        "kitchen": "Deli Buds Kitchen",
        "description": "Grilled plantains (boli) served with succulent, spicy turkey, offering a perfect blend of flavors.",
        "kitchen_slug": "deli-buds-kitchen",
    "category": "special"
    },
    {
        "slug": "catfish",
        "title": "Catfish",
        "image": "images/catfish.jpg",
        "price": 1500,
        "cf": 100,
        "total": 1600,
        "kitchen": "Deli Buds Kitchen",
        "description": "A whole grilled catfish, seasoned to perfection and served with a side of spicy sauce.",
        "kitchen_slug": "deli-buds-kitchen",
    "category": "dessert"
    },
    {
        "slug": "rice",
        "title": "Rice",
        "image": "images/rice.jpg",
        "price": 150,
        "cf": 50,
        "total": 200,
        "kitchen": "SOTA Kitchen",
        "description": "A simple and delicious serving of steamed white rice, a versatile side dish for any meal.",
        "kitchen_slug": "sota-kitchen",
    "category": "special"
    },
    {
        "slug": "eba",
        "title": "Eba",
        "image": "images/eba.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "kitchen": "SOTA Kitchen",
        "description": "A traditional Nigerian staple made from garri, perfect for pairing with various soups.",
        "kitchen_slug": "sota-kitchen",
    "category": "swallow"
    },
    {
        "slug": "moi-moi",
        "title": "Moi Moi",
        "image": "images/moi_moi.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "kitchen": "SOTA Kitchen",
        "description": "A steamed bean pudding made from ground peeled beans, onions, and spices, a nutritious and tasty side dish.",
        "kitchen_slug": "sota-kitchen",
    "category": "special"
    },
    {
        "slug": "okro",
        "title": "Okro Soup",
        "image": "images/okrosoup.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "kitchen": "SOTA Kitchen",
        "description": "A rich and slimy okro soup, cooked with various seasonings, perfect for pairing with traditional Nigerian swallows.",
        "kitchen_slug": "sota-kitchen",
    "category": "soup"
    },
    {
    "slug": "jollof-rice",
    "title": "Jollof Rice",
    "image": "images/jollof.jpg",
    "price": 150,
    "cf": 50,
    "total": 200,
    "kitchen": "Blossom Kitchen",
    "description": "A flavorful rice dish cooked with tomato and spices.",
    "kitchen_slug": "blossom-kitchen",
    "category": "special"
},
{
    "slug": "fried-rice",
    "title": "Fried Rice",
    "image": "images/friedrice.jpg",
    "price": 150,
    "cf": 50,
    "total": 200,
    "kitchen": "Blossom Kitchen",
    "description": "Stir-fried rice mixed with vegetables and seasonings.",
    "kitchen_slug": "blossom-kitchen",
    "category": "special"
},
{
    "slug": "jollof-spaghetti",
    "title": "Jollof Spaghetti",
    "image": "images/jollofspag.jpg",
    "price": 200,
    "cf": 50,
    "total": 250,
    "kitchen": "Blossom Kitchen",
    "description": "Spaghetti cooked in a rich tomato-based sauce.",
    "kitchen_slug": "blossom-kitchen",
    "category": "special"
},
{
    "slug": "beans-and-corn",
    "title": "Beans and Corn",
    "image": "images/oloka.jpg",
    "price": 200,
    "cf": 50,
    "total": 250,
    "kitchen": "Blossom Kitchen",
    "description": "A hearty mix of beans and corn seasoned to perfection.",
    "kitchen_slug": "blossom-kitchen",
    "category": "special"
},
{
    "slug": "white-spaghetti",
    "title": "White Spaghetti",
    "image": "images/white_spag.jpg",
    "price": 150,
    "cf": 50,
    "total": 200,
    "kitchen": "Blossom Kitchen",
    "description": "Plain boiled spaghetti, ready to be enjoyed with any sauce.",
    "kitchen_slug": "blossom-kitchen",
    "category": "special"
},
{
    "slug": "white-rice",
    "title": "White Rice",
    "image": "images/white_rice.jpeg",
    "price": 150,
    "cf": 50,
    "total": 200,
    "kitchen": "Blossom Kitchen",
    "description": "Steamed white rice, a versatile side dish.",
    "kitchen_slug": "blossom-kitchen",
    "category": "special"
},
{
    "slug": "beans",
    "title": "Beans",
    "image": "images/beans.png",
    "price": 200,
    "cf": 50,
    "total": 250,
    "kitchen": "Blossom Kitchen",
    "description": "Soft-cooked beans, rich in flavor and nutrients.",
    "kitchen_slug": "blossom-kitchen",
    "category": "special"
},
{
    "slug": "yam-and-egg",
    "title": "Yam and Egg",
    "image": "images/yam_eggs.webp",
    "price": 500,
    "cf": 100,
    "total": 600,
    "kitchen": "Blossom Kitchen",
    "description": "Boiled yam served with a tasty egg sauce.",
    "kitchen_slug": "blossom-kitchen",
    "category": "special"
},
{
    "slug": "potato-and-egg",
    "title": "Potato and Egg",
    "image": "images/potato_eggs.jpg",
    "price": 500,
    "cf": 100,
    "total": 600,
    "kitchen": "Blossom Kitchen",
    "description": "Boiled potatoes paired with a savory egg sauce.",
    "kitchen_slug": "blossom-kitchen",
    "category": "special"
},
{
    "slug": "amala",
    "title": "Amala",
    "image": "images/amala.jpg",
    "price": 200,
    "cf": 50,
    "total": 250,
    "kitchen": "Blossom Kitchen",
    "description": "Traditional Nigerian swallow made from yam flour.",
    "kitchen_slug": "blossom-kitchen",
    "category": "swallow"
},
{
    "slug": "semolina-semovita",
    "title": "Semolina or Semovita",
    "image": "images/semolina.jpg",
    "price": 200,
    "cf": 50,
    "total": 250,
    "kitchen": "Blossom Kitchen",
    "description": "Smooth, dough-like meal perfect for pairing with soups.",
    "kitchen_slug": "blossom-kitchen",
    "category": "swallow"
},
{
    "slug": "fufu",
    "title": "Fufu",
    "image": "images/fufu.webp",
    "price": 100,
    "cf": 50,
    "total": 150,
    "kitchen": "Blossom Kitchen",
    "description": "Soft and stretchy swallow, often enjoyed with soups.",
    "kitchen_slug": "blossom-kitchen",
    "category": "swallow"
},
{
    "slug": "egg-sauce",
    "title": "Egg Sauce",
    "image": "images/egg_sauce.jpg",
    "price": 100,
    "cf": 50,
    "total": 150,
    "kitchen": "Blossom Kitchen",
    "description": "A flavorful sauce made with scrambled eggs and tomatoes.",
    "kitchen_slug": "blossom-kitchen",
    "category": "sauce"
},
{
    "slug": "fried-plantain",
    "title": "Fried Plantain",
    "image": "images/fried_plantain.jpg",
    "price": 50,
    "cf": 25,
    "total": 75,
    "kitchen": "Blossom Kitchen",
    "description": "Crispy, golden slices of ripe plantain.",
    "kitchen_slug": "blossom-kitchen",
    "category": "side"
},
{
    "slug": "porridge-yam",
    "title": "Porridge Yam",
    "image": "images/yam_porridge.jpg",
    "price": 200,
    "cf": 50,
    "total": 250,
    "kitchen": "Blossom Kitchen",
    "description": "Yam cubes cooked in a rich and spicy tomato sauce.",
    "kitchen_slug": "blossom-kitchen",
    "category": "special"
},
{
    "slug": "akara",
    "title": "Akara",
    "image": "images/akara.jpg",
    "price": 100,
    "cf": 50,
    "total": 150,
    "kitchen": "Blossom Kitchen",
    "description": "Fried bean cakes, crispy on the outside, soft inside.",
    "kitchen_slug": "blossom-kitchen",
    "category": "snack"
},
{
    "slug": "doughnut",
    "title": "Doughnut",
    "image": "images/doughnut.jpg",
    "price": 400,
    "cf": 100,
    "total": 500,
    "kitchen": "Blossom Kitchen",
    "description": "Sweet, fluffy pastry with a soft, airy texture.",
    "kitchen_slug": "blossom-kitchen",
    "category": "snack"
},
{
    "slug": "ice-cream",
    "title": "Ice Cream",
    "image": "images/ice_cream.jpg",
    "price": 1000,
    "cf": 100,
    "total": 1100,
    "kitchen": "Blossom Kitchen",
    "description": "Cold, creamy dessert available in various flavors.",
    "kitchen_slug": "blossom-kitchen",
    "category": "dessert"
},
{
    "slug": "meat",
    "title": "Meat",
    "image": "images/meat.jpg",
    "price": 100,
    "cf": 50,
    "total": 150,
    "kitchen": "Blossom Kitchen",
    "description": "Tender and juicy meat, seasoned to perfection.",
    "kitchen_slug": "blossom-kitchen",
    "category": "protein"
},
{
    "slug": "turkey",
    "title": "Turkey",
    "image": "images/turkey.jpg",
    "price": 1500,
    "cf": 100,
    "total": 1600,
    "kitchen": "Blossom Kitchen",
    "description": "Succulent turkey pieces, full of flavor.",
    "kitchen_slug": "blossom-kitchen",
    "category": "protein"
},
{
    "slug": "chicken",
    "title": "Chicken",
    "image": "images/chicken.jpg",
    "price": 1500,
    "cf": 100,
    "total": 1600,
    "kitchen": "Blossom Kitchen",
    "description": "Grilled or fried chicken, crispy on the outside.",
    "kitchen_slug": "blossom-kitchen",
    "category": "protein"
},
{
    "slug": "fish",
    "title": "Fish",
    "image": "images/fish.jpg",
    "price": 800,
    "cf": 100,
    "total": 900,
    "kitchen": "Blossom Kitchen",
    "description": "Grilled or fried fish, seasoned to perfection.",
    "kitchen_slug": "blossom-kitchen",
    "category": "protein"
},
{
    "slug": "ewedu",
    "title": "Ewedu Soup",
    "image": "images/ewedu.jpg",
    "price": 200,
    "cf": 50,
    "total": 250,
    "kitchen": "Blossom Kitchen",
    "description": "A slimy green soup made from jute leaves.",
    "kitchen_slug": "blossom-kitchen",
    "category": "soup"
},
{
    "slug": "egusi",
    "title": "Egusi Soup",
    "image": "images/egusi.jpg",
    "price": 200,
    "cf": 50,
    "total": 250,
    "kitchen": "Blossom Kitchen",
    "description": "A thick, nutty soup made from ground melon seeds.",
    "kitchen_slug": "blossom-kitchen",
    "category": "soup"
},
{
    "slug": "efo",
    "title": "Efo Soup",
    "image": "images/efo.jpg",
    "price": 200,
    "cf": 50,
    "total": 250,
    "kitchen": "Blossom Kitchen",
    "description": "A rich, leafy vegetable soup, seasoned with spices.",
    "kitchen_slug": "blossom-kitchen",
    "category": "soup"
}
]

def organize_by_kitchen(menu):
    kitchen_dict = {}
    
    for item in menu:
        kitchen_name = item["kitchen"].lower()
        kitchen_name = kitchen_name.split(" ")
        kitchen_name = "-".join(kitchen_name)
        
        if kitchen_name not in kitchen_dict:
            kitchen_dict[kitchen_name] = []
        
        kitchen_dict[kitchen_name].append({
            "slug": item["slug"],
            "title": item["title"],
            "image": item["image"],
            "price": item["price"],
            "cf": item["cf"],
            "total": item["total"],
            "description": item["description"],
            "kitchen_slug": item["kitchen_slug"],
            "category": item["category"]
        })
    
    return kitchen_dict

kitchen_menu = organize_by_kitchen(_menu2)

def generate_specials(menu):
    special_kitchen = {}
    for item in menu:
        kitchen_name = item["kitchen"].lower()
        kitchen_name = kitchen_name.split(" ")
        kitchen_name = "-".join(kitchen_name)
        
        if kitchen_name not in special_kitchen:
            special_kitchen[kitchen_name] = []
            
        if "special" in item["category"]:
            special_kitchen[kitchen_name].append({
            "slug": item["slug"],
            "title": item["title"],
            "image": item["image"],
            "price": item["price"],
            "cf": item["cf"],
            "total": item["total"],
            "description": item["description"],
            "kitchen_slug": item["kitchen_slug"],
            "category": item["category"]
        })
    return special_kitchen

special_menu = generate_specials(_menu2)