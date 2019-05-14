# sysml_v2_api_client.RelationshipApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_relationship**](RelationshipApi.md#create_relationship) | **POST** /relationship | Add a new relationship
[**get_relationship**](RelationshipApi.md#get_relationship) | **GET** /relationship/{id} | Get relationship by its ID
[**get_relationships**](RelationshipApi.md#get_relationships) | **GET** /relationship | Get all relationships
[**get_relationships_by_element**](RelationshipApi.md#get_relationships_by_element) | **GET** /relationship/element/{element_id} | Get all relationships with the given element as either source or target
[**get_relationships_by_source**](RelationshipApi.md#get_relationships_by_source) | **GET** /relationship/source/{source_id} | Get all relationships with the given element as the source
[**get_relationships_by_target**](RelationshipApi.md#get_relationships_by_target) | **GET** /relationship/target/{target_id} | Get all relationships with the given element as the target


# **create_relationship**
> Relationship create_relationship(relationship)

Add a new relationship

### Example
```python
from __future__ import print_function
import time
import sysml_v2_api_client
from sysml_v2_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sysml_v2_api_client.RelationshipApi()
relationship = sysml_v2_api_client.Relationship() # Relationship | 

try:
    # Add a new relationship
    api_response = api_instance.create_relationship(relationship)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationshipApi->create_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relationship** | [**Relationship**](Relationship.md)|  | 

### Return type

[**Relationship**](Relationship.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_relationship**
> Relationship get_relationship(id)

Get relationship by its ID

### Example
```python
from __future__ import print_function
import time
import sysml_v2_api_client
from sysml_v2_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sysml_v2_api_client.RelationshipApi()
id = 'id_example' # str | ID of the relationship

try:
    # Get relationship by its ID
    api_response = api_instance.get_relationship(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationshipApi->get_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the relationship | 

### Return type

[**Relationship**](Relationship.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

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

# create an instance of the API class
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_relationships_by_element**
> list[Relationship] get_relationships_by_element(element_id)

Get all relationships with the given element as either source or target

### Example
```python
from __future__ import print_function
import time
import sysml_v2_api_client
from sysml_v2_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sysml_v2_api_client.RelationshipApi()
element_id = 'element_id_example' # str | ID of the element that is the source or target of relationships

try:
    # Get all relationships with the given element as either source or target
    api_response = api_instance.get_relationships_by_element(element_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationshipApi->get_relationships_by_element: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **element_id** | **str**| ID of the element that is the source or target of relationships | 

### Return type

[**list[Relationship]**](Relationship.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_relationships_by_source**
> list[Relationship] get_relationships_by_source(source_id)

Get all relationships with the given element as the source

### Example
```python
from __future__ import print_function
import time
import sysml_v2_api_client
from sysml_v2_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sysml_v2_api_client.RelationshipApi()
source_id = 'source_id_example' # str | ID of the element that is the source of relationships

try:
    # Get all relationships with the given element as the source
    api_response = api_instance.get_relationships_by_source(source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationshipApi->get_relationships_by_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| ID of the element that is the source of relationships | 

### Return type

[**list[Relationship]**](Relationship.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_relationships_by_target**
> list[Relationship] get_relationships_by_target(target_id)

Get all relationships with the given element as the target

### Example
```python
from __future__ import print_function
import time
import sysml_v2_api_client
from sysml_v2_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sysml_v2_api_client.RelationshipApi()
target_id = 'target_id_example' # str | ID of the element that is the target of relationships

try:
    # Get all relationships with the given element as the target
    api_response = api_instance.get_relationships_by_target(target_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationshipApi->get_relationships_by_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_id** | **str**| ID of the element that is the target of relationships | 

### Return type

[**list[Relationship]**](Relationship.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

