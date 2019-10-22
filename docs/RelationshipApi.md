# sysml_v2_api_client.RelationshipApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_relationship**](RelationshipApi.md#create_relationship) | **POST** /relationships | Add a new relationship
[**get_relationship**](RelationshipApi.md#get_relationship) | **GET** /relationships/{identifier} | Get relationship by its ID
[**get_relationships**](RelationshipApi.md#get_relationships) | **GET** /relationships | Get all relationships
[**get_relationships_by_project**](RelationshipApi.md#get_relationships_by_project) | **GET** /projects/{project_identifier}/relationships | Get all relationships in the project


# **create_relationship**
> Relationship create_relationship(body)

Add a new relationship

### Example

```python
from __future__ import print_function
import time
import sysml_v2_api_client
from sysml_v2_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sysml_v2_api_client.RelationshipApi()
body = sysml_v2_api_client.Relationship() # Relationship | 

try:
    # Add a new relationship
    api_response = api_instance.create_relationship(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationshipApi->create_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Relationship**](Relationship.md)|  | 

### Return type

[**Relationship**](Relationship.md)

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

# **get_relationship**
> Relationship get_relationship(identifier)

Get relationship by its ID

### Example

```python
from __future__ import print_function
import time
import sysml_v2_api_client
from sysml_v2_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sysml_v2_api_client.RelationshipApi()
identifier = 'identifier_example' # str | ID of the relationship

try:
    # Get relationship by its ID
    api_response = api_instance.get_relationship(identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationshipApi->get_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| ID of the relationship | 

### Return type

[**Relationship**](Relationship.md)

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

# **get_relationships**
> list[Relationship] get_relationships()

Get all relationships

### Example

```python
from __future__ import print_function
import time
import sysml_v2_api_client
from sysml_v2_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sysml_v2_api_client.RelationshipApi()

try:
    # Get all relationships
    api_response = api_instance.get_relationships()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationshipApi->get_relationships: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Relationship]**](Relationship.md)

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

# **get_relationships_by_project**
> list[Relationship] get_relationships_by_project(project_identifier)

Get all relationships in the project

### Example

```python
from __future__ import print_function
import time
import sysml_v2_api_client
from sysml_v2_api_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = sysml_v2_api_client.RelationshipApi()
project_identifier = 'project_identifier_example' # str | ID of the project

try:
    # Get all relationships in the project
    api_response = api_instance.get_relationships_by_project(project_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationshipApi->get_relationships_by_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_identifier** | **str**| ID of the project | 

### Return type

[**list[Relationship]**](Relationship.md)

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

