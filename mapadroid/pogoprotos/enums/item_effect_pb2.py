# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/item_effect.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/item_effect.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\"pogoprotos/enums/item_effect.proto\x12\x10pogoprotos.enums*\xd8\x04\n\nItemEffect\x12\x14\n\x10ITEM_EFFECT_NONE\x10\x00\x12\x1c\n\x17ITEM_EFFECT_CAP_NO_FLEE\x10\xe8\x07\x12 \n\x1bITEM_EFFECT_CAP_NO_MOVEMENT\x10\xea\x07\x12\x1e\n\x19ITEM_EFFECT_CAP_NO_THREAT\x10\xeb\x07\x12\x1f\n\x1aITEM_EFFECT_CAP_TARGET_MAX\x10\xec\x07\x12 \n\x1bITEM_EFFECT_CAP_TARGET_SLOW\x10\xed\x07\x12!\n\x1cITEM_EFFECT_CAP_CHANCE_NIGHT\x10\xee\x07\x12#\n\x1eITEM_EFFECT_CAP_CHANCE_TRAINER\x10\xef\x07\x12\'\n\"ITEM_EFFECT_CAP_CHANCE_FIRST_THROW\x10\xf0\x07\x12\"\n\x1dITEM_EFFECT_CAP_CHANCE_LEGEND\x10\xf1\x07\x12!\n\x1cITEM_EFFECT_CAP_CHANCE_HEAVY\x10\xf2\x07\x12\"\n\x1dITEM_EFFECT_CAP_CHANCE_REPEAT\x10\xf3\x07\x12\'\n\"ITEM_EFFECT_CAP_CHANCE_MULTI_THROW\x10\xf4\x07\x12\"\n\x1dITEM_EFFECT_CAP_CHANCE_ALWAYS\x10\xf5\x07\x12(\n#ITEM_EFFECT_CAP_CHANCE_SINGLE_THROW\x10\xf6\x07\x12\x1c\n\x17ITEM_EFFECT_CANDY_AWARD\x10\xf7\x07\x12 \n\x1bITEM_EFFECT_FULL_MOTIVATION\x10\xf8\x07\x62\x06proto3'
)

_ITEMEFFECT = _descriptor.EnumDescriptor(
  name='ItemEffect',
  full_name='pogoprotos.enums.ItemEffect',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ITEM_EFFECT_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_EFFECT_CAP_NO_FLEE', index=1, number=1000,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_EFFECT_CAP_NO_MOVEMENT', index=2, number=1002,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_EFFECT_CAP_NO_THREAT', index=3, number=1003,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_EFFECT_CAP_TARGET_MAX', index=4, number=1004,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_EFFECT_CAP_TARGET_SLOW', index=5, number=1005,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_EFFECT_CAP_CHANCE_NIGHT', index=6, number=1006,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_EFFECT_CAP_CHANCE_TRAINER', index=7, number=1007,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_EFFECT_CAP_CHANCE_FIRST_THROW', index=8, number=1008,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_EFFECT_CAP_CHANCE_LEGEND', index=9, number=1009,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_EFFECT_CAP_CHANCE_HEAVY', index=10, number=1010,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_EFFECT_CAP_CHANCE_REPEAT', index=11, number=1011,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_EFFECT_CAP_CHANCE_MULTI_THROW', index=12, number=1012,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_EFFECT_CAP_CHANCE_ALWAYS', index=13, number=1013,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_EFFECT_CAP_CHANCE_SINGLE_THROW', index=14, number=1014,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_EFFECT_CANDY_AWARD', index=15, number=1015,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_EFFECT_FULL_MOTIVATION', index=16, number=1016,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=57,
  serialized_end=657,
)
_sym_db.RegisterEnumDescriptor(_ITEMEFFECT)

ItemEffect = enum_type_wrapper.EnumTypeWrapper(_ITEMEFFECT)
ITEM_EFFECT_NONE = 0
ITEM_EFFECT_CAP_NO_FLEE = 1000
ITEM_EFFECT_CAP_NO_MOVEMENT = 1002
ITEM_EFFECT_CAP_NO_THREAT = 1003
ITEM_EFFECT_CAP_TARGET_MAX = 1004
ITEM_EFFECT_CAP_TARGET_SLOW = 1005
ITEM_EFFECT_CAP_CHANCE_NIGHT = 1006
ITEM_EFFECT_CAP_CHANCE_TRAINER = 1007
ITEM_EFFECT_CAP_CHANCE_FIRST_THROW = 1008
ITEM_EFFECT_CAP_CHANCE_LEGEND = 1009
ITEM_EFFECT_CAP_CHANCE_HEAVY = 1010
ITEM_EFFECT_CAP_CHANCE_REPEAT = 1011
ITEM_EFFECT_CAP_CHANCE_MULTI_THROW = 1012
ITEM_EFFECT_CAP_CHANCE_ALWAYS = 1013
ITEM_EFFECT_CAP_CHANCE_SINGLE_THROW = 1014
ITEM_EFFECT_CANDY_AWARD = 1015
ITEM_EFFECT_FULL_MOTIVATION = 1016


DESCRIPTOR.enum_types_by_name['ItemEffect'] = _ITEMEFFECT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
