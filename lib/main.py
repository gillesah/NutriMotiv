import flet as ft
import matplotlib.pyplot as plt
import io
import base64


def main(page: ft.Page):
    pesees = []

    # Fonction pour naviguer vers la deuxième page
    def navigate_to_page2(e):
        page2 = ft.Page(title="Seconde Page")
        page2.add(ft.Text("Bienvenue sur la seconde page !"))
        page2.open()

    def add_poids(e):
        poids = poids_input.value
        date_pesee = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        pesees.append((poids, date_pesee))
        update_liste_pesees()
        poids_input.value = ""
        page.update()

    # Fonction pour mettre a jour l'affichage de la liste des pesees
    def update_liste_pesees():
        liste_pesees.controls.clear()
        for poids, date in pesees:
            liste_pesees.controls.append(ft.Text(f"{date}: {poids} kg"))
        liste_pesees.update()

    # Fonction pour mettre à jour le graphique

    def update_graph():
        plt.figure(figsize=(8, 4))
        plt.plot(pesées, marker='o')
        plt.title("Evolution du Poids")
        plt.xlabel("Pesées")
        plt.ylabel("Poids (kg)")

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        plt.close()  # Fermer la figure pour libérer la mémoire
        buf.seek(0)
        image_base64 = base64.b64encode(buf.read()).decode()
        buf.close()

        # Mettre à jour la source de l'image
        graph_image.src = f"data:image/png;base64,{image_base64}"

    def update_liste_pesées():
        liste_pesees.controls.clear()
        for poids, date in pesées:
            liste_pesées.controls.append(ft.Text(f"{date}: {poids} kg"))
        liste_pesees.update()

    # Création de la première page
    page.title = "NutriMotiv - Accueil"

    # Bouton pour naviguer vers la seconde page
    navigate_button = ft.ElevatedButton(
        "Aller à la seconde page",
        on_click=navigate_to_page2
    )

    # Ajout du bouton à la page
    page.add(navigate_button)

   # Champ de saisie pour le poids
    poids_input = ft.TextField(label="Entrez votre poids (kg)", width=300)

    # Bouton pour ajouter le poids
    add_button = ft.ElevatedButton("Ajouter le poids", on_click=add_poids)

    # Liste pour afficher les pesees
    liste_pesees = ft.Column()

    # Ajout des widgets a la page
    page.add(poids_input, add_button, liste_pesees)


# Exécution de l'application
if __name__ == "__main__":
    ft.app(target=main)
