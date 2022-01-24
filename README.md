# pfruck_contabo

> ⚠️ I am not affiliated in any way with Contabo

This is an UNOFFICIAL Python API client for [contabo.com](https://contabo.com), which is a hosting provider for VPS and dedicated servers.

The goal of this client is to make management of your server instances more easy using a native Python API for the freshly released [Contabo API](https://api.contabo.com/).
This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project.

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

The simplest way to install the Contabo API client is by using the provided [pip package](https://pypi.org/project/pfruck-contabo):

```sh
pip install pfruck-contabo
```

You can also install the package directly from the GitHub Repo using pip:
```sh
pip install git+https://github.com/p-fruck/python-contabo.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/p-fruck/python-contabo.git`)

Then import the package:
```python
import pfruck_contabo
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import pfruck_contabo
```
## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import pfruck_contabo
from pfruck_contabo.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pfruck_contabo.ImagesApi(pfruck_contabo.ApiClient(configuration))
body = pfruck_contabo.CreateCustomImageRequest() # CreateCustomImageRequest | 
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Provide a custom image
    api_response = api_instance.create_custom_image(body, x_request_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->create_custom_image: %s\n" % e)


# create an instance of the API class
api_instance = pfruck_contabo.ImagesApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
image_id = 'image_id_example' # str | The identifier of the image
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Delete an uploaded custom image by its id
    api_instance.delete_image(x_request_id, image_id, x_trace_id=x_trace_id)
except ApiException as e:
    print("Exception when calling ImagesApi->delete_image: %s\n" % e)


# create an instance of the API class
api_instance = pfruck_contabo.ImagesApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # List statistics regarding the customer's custom images
    api_response = api_instance.retrieve_custom_images_stats(x_request_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->retrieve_custom_images_stats: %s\n" % e)


# create an instance of the API class
api_instance = pfruck_contabo.ImagesApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
image_id = 'image_id_example' # str | The identifier of the image
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Get details about a specific image by its id
    api_response = api_instance.retrieve_image(x_request_id, image_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->retrieve_image: %s\n" % e)


# create an instance of the API class
api_instance = pfruck_contabo.ImagesApi(pfruck_contabo.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)
page = 789 # int | Number of page to be fetched. (optional)
size = 789 # int | Number of elements per page. (optional)
order_by = ['order_by_example'] # list[str] | Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`. (optional)
name = 'name_example' # str | The name of the image (optional)
standard_image = true # bool | Flag indicating that image is either a standard (true) or a custom image (false) (optional)

try:
    # List available standard and custom images
    api_response = api_instance.retrieve_image_list(x_request_id, x_trace_id=x_trace_id, page=page, size=size, order_by=order_by, name=name, standard_image=standard_image)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->retrieve_image_list: %s\n" % e)


# create an instance of the API class
api_instance = pfruck_contabo.ImagesApi(pfruck_contabo.ApiClient(configuration))
body = pfruck_contabo.UpdateCustomImageRequest() # UpdateCustomImageRequest | 
x_request_id = 'x_request_id_example' # str | [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
image_id = 'image_id_example' # str | The identifier of the image
x_trace_id = 'x_trace_id_example' # str | Identifier to trace group of requests. (optional)

try:
    # Update custom image name by its id
    api_response = api_instance.update_image(body, x_request_id, image_id, x_trace_id=x_trace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->update_image: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ImagesApi* | [**create_custom_image**](docs/ImagesApi.md#create_custom_image) | **POST** /v1/compute/images | Provide a custom image
*ImagesApi* | [**delete_image**](docs/ImagesApi.md#delete_image) | **DELETE** /v1/compute/images/{imageId} | Delete an uploaded custom image by its id
*ImagesApi* | [**retrieve_custom_images_stats**](docs/ImagesApi.md#retrieve_custom_images_stats) | **GET** /v1/compute/images/stats | List statistics regarding the customer&#x27;s custom images
*ImagesApi* | [**retrieve_image**](docs/ImagesApi.md#retrieve_image) | **GET** /v1/compute/images/{imageId} | Get details about a specific image by its id
*ImagesApi* | [**retrieve_image_list**](docs/ImagesApi.md#retrieve_image_list) | **GET** /v1/compute/images | List available standard and custom images
*ImagesApi* | [**update_image**](docs/ImagesApi.md#update_image) | **PATCH** /v1/compute/images/{imageId} | Update custom image name by its id
*ImagesAuditsApi* | [**retrieve_image_audits_list**](docs/ImagesAuditsApi.md#retrieve_image_audits_list) | **GET** /v1/compute/images/audits | List history about your custom images (audit)
*InstanceActionsApi* | [**restart**](docs/InstanceActionsApi.md#restart) | **POST** /v1/compute/instances/{instanceId}/actions/restart | Restart a compute instance / resource identified by its id
*InstanceActionsApi* | [**start**](docs/InstanceActionsApi.md#start) | **POST** /v1/compute/instances/{instanceId}/actions/start | Start a compute instance / resource identified by its id
*InstanceActionsApi* | [**stop**](docs/InstanceActionsApi.md#stop) | **POST** /v1/compute/instances/{instanceId}/actions/stop | Stop compute instance / resource by its id
*InstanceActionsAuditsApi* | [**retrieve_instances_actions_audits_list**](docs/InstanceActionsAuditsApi.md#retrieve_instances_actions_audits_list) | **GET** /v1/compute/instances/actions/audits | List history about your actions (audit) triggered via the API
*InstancesApi* | [**cancel_instance**](docs/InstancesApi.md#cancel_instance) | **POST** /v1/compute/instances/{instanceId}/cancel | Cancel specific instance by id
*InstancesApi* | [**create_instance**](docs/InstancesApi.md#create_instance) | **POST** /v1/compute/instances | Create a new instance
*InstancesApi* | [**reinstall_instance**](docs/InstancesApi.md#reinstall_instance) | **PATCH** /v1/compute/instances/{instanceId} | Reinstall specific instance
*InstancesApi* | [**retrieve_instance**](docs/InstancesApi.md#retrieve_instance) | **GET** /v1/compute/instances/{instanceId} | Get specific instance by id
*InstancesApi* | [**retrieve_instances_list**](docs/InstancesApi.md#retrieve_instances_list) | **GET** /v1/compute/instances | List instances
*InstancesAuditsApi* | [**retrieve_instances_audits_list**](docs/InstancesAuditsApi.md#retrieve_instances_audits_list) | **GET** /v1/compute/instances/audits | List history about your instances (audit) triggered via the API
*RolesApi* | [**create_role**](docs/RolesApi.md#create_role) | **POST** /v1/roles | Create a new role
*RolesApi* | [**delete_role**](docs/RolesApi.md#delete_role) | **DELETE** /v1/roles/{roleId} | Delete existing role by id
*RolesApi* | [**retrieve_api_permissions_list**](docs/RolesApi.md#retrieve_api_permissions_list) | **GET** /v1/roles/api-permissions | List of API permissions
*RolesApi* | [**retrieve_role**](docs/RolesApi.md#retrieve_role) | **GET** /v1/roles/{roleId} | Get specific role by id
*RolesApi* | [**retrieve_role_list**](docs/RolesApi.md#retrieve_role_list) | **GET** /v1/roles | List roles
*RolesApi* | [**update_role**](docs/RolesApi.md#update_role) | **PUT** /v1/roles/{roleId} | Update specific role by id
*RolesAuditsApi* | [**retrieve_role_audits_list**](docs/RolesAuditsApi.md#retrieve_role_audits_list) | **GET** /v1/roles/audits | List history about your roles (audit)
*SecretsApi* | [**create_secret**](docs/SecretsApi.md#create_secret) | **POST** /v1/secrets | Create a new secret
*SecretsApi* | [**delete_secret**](docs/SecretsApi.md#delete_secret) | **DELETE** /v1/secrets/{secretId} | Delete existing secret by id
*SecretsApi* | [**retrieve_secret**](docs/SecretsApi.md#retrieve_secret) | **GET** /v1/secrets/{secretId} | Get specific secret by id
*SecretsApi* | [**retrieve_secret_list**](docs/SecretsApi.md#retrieve_secret_list) | **GET** /v1/secrets | List secrets
*SecretsApi* | [**update_secret**](docs/SecretsApi.md#update_secret) | **PATCH** /v1/secrets/{secretId} | Update specific secret by id
*SecretsAuditsApi* | [**retrieve_secret_audits_list**](docs/SecretsAuditsApi.md#retrieve_secret_audits_list) | **GET** /v1/secrets/audits | List history about your secrets (audit)
*SnapshotsApi* | [**create_snapshot**](docs/SnapshotsApi.md#create_snapshot) | **POST** /v1/compute/instances/{instanceId}/snapshots | Create a new instance snapshot
*SnapshotsApi* | [**delete_snapshot**](docs/SnapshotsApi.md#delete_snapshot) | **DELETE** /v1/compute/instances/{instanceId}/snapshots/{snapshotId} | Delete existing snapshot by id
*SnapshotsApi* | [**retrieve_snapshot**](docs/SnapshotsApi.md#retrieve_snapshot) | **GET** /v1/compute/instances/{instanceId}/snapshots/{snapshotId} | Retrieve a specific snapshot by id
*SnapshotsApi* | [**retrieve_snapshot_list**](docs/SnapshotsApi.md#retrieve_snapshot_list) | **GET** /v1/compute/instances/{instanceId}/snapshots | List snapshots
*SnapshotsApi* | [**rollback_snapshot**](docs/SnapshotsApi.md#rollback_snapshot) | **POST** /v1/compute/instances/{instanceId}/snapshots/{snapshotId}/rollback | Rollback the instance to a specific snapshot by id
*SnapshotsApi* | [**update_snapshot**](docs/SnapshotsApi.md#update_snapshot) | **PATCH** /v1/compute/instances/{instanceId}/snapshots/{snapshotId} | Update specific snapshot by id
*SnapshotsAuditsApi* | [**retrieve_snapshots_audits_list**](docs/SnapshotsAuditsApi.md#retrieve_snapshots_audits_list) | **GET** /v1/compute/snapshots/audits | List history about your snapshots (audit) triggered via the API
*TagAssignmentsApi* | [**create_assignment**](docs/TagAssignmentsApi.md#create_assignment) | **POST** /v1/tags/{tagId}/assignments/{resourceType}/{resourceId} | Create a new assignment for the tag
*TagAssignmentsApi* | [**delete_assignment**](docs/TagAssignmentsApi.md#delete_assignment) | **DELETE** /v1/tags/{tagId}/assignments/{resourceType}/{resourceId} | Delete existing tag assignment
*TagAssignmentsApi* | [**retrieve_assignment**](docs/TagAssignmentsApi.md#retrieve_assignment) | **GET** /v1/tags/{tagId}/assignments/{resourceType}/{resourceId} | Get specific assignment for the tag
*TagAssignmentsApi* | [**retrieve_assignment_list**](docs/TagAssignmentsApi.md#retrieve_assignment_list) | **GET** /v1/tags/{tagId}/assignments | List tag assignments
*TagAssignmentsAuditsApi* | [**retrieve_assignments_audits_list**](docs/TagAssignmentsAuditsApi.md#retrieve_assignments_audits_list) | **GET** /v1/tags/assignments/audits | List history about your assignments (audit)
*TagsApi* | [**create_tag**](docs/TagsApi.md#create_tag) | **POST** /v1/tags | Create a new tag
*TagsApi* | [**delete_tag**](docs/TagsApi.md#delete_tag) | **DELETE** /v1/tags/{tagId} | Delete existing tag by id
*TagsApi* | [**retrieve_tag**](docs/TagsApi.md#retrieve_tag) | **GET** /v1/tags/{tagId} | Get specific tag by id
*TagsApi* | [**retrieve_tag_list**](docs/TagsApi.md#retrieve_tag_list) | **GET** /v1/tags | List tags
*TagsApi* | [**update_tag**](docs/TagsApi.md#update_tag) | **PATCH** /v1/tags/{tagId} | Update specific tag by id
*TagsAuditsApi* | [**retrieve_tag_audits_list**](docs/TagsAuditsApi.md#retrieve_tag_audits_list) | **GET** /v1/tags/audits | List history about your tags (audit)
*UsersApi* | [**create_user**](docs/UsersApi.md#create_user) | **POST** /v1/users | Create a new user
*UsersApi* | [**delete_user**](docs/UsersApi.md#delete_user) | **DELETE** /v1/users/{userId} | Delete existing user by id
*UsersApi* | [**generate_client_secret**](docs/UsersApi.md#generate_client_secret) | **PUT** /v1/users/client/secret | Generate new client secret
*UsersApi* | [**resend_email_verification**](docs/UsersApi.md#resend_email_verification) | **POST** /v1/users/{userId}/resend-email-verification | Resend email verification
*UsersApi* | [**reset_password**](docs/UsersApi.md#reset_password) | **POST** /v1/users/{userId}/reset-password | Send reset password email
*UsersApi* | [**retrieve_user**](docs/UsersApi.md#retrieve_user) | **GET** /v1/users/{userId} | Get specific user by id
*UsersApi* | [**retrieve_user_client**](docs/UsersApi.md#retrieve_user_client) | **GET** /v1/users/client | Get client
*UsersApi* | [**retrieve_user_is_password_set**](docs/UsersApi.md#retrieve_user_is_password_set) | **GET** /v1/users/is-password-set | Get user is password set status
*UsersApi* | [**retrieve_user_list**](docs/UsersApi.md#retrieve_user_list) | **GET** /v1/users | List users
*UsersApi* | [**update_user**](docs/UsersApi.md#update_user) | **PATCH** /v1/users/{userId} | Update specific user by id
*UsersAuditsApi* | [**retrieve_user_audits_list**](docs/UsersAuditsApi.md#retrieve_user_audits_list) | **GET** /v1/users/audits | List history about your users (audit)

## Documentation For Models

 - [AddOnResponse](docs/AddOnResponse.md)
 - [AllOfCancelInstanceResponseLinks](docs/AllOfCancelInstanceResponseLinks.md)
 - [AllOfCreateAssignmentResponseLinks](docs/AllOfCreateAssignmentResponseLinks.md)
 - [AllOfCreateCustomImageResponseLinks](docs/AllOfCreateCustomImageResponseLinks.md)
 - [AllOfCreateInstanceResponseLinks](docs/AllOfCreateInstanceResponseLinks.md)
 - [AllOfCreateRoleResponseLinks](docs/AllOfCreateRoleResponseLinks.md)
 - [AllOfCreateSecretResponseLinks](docs/AllOfCreateSecretResponseLinks.md)
 - [AllOfCreateSnapshotResponseLinks](docs/AllOfCreateSnapshotResponseLinks.md)
 - [AllOfCreateTagResponseLinks](docs/AllOfCreateTagResponseLinks.md)
 - [AllOfCreateUserResponseLinks](docs/AllOfCreateUserResponseLinks.md)
 - [AllOfCustomImagesStatsResponseLinks](docs/AllOfCustomImagesStatsResponseLinks.md)
 - [AllOfFindAssignmentResponseLinks](docs/AllOfFindAssignmentResponseLinks.md)
 - [AllOfFindClientResponseLinks](docs/AllOfFindClientResponseLinks.md)
 - [AllOfFindImageResponseLinks](docs/AllOfFindImageResponseLinks.md)
 - [AllOfFindInstanceResponseLinks](docs/AllOfFindInstanceResponseLinks.md)
 - [AllOfFindRoleResponseLinks](docs/AllOfFindRoleResponseLinks.md)
 - [AllOfFindSecretResponseLinks](docs/AllOfFindSecretResponseLinks.md)
 - [AllOfFindSnapshotResponseLinks](docs/AllOfFindSnapshotResponseLinks.md)
 - [AllOfFindTagResponseLinks](docs/AllOfFindTagResponseLinks.md)
 - [AllOfFindUserIsPasswordSetResponseLinks](docs/AllOfFindUserIsPasswordSetResponseLinks.md)
 - [AllOfFindUserResponseLinks](docs/AllOfFindUserResponseLinks.md)
 - [AllOfGenerateClientSecretResponseLinks](docs/AllOfGenerateClientSecretResponseLinks.md)
 - [AllOfImageAuditResponseLinks](docs/AllOfImageAuditResponseLinks.md)
 - [AllOfImageAuditResponsePagination](docs/AllOfImageAuditResponsePagination.md)
 - [AllOfInstanceRestartActionResponseLinks](docs/AllOfInstanceRestartActionResponseLinks.md)
 - [AllOfInstanceStartActionResponseLinks](docs/AllOfInstanceStartActionResponseLinks.md)
 - [AllOfInstanceStopActionResponseLinks](docs/AllOfInstanceStopActionResponseLinks.md)
 - [AllOfListApiPermissionResponseLinks](docs/AllOfListApiPermissionResponseLinks.md)
 - [AllOfListAssignmentAuditsResponseLinks](docs/AllOfListAssignmentAuditsResponseLinks.md)
 - [AllOfListAssignmentAuditsResponsePagination](docs/AllOfListAssignmentAuditsResponsePagination.md)
 - [AllOfListAssignmentResponseLinks](docs/AllOfListAssignmentResponseLinks.md)
 - [AllOfListAssignmentResponsePagination](docs/AllOfListAssignmentResponsePagination.md)
 - [AllOfListImageResponseLinks](docs/AllOfListImageResponseLinks.md)
 - [AllOfListImageResponsePagination](docs/AllOfListImageResponsePagination.md)
 - [AllOfListInstancesActionsAuditResponseLinks](docs/AllOfListInstancesActionsAuditResponseLinks.md)
 - [AllOfListInstancesActionsAuditResponsePagination](docs/AllOfListInstancesActionsAuditResponsePagination.md)
 - [AllOfListInstancesAuditResponseLinks](docs/AllOfListInstancesAuditResponseLinks.md)
 - [AllOfListInstancesAuditResponsePagination](docs/AllOfListInstancesAuditResponsePagination.md)
 - [AllOfListInstancesResponseLinks](docs/AllOfListInstancesResponseLinks.md)
 - [AllOfListInstancesResponsePagination](docs/AllOfListInstancesResponsePagination.md)
 - [AllOfListRoleAuditResponseLinks](docs/AllOfListRoleAuditResponseLinks.md)
 - [AllOfListRoleResponseLinks](docs/AllOfListRoleResponseLinks.md)
 - [AllOfListRoleResponsePagination](docs/AllOfListRoleResponsePagination.md)
 - [AllOfListSecretAuditResponseLinks](docs/AllOfListSecretAuditResponseLinks.md)
 - [AllOfListSecretAuditResponsePagination](docs/AllOfListSecretAuditResponsePagination.md)
 - [AllOfListSecretResponseLinks](docs/AllOfListSecretResponseLinks.md)
 - [AllOfListSecretResponsePagination](docs/AllOfListSecretResponsePagination.md)
 - [AllOfListSnapshotResponseLinks](docs/AllOfListSnapshotResponseLinks.md)
 - [AllOfListSnapshotResponsePagination](docs/AllOfListSnapshotResponsePagination.md)
 - [AllOfListSnapshotsAuditResponseLinks](docs/AllOfListSnapshotsAuditResponseLinks.md)
 - [AllOfListSnapshotsAuditResponsePagination](docs/AllOfListSnapshotsAuditResponsePagination.md)
 - [AllOfListTagAuditsResponseLinks](docs/AllOfListTagAuditsResponseLinks.md)
 - [AllOfListTagAuditsResponsePagination](docs/AllOfListTagAuditsResponsePagination.md)
 - [AllOfListTagResponseLinks](docs/AllOfListTagResponseLinks.md)
 - [AllOfListTagResponsePagination](docs/AllOfListTagResponsePagination.md)
 - [AllOfListUserAuditResponseLinks](docs/AllOfListUserAuditResponseLinks.md)
 - [AllOfListUserAuditResponsePagination](docs/AllOfListUserAuditResponsePagination.md)
 - [AllOfListUserResponseLinks](docs/AllOfListUserResponseLinks.md)
 - [AllOfListUserResponsePagination](docs/AllOfListUserResponsePagination.md)
 - [AllOfReinstallInstanceResponseLinks](docs/AllOfReinstallInstanceResponseLinks.md)
 - [AllOfRollbackSnapshotResponseLinks](docs/AllOfRollbackSnapshotResponseLinks.md)
 - [AllOfUpdateCustomImageResponseLinks](docs/AllOfUpdateCustomImageResponseLinks.md)
 - [AllOfUpdateRoleResponseLinks](docs/AllOfUpdateRoleResponseLinks.md)
 - [AllOfUpdateSecretResponseLinks](docs/AllOfUpdateSecretResponseLinks.md)
 - [AllOfUpdateSnapshotResponseLinks](docs/AllOfUpdateSnapshotResponseLinks.md)
 - [AllOfUpdateTagResponseLinks](docs/AllOfUpdateTagResponseLinks.md)
 - [AllOfUpdateUserResponseLinks](docs/AllOfUpdateUserResponseLinks.md)
 - [ApiPermissionsResponse](docs/ApiPermissionsResponse.md)
 - [AssignmentAuditResponse](docs/AssignmentAuditResponse.md)
 - [AssignmentResponse](docs/AssignmentResponse.md)
 - [CancelInstanceResponse](docs/CancelInstanceResponse.md)
 - [CancelInstanceResponseData](docs/CancelInstanceResponseData.md)
 - [ClientResponse](docs/ClientResponse.md)
 - [ClientSecretResponse](docs/ClientSecretResponse.md)
 - [CreateAssignmentResponse](docs/CreateAssignmentResponse.md)
 - [CreateCustomImageRequest](docs/CreateCustomImageRequest.md)
 - [CreateCustomImageResponse](docs/CreateCustomImageResponse.md)
 - [CreateCustomImageResponseData](docs/CreateCustomImageResponseData.md)
 - [CreateInstanceRequest](docs/CreateInstanceRequest.md)
 - [CreateInstanceResponse](docs/CreateInstanceResponse.md)
 - [CreateInstanceResponseData](docs/CreateInstanceResponseData.md)
 - [CreateRoleRequest](docs/CreateRoleRequest.md)
 - [CreateRoleResponse](docs/CreateRoleResponse.md)
 - [CreateRoleResponseData](docs/CreateRoleResponseData.md)
 - [CreateSecretRequest](docs/CreateSecretRequest.md)
 - [CreateSecretResponse](docs/CreateSecretResponse.md)
 - [CreateSnapshotRequest](docs/CreateSnapshotRequest.md)
 - [CreateSnapshotResponse](docs/CreateSnapshotResponse.md)
 - [CreateSnapshotResponseData](docs/CreateSnapshotResponseData.md)
 - [CreateTagRequest](docs/CreateTagRequest.md)
 - [CreateTagResponse](docs/CreateTagResponse.md)
 - [CreateTagResponseData](docs/CreateTagResponseData.md)
 - [CreateUserRequest](docs/CreateUserRequest.md)
 - [CreateUserResponse](docs/CreateUserResponse.md)
 - [CreateUserResponseData](docs/CreateUserResponseData.md)
 - [CustomImagesStatsResponse](docs/CustomImagesStatsResponse.md)
 - [CustomImagesStatsResponseData](docs/CustomImagesStatsResponseData.md)
 - [FindAssignmentResponse](docs/FindAssignmentResponse.md)
 - [FindClientResponse](docs/FindClientResponse.md)
 - [FindImageResponse](docs/FindImageResponse.md)
 - [FindInstanceResponse](docs/FindInstanceResponse.md)
 - [FindRoleResponse](docs/FindRoleResponse.md)
 - [FindSecretResponse](docs/FindSecretResponse.md)
 - [FindSnapshotResponse](docs/FindSnapshotResponse.md)
 - [FindTagResponse](docs/FindTagResponse.md)
 - [FindUserIsPasswordSetResponse](docs/FindUserIsPasswordSetResponse.md)
 - [FindUserResponse](docs/FindUserResponse.md)
 - [GenerateClientSecretResponse](docs/GenerateClientSecretResponse.md)
 - [ImageAuditResponse](docs/ImageAuditResponse.md)
 - [ImageAuditResponseData](docs/ImageAuditResponseData.md)
 - [ImageResponse](docs/ImageResponse.md)
 - [InstanceResponse](docs/InstanceResponse.md)
 - [InstanceRestartActionResponse](docs/InstanceRestartActionResponse.md)
 - [InstanceRestartActionResponseData](docs/InstanceRestartActionResponseData.md)
 - [InstanceStartActionResponse](docs/InstanceStartActionResponse.md)
 - [InstanceStartActionResponseData](docs/InstanceStartActionResponseData.md)
 - [InstanceStatus](docs/InstanceStatus.md)
 - [InstanceStopActionResponse](docs/InstanceStopActionResponse.md)
 - [InstanceStopActionResponseData](docs/InstanceStopActionResponseData.md)
 - [InstancesActionsAuditResponse](docs/InstancesActionsAuditResponse.md)
 - [InstancesAuditResponse](docs/InstancesAuditResponse.md)
 - [IpConfig](docs/IpConfig.md)
 - [IpV4](docs/IpV4.md)
 - [IpV6](docs/IpV6.md)
 - [Links](docs/Links.md)
 - [ListApiPermissionResponse](docs/ListApiPermissionResponse.md)
 - [ListAssignmentAuditsResponse](docs/ListAssignmentAuditsResponse.md)
 - [ListAssignmentResponse](docs/ListAssignmentResponse.md)
 - [ListImageResponse](docs/ListImageResponse.md)
 - [ListImageResponseData](docs/ListImageResponseData.md)
 - [ListInstancesActionsAuditResponse](docs/ListInstancesActionsAuditResponse.md)
 - [ListInstancesAuditResponse](docs/ListInstancesAuditResponse.md)
 - [ListInstancesResponse](docs/ListInstancesResponse.md)
 - [ListInstancesResponseData](docs/ListInstancesResponseData.md)
 - [ListRoleAuditResponse](docs/ListRoleAuditResponse.md)
 - [ListRoleResponse](docs/ListRoleResponse.md)
 - [ListSecretAuditResponse](docs/ListSecretAuditResponse.md)
 - [ListSecretResponse](docs/ListSecretResponse.md)
 - [ListSnapshotResponse](docs/ListSnapshotResponse.md)
 - [ListSnapshotsAuditResponse](docs/ListSnapshotsAuditResponse.md)
 - [ListTagAuditsResponse](docs/ListTagAuditsResponse.md)
 - [ListTagResponse](docs/ListTagResponse.md)
 - [ListUserAuditResponse](docs/ListUserAuditResponse.md)
 - [ListUserResponse](docs/ListUserResponse.md)
 - [PaginationMeta](docs/PaginationMeta.md)
 - [PermissionRequest](docs/PermissionRequest.md)
 - [PermissionResponse](docs/PermissionResponse.md)
 - [ReinstallInstanceRequest](docs/ReinstallInstanceRequest.md)
 - [ReinstallInstanceResponse](docs/ReinstallInstanceResponse.md)
 - [ReinstallInstanceResponseData](docs/ReinstallInstanceResponseData.md)
 - [ResourcePermissionsResponse](docs/ResourcePermissionsResponse.md)
 - [RoleAuditResponse](docs/RoleAuditResponse.md)
 - [RoleResponse](docs/RoleResponse.md)
 - [RollbackSnapshotResponse](docs/RollbackSnapshotResponse.md)
 - [SecretAuditResponse](docs/SecretAuditResponse.md)
 - [SecretResponse](docs/SecretResponse.md)
 - [SelfLinks](docs/SelfLinks.md)
 - [SnapshotResponse](docs/SnapshotResponse.md)
 - [SnapshotsAuditResponse](docs/SnapshotsAuditResponse.md)
 - [TagAssignmentSelfLinks](docs/TagAssignmentSelfLinks.md)
 - [TagAuditResponse](docs/TagAuditResponse.md)
 - [TagResponse](docs/TagResponse.md)
 - [TagResponse1](docs/TagResponse1.md)
 - [UpdateCustomImageRequest](docs/UpdateCustomImageRequest.md)
 - [UpdateCustomImageResponse](docs/UpdateCustomImageResponse.md)
 - [UpdateCustomImageResponseData](docs/UpdateCustomImageResponseData.md)
 - [UpdateRoleRequest](docs/UpdateRoleRequest.md)
 - [UpdateRoleResponse](docs/UpdateRoleResponse.md)
 - [UpdateSecretRequest](docs/UpdateSecretRequest.md)
 - [UpdateSecretResponse](docs/UpdateSecretResponse.md)
 - [UpdateSnapshotRequest](docs/UpdateSnapshotRequest.md)
 - [UpdateSnapshotResponse](docs/UpdateSnapshotResponse.md)
 - [UpdateTagRequest](docs/UpdateTagRequest.md)
 - [UpdateTagResponse](docs/UpdateTagResponse.md)
 - [UpdateUserRequest](docs/UpdateUserRequest.md)
 - [UpdateUserResponse](docs/UpdateUserResponse.md)
 - [UserAuditResponse](docs/UserAuditResponse.md)
 - [UserIsPasswordSetResponse](docs/UserIsPasswordSetResponse.md)
 - [UserResponse](docs/UserResponse.md)

## Documentation For Authorization


## bearer



## Author

support@contabo.com
