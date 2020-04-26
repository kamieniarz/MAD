# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/poi_decoration_properties.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/poi_decoration_properties.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n0pogoprotos/enums/poi_decoration_properties.proto\x12\x10pogoprotos.enums*\xd1\x01\n\x17POIDecorationProperties\x12\t\n\x05\x43OLOR\x10\x00\x12\x0c\n\x08POSITION\x10\x01\x12\x08\n\x04SIZE\x10\x02\x12\x08\n\x04TEXT\x10\x03\x12\n\n\x06\x41\x43TIVE\x10\x04\x12\x08\n\x04ICON\x10\x05\x12\x11\n\rSET_RAID_DATA\x10\x06\x12\x19\n\x15NEARBY_CARROT_VISIBLE\x10\x07\x12\x19\n\x15SET_LOWEST_MOTIVATION\x10\x08\x12\x1a\n\x16SET_NPC_CLICKED_ACTION\x10\t\x12\x0e\n\nBEGIN_EXIT\x10\nb\x06proto3'
)

_POIDECORATIONPROPERTIES = _descriptor.EnumDescriptor(
  name='POIDecorationProperties',
  full_name='pogoprotos.enums.POIDecorationProperties',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COLOR', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POSITION', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIZE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEXT', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ICON', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_RAID_DATA', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEARBY_CARROT_VISIBLE', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_LOWEST_MOTIVATION', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_NPC_CLICKED_ACTION', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BEGIN_EXIT', index=10, number=10,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=71,
  serialized_end=280,
)
_sym_db.RegisterEnumDescriptor(_POIDECORATIONPROPERTIES)

POIDecorationProperties = enum_type_wrapper.EnumTypeWrapper(_POIDECORATIONPROPERTIES)
COLOR = 0
POSITION = 1
SIZE = 2
TEXT = 3
ACTIVE = 4
ICON = 5
SET_RAID_DATA = 6
NEARBY_CARROT_VISIBLE = 7
SET_LOWEST_MOTIVATION = 8
SET_NPC_CLICKED_ACTION = 9
BEGIN_EXIT = 10


DESCRIPTOR.enum_types_by_name['POIDecorationProperties'] = _POIDECORATIONPROPERTIES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
