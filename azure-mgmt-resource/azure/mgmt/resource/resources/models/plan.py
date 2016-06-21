# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Plan(Model):
    """Plan for the resource.

    :param name: Gets or sets the plan ID.
    :type name: str
    :param publisher: Gets or sets the publisher ID.
    :type publisher: str
    :param product: Gets or sets the offer ID.
    :type product: str
    :param promotion_code: Gets or sets the promotion code.
    :type promotion_code: str
    """ 

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'publisher': {'key': 'publisher', 'type': 'str'},
        'product': {'key': 'product', 'type': 'str'},
        'promotion_code': {'key': 'promotionCode', 'type': 'str'},
    }

    def __init__(self, name=None, publisher=None, product=None, promotion_code=None):
        self.name = name
        self.publisher = publisher
        self.product = product
        self.promotion_code = promotion_code
