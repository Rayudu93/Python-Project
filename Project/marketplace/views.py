import http

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    html_content="""
    <html>
        <head>
            <title>Home Page</title>
        </head>
        <body>
            <h1>Home Page</h1>
            <p>Connecting You with Local Artisans & Handmade Treasures</p>

        <h2>Explore Categories</h2>
        <ul>
            <li>Home Decor</li>
            <li>Jewelry</li>
            <li>Pottery</li>
            <li>Handwoven</li>
        </ul>

        <h2>Featured Products</h2>
        <ul>
            <li>
                <strong>Macrame Wall Hanging</strong><br>
                By: Artisan A
            </li>
            <li>
                <strong>Clay Mug Set</strong><br>
                By: Artisan B
            </li>
            <li>
                <strong>Beaded Necklace</strong><br>
                By: Artisan C
            </li>
        </ul>

        <h2>Why Choose CraftNest?</h2>
        <p>Support local creators, discover unique handcrafted items, and shop ethically.</p>

        <h2>Become a Seller</h2>
        <p><a href="/signup/">Sign up now</a> to showcase your craft to the world!</p>

        <hr>
        <p>© 2025 CraftNest. All rights reserved.</p>
        </body>
    </html>
    """
    return HttpResponse(html_content)
def contact(request):
    html_content="""
    <html>
        <head>
            <title>Contact Page</title>
        </head>
        <body>
            <h1>Contact Page</h1>
        </body>
    </html>
    """
    return HttpResponse(html_content)