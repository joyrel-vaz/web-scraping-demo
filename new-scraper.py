# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 19:09:46 2020

@author: Joyrel Vaz
"""

import scrape_schema_recipe
url =  'http://www.thehongkongcookery.com/2016/05/hong-kong-style-mango-pudding.html'
recipe_list = scrape_schema_recipe.scrape_url(url, python_objects=True)
print(recipe_list[0]['name'])
