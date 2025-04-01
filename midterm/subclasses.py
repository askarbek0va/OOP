from superclass import ElectricityPlan


class PopulationPlan(ElectricityPlan):
    def __init__(self, total_kwh: int):
        super().__init__('Population', total_kwh)

    def calculate_cost(self):
        kwh = self.get_total_kwh()
        if kwh <= 700:
            return kwh == kwh * 1.00
        else:
            return (700 * 1.00) + ((kwh - 700) * 2.16)


class HighlandsPlan(ElectricityPlan):
    def __init__(self, total_kwh: int):
        super().__init__('Highlands', total_kwh)

    def calculate_cost(self):
        return self.get_total_kwh() * 1.50


class CommercialPlan(ElectricityPlan):
    def __init__(self, total_kwh: int):
        super().__init__('Commercial', total_kwh)

    def calculate_cost(self):
        return self.get_total_kwh() * 2.87

