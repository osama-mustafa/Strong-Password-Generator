import unittest
import password_generator
from unittest.mock import patch


class TestMethods(unittest.TestCase):


    @patch('password_generator.input')
    def test_get_valid_password_length_with_valid_input(self, mocked_input):
            mocked_input.side_effect = '8'
            password_length = password_generator.get_valid_password_length()

            self.assertEqual(password_length, 8)


    def test_generate_password_returns_string(self):
        test_input = 8
        password = password_generator.generate_password(test_input)
        self.assertIsInstance(password, str)

    
    def test_result_password_lenght_matches_password_length_input(self):
         test_input = 33
         result_password = password_generator.generate_password(test_input)
         self.assertEqual(len(result_password), test_input)


if __name__ == '__main__':
    unittest.main()


