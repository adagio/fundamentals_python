class Playlist:
    # Base class __init__ should accept **kwargs to absorb extras in MRO chain
    def __init__(self, nombre, fecha_creacion=None, etiquetas=None, **kwargs):
        # Important: Call super() for cooperative multiple inheritance
        super().__init__(**kwargs)
        self.nombre = nombre
        self.canciones = []
        self.fecha_creacion = fecha_creacion or "Desconocida"
        self.etiquetas = etiquetas or []
        print(f"Playlist.__init__ llamado para {self.nombre}, fecha: {self.fecha_creacion}, etiquetas: {self.etiquetas}")
        print(f"Playlist.__init__ called for {self.nombre}") # Debug print

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)
        return f"'{cancion}' añadida a '{self.nombre}'"

    def reproducir(self):
        if self.canciones:
            return f"Reproduciendo '{self.nombre}': {', '.join(self.canciones)}"
        return f"'{self.nombre}' está vacía"

    def eliminar_cancion(self, cancion):
        if cancion in self.canciones:
            self.canciones.remove(cancion)
            return f"'{cancion}' eliminada de '{self.nombre}'"
        return f"'{cancion}' no está en '{self.nombre}'"

class PlaylistInteligente(Playlist):
    # Needs to accept **kwargs and pass them up
    def __init__(self, nombre, criterio, **kwargs):
        # Call super() *before* accessing self attributes if possible, pass kwargs
        super().__init__(nombre=nombre, **kwargs)
        self.criterio = criterio
        print(f"PlaylistInteligente.__init__ called for {self.nombre}, criterio {self.criterio}") # Debug print


    # This version works fine for single inheritance or as part of MRO
    # if the final call handles args correctly
    def agregar_cancion(self, cancion, **kwargs): # Accept kwargs to handle potential 'usuario'
        if self.criterio.lower() in cancion.lower():
            # Pass all args/kwargs up the chain
            return super().agregar_cancion(cancion, **kwargs)
        return f"'{cancion}' no cumple el criterio '{self.criterio}'"

    def filtrar(self):
        return f"Filtrando '{self.nombre}' por criterio: {self.criterio}"

class PlaylistColaborativa(Playlist):
    # Needs to accept **kwargs and pass them up
    def __init__(self, nombre, usuarios, **kwargs):
        # Call super() *before* accessing self attributes if possible, pass kwargs
        super().__init__(nombre=nombre, **kwargs)
        self.usuarios = usuarios
        print(f"PlaylistColaborativa.__init__ called for {self.nombre}, usuarios {self.usuarios}") # Debug print

    # Needs to accept 'usuario' and potentially other kwargs
    def agregar_cancion(self, cancion, usuario, **kwargs):
        if usuario in self.usuarios:
            # Pass relevant args/kwargs up the chain
            # Note: Base Playlist.agregar_cancion doesn't take 'usuario'
            # This override structure assumes super() eventually leads to something
            # that *either* uses 'usuario' or ignores it via **kwargs.
            # In our specific MRO for the hybrid class, this method won't be
            # called directly via super() from the hybrid's agregar_cancion.
            # But for cooperative inheritance, it *should* call super().
            # The hybrid class will handle the logic differently.
            return super().agregar_cancion(cancion, **kwargs)
        return f"'{usuario}' no tiene permiso para editar '{self.nombre}'"

    def listar_usuarios(self):
        return f"Usuarios de '{self.nombre}': {', '.join(self.usuarios)}"

class PlaylistInteligenteColaborativa(PlaylistInteligente, PlaylistColaborativa):
    # __init__ needs to correctly pass arguments up the MRO chain
    def __init__(self, nombre, criterio, usuarios, **kwargs):
        # Call super() passing all relevant args for the MRO chain
        # PlaylistInteligente needs 'nombre' and 'criterio'
        # PlaylistColaborativa needs 'nombre' and 'usuarios'
        # Playlist needs 'nombre'
        # The super() chain handles calling each __init__ once appropriately.
        super().__init__(nombre=nombre, criterio=criterio, usuarios=usuarios, **kwargs)
        print(f"PlaylistInteligenteColaborativa.__init__ called for {self.nombre}") # Debug print


    # Override agregar_cancion to combine logic explicitly
    def agregar_cancion(self, cancion, usuario):
        # 1. Check permission (from PlaylistColaborativa logic)
        if usuario not in self.usuarios:
            return f"'{usuario}' no tiene permiso para editar '{self.nombre}'"

        # 2. Check criterion (from PlaylistInteligente logic)
        if self.criterio.lower() not in cancion.lower():
            return f"'{cancion}' no cumple el criterio '{self.criterio}'"

        # 3. If both checks pass, call the *base* class method directly
        #    to avoid issues with intermediate methods' signatures/checks.
        return Playlist.agregar_cancion(self, cancion)

