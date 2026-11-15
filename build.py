# Rebuild index.html from src/: python3 build.py
t=open('src/app_template.html').read(); d=open('src/recipes.json').read().replace('</','<\\/')
open('index.html','w').write(t.replace('__RECIPES__',d))
