import flet as ft
import notification
import tracking


def main(page: ft.Page):
    page.title = "NutriMotiv - Accueil"

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(tracking.get_tracking_view(page))
        elif page.route == "/notifications":
            page.views.append(notification.get_notifications_view(page))
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)  # Commencez avec la route par défaut


if __name__ == "__main__":
    ft.app(target=main)
