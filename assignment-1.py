import requests
import csv
import argparse

def fetch_listings(address, page_size):
    url = "https://www.vrbo.com/graphql"

    payload = {
        "variables": {
            "context": {
                "siteId": 9001001,
                "locale": "en_US",
                "eapid": 1,
                "currency": "USD",
                "device": {
                    "type": "DESKTOP"
                },
                "identity": {
                    "duaid": "65cbd87c-ebb5-ab83-a4c1-812db78bb787",
                    "expUserId": "-1",
                    "tuid": "-1",
                    "authState": "ANONYMOUS"
                },
                "privacyTrackingState": "CAN_TRACK",
                "debugContext": {
                    "abacusOverrides": []
                }
            },
            "criteria": {
                "primary": {
                    "dateRange": {
                        "checkInDate": {
                        "day": 1,
                        "month": 3,
                        "year": 2024
                    },
                        "checkOutDate": {
                            "day": 5,
                            "month": 3,
                            "year": 2024
                    }
                    },
                    "destination": {
                        "regionName": address,
                        "regionId": None,
                        "coordinates": None,
                        "pinnedPropertyId": None,
                        "propertyIds": None,
                        "mapBounds": None
                    },
                    "rooms": [
                        {
                            "adults": 2,
                            "children": []
                        }
                    ]
                },
                "secondary": {
                    "counts": [
                        {
                            "id": "resultsStartingIndex",
                            "value": 150
                        },
                        {
                            "id": "resultsSize",
                            "value": page_size
                        }
                    ],
                    "booleans": [],
                    "selections": [
                        {
                            "id": "sort",
                            "value": "RECOMMENDED"
                        },
                        {
                            "id": "privacyTrackingState",
                            "value": "CAN_TRACK"
                        },
                        {
                            "id": "useRewards",
                            "value": "SHOP_WITHOUT_POINTS"
                        },
                        {
                            "id": "searchId",
                            "value": "d1342ebe-2e4c-4c8d-8838-a3967204a6f2"
                        }
                    ],
                    "ranges": []
                }
            },
            "destination": {
                "regionName": None,
                "regionId": None,
                "coordinates": None,
                "pinnedPropertyId": None,
                "propertyIds": None,
                "mapBounds": None
            },
            "shoppingContext": {
                "multiItem": None
            },
            "returnPropertyType": False,
            "includeDynamicMap": True
        },
        "operationName": "LodgingPwaPropertySearch",
        "extensions": {
            "persistedQuery": {
                "sha256Hash": "e4ffcd90dd44f01455f9ddd89228915a177f9ec674f0df0db442ea1b20f551c3",
                "version": 1
            }
        }
    }

    headers = {
        'authority': 'www.vrbo.com',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,no;q=0.7,de;q=0.6',
        'cache-control': 'no-cache',
        'client-info': 'shopping-pwa,unknown,unknown',
        'content-type': 'application/json',
        'origin': 'https://www.vrbo.com',
        'pragma': 'no-cache',
        'referer': 'https://www.vrbo.com/search?adults=2&amenities=&children=&d1=2023-12-27&d2=2023-12-28&destination=73%20W%20Monroe%20St%2C%20Chicago%2C%20IL%2060603%2C%20USA&endDate=2024-03-05&latLong=&mapBounds=&pwaDialog=&regionId&semdtl=&sort=RECOMMENDED&startDate=2024-03-01&theme=&userIntent=',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-enable-apq': 'true',
        'x-page-id': 'page.Hotel-Search,H,20',
        'Cookie': 'DUAID=4db28c66-5933-13d6-0561-5a95950c67c3; HMS=6f38e6ec-8752-47fc-a444-8fcf71b888da; MC1=GUID=4db28c66593313d605615a95950c67c3; ak_bmsc=94C3B5B5E446C4C939BB110723FD1A7A~000000000000000000000000000000~YAAQRgHARdbgqFSNAQAANA+TfRbvjnSz+XnnW15Aqntc8kUZUCmcKyyQ7hnsZnwrUnK6L8BX2QfQjKl5bnDY15A7icizKETHIHb/xcvdjr08n5eIWIHw0+Y4ouil3CJRkgekG4Fvty37cWe3XtYGxUMo2WC3jvmgAX1w/JZjekw+/7KQ25rrIb3G8xa658JhzlGkIkcXFaZgjDqPWs47W99XoNjCIY6WXBe0o2lLEPLARxtJQIuEBj7NP2I8JIOLWUR98R2crIKFDBAGLP6zMLL7k12+RKCQVT6v/y4zFuL+Me9iHFC4ISm0ZymjkjAiLDIsZDNkddN/xCEg2jboourWKwE0UpQLR8pWoht7ZClIPOiPuVeQbw==; bm_sv=3B311CEB3FE8E02E1DFDD302C272C898~YAAQRgHARbSmqFSNAQAA8tNcfRZapd+fb7Lqse8YFWtJsDAH3R7hXS2pmMA2xLTo/JVJmoDL7GXDGqJb63RMrGSH+v/HfJ6MpNo4g4/SadVal5MZ2o/0l8AkIU0DhrRRp9W1qNN8+WGzRu+xCpo6LtF0//BkQgXyq9EjcX2HN3K4HU20HVp4a0hQw+Wm+cHmQ7MEd1yQzcTovMwaM+aTvLbWLqh+9A5rYD1xbKIyg9DlbgXfvo6J2lPydlcmpQ==~1; cesc=%7B%22marketingClick%22%3A%5B%22false%22%2C1707208806176%5D%2C%22hitNumber%22%3A%5B%221%22%2C1707208806176%5D%2C%22visitNumber%22%3A%5B%225%22%2C1707208806176%5D%2C%22entryPage%22%3A%5B%22page.Hotel-Search%22%2C1707208806176%5D%7D; hav=4db28c66-5933-13d6-0561-5a95950c67c3; ha-device-id=4db28c66-5933-13d6-0561-5a95950c67c3; has=108fafee-cc0d-4151-7f3c-58a79ec8c8f6; hav=4db28c66-5933-13d6-0561-5a95950c67c3'
    }

    response = requests.post(url, headers=headers, json=payload)
    return response.json()

def write_to_csv(listings, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Listing ID', 'Listing Title', 'Nightly Price', 'Listing URL']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for listing in listings:
            writer.writerow({
                'Listing ID': listing['id'],
                'Listing Title': listing['headingSection']['heading'],
                'Nightly Price': listing['priceSection']['priceSummary']['displayMessages'][0]['lineItems'][0]['price']['formatted'],
                'Listing URL': listing['cardLink']['resource']['value']
            })

def main():
    parser = argparse.ArgumentParser(description='Fetch listings from VRBO API and generate CSV file')
    parser.add_argument('address', type=str, help='Address of the place')
    parser.add_argument('page_size', type=int, help='Number of listings per page')
    
    args = parser.parse_args()
    
    response = fetch_listings(args.address, args.page_size)
    listings = response['data']['propertySearch']['propertySearchListings']
    write_to_csv(listings, "listings.csv")
    print('CSV file listings.csv generated successfully.')

if __name__ == "__main__":
    main()
