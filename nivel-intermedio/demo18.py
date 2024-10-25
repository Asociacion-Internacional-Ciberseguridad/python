import zipfile

with zipfile.ZipFile('archivo.zip', 'w') as zipf:
    zipf.write('archivo.txt')
