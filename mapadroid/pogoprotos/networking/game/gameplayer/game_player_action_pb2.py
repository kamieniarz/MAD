# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/game/gameplayer/game_player_action.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/game/gameplayer/game_player_action.proto',
  package='pogoprotos.networking.game.gameplayer',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n>pogoprotos/networking/game/gameplayer/game_player_action.proto\x12%pogoprotos.networking.game.gameplayer*G\n\x10GamePlayerAction\x12\x1e\n\x1aUNKNOWN_GAME_PLAYER_ACTION\x10\x00\x12\x13\n\rGET_INVENTORY\x10\xe0\x98\x17\x62\x06proto3'
)

_GAMEPLAYERACTION = _descriptor.EnumDescriptor(
  name='GamePlayerAction',
  full_name='pogoprotos.networking.game.gameplayer.GamePlayerAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_GAME_PLAYER_ACTION', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_INVENTORY', index=1, number=380000,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=105,
  serialized_end=176,
)
_sym_db.RegisterEnumDescriptor(_GAMEPLAYERACTION)

GamePlayerAction = enum_type_wrapper.EnumTypeWrapper(_GAMEPLAYERACTION)
UNKNOWN_GAME_PLAYER_ACTION = 0
GET_INVENTORY = 380000


DESCRIPTOR.enum_types_by_name['GamePlayerAction'] = _GAMEPLAYERACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
