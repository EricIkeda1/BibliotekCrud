from django.contrib import admin
from django.urls import path
from biblioteca_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    path('', views.home, name='home'),

    # Livros
    path('livros/', views.lista_livros, name='lista_livros'),
    path('livros/novo/', views.form_livro, name='form_livro'),
    path('livros/editar/<int:id>/', views.form_livro, name='editar_livro'),
    path('livros/deletar/<int:id>/', views.deletar_livro, name='deletar_livro'),

    # Empréstimos
    path('emprestimos/', views.lista_emprestimos, name='lista_emprestimos'),
    path('emprestimos/novo/', views.form_emprestimo, name='form_emprestimo'),
    path('emprestimos/devolver/<int:id>/', views.devolver_emprestimo, name='devolver_emprestimo'),

    # Login / Logout
    # path('login/', auth_views.LoginView.as_view(template_name='biblioteca_app/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
