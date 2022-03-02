from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.parse


def ksl_cars_search(keyword, amt_listings_to_get=10):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    keyword = urllib.parse.quote_plus(keyword)
    driver.get(f"https://cars.ksl.com/search/keyword/{keyword}")
    time.sleep(1)
    wait = WebDriverWait(driver, 10)
    car_listings = wait.until(
        EC.visibility_of_all_elements_located(
            (By.XPATH, f"(//div[starts-with(@class, 'Listing__Content')])[position()<={amt_listings_to_get}]")))

    all_listings = dict()
    for i, listing in enumerate(car_listings):
        title = listing.find_element_by_xpath(".//a[contains(@class, 'listing-title')]").text
        price = listing.find_element_by_xpath(".//p[contains(@class, 'cIuZqO')]").text
        miles = listing.find_element_by_xpath(".//p[contains(@class, 'bUokqg')]").text
        location = listing.find_element_by_xpath(".//a[contains(@class, 'bmtYEH')]").text
        up_for = listing.find_element_by_xpath(".//span[contains(@class, 'VCixW')]").text
        link = listing.find_element_by_xpath(".//a[contains(@class, 'listing-title')]").get_attribute("href")
        listing_dict = {
            "title": title,
            "price": price,
            "miles": miles,
            "location": location,
            "up_for": up_for,
            "link": link
        }
        all_listings[i] = listing_dict

    driver.close()
    if all_listings:
        return all_listings
    return "No listings found"


if __name__ == "__main__":
    # Example code
    import json

    listings = ksl_cars_search(keyword="Honda civic", amt_listings_to_get=20)
    print(json.dumps(listings, indent=4))
