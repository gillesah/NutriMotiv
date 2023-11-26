import flet as ft


def get_notifications_view(page):
    # Créez ici les éléments de votre page de notifications
    page = ft.Column([
        ft.Text("Page des Notifications"),
        ft.Text("Page des Notifications"),
        # Ajoutez d'autres éléments ici
    ])
    return ft.View(
        "/notifications",
        [ft.AppBar(title=ft.Text("Notifications Page")), ...]  # Autres widgets
    )
