# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/game/gamefitness/messages/get_adventure_sync_fitness_report_message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/game/gamefitness/messages/get_adventure_sync_fitness_report_message.proto',
  package='pogoprotos.networking.game.gamefitness.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n_pogoprotos/networking/game/gamefitness/messages/get_adventure_sync_fitness_report_message.proto\x12/pogoprotos.networking.game.gamefitness.messages\"Q\n$GetAdventureSyncFitnessReportMessage\x12\x13\n\x0bnum_of_days\x18\x01 \x01(\x05\x12\x14\n\x0cnum_of_weeks\x18\x02 \x01(\x05\x62\x06proto3'
)




_GETADVENTURESYNCFITNESSREPORTMESSAGE = _descriptor.Descriptor(
  name='GetAdventureSyncFitnessReportMessage',
  full_name='pogoprotos.networking.game.gamefitness.messages.GetAdventureSyncFitnessReportMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_of_days', full_name='pogoprotos.networking.game.gamefitness.messages.GetAdventureSyncFitnessReportMessage.num_of_days', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_of_weeks', full_name='pogoprotos.networking.game.gamefitness.messages.GetAdventureSyncFitnessReportMessage.num_of_weeks', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=148,
  serialized_end=229,
)

DESCRIPTOR.message_types_by_name['GetAdventureSyncFitnessReportMessage'] = _GETADVENTURESYNCFITNESSREPORTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAdventureSyncFitnessReportMessage = _reflection.GeneratedProtocolMessageType('GetAdventureSyncFitnessReportMessage', (_message.Message,), {
  'DESCRIPTOR' : _GETADVENTURESYNCFITNESSREPORTMESSAGE,
  '__module__' : 'pogoprotos.networking.game.gamefitness.messages.get_adventure_sync_fitness_report_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.game.gamefitness.messages.GetAdventureSyncFitnessReportMessage)
  })
_sym_db.RegisterMessage(GetAdventureSyncFitnessReportMessage)


# @@protoc_insertion_point(module_scope)
