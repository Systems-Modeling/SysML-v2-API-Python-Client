# sysml_v2_api_client.ElementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_element_by_project_commit_id**](ElementApi.md#get_element_by_project_commit_id) | **GET** /projects/{projectId}/commits/{commitId}/elements/{elementId} | Get element by project, commit and ID
[**get_elements_by_project_commit**](ElementApi.md#get_elements_by_project_commit) | **GET** /projects/{projectId}/commits/{commitId}/elements | Get elements by project and commit
[**get_roots_by_project_commit**](ElementApi.md#get_roots_by_project_commit) | **GET** /projects/{projectId}/commits/{commitId}/roots | Get root elements by project and commit


# **get_element_by_project_commit_id**
> Element get_element_by_project_commit_id(project_id, commit_id, element_id)

Get element by project, commit and ID

### Example

```python
from __future__ import print_function
import time
import sysml_v2_api_client
from sysml_v2_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysml_v2_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sysml_v2_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sysml_v2_api_client.ElementApi(api_client)
    project_id = 'project_id_example' # str | ID of the project
commit_id = 'commit_id_example' # str | ID of the commit
element_id = 'element_id_example' # str | ID of the element

    try:
        # Get element by project, commit and ID
        api_response = api_instance.get_element_by_project_commit_id(project_id, commit_id, element_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ElementApi->get_element_by_project_commit_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**str**](.md)| ID of the project | 
 **commit_id** | [**str**](.md)| ID of the commit | 
 **element_id** | [**str**](.md)| ID of the element | 

### Return type

[**Element**](Element.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**404** | Not found. |  -  |
**415** | The requested content type is not acceptable. |  -  |
**500** | Internal server error. |  -  |
**0** | Unexpected response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_elements_by_project_commit**
> list[Element] get_elements_by_project_commit(project_id, commit_id, page_after=page_after, page_before=page_before, page_size=page_size)

Get elements by project and commit

### Example

```python
from __future__ import print_function
import time
import sysml_v2_api_client
from sysml_v2_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysml_v2_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sysml_v2_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sysml_v2_api_client.ElementApi(api_client)
    project_id = 'project_id_example' # str | ID of the project
commit_id = 'commit_id_example' # str | ID of the commit
page_after = 'page_after_example' # str | Page after (optional)
page_before = 'page_before_example' # str | Page before (optional)
page_size = 56 # int | Page size (optional)

    try:
        # Get elements by project and commit
        api_response = api_instance.get_elements_by_project_commit(project_id, commit_id, page_after=page_after, page_before=page_before, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ElementApi->get_elements_by_project_commit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**str**](.md)| ID of the project | 
 **commit_id** | [**str**](.md)| ID of the commit | 
 **page_after** | **str**| Page after | [optional] 
 **page_before** | **str**| Page before | [optional] 
 **page_size** | **int**| Page size | [optional] 

### Return type

[**list[Element]**](Element.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**404** | Not found. |  -  |
**415** | The requested content type is not acceptable. |  -  |
**500** | Internal server error. |  -  |
**0** | Unexpected response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_roots_by_project_commit**
> list[Element] get_roots_by_project_commit(project_id, commit_id, page_after=page_after, page_before=page_before, page_size=page_size)

Get root elements by project and commit

### Example

```python
from __future__ import print_function
import time
import sysml_v2_api_client
from sysml_v2_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sysml_v2_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with sysml_v2_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sysml_v2_api_client.ElementApi(api_client)
    project_id = 'project_id_example' # str | ID of the project
commit_id = 'commit_id_example' # str | ID of the commit
page_after = 'page_after_example' # str | Page after (optional)
page_before = 'page_before_example' # str | Page before (optional)
page_size = 56 # int | Page size (optional)

    try:
        # Get root elements by project and commit
        api_response = api_instance.get_roots_by_project_commit(project_id, commit_id, page_after=page_after, page_before=page_before, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ElementApi->get_roots_by_project_commit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**str**](.md)| ID of the project | 
 **commit_id** | [**str**](.md)| ID of the commit | 
 **page_after** | **str**| Page after | [optional] 
 **page_before** | **str**| Page before | [optional] 
 **page_size** | **int**| Page size | [optional] 

### Return type

[**list[Element]**](Element.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**404** | Not found. |  -  |
**415** | The requested content type is not acceptable. |  -  |
**500** | Internal server error. |  -  |
**0** | Unexpected response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

