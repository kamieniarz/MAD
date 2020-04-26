# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/collect_daily_defender_bonus_response.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/collect_daily_defender_bonus_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\nKpogoprotos/networking/responses/collect_daily_defender_bonus_response.proto\x12\x1fpogoprotos.networking.responses\"\x97\x02\n!CollectDailyDefenderBonusResponse\x12Y\n\x06result\x18\x01 \x01(\x0e\x32I.pogoprotos.networking.responses.CollectDailyDefenderBonusResponse.Result\x12\x15\n\rcurrency_type\x18\x02 \x03(\t\x12\x18\n\x10\x63urrency_awarded\x18\x03 \x03(\x05\x12\x17\n\x0f\x64\x65\x66\x65nders_count\x18\x04 \x01(\x05\"M\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0b\n\x07\x46\x41ILURE\x10\x02\x12\x0c\n\x08TOO_SOON\x10\x03\x12\x10\n\x0cNO_DEFENDERS\x10\x04\x62\x06proto3'
)



_COLLECTDAILYDEFENDERBONUSRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.CollectDailyDefenderBonusResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOO_SOON', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_DEFENDERS', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=315,
  serialized_end=392,
)
_sym_db.RegisterEnumDescriptor(_COLLECTDAILYDEFENDERBONUSRESPONSE_RESULT)


_COLLECTDAILYDEFENDERBONUSRESPONSE = _descriptor.Descriptor(
  name='CollectDailyDefenderBonusResponse',
  full_name='pogoprotos.networking.responses.CollectDailyDefenderBonusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.CollectDailyDefenderBonusResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currency_type', full_name='pogoprotos.networking.responses.CollectDailyDefenderBonusResponse.currency_type', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currency_awarded', full_name='pogoprotos.networking.responses.CollectDailyDefenderBonusResponse.currency_awarded', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='defenders_count', full_name='pogoprotos.networking.responses.CollectDailyDefenderBonusResponse.defenders_count', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COLLECTDAILYDEFENDERBONUSRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=392,
)

_COLLECTDAILYDEFENDERBONUSRESPONSE.fields_by_name['result'].enum_type = _COLLECTDAILYDEFENDERBONUSRESPONSE_RESULT
_COLLECTDAILYDEFENDERBONUSRESPONSE_RESULT.containing_type = _COLLECTDAILYDEFENDERBONUSRESPONSE
DESCRIPTOR.message_types_by_name['CollectDailyDefenderBonusResponse'] = _COLLECTDAILYDEFENDERBONUSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CollectDailyDefenderBonusResponse = _reflection.GeneratedProtocolMessageType('CollectDailyDefenderBonusResponse', (_message.Message,), {
  'DESCRIPTOR' : _COLLECTDAILYDEFENDERBONUSRESPONSE,
  '__module__' : 'pogoprotos.networking.responses.collect_daily_defender_bonus_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.CollectDailyDefenderBonusResponse)
  })
_sym_db.RegisterMessage(CollectDailyDefenderBonusResponse)


# @@protoc_insertion_point(module_scope)
