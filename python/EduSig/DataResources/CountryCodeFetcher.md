# EduSig/DataResources/CountryCodeFetcher

::::: {#content dir="ltr" lang="en"}
:::: {.highlight .python}
::: {.codearea dir="ltr" lang="en"}
``` {#CA-621c305edb53cf73a65c0913f02d1af25ff3e260 dir="ltr" lang="en"}
   1 import urllib2                                                                                                                                       
   2 from BeautifulSoup import BeautifulSoup                                                                                                              
   3                                                                                                                                                      
   4 def FetchCountryCodes():                                                                                                                             
   5     """Country Code List: ISO 3166-1993 (E)                                                                                                          
   6                                                                                                                                                      
   7       This international standard provides a two-letter alphabetic code for                                                                          
   8       representing the names of countries, dependencies, and other areas of                                                                          
   9       special geopolitical interest. The source of this code set is the Codes                                                                        
  10       for the Representation of Names of Countries (ISO 3166-1993 (E)).                                                                              
  11     """                                                                                                                                              
  12                                                                                                                                                      
  13     page = urllib2.urlopen("http://xml.coverpages.org/country3166.html")                                                                             
  14     soup = BeautifulSoup(page)                                                                                                                       
  15     page.close()                                                                                                                                     
  16                                                                                                                                                      
  17     countries = []                                                                                                                                   
  18     for listrow in soup.html.body.table.findAll('tr')[1:]:                                                                                           
  19         col1, col2 = listrow.findAll('td')                                                                                                           
  20         code = col1.renderContents()                                                                                                                 
  21         name = col2.renderContents()                                                                                                                 
  22         countries.append( (code, name) )                                                                                                             
  23     return countries                                                                                                                                 
  24                                                                                                                                                      
  25 codes = FetchCountryCodes()                                                                                                                          
  26 print codes                                                                                                                                          
```
:::
::::

**Note(s):**

- This example uses standard Python except for

  [the BeautifulSoup package](http://www.crummy.com/software/BeautifulSoup/){.http} which must be installed separately.

------------------------------------------------------------------------

[CategoryPythonInEducation](CategoryPythonInEducation)
:::::
