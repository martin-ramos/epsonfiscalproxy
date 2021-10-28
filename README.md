# EpsonFiscalApp
#### Libreria hecha en Python para impresión fiscal utilizando EpsonInterface

### Manual de impresora fiscal

https://github.com/martin-ramos/epsonfiscalproxy/blob/main/ManualImpresoraFiscalEpsonDesarrollador.pdf

### Manual de EpsonFiscalInterface

https://github.com/martin-ramos/epsonfiscalproxy/blob/main/EpsonFiscalInterfaceSpec.pdf

## Comandos
Run:

    python3 app.py

## Trabajar con entorno virtual
- pip3 install virtualenv
- source /venv/Scripts/activate

### - Luego se instalan las dependencias utilizadas

- pip3 install  -r requirements.txt 

### Compilar y utilizarlo en modo exe 
#### Se genera un .exe con pyintaller

    ### Instalación pyinstaller
       https://www.pyinstaller.org/

        - pip3 install pyinstaller
    
    ### Uso de pyinstaller
        Comando :

            Se utilizó python 3.9.7 para compilar

            pyinstaller --onefile .\app.py


