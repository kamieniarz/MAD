# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/store.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/store.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x1cpogoprotos/enums/store.proto\x12\x10pogoprotos.enums*N\n\x05Store\x12\x0f\n\x0bSTORE_UNSET\x10\x00\x12\x0f\n\x0bSTORE_APPLE\x10\x01\x12\x10\n\x0cSTORE_GOOGLE\x10\x02\x12\x11\n\rSTORE_SAMSUNG\x10\x03\x62\x06proto3'
)

_STORE = _descriptor.EnumDescriptor(
  name='Store',
  full_name='pogoprotos.enums.Store',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STORE_UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STORE_APPLE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STORE_GOOGLE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STORE_SAMSUNG', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=50,
  serialized_end=128,
)
_sym_db.RegisterEnumDescriptor(_STORE)

Store = enum_type_wrapper.EnumTypeWrapper(_STORE)
STORE_UNSET = 0
STORE_APPLE = 1
STORE_GOOGLE = 2
STORE_SAMSUNG = 3


DESCRIPTOR.enum_types_by_name['Store'] = _STORE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
