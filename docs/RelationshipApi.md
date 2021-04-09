# sysml_v2_api_client.RelationshipApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_relationships_by_project_commit_related_element**](RelationshipApi.md#get_relationships_by_project_commit_related_element) | **GET** /projects/{projectId}/commits/{commitId}/elements/{relatedElementId}/relationships | Get relationships by project, commit, and related element


# **get_relationships_by_project_commit_related_element**
> list[Relationship] get_relationships_by_project_commit_related_element(project_id, commit_id, related_element_id, direction=direction, page_after=page_after, page_before=page_before, page_size=page_size)

Get relationships by project, commit, and related element

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
    api_instance = sysml_v2_api_client.RelationshipApi(api_client)
    project_id = 'project_id_example' # str | ID of the project
commit_id = 'commit_id_example' # str | ID of the commit
related_element_id = 'related_element_id_example' # str | ID of the related element
direction = 'both' # str | Filter for relationships that are incoming (in), outgoing (out), or both relative to the related element (optional) (default to 'both')
page_after = 'page_after_example' # str | Page after (optional)
page_before = 'page_before_example' # str | Page before (optional)
page_size = 56 # int | Page size (optional)

    try:
        # Get relationships by project, commit, and related element
        api_response = api_instance.get_relationships_by_project_commit_related_element(project_id, commit_id, related_element_id, direction=direction, page_after=page_after, page_before=page_before, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RelationshipApi->get_relationships_by_project_commit_related_element: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**str**](.md)| ID of the project | 
 **commit_id** | [**str**](.md)| ID of the commit | 
 **related_element_id** | [**str**](.md)| ID of the related element | 
 **direction** | **str**| Filter for relationships that are incoming (in), outgoing (out), or both relative to the related element | [optional] [default to &#39;both&#39;]
 **page_after** | **str**| Page after | [optional] 
 **page_before** | **str**| Page before | [optional] 
 **page_size** | **int**| Page size | [optional] 

### Return type

[**list[Relationship]**](Relationship.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**415** | The requested content type is not acceptable. |  -  |
**500** | Internal server error. |  -  |
**0** | Unexpected response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

