# sysml_v2_api_client.ElementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_element**](ElementApi.md#create_element) | **POST** /element | Add a new element
[**get_element**](ElementApi.md#get_element) | **GET** /element/{id} | Get element by its ID
[**get_elements**](ElementApi.md#get_elements) | **GET** /element | Get all elements
[**get_elements_in_model**](ElementApi.md#get_elements_in_model) | **GET** /element/model/{model_id} | Get all elements in the model


# **create_element**
> Element create_element(element)

Add a new element

### Example
```python
from __future__ import print_function
import time
import sysml_v2_api_client
from sysml_v2_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sysml_v2_api_client.ElementApi()
element = sysml_v2_api_client.Element() # Element | 

try:
    # Add a new element
    api_response = api_instance.create_element(element)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementApi->create_element: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **element** | [**Element**](Element.md)|  | 

### Return type

[**Element**](Element.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_element**
> Element get_element(id)

Get element by its ID

### Example
```python
from __future__ import print_function
import time
import sysml_v2_api_client
from sysml_v2_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sysml_v2_api_client.ElementApi()
id = 'id_example' # str | ID of the element

try:
    # Get element by its ID
    api_response = api_instance.get_element(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementApi->get_element: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the element | 

### Return type

[**Element**](Element.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_elements**
> list[Element] get_elements()

Get all elements

### Example
```python
from __future__ import print_function
import time
import sysml_v2_api_client
from sysml_v2_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sysml_v2_api_client.ElementApi()

try:
    # Get all elements
    api_response = api_instance.get_elements()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementApi->get_elements: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Element]**](Element.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_elements_in_model**
> Element get_elements_in_model(model_id)

Get all elements in the model

### Example
```python
from __future__ import print_function
import time
import sysml_v2_api_client
from sysml_v2_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sysml_v2_api_client.ElementApi()
model_id = 'model_id_example' # str | ID of the model

try:
    # Get all elements in the model
    api_response = api_instance.get_elements_in_model(model_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementApi->get_elements_in_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**| ID of the model | 

### Return type

[**Element**](Element.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

