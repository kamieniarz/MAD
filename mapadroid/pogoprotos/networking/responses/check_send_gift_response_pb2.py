# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/check_send_gift_response.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/check_send_gift_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n>pogoprotos/networking/responses/check_send_gift_response.proto\x12\x1fpogoprotos.networking.responses\"\xa2\x02\n\x15\x43heckSendGiftResponse\x12M\n\x06result\x18\x01 \x01(\x0e\x32=.pogoprotos.networking.responses.CheckSendGiftResponse.Result\"\xb9\x01\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x11\n\rERROR_UNKNOWN\x10\x02\x12\x1f\n\x1b\x45RROR_PLAYER_DOES_NOT_EXIST\x10\x03\x12\x1c\n\x18\x45RROR_GIFT_NOT_AVAILABLE\x10\x04\x12!\n\x1d\x45RROR_GIFT_ALREADY_SENT_TODAY\x10\x05\x12\"\n\x1e\x45RROR_PLAYER_HAS_UNOPENED_GIFT\x10\x06\x62\x06proto3'
)



_CHECKSENDGIFTRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.CheckSendGiftResponse.Result',
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
      name='ERROR_UNKNOWN', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_DOES_NOT_EXIST', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_GIFT_NOT_AVAILABLE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_GIFT_ALREADY_SENT_TODAY', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_HAS_UNOPENED_GIFT', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=205,
  serialized_end=390,
)
_sym_db.RegisterEnumDescriptor(_CHECKSENDGIFTRESPONSE_RESULT)


_CHECKSENDGIFTRESPONSE = _descriptor.Descriptor(
  name='CheckSendGiftResponse',
  full_name='pogoprotos.networking.responses.CheckSendGiftResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.CheckSendGiftResponse.result', index=0,
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
    _CHECKSENDGIFTRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=390,
)

_CHECKSENDGIFTRESPONSE.fields_by_name['result'].enum_type = _CHECKSENDGIFTRESPONSE_RESULT
_CHECKSENDGIFTRESPONSE_RESULT.containing_type = _CHECKSENDGIFTRESPONSE
DESCRIPTOR.message_types_by_name['CheckSendGiftResponse'] = _CHECKSENDGIFTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CheckSendGiftResponse = _reflection.GeneratedProtocolMessageType('CheckSendGiftResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHECKSENDGIFTRESPONSE,
  '__module__' : 'pogoprotos.networking.responses.check_send_gift_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.CheckSendGiftResponse)
  })
_sym_db.RegisterMessage(CheckSendGiftResponse)


# @@protoc_insertion_point(module_scope)
