import os
import shutil

folder = os.getcwd()

extension_map = {
    '.txt': 'Textes',
    '.csv': 'Données',
    '.xlsx': 'Données',
    '.json': 'Données',
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.gif': 'Images',
    '.bmp': 'Images',
    '.pdf': 'Documents',
    '.doc': 'Documents',
    '.docx': 'Documents',
}

for subfolder in set(extension_map.values()):
    os.makedirs(os.path.join(folder, subfolder), exist_ok=True)

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    if os.path.isfile(filepath):
        ext = os.path.splitext(filename)[1].lower()
        if ext in extension_map:
            dest_folder = os.path.join(folder, extension_map[ext])
            shutil.move(filepath, os.path.join(dest_folder, filename))