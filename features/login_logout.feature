Feature: Login et Logout sur Sauce Demo
    En tant quutilisateur,
    Je veux pouvoir me connecter et me deconnecter du site Sauce Demo,
    Afin de securiser mon acces aux informations.

    Scenario: Login et Logout sur Sauce Demo
        Given je suis sur la page de login de Sauce Demo
        When je me connecte avec "standard_user" et "secret_sauce"
        Then je suis connecte à Sauce Demo
        When je me deconnecte
        Then je suis deconnecte de Sauce Demo
