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


class DatabaseFileInput(Model):
    """Database file specific information for input.

    :param id: Unique identifier for database file
    :type id: str
    :param logical_name: Logical name of the file
    :type logical_name: str
    :param physical_full_name: Operating-system full path of the file
    :type physical_full_name: str
    :param restore_full_name: Suggested full path of the file for restoring
    :type restore_full_name: str
    :param file_type: Database file type. Possible values include: 'Rows',
     'Log', 'Filestream', 'NotSupported', 'Fulltext'
    :type file_type: str or ~azure.mgmt.datamigration.models.DatabaseFileType
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'logical_name': {'key': 'logicalName', 'type': 'str'},
        'physical_full_name': {'key': 'physicalFullName', 'type': 'str'},
        'restore_full_name': {'key': 'restoreFullName', 'type': 'str'},
        'file_type': {'key': 'fileType', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DatabaseFileInput, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.logical_name = kwargs.get('logical_name', None)
        self.physical_full_name = kwargs.get('physical_full_name', None)
        self.restore_full_name = kwargs.get('restore_full_name', None)
        self.file_type = kwargs.get('file_type', None)