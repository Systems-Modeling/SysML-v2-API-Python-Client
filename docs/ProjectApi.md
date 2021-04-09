# sysml_v2_api_client.ProjectApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_project_by_id**](ProjectApi.md#get_project_by_id) | **GET** /projects/{projectId} | Get project by ID
[**get_projects**](ProjectApi.md#get_projects) | **GET** /projects | Get projects
[**post_project**](ProjectApi.md#post_project) | **POST** /projects | Create project


# **get_project_by_id**
> Project get_project_by_id(project_id)

Get project by ID

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
    api_instance = sysml_v2_api_client.ProjectApi(api_client)
    project_id = 'project_id_example' # str | ID of the project

    try:
        # Get project by ID
        api_response = api_instance.get_project_by_id(project_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->get_project_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**str**](.md)| ID of the project | 

### Return type

[**Project**](Project.md)

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

# **get_projects**
> list[Project] get_projects(page_after=page_after, page_before=page_before, page_size=page_size)

Get projects

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
    api_instance = sysml_v2_api_client.ProjectApi(api_client)
    page_after = 'page_after_example' # str | Page after (optional)
page_before = 'page_before_example' # str | Page before (optional)
page_size = 56 # int | Page size (optional)

    try:
        # Get projects
        api_response = api_instance.get_projects(page_after=page_after, page_before=page_before, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->get_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_after** | **str**| Page after | [optional] 
 **page_before** | **str**| Page before | [optional] 
 **page_size** | **int**| Page size | [optional] 

### Return type

[**list[Project]**](Project.md)

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

# **post_project**
> Project post_project(body=body)

Create project

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
    api_instance = sysml_v2_api_client.ProjectApi(api_client)
    body = sysml_v2_api_client.Project() # Project |  (optional)

    try:
        # Create project
        api_response = api_instance.post_project(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectApi->post_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Project**](Project.md)|  | [optional] 

### Return type

[**Project**](Project.md)

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

