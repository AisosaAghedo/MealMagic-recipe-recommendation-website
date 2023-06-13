'''
integration tests for recipes view
'''
from unittest import TestCase
from api.app import app
import unittest
url_prefix = '/api/meal_magic'


class TestRecipes(TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.res = self.app.post(f'{url_prefix}/recipes/ingredients',
                                 json={'ingredients': 'tomatoes, fish'})
        self.recipe = self.res.json['suggested_recipe'][0][0]


    def test_get_recipe(self):
        '''
        test  for '/recipes/ingredients' endpoint
        '''
        self.assertEqual(200, self.res.status_code)


    def test_find_recipe(self):
        '''
        test for '/get_recipes' endpoint
        '''
        res = self.app.post(f'{url_prefix}/get_recipes',
                            json={'name': self.recipe})
        self.assertEqual(200, res.status_code)


if __name__ == '__main__':
    unittest.main()
