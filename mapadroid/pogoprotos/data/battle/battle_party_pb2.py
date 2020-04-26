# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/battle/battle_party.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/battle/battle_party.proto',
  package='pogoprotos.data.battle',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n)pogoprotos/data/battle/battle_party.proto\x12\x16pogoprotos.data.battle\"W\n\x0b\x42\x61ttleParty\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bteam_number\x18\x02 \x01(\x05\x12\x0b\n\x03ids\x18\x03 \x03(\x06\x12\x18\n\x10\x63ombat_league_id\x18\x04 \x01(\tb\x06proto3'
)




_BATTLEPARTY = _descriptor.Descriptor(
  name='BattleParty',
  full_name='pogoprotos.data.battle.BattleParty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='pogoprotos.data.battle.BattleParty.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='team_number', full_name='pogoprotos.data.battle.BattleParty.team_number', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ids', full_name='pogoprotos.data.battle.BattleParty.ids', index=2,
      number=3, type=6, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='combat_league_id', full_name='pogoprotos.data.battle.BattleParty.combat_league_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=156,
)

DESCRIPTOR.message_types_by_name['BattleParty'] = _BATTLEPARTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BattleParty = _reflection.GeneratedProtocolMessageType('BattleParty', (_message.Message,), {
  'DESCRIPTOR' : _BATTLEPARTY,
  '__module__' : 'pogoprotos.data.battle.battle_party_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.battle.BattleParty)
  })
_sym_db.RegisterMessage(BattleParty)


# @@protoc_insertion_point(module_scope)
