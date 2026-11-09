import tkinter as tk


def obrir_finestra_amb_dades():
    # Obtenim el text del quadre d'entrada (Entry)
    nom_usuari = entrada_nom.get()
   
    # Creem la nova finestra
    finestra_filla = tk.Toplevel(finestra_mare)
    finestra_filla.title("Benvinguda personalitzada")
    finestra_filla.geometry("300x150")
   
    # Mostrem les dades rebudes
    missatge = f"Hola, {nom_usuari}!" if nom_usuari else "Hola, desconegut!"
    tk.Label(finestra_filla, text=missatge, font=("Arial", 12, "bold")).pack(pady=30)


# --- Finestra Mare ---
finestra_mare = tk.Tk()
finestra_mare.title("Formulari Principal")
finestra_mare.geometry("400x250")


tk.Label(finestra_mare, text="Escriu el teu nom:").pack(pady=(20, 5))


entrada_nom = tk.Entry(finestra_mare, font=("Arial", 12))
entrada_nom.pack(pady=5)


boto_enviar = tk.Button(finestra_mare, text="Obrir salutació", command=obrir_finestra_amb_dades)
boto_enviar.pack(pady=20)


finestra_mare.mainloop()
