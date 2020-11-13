# iriusrisk-python-client-lib

This project provides a thick client written in Python to connect to the IriusRisk API.

## How to build

We upload the client generated with the Swagger Codegen CLI tool in this repository with the following command:
```
java -jar swagger-codegen-cli.jar generate -i swagger.yaml -l python -o iriusrisk-python-client-lib -c config.json
```


## How to use

Users only have to install the client with pip or pip3 by executing:
```
pip install iriusrisk-python-client-lib/
```

After that, users can create an API instance with:
```
import iriusrisk_python_client_lib

api_instance = iriusrisk_python_client_lib.ProductsApi(iriusrisk_python_client_lib.ApiClient())
api_instance.api_client.configuration.host = "http://host:8080/api/v1"
```
In this example we are using the ProductsApi to make the requests. Users can see API methods [here](iriusrisk-python-client-lib/README.md).

The file iriusriskclient.py contains an example of products_get and products_ref_get methods.
