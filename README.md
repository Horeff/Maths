# Maths
Module de mathématiques pour étudier des fonctions, résoudre des équations, etc

## Fonctions : 
  - Maths.func(<expression>, <nom>)
  crée la fonction, et calcule si possible la dérivée, la primitive, l'inverse, les limites en + et - l'infini. 
  Pour y accéder : <nom>.der ; <nom>.int ; <nom>.inv ; <nom>.limpinf ; <nom>.limminf
  Pour d'autres limites, il faut les calculer avec la fonction <nom>.limit(<valeur>) (mettre sp.oo pour l'infini)


## Modelisations : 
   - fit: Modélise pour toutes les fonctions disponibles (Voir "fonctions" ci dessous) et renvoie la meilleure modélisation selon le test de Kolmogorov Smirnov et un coefficient de correlation. 
  Pour renvoyer toutes les modélisations : return_every_modelisation=True
  print_tests ne sert qu'à voir les valeurs des résultats de tous les tests effectués pour toutes les modélisations.
  
  Syntaxe:```fit(x, y, print_tests: bool = False, return_every_modelisation: bool = False)```
  
  renvoie: 
  ```[(1)((2) 0.4312706260716667, ((3) True, (4) KstestResult(statistic, pvalue)), (5) array([2.32481706e-01, 2.81973905e+02]), (6) <bound method func.lin of <Maths.Functions.func object at 0x7fcee29b18e0>>), (...]```
  
 (1) - dépend de return_every_modelisation:
  
      Si True:
            renvoie une liste des tuples contenant les informations sur toutes les modélisations.
      Si False:
            renvoie une liste de l'unique tuple contenant les informations sur la meilleure modélisation.
  
 (2) - le résultat du coefficient de correlation
  
 (3) - Si la fonction modélise ou non la répartition (True/False) (donné par le coefficient de correlation)
  
 (4) - résultat du test de Kolmogorov Smirnov
  
 (5) - les paramètres trouvés lors de la modélisation dans l'ordre : (a, b, ...) voir fonctions disponibles ci dessous
  
 (6) - L'adresse de la fonction qui modélise
  
  
  
## fonctions disponibles pour modélisations : 
   - lin: a * x+b 
  ```lin(x, a, b)```
   - exp: a * exp(x*b) + c 
  ```exp(x, a, b, c)```
   - sin: a * sin(b*x + c) + d 
  ```sin(x, a, b, c, d)```
   - pol: a*x**2 + b*x + c 
  ```pol(x, a, b, c)```
   - pol3: a*x**3 + b*x**2 + c*x + d
  ```pol3(x, a, b, c, d)```
   - pol4: a*x**4 + b*x**3 + c*x**2 + d*x + e 
  ```pol4(x, a, b, c, d, e)```
