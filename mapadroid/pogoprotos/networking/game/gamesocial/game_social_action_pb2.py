# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/game/gamesocial/game_social_action.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/game/gamesocial/game_social_action.proto',
  package='pogoprotos.networking.game.gamesocial',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n>pogoprotos/networking/game/gamesocial/game_social_action.proto\x12%pogoprotos.networking.game.gamesocial*u\n\x10GameSocialAction\x12\x1e\n\x1aUNKNOWN_GAME_SOCIAL_ACTION\x10\x00\x12\x19\n\x13PROXY_SOCIAL_ACTION\x10\xf0\xb9&\x12&\n PROXY_SOCIAL_SIDE_CHANNEL_ACTION\x10\xf1\xb9&b\x06proto3'
)

_GAMESOCIALACTION = _descriptor.EnumDescriptor(
  name='GameSocialAction',
  full_name='pogoprotos.networking.game.gamesocial.GameSocialAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_GAME_SOCIAL_ACTION', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROXY_SOCIAL_ACTION', index=1, number=630000,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROXY_SOCIAL_SIDE_CHANNEL_ACTION', index=2, number=630001,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=105,
  serialized_end=222,
)
_sym_db.RegisterEnumDescriptor(_GAMESOCIALACTION)

GameSocialAction = enum_type_wrapper.EnumTypeWrapper(_GAMESOCIALACTION)
UNKNOWN_GAME_SOCIAL_ACTION = 0
PROXY_SOCIAL_ACTION = 630000
PROXY_SOCIAL_SIDE_CHANNEL_ACTION = 630001


DESCRIPTOR.enum_types_by_name['GameSocialAction'] = _GAMESOCIALACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
