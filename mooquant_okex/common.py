# MooQuant BitFinex module
#
# Copyright 2011-2015 Gabriel Martin Becedillas Ruiz
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Modified from MooQuant Bitfinex and Xignite modules

"""
.. moduleauthor:: Mikko Gozalo <mikgozalo@gmail.com>
"""

import mooquant.logger
from mooquant import broker

btc_symbol = "btcusd"
logger = mooquant.logger.getLogger("bitfinex")


class BTCTraits(broker.InstrumentTraits):
    def roundQuantity(self, quantity):
        return round(quantity, 8)
