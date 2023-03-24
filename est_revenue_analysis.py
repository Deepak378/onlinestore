import unittest
from collections import defaultdict
from datetime import datetime
from revenue_analysis import compute_monthly_revenue, compute_product_revenue, compute_customer_revenue, identify_top_10_customers

class TestRevenueAnalysis(unittest.TestCase):

    def setUp(self):
        self.orders = [
            {'order_id': '1', 'customer_id': 'A', 'order_date': '2022-01-01', 'product_id': '100', 'product_name': 'Product A', 'product_price': '10.0', 'quantity': '2'},
            {'order_id': '2', 'customer_id': 'B', 'order_date': '2022-01-02', 'product_id': '101', 'product_name': 'Product B', 'product_price': '20.0', 'quantity': '3'},
            {'order_id': '3', 'customer_id': 'C', 'order_date': '2022-02-01', 'product_id': '100', 'product_name': 'Product A', 'product_price': '10.0', 'quantity': '1'},
            {'order_id': '4', 'customer_id': 'A', 'order_date': '2022-02-02', 'product_id': '102', 'product_name': 'Product C', 'product_price': '30.0', 'quantity': '2'},
            {'order_id': '5', 'customer_id': 'C', 'order_date': '2022-03-01', 'product_id': '100', 'product_name': 'Product A', 'product_price': '10.0', 'quantity': '3'},
            {'order_id': '6', 'customer_id': 'A', 'order_date': '2022-03-02', 'product_id': '101', 'product_name': 'Product B', 'product_price': '20.0', 'quantity': '1'},
        ]

    def test_compute_monthly_revenue(self):
        expected_revenue = defaultdict(float)
        expected_revenue['2022-01'] = 70.0
        expected_revenue['2022-02'] = 70.0
        expected_revenue['2022-03'] = 50.0
        self.assertEqual(compute_monthly_revenue(self.orders), expected_revenue)

    def test_compute_product_revenue(self):
        expected_revenue = defaultdict(float)
        expected_revenue['Product A'] = 40.0
        expected_revenue['Product B'] = 60.0
        expected_revenue['Product C'] = 60.0
        self.assertEqual(compute_product_revenue(self.orders), expected_revenue)

    def test_compute_customer_revenue(self):
        expected_revenue = defaultdict(float)
        expected_revenue['A'] = 100.0
        expected_revenue['B'] = 60.0
        expected_revenue['C'] = 40.0
        self.assertEqual(compute_customer_revenue(self.orders), expected_revenue)

    def test_identify_top_10_customers(self):
        expected_top_10 = [('A', 100.0), ('B', 60.0), ('C', 40.0)]
        self.assertEqual(identify_top_10_customers(self.orders), expected_top_10)

if __name__ == '__main__':
    unittest.main()
