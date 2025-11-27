import unittest
import rectangle

class TestRectangleFunctions(unittest.TestCase):
    '''
    Тестовые случаи для геометрических функций прямоугольника
    '''
    
    def test_area_integers(self):
        '''
        Тест вычисления площади с целыми числами
        '''
        self.assertEqual(rectangle.area(5, 3), 15)
        self.assertEqual(rectangle.area(10, 10), 100)
        self.assertEqual(rectangle.area(1, 1), 1)
    
    def test_area_floats(self):
        '''
        Тест вычисления площади с дробными числами
        '''
        self.assertAlmostEqual(rectangle.area(2.5, 4.0), 10.0)
        self.assertAlmostEqual(rectangle.area(3.14, 2.0), 6.28)
        self.assertAlmostEqual(rectangle.area(0.5, 0.5), 0.25)
    
    def test_area_large_numbers(self):
        '''
        Тест вычисления площади с большими числами
        '''
        self.assertEqual(rectangle.area(1000, 1000), 1000000)
        self.assertEqual(rectangle.area(1000000, 1000000), 1000000000000)
    
    def test_area_zero_values(self):
        '''
        Тест вычисления площади с нулевыми значениями
        '''
        self.assertEqual(rectangle.area(0, 5), 0)
        self.assertEqual(rectangle.area(5, 0), 0)
        self.assertEqual(rectangle.area(0, 0), 0)
    
    def test_area_mixed_types(self):
        '''
        Тест вычисления площади со смешанными числовыми типами
        '''
        self.assertEqual(rectangle.area(5, 3.0), 15.0)
        self.assertEqual(rectangle.area(2.5, 4), 10.0)


    
    def test_perimeter_integers(self):
        '''
        Тест вычисления периметра с целыми числами
        '''
        self.assertEqual(rectangle.perimeter(5, 3), 16)
        self.assertEqual(rectangle.perimeter(10, 10), 40)
        self.assertEqual(rectangle.perimeter(1, 1), 4)
    
    def test_perimeter_floats(self):
        '''
        Тест вычисления периметра с дробными числами
        '''
        self.assertAlmostEqual(rectangle.perimeter(2.5, 4.0), 13.0)
        self.assertAlmostEqual(rectangle.perimeter(3.14, 2.0), 10.28)
        self.assertAlmostEqual(rectangle.perimeter(0.5, 0.5), 2.0)
    
    def test_perimeter_large_numbers(self):
        '''
        Тест вычисления периметра с большими числами
        '''
        self.assertEqual(rectangle.perimeter(1000, 1000), 4000)
        self.assertEqual(rectangle.perimeter(1000000, 1000000), 4000000)
    
    def test_perimeter_zero_values(self):
        '''
        Тест вычисления периметра с нулевыми значениями
        '''
        self.assertEqual(rectangle.perimeter(0, 5), 10)
        self.assertEqual(rectangle.perimeter(5, 0), 10)
        self.assertEqual(rectangle.perimeter(0, 0), 0)
    
    def test_perimeter_mixed_types(self):
        '''
        Тест вычисления периметра со смешанными числовыми типами
        '''
        self.assertEqual(rectangle.perimeter(5, 3.0), 16.0)
        self.assertEqual(rectangle.perimeter(2.5, 4), 13.0)
    
    def test_area_edge_cases(self):
        '''
        Тест площади с граничными значениями
        '''
        self.assertAlmostEqual(rectangle.area(0.0001, 0.0001), 0.00000001)
        self.assertAlmostEqual(rectangle.area(0.001, 1000), 1.0)
    
    def test_perimeter_edge_cases(self):
        '''
        Тест периметра с граничными значениями
        '''
        self.assertAlmostEqual(rectangle.perimeter(0.0001, 0.0001), 0.0004)
        self.assertAlmostEqual(rectangle.perimeter(0.001, 1000), 2000.002)
