# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/central_state.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/central_state.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n$pogoprotos/enums/central_state.proto\x12\x10pogoprotos.enums*|\n\x0c\x43\x65ntralState\x12\x19\n\x15UNKNOWN_CENTRAL_STATE\x10\x00\x12\r\n\tRESETTING\x10\x01\x12\x0f\n\x0bUNSUPPORTED\x10\x02\x12\x10\n\x0cUNAUTHORIZED\x10\x03\x12\x0f\n\x0bPOWERED_OFF\x10\x04\x12\x0e\n\nPOWERED_ON\x10\x05\x62\x06proto3'
)

_CENTRALSTATE = _descriptor.EnumDescriptor(
  name='CentralState',
  full_name='pogoprotos.enums.CentralState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_CENTRAL_STATE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESETTING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSUPPORTED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNAUTHORIZED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POWERED_OFF', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POWERED_ON', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=58,
  serialized_end=182,
)
_sym_db.RegisterEnumDescriptor(_CENTRALSTATE)

CentralState = enum_type_wrapper.EnumTypeWrapper(_CENTRALSTATE)
UNKNOWN_CENTRAL_STATE = 0
RESETTING = 1
UNSUPPORTED = 2
UNAUTHORIZED = 3
POWERED_OFF = 4
POWERED_ON = 5


DESCRIPTOR.enum_types_by_name['CentralState'] = _CENTRALSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
