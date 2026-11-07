from django.shortcuts import render
from .services import obtener_metricas_consumo


def vista_panel_sustentabilidad(request):
    historial = [
        {"planta": "Planta Norte", "consumo_kwh": 12500, "factor_emision": 0.4},
        {"planta": "Planta Sur", "consumo_kwh": 18200, "factor_emision": 0.45},
        {"planta": "Planta Este", "consumo_kwh": 9400, "factor_emision": 0.4},
        {"planta": "Planta Oeste", "consumo_kwh": 15100, "factor_emision": 0.38},
    ]

    contexto = obtener_metricas_consumo(historial)
    return render(request, "sustentabilidad/panel.html", contexto)
