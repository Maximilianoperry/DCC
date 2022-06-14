def revisar_fecha(fecha):
    if "/" not in fecha:
        return False
    else:
        fecha = fecha.split("/")
        if len(fecha) == 3:
            if (len(fecha[0]) == 2 and str(fecha[0]).isdigit()) and (len(fecha[1]) == 2 and str(fecha[1]).isdigit()) and (len(fecha[2]) == 4 and str(fecha[2]).isdigit()):
                if 1 <= int(fecha[1]) <= 12:
                    if 1 <= int(fecha[0]) <= 31:  # Se supone que todos los meses tienen 31 días
                        if int(fecha[2]) <= 2021:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
