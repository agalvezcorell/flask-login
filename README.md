# Flask-Login

He una API con Flask que incluya gestión de usuarios y subida de archivos. Solamente los usuarios administradores podrán borrar archivos.


## ¿Cómo crear la base de datos?

- Abra una ventana en la terminal y sitúese dentro de la carpeta flask-login.
- Inicie python
- Ejecute los siguientes comandos

`from project import db, create_app`
`db.create_all(app=create_app())`


## ¿Cómo iniciar la API?

Sitúese en el directorio flask-login con su terminal y exporte las siguientes variables de entorno:

```
export FLASK_APP=my_app
export FLASK_DEBUG=1
```

Yo estoy utilizando un entorno virtual de conda para este proyecto, puede utilizar un entorno virtual en python o simplemente guardar las variables para esta sesión de la terminal.

Después inicie el programa escribiendo el siguiente comando `flask run`

## ¿Cómo borrar archivos?

Para borrar archivos es necesario tanto estar logueado en la aplicación como ser administrador.
Es necesario gestionar la base de datos y poner el campo "admin" a 1 (True) del usuario deseado.

## Ruta para guardar los archivos

Para guardar los archivos en las rutas deseadas habrá que modificar el programa e indicarle la ruta, ahora mismo en modo "desarrollo" se guardan en la carpeta files.



