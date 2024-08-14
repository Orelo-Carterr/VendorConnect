from datetime import *
import random
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


_menu2 = [
    {
        "slug": "jollof-rice",
        "title": "Jollof Rice",
        "image": "images/jollof.jpg",
        "price": 150,
        "cf": 50,
        "total": 200,
        "kitchen": "Adonai Kitchen",
        "description": "A classic West African dish made from long-grain rice cooked in a tomato-based sauce with spices."
    },
    {
        "slug": "fried-rice",
        "title": "Fried Rice",
        "image": "images/friedrice.jpg",
        "price": 150,
        "cf": 50,
        "total": 200,
        "kitchen": "Adonai Kitchen",
        "description": "Rice stir-fried with vegetables, eggs, and spices, often served with chicken or beef."
    },
    {
        "slug": "jollof-spaghetti",
        "title": "Jollof Spaghetti",
        "image": "images/jollofspag.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "kitchen": "Adonai Kitchen",
        "description": "Spaghetti cooked in a rich tomato sauce, similar to Jollof Rice but with a twist."
    },
    {
        "slug": "beans-and-corn",
        "title": "Beans and Corn",
        "image": "images/oloka.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "kitchen": "Adonai Kitchen",
        "description": "A nutritious and filling dish made from a mix of beans and corn, often seasoned with palm oil and spices."
    },
    {
        "slug": "white-spaghetti",
        "title": "White Spaghetti",
        "image": "images/white_spag.jpg",
        "price": 150,
        "cf": 50,
        "total": 200,
        "kitchen": "Adonai Kitchen",
        "description": "Simple boiled spaghetti served with a light sauce or as a base for other toppings."
    },
    {
        "slug": "white-rice",
        "title": "White Rice",
        "image": "images/white_rice.jpeg",
        "price": 150,
        "cf": 50,
        "total": 200,
        "kitchen": "Adonai Kitchen",
        "description": "Steamed white rice, a staple side dish perfect for pairing with stews and sauces."
    },
    {
        "slug": "beans",
        "title": "Beans",
        "image": "images/beans.png",
        "price": 200,
        "cf": 50,
        "total": 250,
        "kitchen": "Adonai Kitchen",
        "description": "Hearty and flavorful beans cooked to perfection, often enjoyed with rice or bread."
    },
    {
        "slug": "yam-and-egg",
        "title": "Yam and Egg",
        "image": "images/yam_eggs.webp",
        "price": 500,
        "cf": 100,
        "total": 600,
        "kitchen": "Adonai Kitchen",
        "description": "Boiled yam served with a tasty egg sauce, a popular breakfast or brunch option."
    },
    {
        "slug": "potato-and-egg",
        "title": "Potato and Egg",
        "image": "images/potato_eggs.jpg",
        "price": 500,
        "cf": 100,
        "total": 600,
        "kitchen": "Adonai Kitchen",
        "description": "A satisfying dish featuring boiled or fried potatoes paired with an egg sauce."
    },
    {
        "slug": "amala",
        "title": "Amala",
        "image": "images/amala.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "kitchen": "Adonai Kitchen",
        "description": "A traditional Yoruba dish made from yam flour, served with various soups."
    },
    {
        "slug": "semolina-semovita",
        "title": "Semolina or Semovita",
        "image": "images/semolina.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "kitchen": "Adonai Kitchen",
        "description": "Smooth and soft, Semolina or Semovita is a perfect accompaniment to rich, hearty soups."
    },
    {
        "slug": "fufu",
        "title": "Fufu",
        "image": "images/fufu.webp",
        "price": 100,
        "cf": 50,
        "total": 150,
        "kitchen": "Adonai Kitchen",
        "description": "A starchy side dish made from cassava, often served with a variety of African soups."
    },
    {
        "slug": "egg-sauce",
        "title": "Egg Sauce",
        "image": "images/egg_sauce.jpg",
        "price": 100,
        "cf": 50,
        "total": 150,
        "kitchen": "Adonai Kitchen",
        "description": "A savory sauce made with eggs, tomatoes, and onions, perfect for pairing with yams or potatoes."
    },
    {
        "slug": "fried-plantain",
        "title": "Fried Plantain",
        "image": "images/fried_plantain.jpg",
        "price": 50,
        "cf": 25,
        "total": 75,
        "kitchen": "Adonai Kitchen",
        "description": "Sweet, ripe plantains fried to a golden brown, a delicious side or snack."
    },
    {
        "slug": "porridge-yam",
        "title": "Porridge Yam",
        "image": "images/yam_porridge.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "kitchen": "Adonai Kitchen",
        "description": "Yam cooked in a rich sauce with palm oil, tomatoes, and spices, creating a thick porridge."
    },
    {
        "slug": "akara",
        "title": "Akara",
        "image": "images/akara.jpg",
        "price": 100,
        "cf": 50,
        "total": 150,
        "kitchen": "Adonai Kitchen",
        "description": "Deep-fried bean cakes made from ground black-eyed peas, a popular street food snack."
    },
    {
        "slug": "doughnut",
        "title": "Doughnut",
        "image": "images/doughnut.jpg",
        "price": 400,
        "cf": 100,
        "total": 500,
        "kitchen": "Adonai Kitchen",
        "description": "Soft and fluffy doughnuts, sweetened and fried to perfection, a delightful treat."
    },
    {
        "slug": "ice-cream",
        "title": "Ice Cream",
        "image": "images/icecream.jpg",
        "price": 1000,
        "cf": 100,
        "total": 1100,
        "kitchen": "Adonai Kitchen",
        "description": "Creamy and cold, this ice cream is the perfect dessert to cool off on a hot day."
    },
    {
        "slug": "meat",
        "title": "Meat",
        "image": "images/meat.jpg",
        "price": 100,
        "cf": 50,
        "total": 150,
        "kitchen": "Adonai Kitchen",
        "description": "Tender and flavorful meat, perfect as a side dish or main course."
    },
    {
        "slug": "turkey",
        "title": "Turkey",
        "image": "images/turkey.jpeg",
        "price": 1500,
        "cf": 100,
        "total": 1600,
        "kitchen": "Adonai Kitchen",
        "description": "Juicy and well-seasoned turkey, roasted to perfection and served hot."
    },
    {
        "slug": "chicken",
        "title": "Chicken",
        "image": "images/friedchicken.jpg",
        "price": 1500,
        "cf": 100,
        "total": 1600,
        "kitchen": "Adonai Kitchen",
        "description": "Succulent chicken, seasoned and cooked to a golden brown, a crowd favorite."
    },
    {
        "slug": "fish",
        "title": "Fish",
        "image": "images/fish.jpg",
        "price": 800,
        "cf": 100,
        "total": 900,
        "kitchen": "Adonai Kitchen",
        "description": "Fresh fish, grilled or fried, served with a side of vegetables or rice."
    },
    {
        "slug": "ewedu",
        "title": "Ewedu Soup",
        "image": "images/ewedu.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "kitchen": "Adonai Kitchen",
        "description": "A traditional Yoruba soup made from jute leaves, often served with Amala."
    },
    {
        "slug": "efo",
        "title": "Efo Soup",
        "image": "images/efo.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "kitchen": "Adonai Kitchen",
        "description": "A nutritious and flavorful soup made from leafy greens, commonly served with pounded yam or fufu."
    },
    {
        "slug": "ogbono",
        "title": "Ogbono Soup",
        "image": "images/ogbonosoup.jpeg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "kitchen": "Adonai Kitchen",
        "description": "A thick and hearty Nigerian soup made from ground ogbono seeds, known for its slimy texture."
    },
    {
        "slug": "vegetable-soup",
        "title": "Vegetable Soup",
        "image": "images/vegetable_soup.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "kitchen": "Adonai Kitchen",
        "description": "A rich and savory soup made with various vegetables, often served with fufu or rice."
    },
    {
        "slug": "egusi",
        "title": "Egusi Soup",
        "image": "images/egusi.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "kitchen": "Adonai Kitchen",
        "description": "A popular Nigerian soup made with ground melon seeds, often enjoyed with pounded yam."
    },
    {
        "slug": "ogbono-and-egusi",
        "title": "Ogbono and Egusi Soup",
        "image": "images/egusi_ogbono.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "kitchen": "Adonai Kitchen",
        "description": "A combination of Ogbono and Egusi, creating a thick, flavorful soup."
    },
    {
        "slug": "rice-and-beans",
        "title": "Rice and Beans",
        "image": "images/rice_beans.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "kitchen": "Adonai Kitchen",
        "description": "A hearty mix of rice and beans, often served with fried plantain or a side of meat."
    },
    {
        "slug": "bread",
        "title": "Bread",
        "image": "images/bread.jpg",
        "price": 500,
        "cf": 100,
        "total": 600,
        "kitchen": "Hot and Spicy Kitchen",
        "description": "A freshly baked loaf of soft, fluffy bread, perfect for sandwiches or as a side to any meal."
    },
    {
        "slug": "noodles",
        "title": "Noodles",
        "image": "images/noodles.jpg",
        "price": 400,
        "cf": 50,
        "total": 450,
        "kitchen": "Hot and Spicy Kitchen",
        "description": "A savory and spicy plate of stir-fried noodles, cooked to perfection with a blend of special seasonings."
    },
    {
        "slug": "egg",
        "title": "Egg",
        "image": "images/egg.jpg",
        "price": 300,
        "cf": 50,
        "total": 350,
        "kitchen": "Hot and Spicy Kitchen",
        "description": "A perfectly boiled egg, a versatile side that complements any main dish."
    },
    {
        "slug": "sharwarma",
        "title": "Sharwarma",
        "image": "images/sharwarma.jpg",
        "price": 2000,
        "cf": 100,
        "total": 2100,
        "kitchen": "Hot and Spicy Kitchen",
        "description": "A mouthwatering wrap filled with tender, marinated meat, fresh vegetables, and a rich, flavorful sauce."
    },
    {
        "slug": "chicken-and-chips",
        "title": "Chicken and Chips",
        "image": "images/chicken_and_chips.jpg",
        "price": 4000,
        "cf": 100,
        "total": 4100,
        "kitchen": "Hot and Spicy Kitchen",
        "description": "A generous portion of crispy fried chicken served with golden fries, a perfect comfort meal."
    },
    {
        "slug": "egg-roll",
        "title": "Egg Roll",
        "image": "images/egg_roll.jpg",
        "price": 400,
        "cf": 50,
        "total": 450,
        "kitchen": "Hot and Spicy Kitchen",
        "description": "A soft, doughy roll filled with a savory boiled egg, ideal for a quick snack."
    },
    {
        "slug": "fish-roll",
        "title": "Fish Roll",
        "image": "images/fish_roll.jpg",
        "price": 150,
        "cf": 50,
        "total": 200,
        "kitchen": "Hot and Spicy Kitchen",
        "description": "A delightful pastry filled with seasoned fish, offering a tasty and convenient snack option."
    },
    {
        "slug": "smoothie",
        "title": "Smoothie",
        "image": "images/smoothie.jpg",
        "price": 1000,
        "cf": 100,
        "total": 1100,
        "kitchen": "Deli Buds Kitchen",
        "description": "A refreshing blend of fruits, providing a healthy and delicious drink to quench your thirst."
    },
    {
        "slug": "suya",
        "title": "Suya",
        "image": "images/suya.jpg",
        "price": 700,
        "cf": 50,
        "total": 750,
        "kitchen": "Deli Buds Kitchen",
        "description": "A spicy and succulent skewered meat, grilled to perfection and seasoned with traditional suya spices."
    },
    {
        "slug": "gizzards",
        "title": "Gizzards",
        "image": "images/gizzards.jpg",
        "price": 700,
        "cf": 50,
        "total": 750,
        "kitchen": "Deli Buds Kitchen",
        "description": "Tender and flavorful gizzards, cooked with a blend of spices, perfect for a quick snack or as a side dish."
    },
    {
        "slug": "shaki-suya",
        "title": "Shaki Suya",
        "image": "images/shaki_suya.jpg",
        "price": 700,
        "cf": 50,
        "total": 750,
        "kitchen": "Deli Buds Kitchen",
        "description": "Spicy and tender shaki (tripe) grilled with a unique blend of suya spices, offering a traditional taste experience."
    },
    {
        "slug": "goat-meat-suya",
        "title": "Goat Meat Suya",
        "image": "images/goat_meat_suya.jpg",
        "price": 700,
        "cf": 50,
        "total": 750,
        "kitchen": "Deli Buds Kitchen",
        "description": "Juicy goat meat grilled with suya spices, a must-try for lovers of spicy, flavorful meats."
    },
    {
        "slug": "small-chops",
        "title": "Small Chops",
        "image": "images/smallchops.jpg",
        "price": 1700,
        "cf": 100,
        "total": 1800,
        "kitchen": "Deli Buds Kitchen",
        "description": "A delightful mix of bite-sized snacks, perfect for sharing and enjoying with friends."
    },
    {
        "slug": "spaghetti-stir-fry",
        "title": "Spaghetti Stir Fry",
        "image": "images/spaghetti_stir_fry.jpg",
        "price": 3000,
        "cf": 100,
        "total": 3100,
        "kitchen": "Deli Buds Kitchen",
        "description": "A flavorful stir-fried spaghetti dish, packed with vegetables and protein, offering a satisfying meal."
    },
    {
        "slug": "asun",
        "title": "Asun",
        "image": "images/asun.jpg",
        "price": 1000,
        "cf": 100,
        "total": 1100,
        "kitchen": "Deli Buds Kitchen",
        "description": "Spicy roasted goat meat, a traditional Nigerian delicacy that packs a punch of flavor."
    },
    {
        "slug": "boli-and-turkey",
        "title": "Boli and Turkey",
        "image": "images/bole.jpg",
        "price": 2700,
        "cf": 100,
        "total": 2800,
        "kitchen": "Deli Buds Kitchen",
        "description": "Grilled plantains (boli) served with succulent, spicy turkey, offering a perfect blend of flavors."
    },
    {
        "slug": "catfish",
        "title": "Catfish",
        "image": "images/catfish.jpg",
        "price": 1500,
        "cf": 100,
        "total": 1600,
        "kitchen": "Deli Buds Kitchen",
        "description": "A whole grilled catfish, seasoned to perfection and served with a side of spicy sauce."
    },
    {
        "slug": "rice",
        "title": "Rice",
        "image": "images/rice.jpg",
        "price": 150,
        "cf": 50,
        "total": 200,
        "kitchen": "SOTA Kitchen",
        "description": "A simple and delicious serving of steamed white rice, a versatile side dish for any meal."
    },
    {
        "slug": "eba",
        "title": "Eba",
        "image": "images/eba.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "kitchen": "SOTA Kitchen",
        "description": "A traditional Nigerian staple made from garri, perfect for pairing with various soups."
    },
    {
        "slug": "moi-moi",
        "title": "Moi Moi",
        "image": "images/moi_moi.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "kitchen": "SOTA Kitchen",
        "description": "A steamed bean pudding made from ground peeled beans, onions, and spices, a nutritious and tasty side dish."
    },
    {
        "slug": "okro",
        "title": "Okro Soup",
        "image": "images/okrosoup.jpg",
        "price": 200,
        "cf": 50,
        "total": 250,
        "kitchen": "SOTA Kitchen",
        "description": "A rich and slimy okro soup, cooked with various seasonings, perfect for pairing with traditional Nigerian swallows."
    },
    {
    "slug": "jollof-rice",
    "title": "Jollof Rice",
    "image": "images/jollof_rice.jpg",
    "price": 150,
    "cf": 50,
    "total": 200,
    "kitchen": "Blossom Kitchen",
    "description": "A flavorful rice dish cooked with tomato and spices."
},
{
    "slug": "fried-rice",
    "title": "Fried Rice",
    "image": "images/fried_rice.jpg",
    "price": 150,
    "cf": 50,
    "total": 200,
    "kitchen": "Blossom Kitchen",
    "description": "Stir-fried rice mixed with vegetables and seasonings."
},
{
    "slug": "jollof-spaghetti",
    "title": "Jollof Spaghetti",
    "image": "images/jollof_spaghetti.jpg",
    "price": 200,
    "cf": 50,
    "total": 250,
    "kitchen": "Blossom Kitchen",
    "description": "Spaghetti cooked in a rich tomato-based sauce."
},
{
    "slug": "beans-and-corn",
    "title": "Beans and Corn",
    "image": "images/beans_and_corn.jpg",
    "price": 200,
    "cf": 50,
    "total": 250,
    "kitchen": "Blossom Kitchen",
    "description": "A hearty mix of beans and corn seasoned to perfection."
},
{
    "slug": "white-spaghetti",
    "title": "White Spaghetti",
    "image": "images/white_spaghetti.jpg",
    "price": 150,
    "cf": 50,
    "total": 200,
    "kitchen": "Blossom Kitchen",
    "description": "Plain boiled spaghetti, ready to be enjoyed with any sauce."
},
{
    "slug": "white-rice",
    "title": "White Rice",
    "image": "images/white_rice.jpg",
    "price": 150,
    "cf": 50,
    "total": 200,
    "kitchen": "Blossom Kitchen",
    "description": "Steamed white rice, a versatile side dish."
},
{
    "slug": "beans",
    "title": "Beans",
    "image": "images/beans.jpg",
    "price": 200,
    "cf": 50,
    "total": 250,
    "kitchen": "Blossom Kitchen",
    "description": "Soft-cooked beans, rich in flavor and nutrients."
},
{
    "slug": "yam-and-egg",
    "title": "Yam and Egg",
    "image": "images/yam_and_egg.jpg",
    "price": 500,
    "cf": 100,
    "total": 600,
    "kitchen": "Blossom Kitchen",
    "description": "Boiled yam served with a tasty egg sauce."
},
{
    "slug": "potato-and-egg",
    "title": "Potato and Egg",
    "image": "images/potato_and_egg.jpg",
    "price": 500,
    "cf": 100,
    "total": 600,
    "kitchen": "Blossom Kitchen",
    "description": "Boiled potatoes paired with a savory egg sauce."
},
{
    "slug": "amala",
    "title": "Amala",
    "image": "images/amala.jpg",
    "price": 200,
    "cf": 50,
    "total": 250,
    "kitchen": "Blossom Kitchen",
    "description": "Traditional Nigerian swallow made from yam flour."
},
{
    "slug": "semolina-semovita",
    "title": "Semolina or Semovita",
    "image": "images/semolina.jpg",
    "price": 200,
    "cf": 50,
    "total": 250,
    "kitchen": "Blossom Kitchen",
    "description": "Smooth, dough-like meal perfect for pairing with soups."
},
{
    "slug": "fufu",
    "title": "Fufu",
    "image": "images/fufu.jpg",
    "price": 100,
    "cf": 50,
    "total": 150,
    "kitchen": "Blossom Kitchen",
    "description": "Soft and stretchy swallow, often enjoyed with soups."
},
{
    "slug": "egg-sauce",
    "title": "Egg Sauce",
    "image": "images/egg_sauce.jpg",
    "price": 100,
    "cf": 50,
    "total": 150,
    "kitchen": "Blossom Kitchen",
    "description": "A flavorful sauce made with scrambled eggs and tomatoes."
},
{
    "slug": "fried-plantain",
    "title": "Fried Plantain",
    "image": "images/fried_plantain.jpg",
    "price": 50,
    "cf": 25,
    "total": 75,
    "kitchen": "Blossom Kitchen",
    "description": "Crispy, golden slices of ripe plantain."
},
{
    "slug": "porridge-yam",
    "title": "Porridge Yam",
    "image": "images/porridge_yam.jpg",
    "price": 200,
    "cf": 50,
    "total": 250,
    "kitchen": "Blossom Kitchen",
    "description": "Yam cubes cooked in a rich and spicy tomato sauce."
},
{
    "slug": "akara",
    "title": "Akara",
    "image": "images/akara.jpg",
    "price": 100,
    "cf": 50,
    "total": 150,
    "kitchen": "Blossom Kitchen",
    "description": "Fried bean cakes, crispy on the outside, soft inside."
},
{
    "slug": "doughnut",
    "title": "Doughnut",
    "image": "images/doughnut.jpg",
    "price": 400,
    "cf": 100,
    "total": 500,
    "kitchen": "Blossom Kitchen",
    "description": "Sweet, fluffy pastry with a soft, airy texture."
},
{
    "slug": "ice-cream",
    "title": "Ice Cream",
    "image": "images/ice_cream.jpg",
    "price": 1000,
    "cf": 100,
    "total": 1100,
    "kitchen": "Blossom Kitchen",
    "description": "Cold, creamy dessert available in various flavors."
},
{
    "slug": "meat",
    "title": "Meat",
    "image": "images/meat.jpg",
    "price": 100,
    "cf": 50,
    "total": 150,
    "kitchen": "Blossom Kitchen",
    "description": "Tender and juicy meat, seasoned to perfection."
},
{
    "slug": "turkey",
    "title": "Turkey",
    "image": "images/turkey.jpg",
    "price": 1500,
    "cf": 100,
    "total": 1600,
    "kitchen": "Blossom Kitchen",
    "description": "Succulent turkey pieces, full of flavor."
},
{
    "slug": "chicken",
    "title": "Chicken",
    "image": "images/chicken.jpg",
    "price": 1500,
    "cf": 100,
    "total": 1600,
    "kitchen": "Blossom Kitchen",
    "description": "Grilled or fried chicken, crispy on the outside."
},
{
    "slug": "fish",
    "title": "Fish",
    "image": "images/fish.jpg",
    "price": 800,
    "cf": 100,
    "total": 900,
    "kitchen": "Blossom Kitchen",
    "description": "Grilled or fried fish, seasoned to perfection."
},
{
    "slug": "ewedu",
    "title": "Ewedu Soup",
    "image": "images/ewedu.jpg",
    "price": 200,
    "cf": 50,
    "total": 250,
    "kitchen": "Blossom Kitchen",
    "description": "A slimy green soup made from jute leaves."
},
{
    "slug": "egusi",
    "title": "Egusi Soup",
    "image": "images/egusi.jpg",
    "price": 200,
    "cf": 50,
    "total": 250,
    "kitchen": "Blossom Kitchen",
    "description": "A thick, nutty soup made from ground melon seeds."
},
{
    "slug": "efo",
    "title": "Efo Soup",
    "image": "images/efo.jpg",
    "price": 200,
    "cf": 50,
    "total": 250,
    "kitchen": "Blossom Kitchen",
    "description": "A rich, leafy vegetable soup, seasoned with spices."
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
            "description": item["description"]
        })
    
    return kitchen_dict

