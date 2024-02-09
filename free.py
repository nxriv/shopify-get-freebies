import requests


def ensure_scheme(url):
    """Ensure the URL has http:// or https:// scheme."""
    if not url.startswith('http://') and not url.startswith('https://'):
        return 'https://' + url  # Defaulting to HTTPS for security
    return url


def fetch_shopify_products(store):
    free = []
    page = 1
    while True:
        page_url = f'{store}/products.json?limit=250&page={page}'
        response = requests.get(page_url)

        if response.status_code == 200 and 'application/json' in response.headers.get('Content-Type', ''):
            try:
                data = response.json()
            except ValueError:
                print("Failed to decode JSON from response")
                break

            if 'products' in data and data['products']:
                for product in data['products']:
                    for variant in product['variants']:
                        if float(variant['price']) == 0.0:
                            free.append({
                                'Variant ID': variant['id'],
                                'Quantity': 1
                            })
                page += 1
            else:
                break  # No more products, exit the loop
        else:
            print(f"Failed to fetch data: HTTP {response.status_code}")
            break

    return free


def generate_cart_link(store_url, free_products):
    product_string = ','.join([f"{product['Variant ID']}:{product['Quantity']}" for product in free_products])
    cart_link = f"{store_url}/cart/{product_string}"
    return cart_link


# Prompt user to enter the store URL
user_input_url = input("Please enter the store URL: ")
store_url = ensure_scheme(user_input_url)  # Ensure the URL has the correct scheme

free_products = fetch_shopify_products(store_url)

if free_products:
    cart_link = generate_cart_link(store_url, free_products)
    print('Cart link to add all free products:', cart_link)
else:
    print('No free products found.')
