Feature: Login et Logout sur Sauce Demo
    En tant qu'utilisateur,
    Je veux pouvoir me connecter et me deconnecter de Sauce Demo,
    Afin de.

    Scenario: Login et Logout sur Sauce Demo
        Given je suis sur la page de login de Sauce Demo
        When je me connecte avec "standard_user" et "secret_sauce"
        Then je suis connecte à Sauce Demo
        When je me deconnecte
        Then je suis deconnecte de Sauce Demo

    Scenario: Login avec un compte verrouille
        Given je suis sur la page de login de Sauce Demo
        When je me connecte avec "locked_out_user" et "secret_sauce"
        Then je vois un message derreur indiquant que lutilisateur est verrouille
