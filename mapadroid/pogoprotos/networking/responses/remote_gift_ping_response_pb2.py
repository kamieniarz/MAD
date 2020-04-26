# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/remote_gift_ping_response.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/remote_gift_ping_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n?pogoprotos/networking/responses/remote_gift_ping_response.proto\x12\x1fpogoprotos.networking.responses\"\xeb\x01\n\x16RemoteGiftPingResponse\x12N\n\x06result\x18\x01 \x01(\x0e\x32>.pogoprotos.networking.responses.RemoteGiftPingResponse.Result\"\x80\x01\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x16\n\x12STILL_IN_COOL_DOWN\x10\x02\x12\x11\n\rBUDDY_NOT_SET\x10\x03\x12\x18\n\x14\x45RROR_INVENTORY_FULL\x10\x04\x12\x19\n\x15\x45RROR_NO_REMOTE_GIFTS\x10\x05\x62\x06proto3'
)



_REMOTEGIFTPINGRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.RemoteGiftPingResponse.Result',
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
      name='STILL_IN_COOL_DOWN', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_NOT_SET', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVENTORY_FULL', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NO_REMOTE_GIFTS', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=208,
  serialized_end=336,
)
_sym_db.RegisterEnumDescriptor(_REMOTEGIFTPINGRESPONSE_RESULT)


_REMOTEGIFTPINGRESPONSE = _descriptor.Descriptor(
  name='RemoteGiftPingResponse',
  full_name='pogoprotos.networking.responses.RemoteGiftPingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.RemoteGiftPingResponse.result', index=0,
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
    _REMOTEGIFTPINGRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=336,
)

_REMOTEGIFTPINGRESPONSE.fields_by_name['result'].enum_type = _REMOTEGIFTPINGRESPONSE_RESULT
_REMOTEGIFTPINGRESPONSE_RESULT.containing_type = _REMOTEGIFTPINGRESPONSE
DESCRIPTOR.message_types_by_name['RemoteGiftPingResponse'] = _REMOTEGIFTPINGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RemoteGiftPingResponse = _reflection.GeneratedProtocolMessageType('RemoteGiftPingResponse', (_message.Message,), {
  'DESCRIPTOR' : _REMOTEGIFTPINGRESPONSE,
  '__module__' : 'pogoprotos.networking.responses.remote_gift_ping_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.RemoteGiftPingResponse)
  })
_sym_db.RegisterMessage(RemoteGiftPingResponse)


# @@protoc_insertion_point(module_scope)
