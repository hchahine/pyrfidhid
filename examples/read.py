# Copyright (c) 2018 charlysan

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


r"""
Example script to read a tag's id

Flow:
    - Try to read a tag within an infinite loop.
    - If a tag is found then beep once and output Customer ID, UID and CRC Sum.

Note: extra check has been added to avoid processing the same tag (CID/UID) more than once in a row.
"""

from rfidhid.core import RfidHid
from time import sleep

def arrayToHexString(self, input):
    return ' '.join([hex(x) for x in input])

try:
    # Try to open RFID device using default vid:pid (ffff:0035)
	rfid = RfidHid()
except Exception as e:
	print(e)
	exit()

id_temp = None

while True:
    payload_response = rfid.readTag()
    if payload_response.hasIdData():
        id = payload_response.getTagUID()
        # Avoid processing the same tag (CID/UID) more than once in a row
        if id != id_temp:
            id_temp = id
            print('uid: %s' % id)
            print('customer_id: %s' % payload_response.getTagCID())
            print('CRC Sum: %s' % hex(payload_response.getCRCSum()))
            rfid.beep()
    else:
        id_temp = None
    sleep(0.1)
