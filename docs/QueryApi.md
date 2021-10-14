# sysml_v2_api_client.QueryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_query_by_project_and_id**](QueryApi.md#delete_query_by_project_and_id) | **DELETE** /projects/{projectId}/queries/{queryId} | Delete query by project and ID
[**get_queries_by_project**](QueryApi.md#get_queries_by_project) | **GET** /projects/{projectId}/queries | Get queries by project
[**get_query_by_project_and_id**](QueryApi.md#get_query_by_project_and_id) | **GET** /projects/{projectId}/queries/{queryId} | Get query by project and ID
[**get_query_results_by_project_id_query**](QueryApi.md#get_query_results_by_project_id_query) | **GET** /projects/{projectId}/query-results | Get query results by project and query definition
[**get_query_results_by_project_id_query_id**](QueryApi.md#get_query_results_by_project_id_query_id) | **GET** /projects/{projectId}/queries/{queryId}/results | Get query results by project and query
[**get_query_results_by_project_id_query_post**](QueryApi.md#get_query_results_by_project_id_query_post) | **POST** /projects/{projectId}/query-results | Get query results by project and query definition via POST
[**post_query_by_project**](QueryApi.md#post_query_by_project) | **POST** /projects/{projectId}/queries | Create query by project


# **delete_query_by_project_and_id**
> Query delete_query_by_project_and_id(project_id, query_id)

Delete query by project and ID

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
    api_instance = sysml_v2_api_client.QueryApi(api_client)
    project_id = 'project_id_example' # str | ID of the project
query_id = 'query_id_example' # str | ID of the query

    try:
        # Delete query by project and ID
        api_response = api_instance.delete_query_by_project_and_id(project_id, query_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling QueryApi->delete_query_by_project_and_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**str**](.md)| ID of the project | 
 **query_id** | [**str**](.md)| ID of the query | 

### Return type

[**Query**](Query.md)

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

# **get_queries_by_project**
> list[Query] get_queries_by_project(project_id, page_after=page_after, page_before=page_before, page_size=page_size)

Get queries by project

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
    api_instance = sysml_v2_api_client.QueryApi(api_client)
    project_id = 'project_id_example' # str | ID of the project
page_after = 'page_after_example' # str | Page after (optional)
page_before = 'page_before_example' # str | Page before (optional)
page_size = 56 # int | Page size (optional)

    try:
        # Get queries by project
        api_response = api_instance.get_queries_by_project(project_id, page_after=page_after, page_before=page_before, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling QueryApi->get_queries_by_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**str**](.md)| ID of the project | 
 **page_after** | **str**| Page after | [optional] 
 **page_before** | **str**| Page before | [optional] 
 **page_size** | **int**| Page size | [optional] 

### Return type

[**list[Query]**](Query.md)

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

# **get_query_by_project_and_id**
> Query get_query_by_project_and_id(project_id, query_id)

Get query by project and ID

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
    api_instance = sysml_v2_api_client.QueryApi(api_client)
    project_id = 'project_id_example' # str | ID of the project
query_id = 'query_id_example' # str | ID of the query

    try:
        # Get query by project and ID
        api_response = api_instance.get_query_by_project_and_id(project_id, query_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling QueryApi->get_query_by_project_and_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**str**](.md)| ID of the project | 
 **query_id** | [**str**](.md)| ID of the query | 

### Return type

[**Query**](Query.md)

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

# **get_query_results_by_project_id_query**
> list[Element] get_query_results_by_project_id_query(project_id, body, commit_id=commit_id)

Get query results by project and query definition

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
    api_instance = sysml_v2_api_client.QueryApi(api_client)
    project_id = 'project_id_example' # str | ID of the project
body = sysml_v2_api_client.Query() # Query | 
commit_id = 'commit_id_example' # str | ID of the commit - defaults to head of project (optional)

    try:
        # Get query results by project and query definition
        api_response = api_instance.get_query_results_by_project_id_query(project_id, body, commit_id=commit_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling QueryApi->get_query_results_by_project_id_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**str**](.md)| ID of the project | 
 **body** | [**Query**](Query.md)|  | 
 **commit_id** | [**str**](.md)| ID of the commit - defaults to head of project | [optional] 

### Return type

[**list[Element]**](Element.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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

# **get_query_results_by_project_id_query_id**
> list[Element] get_query_results_by_project_id_query_id(project_id, query_id, commit_id=commit_id)

Get query results by project and query

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
    api_instance = sysml_v2_api_client.QueryApi(api_client)
    project_id = 'project_id_example' # str | ID of the project
query_id = 'query_id_example' # str | ID of the query
commit_id = 'commit_id_example' # str | ID of the commit - defaults to head of project (optional)

    try:
        # Get query results by project and query
        api_response = api_instance.get_query_results_by_project_id_query_id(project_id, query_id, commit_id=commit_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling QueryApi->get_query_results_by_project_id_query_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**str**](.md)| ID of the project | 
 **query_id** | [**str**](.md)| ID of the query | 
 **commit_id** | [**str**](.md)| ID of the commit - defaults to head of project | [optional] 

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

# **get_query_results_by_project_id_query_post**
> list[Element] get_query_results_by_project_id_query_post(project_id, body, commit_id=commit_id)

Get query results by project and query definition via POST

For compatibility with clients that don't support GET requests with a body

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
    api_instance = sysml_v2_api_client.QueryApi(api_client)
    project_id = 'project_id_example' # str | ID of the project
body = sysml_v2_api_client.Query() # Query | 
commit_id = 'commit_id_example' # str | ID of the commit - defaults to head of project (optional)

    try:
        # Get query results by project and query definition via POST
        api_response = api_instance.get_query_results_by_project_id_query_post(project_id, body, commit_id=commit_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling QueryApi->get_query_results_by_project_id_query_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**str**](.md)| ID of the project | 
 **body** | [**Query**](Query.md)|  | 
 **commit_id** | [**str**](.md)| ID of the commit - defaults to head of project | [optional] 

### Return type

[**list[Element]**](Element.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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

# **post_query_by_project**
> Query post_query_by_project(project_id, body)

Create query by project

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
    api_instance = sysml_v2_api_client.QueryApi(api_client)
    project_id = 'project_id_example' # str | ID of the project
body = sysml_v2_api_client.Query() # Query | 

    try:
        # Create query by project
        api_response = api_instance.post_query_by_project(project_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling QueryApi->post_query_by_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**str**](.md)| ID of the project | 
 **body** | [**Query**](Query.md)|  | 

### Return type

[**Query**](Query.md)

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

