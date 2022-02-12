# coding: utf-8

"""
    Contabo API


    OpenAPI spec version: 1.0.0
    Contact: support@contabo.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pfruck_contabo.api_client import ApiClient


class ImagesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_custom_image(self, body, x_request_id, **kwargs):  # noqa: E501
        """Provide a custom image  # noqa: E501

        In order to provide a custom image please specify an URL from where the image can be directly downloaded. A custom image must be in either `.iso` or `.qcow2` format. Other formats will be rejected. Please note that downloading can take a while depending on network speed resp. bandwidth and size of image. You can check the status by retrieving information about the image via a GET request. Download will be rejected if you have exceeded your limits.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_custom_image(body, x_request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateCustomImageRequest body: (required)
        :param str x_request_id: [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. (required)
        :param str x_trace_id: Identifier to trace group of requests.
        :return: CreateCustomImageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_custom_image_with_http_info(body, x_request_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_custom_image_with_http_info(body, x_request_id, **kwargs)  # noqa: E501
            return data

    def create_custom_image_with_http_info(self, body, x_request_id, **kwargs):  # noqa: E501
        """Provide a custom image  # noqa: E501

        In order to provide a custom image please specify an URL from where the image can be directly downloaded. A custom image must be in either `.iso` or `.qcow2` format. Other formats will be rejected. Please note that downloading can take a while depending on network speed resp. bandwidth and size of image. You can check the status by retrieving information about the image via a GET request. Download will be rejected if you have exceeded your limits.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_custom_image_with_http_info(body, x_request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateCustomImageRequest body: (required)
        :param str x_request_id: [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. (required)
        :param str x_trace_id: Identifier to trace group of requests.
        :return: CreateCustomImageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_request_id', 'x_trace_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_custom_image" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_custom_image`")  # noqa: E501
        # verify the required parameter 'x_request_id' is set
        if ('x_request_id' not in params or
                params['x_request_id'] is None):
            raise ValueError("Missing the required parameter `x_request_id` when calling `create_custom_image`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['x-request-id'] = params['x_request_id']  # noqa: E501
        if 'x_trace_id' in params:
            header_params['x-trace-id'] = params['x_trace_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/compute/images', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateCustomImageResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_image(self, x_request_id, image_id, **kwargs):  # noqa: E501
        """Delete an uploaded custom image by its id  # noqa: E501

        Your are free to delete a previously uploaded custom images at any time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_image(x_request_id, image_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. (required)
        :param str image_id: The identifier of the image (required)
        :param str x_trace_id: Identifier to trace group of requests.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_image_with_http_info(x_request_id, image_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_image_with_http_info(x_request_id, image_id, **kwargs)  # noqa: E501
            return data

    def delete_image_with_http_info(self, x_request_id, image_id, **kwargs):  # noqa: E501
        """Delete an uploaded custom image by its id  # noqa: E501

        Your are free to delete a previously uploaded custom images at any time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_image_with_http_info(x_request_id, image_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. (required)
        :param str image_id: The identifier of the image (required)
        :param str x_trace_id: Identifier to trace group of requests.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_request_id', 'image_id', 'x_trace_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_image" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_request_id' is set
        if ('x_request_id' not in params or
                params['x_request_id'] is None):
            raise ValueError("Missing the required parameter `x_request_id` when calling `delete_image`")  # noqa: E501
        # verify the required parameter 'image_id' is set
        if ('image_id' not in params or
                params['image_id'] is None):
            raise ValueError("Missing the required parameter `image_id` when calling `delete_image`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'image_id' in params:
            path_params['imageId'] = params['image_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['x-request-id'] = params['x_request_id']  # noqa: E501
        if 'x_trace_id' in params:
            header_params['x-trace-id'] = params['x_trace_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/compute/images/{imageId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_custom_images_stats(self, x_request_id, **kwargs):  # noqa: E501
        """List statistics regarding the customer's custom images  # noqa: E501

        List statistics regarding the customer's custom images such as the number of custom images uploaded, used disk space, free available disk space and total available disk space  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_custom_images_stats(x_request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. (required)
        :param str x_trace_id: Identifier to trace group of requests.
        :return: CustomImagesStatsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_custom_images_stats_with_http_info(x_request_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_custom_images_stats_with_http_info(x_request_id, **kwargs)  # noqa: E501
            return data

    def retrieve_custom_images_stats_with_http_info(self, x_request_id, **kwargs):  # noqa: E501
        """List statistics regarding the customer's custom images  # noqa: E501

        List statistics regarding the customer's custom images such as the number of custom images uploaded, used disk space, free available disk space and total available disk space  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_custom_images_stats_with_http_info(x_request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. (required)
        :param str x_trace_id: Identifier to trace group of requests.
        :return: CustomImagesStatsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_request_id', 'x_trace_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_custom_images_stats" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_request_id' is set
        if ('x_request_id' not in params or
                params['x_request_id'] is None):
            raise ValueError("Missing the required parameter `x_request_id` when calling `retrieve_custom_images_stats`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['x-request-id'] = params['x_request_id']  # noqa: E501
        if 'x_trace_id' in params:
            header_params['x-trace-id'] = params['x_trace_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/compute/images/stats', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CustomImagesStatsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_image(self, x_request_id, image_id, **kwargs):  # noqa: E501
        """Get details about a specific image by its id  # noqa: E501

        Get details about a specific image. This could be either a standard or custom image. In case of an custom image you can also check the download status.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_image(x_request_id, image_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. (required)
        :param str image_id: The identifier of the image (required)
        :param str x_trace_id: Identifier to trace group of requests.
        :return: FindImageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_image_with_http_info(x_request_id, image_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_image_with_http_info(x_request_id, image_id, **kwargs)  # noqa: E501
            return data

    def retrieve_image_with_http_info(self, x_request_id, image_id, **kwargs):  # noqa: E501
        """Get details about a specific image by its id  # noqa: E501

        Get details about a specific image. This could be either a standard or custom image. In case of an custom image you can also check the download status.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_image_with_http_info(x_request_id, image_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. (required)
        :param str image_id: The identifier of the image (required)
        :param str x_trace_id: Identifier to trace group of requests.
        :return: FindImageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_request_id', 'image_id', 'x_trace_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_image" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_request_id' is set
        if ('x_request_id' not in params or
                params['x_request_id'] is None):
            raise ValueError("Missing the required parameter `x_request_id` when calling `retrieve_image`")  # noqa: E501
        # verify the required parameter 'image_id' is set
        if ('image_id' not in params or
                params['image_id'] is None):
            raise ValueError("Missing the required parameter `image_id` when calling `retrieve_image`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'image_id' in params:
            path_params['imageId'] = params['image_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['x-request-id'] = params['x_request_id']  # noqa: E501
        if 'x_trace_id' in params:
            header_params['x-trace-id'] = params['x_trace_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/compute/images/{imageId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FindImageResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_image_list(self, x_request_id, **kwargs):  # noqa: E501
        """List available standard and custom images  # noqa: E501

        List and filter all available standard images provided by [Contabo](https://contabo.com) and your uploaded custom images.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_image_list(x_request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. (required)
        :param str x_trace_id: Identifier to trace group of requests.
        :param int page: Number of page to be fetched.
        :param int size: Number of elements per page.
        :param list[str] order_by: Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`.
        :param str name: The name of the image
        :param bool standard_image: Flag indicating that image is either a standard (true) or a custom image (false)
        :return: ListImageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_image_list_with_http_info(x_request_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_image_list_with_http_info(x_request_id, **kwargs)  # noqa: E501
            return data

    def retrieve_image_list_with_http_info(self, x_request_id, **kwargs):  # noqa: E501
        """List available standard and custom images  # noqa: E501

        List and filter all available standard images provided by [Contabo](https://contabo.com) and your uploaded custom images.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_image_list_with_http_info(x_request_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. (required)
        :param str x_trace_id: Identifier to trace group of requests.
        :param int page: Number of page to be fetched.
        :param int size: Number of elements per page.
        :param list[str] order_by: Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`.
        :param str name: The name of the image
        :param bool standard_image: Flag indicating that image is either a standard (true) or a custom image (false)
        :return: ListImageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_request_id', 'x_trace_id', 'page', 'size', 'order_by', 'name', 'standard_image']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_image_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_request_id' is set
        if ('x_request_id' not in params or
                params['x_request_id'] is None):
            raise ValueError("Missing the required parameter `x_request_id` when calling `retrieve_image_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'size' in params:
            query_params.append(('size', params['size']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('orderBy', params['order_by']))  # noqa: E501
            collection_formats['orderBy'] = 'multi'  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'standard_image' in params:
            query_params.append(('standardImage', params['standard_image']))  # noqa: E501

        header_params = {}
        if 'x_request_id' in params:
            header_params['x-request-id'] = params['x_request_id']  # noqa: E501
        if 'x_trace_id' in params:
            header_params['x-trace-id'] = params['x_trace_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/compute/images', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListImageResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_image(self, body, x_request_id, image_id, **kwargs):  # noqa: E501
        """Update custom image name by its id  # noqa: E501

        Update name of the custom image.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_image(body, x_request_id, image_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateCustomImageRequest body: (required)
        :param str x_request_id: [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. (required)
        :param str image_id: The identifier of the image (required)
        :param str x_trace_id: Identifier to trace group of requests.
        :return: UpdateCustomImageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_image_with_http_info(body, x_request_id, image_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_image_with_http_info(body, x_request_id, image_id, **kwargs)  # noqa: E501
            return data

    def update_image_with_http_info(self, body, x_request_id, image_id, **kwargs):  # noqa: E501
        """Update custom image name by its id  # noqa: E501

        Update name of the custom image.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_image_with_http_info(body, x_request_id, image_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateCustomImageRequest body: (required)
        :param str x_request_id: [Uuid4](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)) to identify individual requests for support cases. You can use [uuidgenerator](https://www.uuidgenerator.net/version4) to generate them manually. (required)
        :param str image_id: The identifier of the image (required)
        :param str x_trace_id: Identifier to trace group of requests.
        :return: UpdateCustomImageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_request_id', 'image_id', 'x_trace_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_image" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_image`")  # noqa: E501
        # verify the required parameter 'x_request_id' is set
        if ('x_request_id' not in params or
                params['x_request_id'] is None):
            raise ValueError("Missing the required parameter `x_request_id` when calling `update_image`")  # noqa: E501
        # verify the required parameter 'image_id' is set
        if ('image_id' not in params or
                params['image_id'] is None):
            raise ValueError("Missing the required parameter `image_id` when calling `update_image`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'image_id' in params:
            path_params['imageId'] = params['image_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['x-request-id'] = params['x_request_id']  # noqa: E501
        if 'x_trace_id' in params:
            header_params['x-trace-id'] = params['x_trace_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/v1/compute/images/{imageId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UpdateCustomImageResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
