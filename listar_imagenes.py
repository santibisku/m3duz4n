import os

# Ruta de la carpeta de dibujos
folder_path = r"C:\Users\bisku\Desktop\m3duz4n\images\dibujos"

# Obtener la lista de archivos en la carpeta
files = os.listdir(folder_path)

# Filtrar solo los archivos de imagen
image_files = [f for f in files if f.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

# Generar el código HTML para cada imagen
for image in image_files:
    print(f'<img src="/images/dibujos/{image}" alt="{image}">')