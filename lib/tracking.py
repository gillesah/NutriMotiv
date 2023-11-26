import flet as ft

def get_tracking_page():
    page = ft.Column([
        ft.Text("Page de Suivi du Poids")
    def add_poids(e):
        try:
            poids = float(poids_input.value)
        except ValueError:
            page.snackbar(ft.Snackbar(
                "Veuillez entrer un nombre valide pour le poids."))
            return

        date_pesee = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Verifier si le poids actuel est inferieur au dernier poids enregistre
        if pesees and poids < pesees[-1][0]:
            show_encouragement()
        pesees.append((poids, date_pesee))
        update_liste_pesees()
        poids_input.value = ""
        page.update()

    def show_encouragement():
        dialog = ft.AlertDialog(
            title=ft.Text("Félicitations !"),
            content=ft.Text(
                "Bravo ! Vous avez perdu du poids ! Continuez comme ça !"),
            actions=[ft.TextButton("OK", on_click=lambda e: dialog.close())]
        )
        page.dialog = dialog
        dialog.open = True
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
        plt.plot(pesees, marker='o')
        plt.title("Evolution du Poids")
        plt.xlabel("pesees")
        plt.ylabel("Poids (kg)")

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        plt.close()  # Fermer la figure pour libérer la mémoire
        buf.seek(0)
        image_base64 = base64.b64encode(buf.read()).decode()
        buf.close()

        # Mettre à jour la source de l'image
      #  graph_image.src = f"data:image/png;base64,{image_base64}"

    def update_liste_pesees():
        liste_pesees.controls.clear()
        for poids, date in pesees:
            liste_pesees.controls.append(ft.Text(f"{date}: {poids} kg"))
        liste_pesees.update()

   
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
    ])
    return page