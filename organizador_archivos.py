import os
import shutil

# Diccionario de categorías y extensiones asociadas
CATEGORÍAS = {
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Imágenes": [".jpg", ".jpeg", ".png", ".gif"],
    "Vídeos": [".mp4", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Comprimidos": [".zip", ".rar", ".7z"],
    "Otros": []
}

def organizar_archivos(directorio):
    if not os.path.exists(directorio):
        print(f"El directorio '{directorio}' no existe.")
        return

    for archivo in os.listdir(directorio):
        ruta_archivo = os.path.join(directorio, archivo)

        # Saltar carpetas
        if os.path.isdir(ruta_archivo):
            continue

        # Obtener la extensión del archivo
        _, extension = os.path.splitext(archivo)
        categoría = "Otros"
        for cat, extensiones in CATEGORÍAS.items():
            if extension.lower() in extensiones:
                categoría = cat
                break

        # Crear la carpeta de la categoría si no existe
        carpeta_categoría = os.path.join(directorio, categoría)
        os.makedirs(carpeta_categoría, exist_ok=True)

        # Mover el archivo a la carpeta correspondiente
        shutil.move(ruta_archivo, os.path.join(carpeta_categoría, archivo))

    print("¡Organización completada!")

if __name__ == "__main__":
    print("Organizador de Archivos Inteligente")
    ruta = input("Introduce la ruta de la carpeta que deseas organizar: ").strip()
    organizar_archivos(ruta)