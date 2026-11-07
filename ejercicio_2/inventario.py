import json


class StockInvalidoError(Exception):
    pass


class DispositivoEcologico:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, valor):
        if valor < 0:
            raise StockInvalidoError("El stock no puede ser negativo")
        self._stock = valor

    def ficha_tecnica(self):
        return (
            f"Codigo: {self.codigo} | Nombre: {self.nombre} | "
            f"Precio: ${self.precio} | Stock: {self.stock}"
        )

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
        }


class PanelSolar(DispositivoEcologico):
    def __init__(self, codigo, nombre, precio, stock, potencia_watts, eficiencia):
        super().__init__(codigo, nombre, precio, stock)
        self.potencia_watts = potencia_watts
        self.eficiencia = eficiencia

    def ficha_tecnica(self):
        ficha = super().ficha_tecnica()
        return ficha + f" | Potencia: {self.potencia_watts} | Eficiencia: {self.eficiencia}"

    def to_dict(self):
        datos = super().to_dict()
        datos["potencia_watts"] = self.potencia_watts
        datos["eficiencia"] = self.eficiencia
        return datos


class GestorInventario:
    @staticmethod
    def guardar_catalogo_json(lista_dispositivos, ruta_archivo="catalogo_ecotech.json"):
        datos = []
        for dispositivo in lista_dispositivos:
            datos.append(dispositivo.to_dict())

        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    try:
        panel_error = PanelSolar("PF-000", "Panel Solar", 150000, -5, 300, 18.5)
    except StockInvalidoError as error:
        print("Error controlado:", error)

    panel1 = PanelSolar("PF-001", "Panel Solar Residencial", 250000, 10, 450, 21.5)
    panel2 = PanelSolar("PF-002", "Panel Solar Industrial", 420000, 5, 600, 23.5)
    controlador = DispositivoEcologico("EE-001", "Controlador de Carga", 85000, 8)

    try:
        panel1.stock = -2
    except StockInvalidoError as error:
        print("Error controlado:", error)

    catalogo = [panel1, panel2, controlador]

    for dispositivo in catalogo:
        print(dispositivo.ficha_tecnica())

    GestorInventario.guardar_catalogo_json(catalogo)
    print("Catalogo guardado correctamente.")
