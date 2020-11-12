import iriusrisk_python_client_lib

api_instance = iriusrisk_python_client_lib.ProductsApi(iriusrisk_python_client_lib.ApiClient())
api_instance.api_client.configuration.host = "http://host:8080/api/v1"
api_token = '83890825-6ffb-4e57-a443-93c89559a44b'

# Show all products
allProducts = api_instance.products_get(api_token)
print(allProducts)

# Show a specific product
productRef = 'test'
product = api_instance.products_ref_get(api_token, productRef)

print(product)