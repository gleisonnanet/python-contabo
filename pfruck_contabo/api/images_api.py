"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from pfruck_contabo.api_client import ApiClient, Endpoint as _Endpoint
from pfruck_contabo.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from pfruck_contabo.model.create_custom_image_fail_response import CreateCustomImageFailResponse
from pfruck_contabo.model.create_custom_image_request import CreateCustomImageRequest
from pfruck_contabo.model.create_custom_image_response import CreateCustomImageResponse
from pfruck_contabo.model.custom_images_stats_response import CustomImagesStatsResponse
from pfruck_contabo.model.find_image_response import FindImageResponse
from pfruck_contabo.model.list_image_response import ListImageResponse
from pfruck_contabo.model.update_custom_image_request import UpdateCustomImageRequest
from pfruck_contabo.model.update_custom_image_response import UpdateCustomImageResponse


class ImagesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_custom_image_endpoint = _Endpoint(
            settings={
                'response_type': (CreateCustomImageResponse,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/v1/compute/images',
                'operation_id': 'create_custom_image',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_request_id',
                    'create_custom_image_request',
                    'x_trace_id',
                ],
                'required': [
                    'x_request_id',
                    'create_custom_image_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'x_request_id',
                ]
            },
            root_map={
                'validations': {
                    ('x_request_id',): {

                        'regex': {
                            'pattern': r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-5][0-9A-Fa-f]{3}-[089abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_request_id':
                        (str,),
                    'create_custom_image_request':
                        (CreateCustomImageRequest,),
                    'x_trace_id':
                        (str,),
                },
                'attribute_map': {
                    'x_request_id': 'x-request-id',
                    'x_trace_id': 'x-trace-id',
                },
                'location_map': {
                    'x_request_id': 'header',
                    'create_custom_image_request': 'body',
                    'x_trace_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.delete_image_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/v1/compute/images/{imageId}',
                'operation_id': 'delete_image',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_request_id',
                    'image_id',
                    'x_trace_id',
                ],
                'required': [
                    'x_request_id',
                    'image_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'x_request_id',
                ]
            },
            root_map={
                'validations': {
                    ('x_request_id',): {

                        'regex': {
                            'pattern': r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-5][0-9A-Fa-f]{3}-[089abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_request_id':
                        (str,),
                    'image_id':
                        (str,),
                    'x_trace_id':
                        (str,),
                },
                'attribute_map': {
                    'x_request_id': 'x-request-id',
                    'image_id': 'imageId',
                    'x_trace_id': 'x-trace-id',
                },
                'location_map': {
                    'x_request_id': 'header',
                    'image_id': 'path',
                    'x_trace_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client
        )
        self.retrieve_custom_images_stats_endpoint = _Endpoint(
            settings={
                'response_type': (CustomImagesStatsResponse,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/v1/compute/images/stats',
                'operation_id': 'retrieve_custom_images_stats',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_request_id',
                    'x_trace_id',
                ],
                'required': [
                    'x_request_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'x_request_id',
                ]
            },
            root_map={
                'validations': {
                    ('x_request_id',): {

                        'regex': {
                            'pattern': r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-5][0-9A-Fa-f]{3}-[089abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_request_id':
                        (str,),
                    'x_trace_id':
                        (str,),
                },
                'attribute_map': {
                    'x_request_id': 'x-request-id',
                    'x_trace_id': 'x-trace-id',
                },
                'location_map': {
                    'x_request_id': 'header',
                    'x_trace_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.retrieve_image_endpoint = _Endpoint(
            settings={
                'response_type': (FindImageResponse,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/v1/compute/images/{imageId}',
                'operation_id': 'retrieve_image',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_request_id',
                    'image_id',
                    'x_trace_id',
                ],
                'required': [
                    'x_request_id',
                    'image_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'x_request_id',
                ]
            },
            root_map={
                'validations': {
                    ('x_request_id',): {

                        'regex': {
                            'pattern': r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-5][0-9A-Fa-f]{3}-[089abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_request_id':
                        (str,),
                    'image_id':
                        (str,),
                    'x_trace_id':
                        (str,),
                },
                'attribute_map': {
                    'x_request_id': 'x-request-id',
                    'image_id': 'imageId',
                    'x_trace_id': 'x-trace-id',
                },
                'location_map': {
                    'x_request_id': 'header',
                    'image_id': 'path',
                    'x_trace_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.retrieve_image_list_endpoint = _Endpoint(
            settings={
                'response_type': (ListImageResponse,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/v1/compute/images',
                'operation_id': 'retrieve_image_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_request_id',
                    'x_trace_id',
                    'page',
                    'size',
                    'order_by',
                    'name',
                    'standard_image',
                ],
                'required': [
                    'x_request_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'x_request_id',
                ]
            },
            root_map={
                'validations': {
                    ('x_request_id',): {

                        'regex': {
                            'pattern': r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-5][0-9A-Fa-f]{3}-[089abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_request_id':
                        (str,),
                    'x_trace_id':
                        (str,),
                    'page':
                        (int,),
                    'size':
                        (int,),
                    'order_by':
                        ([str],),
                    'name':
                        (str,),
                    'standard_image':
                        (bool,),
                },
                'attribute_map': {
                    'x_request_id': 'x-request-id',
                    'x_trace_id': 'x-trace-id',
                    'page': 'page',
                    'size': 'size',
                    'order_by': 'orderBy',
                    'name': 'name',
                    'standard_image': 'standardImage',
                },
                'location_map': {
                    'x_request_id': 'header',
                    'x_trace_id': 'header',
                    'page': 'query',
                    'size': 'query',
                    'order_by': 'query',
                    'name': 'query',
                    'standard_image': 'query',
                },
                'collection_format_map': {
                    'order_by': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.update_image_endpoint = _Endpoint(
            settings={
                'response_type': (UpdateCustomImageResponse,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/v1/compute/images/{imageId}',
                'operation_id': 'update_image',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_request_id',
                    'image_id',
                    'update_custom_image_request',
                    'x_trace_id',
                ],
                'required': [
                    'x_request_id',
                    'image_id',
                    'update_custom_image_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'x_request_id',
                ]
            },
            root_map={
                'validations': {
                    ('x_request_id',): {

                        'regex': {
                            'pattern': r'^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-5][0-9A-Fa-f]{3}-[089abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_request_id':
                        (str,),
                    'image_id':
                        (str,),
                    'update_custom_image_request':
                        (UpdateCustomImageRequest,),
                    'x_trace_id':
                        (str,),
                },
                'attribute_map': {
                    'x_request_id': 'x-request-id',
                    'image_id': 'imageId',
                    'x_trace_id': 'x-trace-id',
                },
                'location_map': {
                    'x_request_id': 'header',
                    'image_id': 'path',
                    'update_custom_image_request': 'body',
                    'x_trace_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def create_custom_image(
        self,
        x_request_id,
        create_custom_image_request,
        **kwargs
    ):
        """Provide a custom image  # noqa: E501

        In order to provide a custom image please specify an URL from where the image can be directly downloaded. A custom image must be in either `.iso` or `.qcow2` format. Other formats will be rejected. Please note that downloading can take a while depending on network speed resp. bandwidth and size of image. You can check the status by retrieving information about the image via a GET request. Download will be rejected if you have exceeded your limits.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_custom_image(x_request_id, create_custom_image_request, async_req=True)
        >>> result = thread.get()

        Args:
            x_request_id (str): [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
            create_custom_image_request (CreateCustomImageRequest):

        Keyword Args:
            x_trace_id (str): Identifier to trace group of requests.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            CreateCustomImageResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['x_request_id'] = \
            x_request_id
        kwargs['create_custom_image_request'] = \
            create_custom_image_request
        return self.create_custom_image_endpoint.call_with_http_info(**kwargs)

    def delete_image(
        self,
        x_request_id,
        image_id,
        **kwargs
    ):
        """Delete an uploaded custom image by its id  # noqa: E501

        Your are free to delete a previously uploaded custom images at any time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_image(x_request_id, image_id, async_req=True)
        >>> result = thread.get()

        Args:
            x_request_id (str): [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
            image_id (str): The identifier of the image

        Keyword Args:
            x_trace_id (str): Identifier to trace group of requests.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['x_request_id'] = \
            x_request_id
        kwargs['image_id'] = \
            image_id
        return self.delete_image_endpoint.call_with_http_info(**kwargs)

    def retrieve_custom_images_stats(
        self,
        x_request_id,
        **kwargs
    ):
        """List statistics regarding the customer's custom images  # noqa: E501

        List statistics regarding the customer's custom images such as the number of custom images uploaded, used disk space, free available disk space and total available disk space  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.retrieve_custom_images_stats(x_request_id, async_req=True)
        >>> result = thread.get()

        Args:
            x_request_id (str): [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.

        Keyword Args:
            x_trace_id (str): Identifier to trace group of requests.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            CustomImagesStatsResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['x_request_id'] = \
            x_request_id
        return self.retrieve_custom_images_stats_endpoint.call_with_http_info(**kwargs)

    def retrieve_image(
        self,
        x_request_id,
        image_id,
        **kwargs
    ):
        """Get details about a specific image by its id  # noqa: E501

        Get details about a specific image. This could be either a standard or custom image. In case of an custom image you can also check the download status.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.retrieve_image(x_request_id, image_id, async_req=True)
        >>> result = thread.get()

        Args:
            x_request_id (str): [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
            image_id (str): The identifier of the image

        Keyword Args:
            x_trace_id (str): Identifier to trace group of requests.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            FindImageResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['x_request_id'] = \
            x_request_id
        kwargs['image_id'] = \
            image_id
        return self.retrieve_image_endpoint.call_with_http_info(**kwargs)

    def retrieve_image_list(
        self,
        x_request_id,
        **kwargs
    ):
        """List available standard and custom images  # noqa: E501

        List and filter all available standard images provided by [Contabo](https://contabo.com) and your uploaded custom images.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.retrieve_image_list(x_request_id, async_req=True)
        >>> result = thread.get()

        Args:
            x_request_id (str): [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.

        Keyword Args:
            x_trace_id (str): Identifier to trace group of requests.. [optional]
            page (int): Number of page to be fetched.. [optional]
            size (int): Number of elements per page.. [optional]
            order_by ([str]): Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`.. [optional]
            name (str): The name of the image. [optional]
            standard_image (bool): Flag indicating that image is either a standard (true) or a custom image (false). [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ListImageResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['x_request_id'] = \
            x_request_id
        return self.retrieve_image_list_endpoint.call_with_http_info(**kwargs)

    def update_image(
        self,
        x_request_id,
        image_id,
        update_custom_image_request,
        **kwargs
    ):
        """Update custom image name by its id  # noqa: E501

        Update name of the custom image.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_image(x_request_id, image_id, update_custom_image_request, async_req=True)
        >>> result = thread.get()

        Args:
            x_request_id (str): [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually.
            image_id (str): The identifier of the image
            update_custom_image_request (UpdateCustomImageRequest):

        Keyword Args:
            x_trace_id (str): Identifier to trace group of requests.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            UpdateCustomImageResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['x_request_id'] = \
            x_request_id
        kwargs['image_id'] = \
            image_id
        kwargs['update_custom_image_request'] = \
            update_custom_image_request
        return self.update_image_endpoint.call_with_http_info(**kwargs)

