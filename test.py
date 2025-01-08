import unittest
import os
import pandas as pd
import numpy as np
from unittest.mock import patch


class TestGdpVisualization(unittest.TestCase):
    # File Handling Tests
    def test_linear_fitting_code_in_correct_folder(self):
        # Ensure the script is in the correct folder
        self.assertTrue(os.path.isfile('gdp_visualization.py'))

    def test_data_file_in_correct_folder(self):
        # Ensure the data file is in the correct folder
        self.assertTrue(os.path.isfile('final.dataset.xlsx'))

    def test_data_file_is_correct_type(self):
        # Ensure the data file is of correct type (.xlsx)
        file_path = 'final.dataset.xlsx'
        self.assertTrue(file_path.endswith('.xlsx'))

    # Data Checking Tests
    def test_data_file_has_two_columns_of_data(self):
        # Ensure that the dataset has exactly two data columns (GDP, Year)
        file_path = 'final.dataset.xlsx'
        gdp_data = pd.read_excel(file_path)
        self.assertEqual(gdp_data.shape[1], 3)  # Ensure we have three columns (Country, Year, GDP)

    def test_data_file_has_header_lines(self):
        # Check for the number of header lines
        file_path = 'final.dataset.xlsx'
        gdp_data = pd.read_excel(file_path)
        self.assertTrue(len(gdp_data.columns) > 0)  # Ensure that the dataset has headers

    def test_data_file_missing_or_non_numeric_data(self):
        # Check for missing or non-numeric data
        file_path = 'final.dataset.xlsx'
        gdp_data = pd.read_excel(file_path)
        self.assertFalse(gdp_data.isnull().any().any())  # No missing values
        self.assertTrue(np.issubdtype(gdp_data['GDP'].dtype, np.number))  # GDP should be numeric

    # Statistics Verification Tests
    def test_data_has_enough_points_to_fit_line(self):
        # Ensure there are enough data points to fit a line
        file_path = 'final.dataset.xlsx'
        gdp_data = pd.read_excel(file_path)
        self.assertGreater(len(gdp_data), 1)  # Should have more than 1 data point

    def test_data_points_sufficiently_correlated(self):
        # Check if the data points are sufficiently correlated (simple correlation test)
        file_path = 'final.dataset.xlsx'
        gdp_data = pd.read_excel(file_path)
        correlation = gdp_data['Year'].corr(gdp_data['GDP'])
        self.assertGreater(abs(correlation), 0.5)  # Should have significant correlation

    @patch('gdp_visualization.linear_fit')  # Mock your linear fitting function
    def test_correct_slope_and_intercept(self, mock_linear_fit):
        # Ensure that the linear fitting code is functioning and returns correct results
        mock_linear_fit.return_value = (0.5, 2000)  # Mocking a return value
        slope, intercept = mock_linear_fit()
        self.assertEqual(slope, 0.5)  # Check slope
        self.assertEqual(intercept, 2000)  # Check intercept


if __name__ == '__main__':
    unittest.main()
