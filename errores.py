def escribir_errores(excepcion, texto):
    with open ('error.log', 'a+') as archivo_error:

        archivo_error.write('----------------------------------------------------------------------------\n')

        archivo_error.write(str(excepcion))
        archivo_error.write(texto)

        archivo_error.write('----------------------------------------------------------------------------\n')