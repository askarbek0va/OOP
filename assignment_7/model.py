

class CalculatorModel:

    def __init__(self):
        self.expression=""

    def add_to_expression(self,char:str):
        self.expression=self.expression +char

    def remove_last_character(self):
        self.expression=self.expression[:-1]

    def clear_expression(self):
        self.expression=""


    def calculate(self):
        try:
            expression = self.expression.replace("%", "/100")
            print(f"Evaluating: {expression}")
            result = eval(expression)
            return str(result)
        except ZeroDivisionError:
            return "Error"
        except Exception as e:
            print(f"Error: {e}")
            return "Error"

    def get_expression(self):
        return self.expression

    def __str__(self):
        return self.expression