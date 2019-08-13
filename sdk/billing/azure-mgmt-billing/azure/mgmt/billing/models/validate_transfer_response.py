# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ValidateTransferResponse(Model):
    """Transfer validation response.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar status: The status of validation
    :vartype status: str
    :param results: Array of validation results.
    :type results: list[~azure.mgmt.billing.models.ValidationResultProperties]
    """

    _validation = {
        'status': {'readonly': True},
    }

    _attribute_map = {
        'status': {'key': 'properties.status', 'type': 'str'},
        'results': {'key': 'properties.results', 'type': '[ValidationResultProperties]'},
    }

    def __init__(self, **kwargs):
        super(ValidateTransferResponse, self).__init__(**kwargs)
        self.status = None
        self.results = kwargs.get('results', None)
