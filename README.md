# movies_app
Welcome to Movies Project, a very basic Django website developed by Borja Diago

Requisitos Generales:

Se desea poder listar un conjunto de películas en una pagina web almacenadas en una base de datos y que cuando se seleccione una, se pueda ver el detalle. Las películas tienen titulo,actores, director rating y sinopsis. 


Requisitos Funcionales:

Framework a implementar DJANGO:

-La version de Django escogida ha sido la 2.1.7


La implementación debe implementar un ORM:

-El ORM escogido ha sido el que viene por defecto en Django, capaz de gestionar bases de datos como MySql, PostgreSQL, SQLite..


Esta prohibido que un Entity(objeto que representa un registro de base de datos) sea devuelto a la vista:

-Para abordar esta problematica he optado por crear una capa 'services' que es la encargada de realizar las llamadas a la base de datos con metodos estaticos, para que solo la clase MovieServices tenga acceso a la base de datos.


Debe separarse el código en tres capas, acceso a datos, capa de negocio y vista/controller:

-Las capas han sido:

--Capa 'models' -----> Encargada de la creación de los modelos y de su relación con la bbdd.

--Capa 'services' -----> Encargada de la gestión entre los modelos/bbdd y la capa de negocio(views).

--Capa 'views' -----> Encargada de la lógica de negocio.

--Capa 'templates' -----> Encargada de las vistas finales.


La lógica de negocio no puede estar en views.py:

-Esta problematica se resuelve con la capa 'views'.


Las vistas( clases de tipo view) a implementar deben estar separadas( deben residir en su propio paquete/fichero.py) y no deben estar dentro de views.py

-Cada vista se aloja en su propio fichero .py, en este caso solo están en movie_view.py, ya que la funcionalidad de los objetos Director y Character aun no ha sido implementada.


Los Entities ( modelos de base de datos) deben estar en un paquete/fichero.py diferente a models.py:

-Se han creado tres Entities(Movie, Director, Character) con relacion de ManyToMany sobre Movie---Director y sobre Movie---Character, NO siendo dependientes entre sí. Cada una en su fichero 'nombre_entity.py'

Base de datos a elegir:

-La base de datos escogida ha sido SQLite, ya que debido a la poca carga de datos que por ahora va a tener el proyecto, he preferido utilizar una base de datos que pese poco y tenga un acceso rápido.


Requisitos no funcionales:

En el listado solo sera visible el titulo y el rating. -----> Se presenta de esta forma.

Diseño de paginas listado/detalle libre, no hace falta que sean vistosas:

-Debido a la falta de tiempo el diseño web ha sido el punto en el que menos incapie he hecho. Como por ejemplo implementar la paginacion.
