# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/collect_daily_bonus_response.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/collect_daily_bonus_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\nBpogoprotos/networking/responses/collect_daily_bonus_response.proto\x12\x1fpogoprotos.networking.responses\"\xab\x01\n\x19\x43ollectDailyBonusResponse\x12Q\n\x06result\x18\x01 \x01(\x0e\x32\x41.pogoprotos.networking.responses.CollectDailyBonusResponse.Result\";\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0b\n\x07\x46\x41ILURE\x10\x02\x12\x0c\n\x08TOO_SOON\x10\x03\x62\x06proto3'
)



_COLLECTDAILYBONUSRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.CollectDailyBonusResponse.Result',
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
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=216,
  serialized_end=275,
)
_sym_db.RegisterEnumDescriptor(_COLLECTDAILYBONUSRESPONSE_RESULT)


_COLLECTDAILYBONUSRESPONSE = _descriptor.Descriptor(
  name='CollectDailyBonusResponse',
  full_name='pogoprotos.networking.responses.CollectDailyBonusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.CollectDailyBonusResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COLLECTDAILYBONUSRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=104,
  serialized_end=275,
)

_COLLECTDAILYBONUSRESPONSE.fields_by_name['result'].enum_type = _COLLECTDAILYBONUSRESPONSE_RESULT
_COLLECTDAILYBONUSRESPONSE_RESULT.containing_type = _COLLECTDAILYBONUSRESPONSE
DESCRIPTOR.message_types_by_name['CollectDailyBonusResponse'] = _COLLECTDAILYBONUSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CollectDailyBonusResponse = _reflection.GeneratedProtocolMessageType('CollectDailyBonusResponse', (_message.Message,), {
  'DESCRIPTOR' : _COLLECTDAILYBONUSRESPONSE,
  '__module__' : 'pogoprotos.networking.responses.collect_daily_bonus_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.CollectDailyBonusResponse)
  })
_sym_db.RegisterMessage(CollectDailyBonusResponse)


# @@protoc_insertion_point(module_scope)
