# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/raid_level.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/raid_level.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n!pogoprotos/enums/raid_level.proto\x12\x10pogoprotos.enums*{\n\tRaidLevel\x12\x14\n\x10RAID_LEVEL_UNSET\x10\x00\x12\x10\n\x0cRAID_LEVEL_1\x10\x01\x12\x10\n\x0cRAID_LEVEL_2\x10\x02\x12\x10\n\x0cRAID_LEVEL_3\x10\x03\x12\x10\n\x0cRAID_LEVEL_4\x10\x04\x12\x10\n\x0cRAID_LEVEL_5\x10\x05\x62\x06proto3'
)

_RAIDLEVEL = _descriptor.EnumDescriptor(
  name='RaidLevel',
  full_name='pogoprotos.enums.RaidLevel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RAID_LEVEL_UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RAID_LEVEL_1', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RAID_LEVEL_2', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RAID_LEVEL_3', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RAID_LEVEL_4', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RAID_LEVEL_5', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=55,
  serialized_end=178,
)
_sym_db.RegisterEnumDescriptor(_RAIDLEVEL)

RaidLevel = enum_type_wrapper.EnumTypeWrapper(_RAIDLEVEL)
RAID_LEVEL_UNSET = 0
RAID_LEVEL_1 = 1
RAID_LEVEL_2 = 2
RAID_LEVEL_3 = 3
RAID_LEVEL_4 = 4
RAID_LEVEL_5 = 5


DESCRIPTOR.enum_types_by_name['RaidLevel'] = _RAIDLEVEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
