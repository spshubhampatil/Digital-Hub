from django.contrib import admin
from django.urls import path
from shop.cviews import index
from shop.cviews.index import search, tandc
from shop.cviews.profile import profile
from shop.cviews.updateprofile import updateprofile
from shop.cviews.change_password import ChangePassword
from shop.cviews import LoginView, SignupView
from shop.cviews import ContactView
from shop.cviews.email_verification import sendotp,verifyotp
from shop.cviews.product import productdetails
from shop.cviews.download import downloadfree, downloadpaidproduct
from shop.cviews.orders import my_orders
from shop.cviews.payment import createpayment, verifypayment
from shop.middlewares.login_required_middleware import login_required
from shop.middlewares.cannot_access_after_login import cantaccessafterlogin
from shop.middlewares.active_required import active_required
from shop.cviews.reset_password import ResetPassword, PasswordResetVerification, verifyResetPasswordCode


urlpatterns = [
    path('', index.index, name="index"),

    path('tandc', index.tandc, name="tandc"),
    path('ppolicy', index.ppolicy, name="ppolicy"),

    path('contact', ContactView.as_view(), name="contact"),
    path('login', cantaccessafterlogin(LoginView.as_view()), name="login"),
    path('search', search, name="search"),
    path('profile', active_required(login_required(profile)), name="profile"),
    path('updateprofile', active_required(login_required(updateprofile.as_view())), name="updateprofile"),
    path('logout', index.logout, name="logout"),
    path('signup',cantaccessafterlogin(SignupView.as_view()), name="signup"),
    path('orders',active_required(login_required(my_orders)), name="myorders"),
    path('changepassword',active_required(login_required(ChangePassword.as_view())), name="changepassword"),
    path('reset-password',ResetPassword.as_view(), name="reset-password"),
    path('reset-password-verification',PasswordResetVerification.as_view(), name="reset-password-verification"),
    path('verify-reset-password-code',verifyResetPasswordCode, name="verify-reset-password-code"),

    path('product/<int:product_id>', productdetails, name="productdetails"),
    path('free-download/<int:product_id>', downloadfree, name="downloadfree"),
    path('create-payment/<int:product_id>', active_required(login_required(createpayment)), name="createpayment"),
    path('complete-payment', active_required(login_required(verifypayment)), name="verifypayment"),
    path('download/paidproduct/<int:product_id>',active_required(login_required(downloadpaidproduct)), name="downloadpaidproduct"),
    
    path('send-otp',cantaccessafterlogin(sendotp), name="sendotp"),
    path('verify',cantaccessafterlogin(verifyotp), name="verify")
]
