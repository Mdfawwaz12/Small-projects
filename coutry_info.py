# pip install countryinfo
#ye poora information api mein haiso countryinfo aako usse use karko implement hotaso
from countryinfo import CountryInfo

#step 1:creating an object
country = CountryInfo('India')
a = country.capital()
print(a)

'''
many other function are present you can use
'''