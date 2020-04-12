# sysml_v2_api_client.CommitApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_commit_by_project_and_id**](CommitApi.md#get_commit_by_project_and_id) | **GET** /projects/{projectId}/commits/{commitId} | Get commit by project and ID
[**get_commits_by_project**](CommitApi.md#get_commits_by_project) | **GET** /projects/{projectId}/commits | Get commits by project
[**get_head_commit_by_project**](CommitApi.md#get_head_commit_by_project) | **GET** /projects/{projectId}/head | Get head commit by project
[**post_commit_by_project**](CommitApi.md#post_commit_by_project) | **POST** /projects/{projectId}/commits | Create commit by project


# **get_commit_by_project_and_id**
> Commit get_commit_by_project_and_id(project_id, commit_id)

Get commit by project and ID

### Example

```python
from __future__ import print_function
import time
import sysml_v2_api_client
from sysml_v2_api_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with sysml_v2_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sysml_v2_api_client.CommitApi(api_client)
    project_id = 'project_id_example' # str | ID of the project
commit_id = 'commit_id_example' # str | ID of the commit

    try:
        # Get commit by project and ID
        api_response = api_instance.get_commit_by_project_and_id(project_id, commit_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommitApi->get_commit_by_project_and_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**str**](.md)| ID of the project | 
 **commit_id** | [**str**](.md)| ID of the commit | 

### Return type

[**Commit**](Commit.md)

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

# **get_commits_by_project**
> list[Commit] get_commits_by_project(project_id)

Get commits by project

### Example

```python
from __future__ import print_function
import time
import sysml_v2_api_client
from sysml_v2_api_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with sysml_v2_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sysml_v2_api_client.CommitApi(api_client)
    project_id = 'project_id_example' # str | ID of the project

    try:
        # Get commits by project
        api_response = api_instance.get_commits_by_project(project_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommitApi->get_commits_by_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**str**](.md)| ID of the project | 

### Return type

[**list[Commit]**](Commit.md)

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

# **get_head_commit_by_project**
> Commit get_head_commit_by_project(project_id)

Get head commit by project

### Example

```python
from __future__ import print_function
import time
import sysml_v2_api_client
from sysml_v2_api_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with sysml_v2_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sysml_v2_api_client.CommitApi(api_client)
    project_id = 'project_id_example' # str | ID of the project

    try:
        # Get head commit by project
        api_response = api_instance.get_head_commit_by_project(project_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommitApi->get_head_commit_by_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**str**](.md)| ID of the project | 

### Return type

[**Commit**](Commit.md)

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

# **post_commit_by_project**
> Commit post_commit_by_project(project_id, body)

Create commit by project

### Example

```python
from __future__ import print_function
import time
import sysml_v2_api_client
from sysml_v2_api_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with sysml_v2_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sysml_v2_api_client.CommitApi(api_client)
    project_id = 'project_id_example' # str | ID of the project
body = sysml_v2_api_client.Commit() # Commit | 

    try:
        # Create commit by project
        api_response = api_instance.post_commit_by_project(project_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommitApi->post_commit_by_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**str**](.md)| ID of the project | 
 **body** | [**Commit**](Commit.md)|  | 

### Return type

[**Commit**](Commit.md)

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

