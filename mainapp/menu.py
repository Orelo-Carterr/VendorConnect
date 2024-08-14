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