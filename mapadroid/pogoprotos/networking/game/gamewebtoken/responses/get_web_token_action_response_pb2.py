# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/game/gamewebtoken/responses/get_web_token_action_response.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/game/gamewebtoken/responses/get_web_token_action_response.proto',
  package='pogoprotos.networking.game.gamewebtoken.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\nUpogoprotos/networking/game/gamewebtoken/responses/get_web_token_action_response.proto\x12\x31pogoprotos.networking.game.gamewebtoken.responses\"\xcb\x01\n\x19GetWebTokenActionResponse\x12\x63\n\x06status\x18\x01 \x01(\x0e\x32S.pogoprotos.networking.game.gamewebtoken.responses.GetWebTokenActionResponse.Status\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x02 \x01(\t\"3\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x11\n\rERROR_UNKNOWN\x10\x02\x62\x06proto3'
)



_GETWEBTOKENACTIONRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.game.gamewebtoken.responses.GetWebTokenActionResponse.Status',
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
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=293,
  serialized_end=344,
)
_sym_db.RegisterEnumDescriptor(_GETWEBTOKENACTIONRESPONSE_STATUS)


_GETWEBTOKENACTIONRESPONSE = _descriptor.Descriptor(
  name='GetWebTokenActionResponse',
  full_name='pogoprotos.networking.game.gamewebtoken.responses.GetWebTokenActionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.game.gamewebtoken.responses.GetWebTokenActionResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='access_token', full_name='pogoprotos.networking.game.gamewebtoken.responses.GetWebTokenActionResponse.access_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETWEBTOKENACTIONRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=141,
  serialized_end=344,
)

_GETWEBTOKENACTIONRESPONSE.fields_by_name['status'].enum_type = _GETWEBTOKENACTIONRESPONSE_STATUS
_GETWEBTOKENACTIONRESPONSE_STATUS.containing_type = _GETWEBTOKENACTIONRESPONSE
DESCRIPTOR.message_types_by_name['GetWebTokenActionResponse'] = _GETWEBTOKENACTIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetWebTokenActionResponse = _reflection.GeneratedProtocolMessageType('GetWebTokenActionResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETWEBTOKENACTIONRESPONSE,
  '__module__' : 'pogoprotos.networking.game.gamewebtoken.responses.get_web_token_action_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.game.gamewebtoken.responses.GetWebTokenActionResponse)
  })
_sym_db.RegisterMessage(GetWebTokenActionResponse)


# @@protoc_insertion_point(module_scope)