# Pruebas (Debug prints added to see __init__ calls)
print("--- MRO ---")
print(PlaylistInteligenteColaborativa.__mro__)
print("\n")


print("=== Playlist Básica ===")
basic_playlist = Playlist(nombre="Mi Lista")
print(basic_playlist.agregar_cancion("Bohemian Rhapsody"))
print(basic_playlist.reproducir())

print("\n=== Playlist Inteligente ===")
smart_playlist = PlaylistInteligente(nombre="Rock Hits", criterio="rock")
print(smart_playlist.agregar_cancion("Rock You Like a Hurricane"))
print(smart_playlist.agregar_cancion("Sweet Caroline"))  # No cumple criterio
print(smart_playlist.reproducir())
print(smart_playlist.filtrar()) # Added test for filtrar

print("\n=== Playlist Colaborativa ===")
collab_playlist = PlaylistColaborativa(nombre="Equipo Party", usuarios=["Alice", "Bob"])
print(collab_playlist.agregar_cancion("Happy Birthday", "Alice"))
print(collab_playlist.agregar_cancion("Sweet Home Alabama", "Charlie"))  # Sin permiso
print(collab_playlist.reproducir())
print(collab_playlist.listar_usuarios()) # Added test for listar_usuarios

print("\n=== Playlist Inteligente y Colaborativa ===")
# Ensure all args are passed correctly
hybrid_playlist = PlaylistInteligenteColaborativa(nombre="Rock en Equipo", criterio="rock", usuarios=["Alice", "Bob"])
print(hybrid_playlist.agregar_cancion("Rock You Like a Hurricane", "Alice"))
print(hybrid_playlist.agregar_cancion("Pop Song", "Bob"))  # No cumple criterio
print(hybrid_playlist.agregar_cancion("Sweet Child O' Mine", "Charlie"))  # Sin permiso
print(hybrid_playlist.agregar_cancion("Stairway to Heaven", "Bob")) # Should work
print(hybrid_playlist.reproducir())
print(hybrid_playlist.filtrar()) # Should work (inherited from PlaylistInteligente)
print(hybrid_playlist.listar_usuarios()) # Should work (inherited from PlaylistColaborativa)

# Ejemplo de uso que aprovecha los kwargs
print("\n=== Playlist Inteligente y Colaborativa con parámetros adicionales ===")
hybrid_playlist = PlaylistInteligenteColaborativa(
    nombre="Rock de los 80s",
    criterio="rock",
    usuarios=["Alice", "Bob"],
    fecha_creacion="2025-04-03",  # Parámetro adicional que llegará hasta Playlist
    etiquetas=["80s", "clásicos", "guitarras"]  # Otro parámetro adicional
)

# Verificar que los parámetros adicionales se hayan propagado correctamente
print(f"\nVerificando parámetros adicionales:")
print(f"Fecha de creación: {hybrid_playlist.fecha_creacion}")
print(f"Etiquetas: {hybrid_playlist.etiquetas}")

print("\nAgregando canciones:")
print(hybrid_playlist.agregar_cancion("Sweet Child O' Mine", "Alice"))
print(hybrid_playlist.agregar_cancion("Highway to Hell", "Bob"))
print(hybrid_playlist.reproducir())

# Definir una función que muestra la información completa de una playlist
def mostrar_info_completa(playlist):
    info = [
        f"Nombre: {playlist.nombre}",
        f"Fecha de creación: {playlist.fecha_creacion}",
        f"Etiquetas: {', '.join(playlist.etiquetas)}",
    ]
    
    if hasattr(playlist, 'criterio'):
        info.append(f"Criterio: {playlist.criterio}")
    
    if hasattr(playlist, 'usuarios'):
        info.append(f"Colaboradores: {', '.join(playlist.usuarios)}")
        
    info.append(f"Canciones: {', '.join(playlist.canciones) if playlist.canciones else 'Ninguna'}")
    
    return "\n".join(info)

print("\nInformación completa de la playlist:")
print(mostrar_info_completa(hybrid_playlist))