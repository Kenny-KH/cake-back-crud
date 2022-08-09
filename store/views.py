from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.


def business_login_detail(request, blog_id):
    blog_business_login = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'business-login-detail.html', {"post_business_login":blog_business_login})