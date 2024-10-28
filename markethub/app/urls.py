from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm

urlpatterns = [
    path('', views.ProductView.as_view(), name="home"),   # for class method
    path('product-detail/<int:id>', views.ProductDetailView.as_view(), name='product-detail'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    
    # SignUp, Login and Logout URL
    path('registration/', views.CustomRegistrationView.as_view(), name='customerregistration'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm),  name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    # path('logout/', views.user_logout, name='logout'),
    
    # Change Password URL
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    
    # Reset Password URL
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),  # uid64 is given in source code
     path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),
    
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'), 
    path('pluscart/', views.plus_cart), 
    path('minuscart/', views.minus_cart), 
    path('removecart/', views.remove_cart), 
    
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    
    path('orders/', views.orders, name='orders'),
    path('buy/', views.buy_now, name='buy-now'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
