# sysml_v2_api_client.ModelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_model**](ModelApi.md#create_model) | **POST** /model | Add a new model
[**get_model**](ModelApi.md#get_model) | **GET** /model/{id} | Get model by its ID
[**get_models**](ModelApi.md#get_models) | **GET** /model | Get all models


# **create_model**
> Model create_model(model=model)

Add a new model

### Example
```python
from __future__ import print_function
import time
import sysml_v2_api_client
from sysml_v2_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sysml_v2_api_client.ModelApi()
model = sysml_v2_api_client.Model() # Model |  (optional)

try:
    # Add a new model
    api_response = api_instance.create_model(model=model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->create_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**Model**](Model.md)|  | [optional] 

### Return type

[**Model**](Model.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model**
> Model get_model(id)

Get model by its ID

### Example
```python
from __future__ import print_function
import time
import sysml_v2_api_client
from sysml_v2_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sysml_v2_api_client.ModelApi()
id = 'id_example' # str | ID of the model

try:
    # Get model by its ID
    api_response = api_instance.get_model(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->get_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the model | 

### Return type

[**Model**](Model.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_models**
> list[Model] get_models()

Get all models

### Example
```python
from __future__ import print_function
import time
import sysml_v2_api_client
from sysml_v2_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sysml_v2_api_client.ModelApi()

try:
    # Get all models
    api_response = api_instance.get_models()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->get_models: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Model]**](Model.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

