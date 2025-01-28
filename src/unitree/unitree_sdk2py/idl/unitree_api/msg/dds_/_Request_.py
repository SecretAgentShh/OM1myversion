"""
  Generated by Eclipse Cyclone DDS idlc Python Backend
  Cyclone DDS IDL version: v0.10.2
  Module: unitree_api.msg.dds_
  IDL file: Request_.idl

"""

from dataclasses import dataclass

import cyclonedds.idl as idl
import cyclonedds.idl.annotations as annotate
import cyclonedds.idl.types as types

# root module import for resolving types
# import unitree_api


@dataclass
@annotate.final
@annotate.autoid("sequential")
class Request_(idl.IdlStruct, typename="unitree_api.msg.dds_.Request_"):
    header: "unitree_sdk2py.idl.unitree_api.msg.dds_.RequestHeader_"
    parameter: str
    binary: types.sequence[types.uint8]
