# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/map/map_objects_status.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/map/map_objects_status.proto',
  package='pogoprotos.map',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\'pogoprotos/map/map_objects_status.proto\x12\x0epogoprotos.map*P\n\x10MapObjectsStatus\x12\x10\n\x0cUNSET_STATUS\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x12\n\x0eLOCATION_UNSET\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x62\x06proto3'
)

_MAPOBJECTSSTATUS = _descriptor.EnumDescriptor(
  name='MapObjectsStatus',
  full_name='pogoprotos.map.MapObjectsStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET_STATUS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCATION_UNSET', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=59,
  serialized_end=139,
)
_sym_db.RegisterEnumDescriptor(_MAPOBJECTSSTATUS)

MapObjectsStatus = enum_type_wrapper.EnumTypeWrapper(_MAPOBJECTSSTATUS)
UNSET_STATUS = 0
SUCCESS = 1
LOCATION_UNSET = 2
ERROR = 3


DESCRIPTOR.enum_types_by_name['MapObjectsStatus'] = _MAPOBJECTSSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
