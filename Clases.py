# En este fichero se especificarán las distintas clases.

# CPUEvent: Clase genérica para procesar los correos.
# De ella que heredarán las que son específicas de cada tipo de correo
# con la lógica adecuada en cada caso
from pyasn1.type import char


class CPUEvent:

    def textoEvento(mail, tag, hasta):
        indiceTag = 0
        #print(tag)
        #print(hasta)
        #print(mail)
        fin = 0
        cadena = ""
        indiceTag = str.find(mail, tag, indiceTag)
        fin = str.find(mail, hasta, fin)
        cadenaCh = ['']
        for i in mail:
            cadenaCh.append(i)
        print(str(mail)[indiceTag:fin])
        if indiceTag != -1 & fin != -1:
            cadena = mail[indiceTag:fin]
        #print(cadena)
        return cadena
    #print("Aqui: " + textoEvento("Sistema: Legados coliving y su madre a caballo \n Lunes al sol", "Sistema: ","\n"))


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
        aux=""
        length = len(old)
        while str.find(cadena, old) != -1:
            index = str.find(cadena, old)
            aux = cadena[0:index] + new + cadena[index + length:]
            cadena = aux
        print("Old: " + old)
        print("New: " + new)
        #print(cadena)
        return cadena

    def sinEtiquetasNew(mail):
        c = 'a'
        beerre = ""
        salto = False
        aux = ""
        cadena = ""
        tag = False
        for i in mail:
            c = i
            if ord(i) > 31 or ord(i) == 13 or ord(i) == 10:
                if c == '<':
                    tag = True
                if tag:
                    if (beerre == "" and c == 'b') or (beerre == "b" and c == 'r'):
                        aux = beerre + c
                        beerre = aux
                    elif c == '>':
                        tag = False
                else:
                    aux = cadena + c
                    cadena = aux
        return cadena


    def sinEtiquetas(mail):
        import re
        Correo.replace_all("<br>", "\r", mail)
        cadena=['']
        etiquetas = re.findall("<.*>", mail)
        for eti in etiquetas:
            print(eti)
        for cad in etiquetas:
            cadena.append(Correo.replace_all(cad, "", mail))
        #for cad in cadenas:
        #  Correo.remove_all(cad, mail)
        resultado=str(cadena)
        print("Cadena: " + resultado)
        return resultado