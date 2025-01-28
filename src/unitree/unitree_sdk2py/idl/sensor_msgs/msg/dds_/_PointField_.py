"""
  Generated by Eclipse Cyclone DDS idlc Python Backend
  Cyclone DDS IDL version: v0.11.0
  Module: sensor_msgs.msg.dds_
  IDL file: PointField_.idl

"""

from dataclasses import dataclass

import cyclonedds.idl as idl
import cyclonedds.idl.annotations as annotate
import cyclonedds.idl.types as types

# root module import for resolving types
# import sensor_msgs


@dataclass
@annotate.final
@annotate.autoid("sequential")
class PointField_(idl.IdlStruct, typename="sensor_msgs.msg.dds_.PointField_"):
    name: str
    offset: types.uint32
    datatype: types.uint8
    count: types.uint32
