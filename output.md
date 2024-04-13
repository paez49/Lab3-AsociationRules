# General Information
The total registered transactions on friday was: 18,330
The total items bought on friday was: 66,058
The total amount of bills on friday was: 317
The mean of products per bill on friday was: 208.38
The max amount of products in a bill on friday was: 6,205
The total sells on friday was: 140,352,837.98
The total taxes on friday was: 21,232,436.19

## The top 10 most bought products on friday were: 
1. EMPANADAS: 857
2. PASTELES. PALITOS: 374
3. JUGO HIT 500 ML: 333
4. COCA COLA FLEXI 400 ML: 287
5. SANDWICH SENCILLO: 252
6. CANDYRANCH 13GR: 247
7. TRIDENT 10 GR: 237
8. PASTILLAS CHAO CEREZA: 231
9. HALLS BARRA 25 GR: 212
10. MENTA CHAO LNEA: 198

## The top 10 least bought products on friday were: 
1. NUTRIBELA 10: 1
2. MAIZ TOSTADO 160GR: 1
3. PLANEADOR ESCRITORIO: 1
4. MALVAVISCOS ANGELITOS 50GR: 1
5. ESCENCIA VAINILLA 60ML: 1
6. COSEDORA KITTY: 1
7. CHAPSTICK SABORES: 1
8. SEDA DENTAL 20M: 1
9. ESCENCIA VUSE ORIGINAL: 1
10. VELA DEGRADE X: 1
## One of the less bought products was'MAIZ TOSTADO 160GR' and was selled with:
- EMPANADAS
- PASTELES. PALITOS
- PASTILLAS CHAO CEREZA
- JET FRESAS CON CREMA 29GR
- TODO RICO BBQ 45GR
- PROTECTORES NOSOTRAS X15
- SANDWICH SENCILLO
- NECTAR FRUTTO 300ML
- PASTELES. PALITOS
- CIFRUT 400ML
# Association Rules 
## Threshold: 0.2
|    | antecedents                              | consequents                              |   antecedent support |   consequent support |   support |   confidence |    lift |   leverage |   conviction |   zhangs_metric |
|---:|:-----------------------------------------|:-----------------------------------------|---------------------:|---------------------:|----------:|-------------:|--------:|-----------:|-------------:|----------------:|
|  0 | frozenset({'BRISA LIMON-MANZANA 600ML'}) | frozenset({'EMPANADAS'})                 |             0.255521 |             0.589905 |  0.22082  |     0.864198 | 1.46498 |  0.0700873 |      3.01979 |        0.426332 |
|  1 | frozenset({'EMPANADAS'})                 | frozenset({'BRISA LIMON-MANZANA 600ML'}) |             0.589905 |             0.255521 |  0.22082  |     0.374332 | 1.46498 |  0.0700873 |      1.18989 |        0.773956 |
|  2 | frozenset({'COCA COLA FLEXI 400 ML'})    | frozenset({'CANDYRANCH 13GR'})           |             0.394322 |             0.432177 |  0.271293 |     0.688    | 1.59194 |  0.100877  |      1.81995 |        0.613917 |
|  3 | frozenset({'CANDYRANCH 13GR'})           | frozenset({'COCA COLA FLEXI 400 ML'})    |             0.432177 |             0.394322 |  0.271293 |     0.627737 | 1.59194 |  0.100877  |      1.62702 |        0.654845 |
|  4 | frozenset({'CANDYRANCH 13GR'})           | frozenset({'EMPANADAS'})                 |             0.432177 |             0.589905 |  0.337539 |     0.781022 | 1.32398 |  0.0825961 |      1.87277 |        0.430945 |
### Time elapsed apriori_execution: 0.01 seconds.
|    | antecedents                          | consequents                          |   antecedent support |   consequent support |   support |   confidence |    lift |   leverage |   conviction |   zhangs_metric |
|---:|:-------------------------------------|:-------------------------------------|---------------------:|---------------------:|----------:|-------------:|--------:|-----------:|-------------:|----------------:|
|  0 | frozenset({'PASTILLAS CHAO CEREZA'}) | frozenset({'EMPANADAS'})             |             0.384858 |             0.589905 |  0.305994 |     0.795082 | 1.34781 |  0.0789639 |      2.00126 |        0.419508 |
|  1 | frozenset({'EMPANADAS'})             | frozenset({'PASTILLAS CHAO CEREZA'}) |             0.589905 |             0.384858 |  0.305994 |     0.518717 | 1.34781 |  0.0789639 |      1.27813 |        0.629262 |
|  2 | frozenset({'PASTILLAS CHAO CEREZA'}) | frozenset({'JUGO HIT 500 ML'})       |             0.384858 |             0.470032 |  0.258675 |     0.672131 | 1.42997 |  0.0777797 |      1.6164  |        0.488806 |
|  3 | frozenset({'JUGO HIT 500 ML'})       | frozenset({'PASTILLAS CHAO CEREZA'}) |             0.470032 |             0.384858 |  0.258675 |     0.550336 | 1.42997 |  0.0777797 |      1.368   |        0.567364 |
|  4 | frozenset({'CANDYRANCH 13GR'})       | frozenset({'PASTILLAS CHAO CEREZA'}) |             0.432177 |             0.384858 |  0.246057 |     0.569343 | 1.47936 |  0.0797301 |      1.42838 |        0.570655 |
### Time elapsed fp_growth_execution: 0.02 seconds.
## Threshold: 0.25
|    | antecedents                           | consequents                           |   antecedent support |   consequent support |   support |   confidence |    lift |   leverage |   conviction |   zhangs_metric |
|---:|:--------------------------------------|:--------------------------------------|---------------------:|---------------------:|----------:|-------------:|--------:|-----------:|-------------:|----------------:|
|  0 | frozenset({'COCA COLA FLEXI 400 ML'}) | frozenset({'CANDYRANCH 13GR'})        |             0.394322 |             0.432177 |  0.271293 |     0.688    | 1.59194 |  0.100877  |      1.81995 |        0.613917 |
|  1 | frozenset({'CANDYRANCH 13GR'})        | frozenset({'COCA COLA FLEXI 400 ML'}) |             0.432177 |             0.394322 |  0.271293 |     0.627737 | 1.59194 |  0.100877  |      1.62702 |        0.654845 |
|  2 | frozenset({'CANDYRANCH 13GR'})        | frozenset({'EMPANADAS'})              |             0.432177 |             0.589905 |  0.337539 |     0.781022 | 1.32398 |  0.0825961 |      1.87277 |        0.430945 |
|  3 | frozenset({'EMPANADAS'})              | frozenset({'CANDYRANCH 13GR'})        |             0.589905 |             0.432177 |  0.337539 |     0.572193 | 1.32398 |  0.0825961 |      1.32729 |        0.596693 |
|  4 | frozenset({'CANDYRANCH 13GR'})        | frozenset({'JUGO HIT 500 ML'})        |             0.432177 |             0.470032 |  0.280757 |     0.649635 | 1.38211 |  0.0776204 |      1.51262 |        0.486891 |
### Time elapsed apriori_execution: 0.01 seconds.
|    | antecedents                          | consequents                          |   antecedent support |   consequent support |   support |   confidence |    lift |   leverage |   conviction |   zhangs_metric |
|---:|:-------------------------------------|:-------------------------------------|---------------------:|---------------------:|----------:|-------------:|--------:|-----------:|-------------:|----------------:|
|  0 | frozenset({'PASTILLAS CHAO CEREZA'}) | frozenset({'EMPANADAS'})             |             0.384858 |             0.589905 |  0.305994 |     0.795082 | 1.34781 |  0.0789639 |      2.00126 |        0.419508 |
|  1 | frozenset({'EMPANADAS'})             | frozenset({'PASTILLAS CHAO CEREZA'}) |             0.589905 |             0.384858 |  0.305994 |     0.518717 | 1.34781 |  0.0789639 |      1.27813 |        0.629262 |
|  2 | frozenset({'PASTILLAS CHAO CEREZA'}) | frozenset({'JUGO HIT 500 ML'})       |             0.384858 |             0.470032 |  0.258675 |     0.672131 | 1.42997 |  0.0777797 |      1.6164  |        0.488806 |
|  3 | frozenset({'JUGO HIT 500 ML'})       | frozenset({'PASTILLAS CHAO CEREZA'}) |             0.470032 |             0.384858 |  0.258675 |     0.550336 | 1.42997 |  0.0777797 |      1.368   |        0.567364 |
|  4 | frozenset({'PONKY 33 GR'})           | frozenset({'EMPANADAS'})             |             0.312303 |             0.589905 |  0.258675 |     0.828283 | 1.40409 |  0.074446  |      2.3882  |        0.418494 |
### Time elapsed fp_growth_execution: 0.01 seconds.
## Threshold: 0.3
|    | antecedents                      | consequents                    |   antecedent support |   consequent support |   support |   confidence |    lift |   leverage |   conviction |   zhangs_metric |
|---:|:---------------------------------|:-------------------------------|---------------------:|---------------------:|----------:|-------------:|--------:|-----------:|-------------:|----------------:|
|  0 | frozenset({'CANDYRANCH 13GR'})   | frozenset({'EMPANADAS'})       |             0.432177 |             0.589905 |  0.337539 |     0.781022 | 1.32398 |  0.0825961 |      1.87277 |        0.430945 |
|  1 | frozenset({'EMPANADAS'})         | frozenset({'CANDYRANCH 13GR'}) |             0.589905 |             0.432177 |  0.337539 |     0.572193 | 1.32398 |  0.0825961 |      1.32729 |        0.596693 |
|  2 | frozenset({'JUGO HIT 500 ML'})   | frozenset({'EMPANADAS'})       |             0.470032 |             0.589905 |  0.384858 |     0.818792 | 1.38801 |  0.107584  |      2.26311 |        0.527469 |
|  3 | frozenset({'EMPANADAS'})         | frozenset({'JUGO HIT 500 ML'}) |             0.589905 |             0.470032 |  0.384858 |     0.652406 | 1.38801 |  0.107584  |      1.52468 |        0.681652 |
|  4 | frozenset({'PASTELES. PALITOS'}) | frozenset({'EMPANADAS'})       |             0.37224  |             0.589905 |  0.312303 |     0.838983 | 1.42223 |  0.0927166 |      2.5469  |        0.47292  |
### Time elapsed apriori_execution: 0.01 seconds.
|    | antecedents                          | consequents                          |   antecedent support |   consequent support |   support |   confidence |    lift |   leverage |   conviction |   zhangs_metric |
|---:|:-------------------------------------|:-------------------------------------|---------------------:|---------------------:|----------:|-------------:|--------:|-----------:|-------------:|----------------:|
|  0 | frozenset({'PASTILLAS CHAO CEREZA'}) | frozenset({'EMPANADAS'})             |             0.384858 |             0.589905 |  0.305994 |     0.795082 | 1.34781 |  0.0789639 |      2.00126 |        0.419508 |
|  1 | frozenset({'EMPANADAS'})             | frozenset({'PASTILLAS CHAO CEREZA'}) |             0.589905 |             0.384858 |  0.305994 |     0.518717 | 1.34781 |  0.0789639 |      1.27813 |        0.629262 |
|  2 | frozenset({'JUGO HIT 500 ML'})       | frozenset({'EMPANADAS'})             |             0.470032 |             0.589905 |  0.384858 |     0.818792 | 1.38801 |  0.107584  |      2.26311 |        0.527469 |
|  3 | frozenset({'EMPANADAS'})             | frozenset({'JUGO HIT 500 ML'})       |             0.589905 |             0.470032 |  0.384858 |     0.652406 | 1.38801 |  0.107584  |      1.52468 |        0.681652 |
|  4 | frozenset({'CANDYRANCH 13GR'})       | frozenset({'EMPANADAS'})             |             0.432177 |             0.589905 |  0.337539 |     0.781022 | 1.32398 |  0.0825961 |      1.87277 |        0.430945 |
### Time elapsed fp_growth_execution: 0.01 seconds.
## Threshold: 0.35
|    | antecedents                    | consequents                    |   antecedent support |   consequent support |   support |   confidence |    lift |   leverage |   conviction |   zhangs_metric |
|---:|:-------------------------------|:-------------------------------|---------------------:|---------------------:|----------:|-------------:|--------:|-----------:|-------------:|----------------:|
|  0 | frozenset({'JUGO HIT 500 ML'}) | frozenset({'EMPANADAS'})       |             0.470032 |             0.589905 |  0.384858 |     0.818792 | 1.38801 |   0.107584 |      2.26311 |        0.527469 |
|  1 | frozenset({'EMPANADAS'})       | frozenset({'JUGO HIT 500 ML'}) |             0.589905 |             0.470032 |  0.384858 |     0.652406 | 1.38801 |   0.107584 |      1.52468 |        0.681652 |
### Time elapsed apriori_execution: 0.01 seconds.
|    | antecedents                    | consequents                    |   antecedent support |   consequent support |   support |   confidence |    lift |   leverage |   conviction |   zhangs_metric |
|---:|:-------------------------------|:-------------------------------|---------------------:|---------------------:|----------:|-------------:|--------:|-----------:|-------------:|----------------:|
|  0 | frozenset({'JUGO HIT 500 ML'}) | frozenset({'EMPANADAS'})       |             0.470032 |             0.589905 |  0.384858 |     0.818792 | 1.38801 |   0.107584 |      2.26311 |        0.527469 |
|  1 | frozenset({'EMPANADAS'})       | frozenset({'JUGO HIT 500 ML'}) |             0.589905 |             0.470032 |  0.384858 |     0.652406 | 1.38801 |   0.107584 |      1.52468 |        0.681652 |
### Time elapsed fp_growth_execution: 0.01 seconds.
