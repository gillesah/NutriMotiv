import flet as ft
import matplotlib.pyplot as plt
# from matplotlib import graph_image
import io
import base64
from datetime import datetime
import notification


def main(page: ft.Page):
    pesees = []

    # Fonction pour naviguer vers la deuxième page
    # Définition de la fonction pour changer de page
    def on_nav_item_selected(e):
        if e.control.selected_index == 0:
            page.views.content = tracking.get_tracking_page()
        elif e.control.selected_index == 1:
            page.views.content = notification.get_notifications_page()
        page.update()

    # Création de la BottomNavigationBar
    bottom_nav = ft.BottomNavigationBar(
        items=[
            ft.BottomNavigationBarItem(icon=ft.Icon(
                ft.icons.FITNESS_CENTER), label="Poids"),
            ft.BottomNavigationBarItem(icon=ft.Icon(
                ft.icons.NOTIFICATIONS), label="Notifications")
        ],
        on_change=on_nav_item_selected
    )

    # Définir la vue initiale
    page.views.content = tracking.get_tracking_page()
    page.views.bottom = bottom_nav

 # Création de la première page
    page.title = "NutriMotiv - Accueil"


# Exécution de l'application
if __name__ == "__main__":
    ft.app(target=main)
