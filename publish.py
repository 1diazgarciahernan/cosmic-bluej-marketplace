#!/usr/bin/env python3
"""Genera plugins.json cuando DISPONGAS de un plugin Android compilado válido."""
from pathlib import Path
import hashlib,json,sys,zipfile
if len(sys.argv) != 3:
    sys.exit('Uso: python3 publish.py USUARIO_GITHUB artifacts/bluej-support-1.0.0.zip')
username, filename = sys.argv[1:]
path = Path(filename)
if not path.is_file(): sys.exit('No existe el archivo de plugin compilado')
with zipfile.ZipFile(path) as z:
    names=set(z.namelist())
    if 'manifest.json' not in names: sys.exit('El ZIP no contiene manifest.json en la raíz')
    manifest=json.loads(z.read('manifest.json'))
    if not all(artifact in names for artifact in manifest.get('classPath', [])):
        sys.exit('Faltan los binarios APK/JAR declarados en classPath')
    if not manifest.get('classPath'): sys.exit('classPath está vacío')
    if manifest.get('id') != 'com.bluejsupport': sys.exit('ID del plugin inesperado')
    version=manifest['version']
    if not path.resolve().is_relative_to((Path.cwd()/'artifacts').resolve()):
        sys.exit('El ZIP debe guardarse bajo artifacts/')
    if path.stat().st_size > 25*1024*1024: sys.exit('El ZIP supera 25 MB')
index=[{
  'id':'com.bluejsupport','name':'BlueJ Support','version':version,
  'author':username,
  'description':'Compile and run standard Java projects without Gradle.',
  'detailedDescription':'Compile and run ordinary Java classes using javac and java. Requires a working JDK.',
  'downloadUrl':f'https://raw.githubusercontent.com/{username}/{Path.cwd().name}/main/{path.as_posix()}',
  'sha256':hashlib.sha256(path.read_bytes()).hexdigest()
}]
Path('plugins.json').write_text(json.dumps(index,indent=2,ensure_ascii=False)+'\n')
print('plugins.json generado. Comprueba que el binario realmente carga y registra acciones antes de publicarlo.')
