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
    }
]

def organize_by_kitchen(menu):
    kitchen_dict = {}
    
    for item in menu:
        kitchen_name = item["kitchen"]
        
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