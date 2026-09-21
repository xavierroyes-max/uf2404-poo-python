# Guía Git y GitHub

Esta guía parte del proyecto ubicado en:

```text
C:\curso_python\curso_python_interactivo
```

## 1. Comprobar Git

En PowerShell:

```powershell
git --version
```

## 2. Configurar identidad

Para este proyecto:

```powershell
git config --global user.name "Xavier Royes"
git config --global user.email "xavierroyes@gmail.com"
```

Comprobar:

```powershell
git config --global --list
```

## 3. Entrar en el proyecto

```powershell
cd C:\curso_python\curso_python_interactivo
```

## 4. Inicializar Git

```powershell
git init
```

## 5. Comprobar qué se va a subir

```powershell
git status
```

El archivo `.gitignore` excluye, entre otros:

- `__pycache__/`;
- `*.pyc`;
- `*.bak`;
- entornos virtuales;
- archivos temporales del sistema y del editor.

## 6. Añadir archivos

```powershell
git add .
```

Volver a comprobar:

```powershell
git status
```

## 7. Primer commit

```powershell
git commit -m "Entrega UF2404: ejercicios POO y laboratorio interactivo"
```

## 8. Rama principal

```powershell
git branch -M main
```

## 9. Crear el repositorio en GitHub

Nombre sugerido:

```text
uf2404-poo-python-laboratorio
```

Al crear el repositorio remoto, si el proyecto local ya contiene README y `.gitignore`, es preferible crear el remoto **vacío** para evitar un commit inicial diferente.

## 10. Conectar el remoto

Copiar la URL HTTPS que proporciona GitHub y ejecutar:

```powershell
git remote add origin https://github.com/USUARIO/uf2404-poo-python-laboratorio.git
```

`USUARIO` debe sustituirse por el nombre real de la cuenta GitHub.

Comprobar:

```powershell
git remote -v
```

## 11. Subir el proyecto

```powershell
git push -u origin main
```

En Windows, Git Credential Manager puede abrir el navegador para autorizar la cuenta.

## 12. Trabajo posterior

Después de modificar archivos:

```powershell
git status
git add .
git commit -m "Descripción del cambio"
git push
```

## 13. Historial

```powershell
git log --oneline --decorate --graph
```

## 14. Comandos de comprobación antes de entregar

```powershell
git status
python ejercicios\ejercicio_01_reparar_diseno.py
python ejercicios\ejercicio_08_mro_super.py
python ejercicios\ejercicio_10_sistema_extensible_pedidos.py
```

Y comprobar también el laboratorio:

```powershell
python server.py
```

## 15. Qué no debe subirse

No deben aparecer en Git:

```text
__pycache__/
*.pyc
*.bak
.venv/
venv/
```

Si accidentalmente ya se añadieron antes de crear `.gitignore`:

```powershell
git rm -r --cached __pycache__
git rm --cached *.bak
```

Después:

```powershell
git add .
git commit -m "Limpia archivos temporales"
```
