"""demand URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.chumma),
    # path('a',views.admin_view),
    path('b',views.regi),
    path('c',views.uslogin),
    path('d',views.profile),
    path('e',views.logout),
    path('f',views.worregi),
    path('g',views.worentry),
    path('h',views.display),
    path('i',views.deletew),
    path('j',views.acceptw),
    path('k',views.display2),
    path('l',views.userview),
    path('m',views.msg1),
    # path('n',views.selectw),
    path('o',views.display3),
    path('p',views.msg2),
    path('chose_worker/<str:id>',views.choose_worker),
    path('send_req/<str:wor>',views.send_request),
    path('view_req',views.view_request),
    path('view_accept_request',views.accept_request),
    path('reject_accept_request',views.reject_request),
    path('pay_req/<str:wor>',views.pay_start),
    path('view_pay_1',views.customer_pay_view),
    path('to_payment',views.payment),
    path('amount_for_payment',views.to_the_payment),
    path('feed',views.feedback), # ith namal kodukkuna feed back
    path('admin_feed',views.adfeed), # ith admin feed_back kaanunath
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
