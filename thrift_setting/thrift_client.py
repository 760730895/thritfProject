# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# Author     ：hu_cl
# Date       ：2022/4/28 14:26
# File       : thrift_client.py
# Description： thrift_rpc 客户端
"""
import sys
import json
import Transmit
from ttypes import *
from constants import *
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

if __name__ == '__main__':
    transport = TSocket.TSocket('127.0.0.1', 8000)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = Transmit.Client(protocol)
    # Connect!
    transport.open()

    cmd = 1
    token = '1111-2222-3333-4444'
    data = json.dumps({"name": "zhoujielun"})
    msg = client.invoke(cmd, token, data)
    print(msg)
    transport.close()

    # 执行结果：cmd不匹配
