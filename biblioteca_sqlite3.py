
# Base de datos ligera basada en disco
import sqlite3


class Autor:
    def __init__(self, nombre, apellidos):
        self.Nombre = nombre
        self.Apellidos = apellidos

    def MostrarAutor(self):
        print(f"Autor: {self.Nombre}, {self.Apellidos}")


class Libro:
    def __init__(self, titulo, isbn):
        self.Titulo = titulo
        self.Isbn = isbn

    def AñadirAutor(self, autor):
        self.Autor = autor

    def MostrarLibro(self):
        """Mostrará cada libro al final de cada iteración del método
          MostrarBiblioteca() del clase Bibliotec()"""
        print("------Libro------")
        print(f"Título: {self.Titulo}\nISBN: {self.Isbn}")
        self.Autor.MostrarAutor()
        print("-----------------")

    def ObtenerTitulo(self):
        """Sin funcionalidad en este programa"""
        return self.Titulo


class Biblioteca:
    def __init__(self):
        """Conexión a la base de datos, creación y commit de la tabla libros"""
        try:
            # Se crea la conexión a la base de datos. El archivo se guarda en el directorio raíz python
            self.conn = sqlite3.connect('biblioteca.db')
            # Permito ejecutar comandos SQL en la conexión a la base de datos
            self.c = self.conn.cursor()
            # Consulta SQL
            self.c.execute('''CREATE TABLE IF NOT EXISTS libros
                            (titulo TEXT, isbn CHAR(13), autor_nombre TEXT, autor_apellidos TEXT)''')
            # Guardo los cambios en la base de datos
            self.conn.commit()
        except sqlite3.Error as e:
            print("Error al conectarse a la base de datos", e)

    def AñadirLibros(self, libro):
        # inserto los valores de los atributos de la clase Libro() y del constructor de la clase Autor()
        self.c.execute("INSERT INTO libros VALUES (?, ?, ?, ?)",
                       (libro.Titulo, libro.Isbn, libro.Autor.Nombre, libro.Autor.Apellidos))
        # Guardo los cambios
        self.conn.commit()

    def MostrarBiblioteca(self):
        # Selecciono todas las columnas de la tabla libros
        self.c.execute("SELECT * FROM libros")
        # Almaceno en una variablo todos los registros de la consulta anterior. Devuelve una lista de todas las filas de los resultados
        libros = self.c.fetchall()
        print("##############################")
        # Se itera sobre cada libro y se extraen los valores.
        # El método 'commit()' no es necesario, porque la consulta es solo de lectura
        for libro in libros:
            titulo, isnb, autor_nombre, autor_apellidos = libro
            autor = Autor(autor_nombre, autor_apellidos)
            libro = Libro(titulo, isnb)
            libro.AñadirAutor(autor)
            libro.MostrarLibro()
        print("##############################")

    def BorrarLibro(self, titulo):
        self.c.execute("DELETE FROM libros WHERE titulo=?", (titulo,))
        self.conn.commit()
        # Compruebo el número de filas afectadas en la opración anterior
        if self.c.rowcount == 0:
            print("El libro no se encuentra en la biblioteca")
        else:
            print("Libro borrado correctamente")

    def NumeroLibros(self):
        # Cuento el número de filas en la tabla libros, y 'self.c' obtiene el resultado
        # de la consulta
        self.c.execute("SELECT COUNT(*) FROM libros")
        # Recupero el resultado accediendo al índice [0] de la tupla,
        # que contiene un solo valor(COUNT)
        num_libros = self.c.fetchone()[0]  # Recuento de filas
        return num_libros


def MostrarMenu():
    print("1. Añadir Libro a la biblioteca.\n"
          "2. Mostrar la biblioteca.\n"
          "3. Borrar libro de la biblioteca.\n"
          "4. Mostrar el número de libros que componen la biblioteca.\n"
          "5. Salir")


def AñadirLibroBiblioteca(biblioteca):
    titulo = input("Introduce el título del libro: ")
    isbn = input("Introduce el ISBN del libro: ")
    if len(isbn) > 13:
        print("El ISBN no puede contener más de 13 caracteres")

    else:
        autornombre = input("Introduce el nombre del autor: ")
        autorapellidos = input("Introduce los apellidos del autor: ")
        # Creo dos objetos
        autor = Autor(autornombre, autorapellidos)
        libro = Libro(titulo, isbn)
        libro.AñadirAutor(autor)
        biblioteca.AñadirLibros(libro)
        return biblioteca


def MostrarBiblioteca(biblioteca):
    biblioteca.MostrarBiblioteca()


def BorrarLibro(biblioteca):
    titulo = input("Introduce el título del libro a borrar: ")
    biblioteca.BorrarLibro(titulo)


def NumeroLibros(biblioteca):
    print("El número de libros en la biblioteca es: ", biblioteca.NumeroLibros())


fin = False
# objeto de la clase Biblioteca()
biblioteca = Biblioteca()

# Bucle para las opciones del menú MostrarMenu()
while not fin:
    MostrarMenu()
    opcion = int(input("Seleccione opción: "))
    if opcion == 1:
        biblioteca = AñadirLibroBiblioteca(biblioteca)
    elif opcion == 2:
        MostrarBiblioteca(biblioteca)
    elif opcion == 3:
        BorrarLibro(biblioteca)
    elif opcion == 4:
        NumeroLibros(biblioteca)
    elif opcion == 5:
        fin = True

print('¡Hasta Luego!')
