#%%

import pandas as pd

data = {'gdp_usa':[15542, 16197, 16785, 17527, 18238, 18745, 19543], 
        'gdp_canada':[1789, 1829, 1847, 1804, 1556, 1528, 1650], 
        'gdp_mexico':[1181, 1201, 1274, 1315, 1172, 1078, 1159], 
        'unemp_usa':[8.9, 8.1, 7.4, 16.2, 5.3, 4.9, 4.4], 
        'unemp_canada':[7.5, 7.4, 7.2, 7.1, 7, 7.2, 6.4], 
        'unemp_mexico':[7.3, 7, 6.9, 6.6, 6.6, 6.8, 6.1]}

years = [2011, 2012, 2013, 2014, 2015, 2016, 2017]

na_econ = pd.DataFrame(data, index=years)
print(na_econ)


#%%
#1. write one line that selects only the GDP columns, for the years 
#   2013-2014
na_gdp = na_econ.loc[[row for row in na_econ.index if row in [2013, 2014]],[col for col in na_econ.columns if col.startswith("gdp")]]
na_gdp_13 = na_econ.loc[ [2013, 2014] , [col for col in na_econ.columns if col.startswith("gdp")] ]
print(na_gdp_13)

#%%
#2. the unemployment rate in the USA in 2014 should be 6.2, not 16.2.
#   write one line that replaces that value
na_econ.loc[2014,"unemp_usa"] = 6.2
print(na_econ)
#%%