kitchen_menu = organize_by_kitchen(_menu2)

# tabs = {
#   "Access-control" : "Access-control Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis",
#   "Goals" : "Goals Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis",
  
# }

#  sp_services = [
#   {
#         "slug": "secured-managed-it",
#         "excerpt": "Secured ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor sit amet, dolor consectetur",
#         "title": "Secured Managed IT",
#         "image" : rimages/andom.choice(["consultation", "consultation2"]) + ".jpg",
#         "content": """Nowon offers the best service in secured IT management. The field of IT management is a vital component in the success of an organization as information technology serves as the backbone of virtually every aspect of business operations. IT management involves the administration, direction, and control of various technological resources to meet the objectives of an organization through effective management of IT personnel and resources. It encompasses the strategic decision making, deployment and maintenance of a range of information technology assets including hardware, software, databases, and networks, as well as the optimization of technology use to enhance an organization's productivity and performance.
#           Here are some key aspects of our secured IT management:
#           Conducting regular risk assessments to identify potential vulnerabilities and threats within the IT infrastructure. This involves evaluating security risks, determining their potential impact, and implementing appropriate risk mitigation strategies.
#           Security Policies and Procedures: Developing and enforcing comprehensive security policies and procedures that outline acceptable use of IT resources, password management, data handling practices, incident response protocols, and other security-related guidelines. These policies should be communicated to all employees and regularly updated to address emerging threats.""",
#         "options" : [
#           {
#             "slug": "access-control-services",
#             "excerpt": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor sit amet, dolor consectetur",
#             "title": "Access Control Services",
#             "image" : rimages/andom.choice(["access_control","access_control2"]) + ".jpg",
#             "content": """
#               Implementing strong access control mechanisms to ensure that only authorized individuals have access to sensitive systems and data. This involves using techniques like user authentication, role-based access control (RBAC), and multi-factor authentication (MFA) to verify user identities and restrict access privileges.
#             """
#         },
#         {
#         "slug": "order",
#         "excerpt": "Tega ipsum dolor sit amet, consectetur adipiscing elit,quos ivelit labore vero culpa sed do eiusmod tempor sit amet, dolor consectetur",
#         "title": "Make an Order",
#         "image" : rimages/andom.choice(["consultation", "consultation2"]) + ".jpg",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     },
#         {
#         "slug": "request",
#         "excerpt": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor sit amet, dolor consectetur",
#         "title": "Request Delivery",
#         "image" : rimages/andom.choice(["access_control","access_control2"]) + ".jpg",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#         }
#         ]
#     }
#   ]