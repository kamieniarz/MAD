# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/combat/combat_season_result.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/combat/combat_season_result.proto',
  package='pogoprotos.data.combat',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n1pogoprotos/data/combat/combat_season_result.proto\x12\x16pogoprotos.data.combat\"\xba\x01\n\x12\x43ombatSeasonResult\x12\x0e\n\x06season\x18\x01 \x01(\x05\x12\x0c\n\x04rank\x18\x02 \x01(\x05\x12\x15\n\rtotal_battles\x18\x03 \x01(\x05\x12\x12\n\ntotal_wins\x18\x04 \x01(\x05\x12\x0e\n\x06rating\x18\x05 \x01(\x02\x12\x1a\n\x12longest_win_streak\x18\x06 \x01(\x05\x12\x16\n\x0e\x63urrent_streak\x18\x07 \x01(\x05\x12\x17\n\x0fstardust_earned\x18\x08 \x01(\x03\x62\x06proto3'
)




_COMBATSEASONRESULT = _descriptor.Descriptor(
  name='CombatSeasonResult',
  full_name='pogoprotos.data.combat.CombatSeasonResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='season', full_name='pogoprotos.data.combat.CombatSeasonResult.season', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rank', full_name='pogoprotos.data.combat.CombatSeasonResult.rank', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_battles', full_name='pogoprotos.data.combat.CombatSeasonResult.total_battles', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_wins', full_name='pogoprotos.data.combat.CombatSeasonResult.total_wins', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rating', full_name='pogoprotos.data.combat.CombatSeasonResult.rating', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longest_win_streak', full_name='pogoprotos.data.combat.CombatSeasonResult.longest_win_streak', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_streak', full_name='pogoprotos.data.combat.CombatSeasonResult.current_streak', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stardust_earned', full_name='pogoprotos.data.combat.CombatSeasonResult.stardust_earned', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=78,
  serialized_end=264,
)

DESCRIPTOR.message_types_by_name['CombatSeasonResult'] = _COMBATSEASONRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CombatSeasonResult = _reflection.GeneratedProtocolMessageType('CombatSeasonResult', (_message.Message,), {
  'DESCRIPTOR' : _COMBATSEASONRESULT,
  '__module__' : 'pogoprotos.data.combat.combat_season_result_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.combat.CombatSeasonResult)
  })
_sym_db.RegisterMessage(CombatSeasonResult)


# @@protoc_insertion_point(module_scope)
