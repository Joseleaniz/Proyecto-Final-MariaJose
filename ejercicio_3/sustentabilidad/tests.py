import unittest
from .services import calcular_emisiones_carbono, obtener_metricas_consumo


class TestCalculoEmisiones(unittest.TestCase):

    def test_calculo_valor_nominal(self):
        resultado = calcular_emisiones_carbono(100)
        self.assertEqual(resultado, 40.0)

    def test_calculo_factor_personalizado(self):
        resultado = calcular_emisiones_carbono(200, 0.5)
        self.assertEqual(resultado, 100.0)

    def test_consumo_cero(self):
        resultado = calcular_emisiones_carbono(0)
        self.assertEqual(resultado, 0.0)

    def test_consumo_negativo_lanza_error(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-10)


class TestMetricasConsumo(unittest.TestCase):

    def test_obtener_metricas(self):
        datos = [
            {"planta": "Planta 1", "consumo_kwh": 100, "factor_emision": 0.4},
            {"planta": "Planta 2", "consumo_kwh": 300, "factor_emision": 0.4},
        ]
        metricas = obtener_metricas_consumo(datos)

        self.assertEqual(metricas["total_emisiones"], 160.0)
        self.assertEqual(metricas["planta_mayor_consumo"], "Planta 2")


if __name__ == "__main__":
    unittest.main()
