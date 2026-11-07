def limpiar_registro_sensor(registro_raw):
    sensor_id = registro_raw["sensor_id"].strip()

    temperatura = str(registro_raw["temperatura"])
    temperatura = temperatura.replace("°", "")
    temperatura = temperatura.replace("C", "")
    temperatura = temperatura.strip()
    temperatura = float(temperatura)

    ubicacion = registro_raw.get("ubicacion")
    if ubicacion is None:
        ubicacion = ""

    ubicacion = str(ubicacion).strip()
    if ubicacion == "":
        ubicacion = "Ubicación desconocida"

    return {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion,
    }

def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    sensores_alerta = []
    suma_temperaturas = 0.0

    for sensor in lista_sensores_limpios:
        suma_temperaturas = suma_temperaturas + sensor["temperatura"]
        if sensor["temperatura"] > umbral_temperatura:
            sensores_alerta.append(sensor["sensor_id"])

    promedio = 0.0
    if len(lista_sensores_limpios) > 0:
        promedio = suma_temperaturas / len(lista_sensores_limpios)
        promedio = round(promedio, 2)

    return sensores_alerta, promedio

registros_crudos = [
    {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
    {"sensor_id": " SENSOR-002", "temperatura": "31.2°C", "ubicacion": "Planta Sur "},
    {"sensor_id": "SENSOR-003  ", "temperatura": " 18.0 C"},
    {"sensor_id": " SENSOR-004 ", "temperatura": "35.8C", "ubicacion": ""},
    {"sensor_id": "SENSOR-005", "temperatura": "28.4 C", "ubicacion": "Planta Este"},
    {"sensor_id": "  SENSOR-006  ", "temperatura": "29.9°C", "ubicacion": "  Planta Oeste  "},
]

registros_limpios = []
for registro in registros_crudos:
    registro_limpio = limpiar_registro_sensor(registro)
    registros_limpios.append(registro_limpio)

for registro in registros_limpios:
    print("sensor:", registro["sensor_id"], "- temperatura:", registro["temperatura"], "- ubicación:", registro["ubicacion"])

umbral = 30.0
alertas, promedio = generar_resumen_sensores(registros_limpios, umbral)

print("Umbral establecido:", umbral)
print("Promedio global:", promedio, "°C")
print("Dispositivos en alerta (superan el umbral):", alertas)