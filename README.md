<h1>Spotmusic APP en proceso</h1>

<h4> Spotmusic, será un reproductor de música que te permitirá agregar y escuchar canciones 
desde cualquier parte del mundo.</h4>


<h2> Caracteristicas </h2>

<h4> Te permitirá:
<ol>
<li>Agregar musica nueva </li>
<li>Agregar albumes nuevos </li>
<li>Conocer nueva musica y artistas </li>
<li>Buscar a tus canciones y artistas favoritos </li>
</ol>
</h4>

<h2> Herramientas </h2>

<h4> Antes de crear esta app, necesitas instalar ciertas herramientas en tu IDE </h4>

<h2> Instalar tu entorno virtual </h3>

<h4> 
<ol>
<li>Creamos un entorno virtual con "py -m venv <nombre entorno virtual>"</li>
<li>Activar el entorno virtual con ". <nombre entorno virtual>/Scripts/activate"
( En caso de usar linux o mac reemplazar el 'Scripts' por 'bin )</li>
</ol>
</h4>

<h2> Instalar Django </h3>

<h4> 
<ol>
<li>En la terminal de tu IDE, escribir - pip install Django</li>
<li>Luego, para chequear si DJANGO estaba instalado creamos un requirements.txt ejecutando 
con el entorno virtual activo el siguiente codigo: "pip freeze > requirements.txt" </li>
</ol>
</h4>

<h2>Crear proyecto</h2>

<h4>
<ol>
<li> En la terminal, colocamos -django-admin startproject <nombre del proyecto </li>
</ol>
</h4>

<h2>Generar la base de datos / MIGRATE</h2>

<h4> Las migraciones son la forma en que Django propaga los cambios que realiza en sus modelos 
(agregar un campo, eliminar un modelo, etc.) en el esquema de su base de datos:

python manage.py makemigrations
python manage.py migrate 
python manage.py runserver

</h4>

<h2>Correr el codigo </h2>

<h4> Ir a la terminal de tu IDE, y escribir 
}
python manage.py runserver. 

"Spotmusic" app va a empezar 127.0.0.1:8000
</h4>
