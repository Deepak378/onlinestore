import unittest
import pandas as pd

class TestOrderAnalysis(unittest.TestCase):
    def setUp(self):
        
        self.sample_data = {
            'order_id': [1, 2, 3, 4, 5],
            'customer_id': [101, 102, 103, 101, 102],
            'order_date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-02-01', '2023-02-02'],
            'product_id': [1, 2, 3, 1, 2],
            'product_name': ['Product A', 'Product B', 'Product C', 'Product A', 'Product B'],
            'product_price': [10, 20, 30, 10, 20],
            'quantity': [1, 2, 1, 3, 2]
        }
        self.df = pd.DataFrame(self.sample_data)
        
    def test_monthly_revenue(self):
        self.df['order_date'] = pd.to_datetime(self.df['order_date'])
        self.df['revenue'] = self.df['product_price'] * self.df['quantity']
        monthly_revenue = self.df.groupby(self.df['order_date'].dt.to_period('M'))['revenue'].sum()
        expected_result = pd.Series([60, 100], index=pd.PeriodIndex(['2023-01', '2023-02'], freq='M'))
        pd.testing.assert_series_equal(monthly_revenue, expected_result)
        
    def test_product_revenue(self):
        product_revenue = self.df.groupby('product_name')['revenue'].sum()
        expected_result = pd.Series([20, 40, 30], index=['Product A', 'Product B', 'Product C'])
        pd.testing.assert_series_equal(product_revenue, expected_result)
        
    def test_customer_revenue(self):
        customer_revenue = self.df.groupby('customer_id')['revenue'].sum()
        expected_result = pd.Series([70, 130, 30], index=[101, 102, 103])
        pd.testing.assert_series_equal(customer_revenue, expected_result)
        
    def test_top_customers(self):
        customer_revenue = self.df.groupby('customer_id')['revenue'].sum()
        top_customers = customer_revenue.nlargest(2)  # Selecting top 2 for testing
        expected_result = pd.Series([130, 70], index=[102, 101])
        pd.testing.assert_series_equal(top_customers, expected_result)

if __name__ == '__main__':
    unittest.main()
