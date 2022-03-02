# ksl_cars_scraper_selenium

Automatically scrape KSL Cars listings with Selenium.

Dependencies:
- Selenium

Example usage and output:

```python
from ksl_cars import ksl_cars_search
import json

listings = ksl_cars_search(keyword="Honda civic", amt_listings_to_get=20)
print(json.dumps(listings, indent=4))
```
Output: 
```commandline
{
    "0": {
        "title": "2019 Honda Civic LX",
        "price": "$19,989",
        "miles": "35,591 Miles",
        "location": "Draper, UT",
        "up_for": "",
        "link": "https://cars.ksl.com/listing/7410807"
    },
    "1": {
        "title": "2002 Honda Civic DX",
        "price": "$2,000",
        "miles": "165,000 Miles",
        "location": "Mapleton, UT",
        "up_for": "| 13 minutes",
        "link": "https://cars.ksl.com/listing/7435817"
    },
    "2": {
        "title": "2015 Honda Civic",
        "price": "$15,000",
        "miles": "65,300 Miles",
        "location": "Riverton, UT",
        "up_for": "| 29 minutes",
        "link": "https://cars.ksl.com/listing/7435783"
    }, ...
}
```
