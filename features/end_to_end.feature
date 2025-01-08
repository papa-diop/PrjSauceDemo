Feature: E-commerce sur Sauce Demo
    En tant qu'utilisateur,
    Je veux pouvoir acheter des produits sur Sauce Demo,
    Afin de compléter une commande avec succès.

    Scenario: Acheter des produits sur Sauce Demo
        Given je suis sur la page de login de Sauce Demo
        When je me connecte avec "standard_user" et "secret_sauce"
        And je trie la liste du plus cher au moins cher
        And jajoute les deux premiers produits au panier
        And je vais au panier
        Then je verifie quil y a deux produits dans le panier
        And je vais au ckeckout
        When je saisis les informations du client
        When je finalise la commande
        Then je verifie que la commande sest bien realisee
