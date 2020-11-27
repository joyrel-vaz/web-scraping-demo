# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 15:23:22 2020

@author: Joyrel Vaz
"""

from recipe_scrapers import scrape_me

print('running scraping.py')
# give the url as a string, it can be url from any site listed below
#scraper = scrape_me('https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/')

# Q: What if the recipe site I want to extract information from is not listed below?
# A: You can give it a try with the wild_mode option! If there is Schema/Recipe available it will work just fine.

urls = [#'https://www.chinasichuanfood.com/kung-pao-chicken/',
        #'https://www.chinasichuanfood.com/mushroom-stir-fry/'
        #'https://www.priyascurrynation.com/caramel-sauce/',
        #'https://www.manjulaskitchen.com/paneer-pasanda/'
        'https://www.jeyashriskitchen.com/biryani-masalabiryani-masala-recipe/'
        # home remedies 'https://tarladalal.com/recipes-for-Anorexia-Home-Remedies-466'
        #'https://www.vegrecipesofindia.com/barfi-recipe-quick-khoya-barfi/'
        #'https://www.indianfoodforever.com/mughlai/shahi-chicken-korma.html'
        #'https://www.goanfoodrecipes.com/recipe-items/bread-pudding-with-dry-fruits'
        #'https://thewoksoflife.com/vegan-queso/#wprm-recipe-container-45690',
        #'https://www.chinayummyfood.com/biang-biang-noodles/',
        #'https://justamumnz.com/2014/09/02/honey-cornflake-super-crunch-cookies/',
        #'https://chinesehealthycooking.com/steamed-ribs-with-black-bean-paste-pumpkin-and-rice-a-meal-in-a-bowl-%e8%b1%86%e8%b1%89%e9%85%b1%e8%92%b8%e6%8e%92%e9%aa%a8%ef%bc%8c%e6%99%9a%e9%a4%90%e4%b8%80%e7%a2%97%e6%90%9e%e5%ae%9a/'
       # 'http://appetiteforchina.com/recipes/chinese-tea-eggs',
        #'http://www.thehongkongcookery.com/2020/10/chinese-cha-siu-bao-roasted-pork-buns.html'
        ]

for url in urls:   
    scraper = scrape_me(url, wild_mode=True)  
    print('##################################')
    print(scraper.title())
    print(scraper.host())
 # scraper.total_time()
  #scraper.yields()
    print(scraper.ingredients())
    print(scraper.instructions())
  #scraper.image()
  #scraper.host()


