# Ejemplo de los usos de parametros arbitrarios

def crearPersonaje(nombre, *args, **kwargs):
    descripcion = f"#### {nombre.upper()} #### \n\n"
    descripcion += "#### DESCRIPCION #### \n\n"
    for clave, valor in kwargs.items():
        descripcion += f"----- {clave} ----- {valor} -----\n"
    descripcion += "\n#### HABILIDADES #### \n\n"
    for datos in args:
        descripcion += f"----- {datos} \n"
    return descripcion

personaje = crearPersonaje ("Seiya", "Meteoritos de pegazo", "Destellos dorados", caballero = "Dorado", signo = "Sagiatario")
print (personaje)


