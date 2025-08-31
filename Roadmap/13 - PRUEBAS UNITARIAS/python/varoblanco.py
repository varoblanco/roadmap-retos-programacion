import unittest
from datetime import datetime

"""EJERCICIO"""

def sum(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Los arguentos han de ser numeros enteros o decimales")
    return a + b 


print(sum(2, 5))

class TestSum(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(sum(3, 5), 8)
        self.assertEqual(sum(6, 5), 11)
        
    def test_sum_type(self):
        with self.assertRaises(ValueError):
            sum("5", 4)
            sum("5", "abc")

"""EXTRA"""

class TestData(unittest.TestCase):
    
    def setUp(self) -> None:
        self.data = {
            "name": "Alvaro Blanco",
            "age": 33,
            "birth_date": datetime.strptime("23-10-1991", "%d-%m-%Y").date(),
            "programming_languages": ["python", "JS"]
            }
    
    def test_fields_exist(self):
        self.assertIn("name", self.data)
        self.assertIn("age", self.data)
        self.assertIn("birth_date", self.data)
        self.assertIn("programming_languages", self.data)
    
    def test_data_is_correct(self):
        self.assertIsInstance(self.data["name"], str)
        
unittest.main()
