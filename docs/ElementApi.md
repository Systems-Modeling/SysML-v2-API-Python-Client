# sysml_v2_api_client.ElementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_element**](ElementApi.md#create_element) | **POST** /elements | Add a new element
[**get_element**](ElementApi.md#get_element) | **GET** /elements/{identifier} | Get element by its ID
[**get_element_by_project_and_id**](ElementApi.md#get_element_by_project_and_id) | **GET** /projects/{project_identifier}/elements/{element_identifier} | Get element by project ID and its ID
[**get_elements**](ElementApi.md#get_elements) | **GET** /elements | Get all elements
[**get_elements_in_project**](ElementApi.md#get_elements_in_project) | **GET** /projects/{project_identifier}/elements | Get all elements in the project


# **create_element**
> Element create_element(body)

Add a new element

### Example

```python
from __future__ import print_function
import time
import sysml_v2_api_client
from sysml_v2_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sysml_v2_api_client.ElementApi()
body = None # dict(str, object) | 

try:
    # Add a new element
    api_response = api_instance.create_element(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementApi->create_element: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](object.md)|  | 

### Return type

[**Element**](Element.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**415** | The requested content type is not acceptable. |  -  |
**500** | Internal server error. |  -  |
**0** | Unexpected response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_element**
> Element get_element(identifier)

Get element by its ID

### Example

```python
from __future__ import print_function
import time
import sysml_v2_api_client
from sysml_v2_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sysml_v2_api_client.ElementApi()
identifier = 'identifier_example' # str | ID of the element

try:
    # Get element by its ID
    api_response = api_instance.get_element(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementApi->get_element: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| ID of the element | 

### Return type

[**Element**](Element.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**404** | Not found. |  -  |
**415** | The requested content type is not acceptable. |  -  |
**500** | Internal server error. |  -  |
**0** | Unexpected response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_element_by_project_and_id**
> Element get_element_by_project_and_id(project_identifier, element_identifier)

Get element by project ID and its ID

### Example

```python
from __future__ import print_function
import time
import sysml_v2_api_client
from sysml_v2_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sysml_v2_api_client.ElementApi()
project_identifier = 'project_identifier_example' # str | ID of the project
element_identifier = 'element_identifier_example' # str | ID of the element

try:
    # Get element by project ID and its ID
    api_response = api_instance.get_element_by_project_and_id(project_identifier, element_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementApi->get_element_by_project_and_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_identifier** | **str**| ID of the project | 
 **element_identifier** | **str**| ID of the element | 

### Return type

[**Element**](Element.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**404** | Not found. |  -  |
**415** | The requested content type is not acceptable. |  -  |
**500** | Internal server error. |  -  |
**0** | Unexpected response. |  -  |

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

# Create an instance of the API class
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**415** | The requested content type is not acceptable. |  -  |
**500** | Internal server error. |  -  |
**0** | Unexpected response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_elements_in_project**
> Element get_elements_in_project(project_identifier)

Get all elements in the project

### Example

```python
from __future__ import print_function
import time
import sysml_v2_api_client
from sysml_v2_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sysml_v2_api_client.ElementApi()
project_identifier = 'project_identifier_example' # str | ID of the project

try:
    # Get all elements in the project
    api_response = api_instance.get_elements_in_project(project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ElementApi->get_elements_in_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_identifier** | **str**| ID of the project | 

### Return type

[**Element**](Element.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**404** | Not found. |  -  |
**415** | The requested content type is not acceptable. |  -  |
**500** | Internal server error. |  -  |
**0** | Unexpected response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

