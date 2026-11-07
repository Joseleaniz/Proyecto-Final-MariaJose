def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    if consumo_kwh < 0:
        raise ValueError("El consumo no puede ser negativo")

    emisiones = consumo_kwh * factor_emision
    return emisiones


def obtener_metricas_consumo(registros):
    total_emisiones = 0.0
    planta_mayor = None
    mayor_consumo = -1
    plantas_procesadas = []

    for registro in registros:
        planta = registro["planta"]
        consumo = registro["consumo_kwh"]
        factor = registro.get("factor_emision", 0.4)

        emisiones = calcular_emisiones_carbono(consumo, factor)
        total_emisiones = total_emisiones + emisiones

        if consumo > mayor_consumo:
            mayor_consumo = consumo
            planta_mayor = planta

        datos_planta = {
            "planta": planta,
            "consumo_kwh": consumo,
            "emisiones": round(emisiones, 2),
        }
        plantas_procesadas.append(datos_planta)

    return {
        "total_emisiones": round(total_emisiones, 2),
        "planta_mayor_consumo": planta_mayor,
        "registros": plantas_procesadas,
    }
