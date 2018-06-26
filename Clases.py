# En este fichero se especificarán las distintas clases.

# CPUEvent: Clase genérica para procesar los correos.
# De ella que heredarán las que son específicas de cada tipo de correo
# con la lógica adecuada en cada caso
from pyasn1.type import char


class CPUEvent:

    def textoEvento(mail, tag, hasta):
        indiceTag = 0
        fin = 0
        cadena = ""
        indiceTag = str.find(mail, tag, indiceTag)
        fin = str.find(mail, hasta, fin)
        if indiceTag != -1 & fin != -1:
            cadena = mail[indiceTag:fin]
        print(cadena)
        return cadena
    print("Aqui: " + textoEvento("Sistema: Legados coliving y su madre a caballo \n Lunes al sol", "Sistema: ","\n"))


class Correo:

    def remove_all(subcad, cadena):
        index = 0
        length = len(subcad)
        while str.find(cadena, subcad) != -1:
            index = str.find(cadena, subcad)
            cadena = cadena[0:index] + cadena[index + length:]
        return cadena

    def replace_all(old, new, cadena):
        index = 0
        length = len(old)
        while str.find(cadena, old) != -1:
            index = str.find(cadena, old)
            cadena = cadena[0:index] + new + cadena[index + length:]
        return cadena

    def sinEtiquetas(mail):
        import re
        Correo.replace_all("<br>", "\r", mail)
        cadenas = re.findall("<.*>",mail)
        for cad in cadenas:
          Correo.remove_all(cad, mail)
        return mail