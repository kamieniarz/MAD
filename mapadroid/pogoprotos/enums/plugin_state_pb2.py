# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/plugin_state.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/plugin_state.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n#pogoprotos/enums/plugin_state.proto\x12\x10pogoprotos.enums*y\n\x0bPluginState\x12\x18\n\x14UNKNOWN_PLUGIN_STATE\x10\x00\x12\x0f\n\x0bINITIALIZED\x10\x01\x12\x0c\n\x08STARTING\x10\x02\x12\x0b\n\x07STARTED\x10\x03\x12\x0b\n\x07RESUMED\x10\x04\x12\n\n\x06PAUSED\x10\x05\x12\x0b\n\x07STOPPED\x10\x06\x62\x06proto3'
)

_PLUGINSTATE = _descriptor.EnumDescriptor(
  name='PluginState',
  full_name='pogoprotos.enums.PluginState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_PLUGIN_STATE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INITIALIZED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STARTING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STARTED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESUMED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAUSED', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOPPED', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=57,
  serialized_end=178,
)
_sym_db.RegisterEnumDescriptor(_PLUGINSTATE)

PluginState = enum_type_wrapper.EnumTypeWrapper(_PLUGINSTATE)
UNKNOWN_PLUGIN_STATE = 0
INITIALIZED = 1
STARTING = 2
STARTED = 3
RESUMED = 4
PAUSED = 5
STOPPED = 6


DESCRIPTOR.enum_types_by_name['PluginState'] = _PLUGINSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
