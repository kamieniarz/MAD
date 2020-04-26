# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/social/responses/update_facebook_status_response.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/social/responses/update_facebook_status_response.proto',
  package='pogoprotos.networking.social.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\nLpogoprotos/networking/social/responses/update_facebook_status_response.proto\x12&pogoprotos.networking.social.responses\"\xff\x01\n\x1cUpdateFacebookStatusResponse\x12[\n\x06result\x18\x01 \x01(\x0e\x32K.pogoprotos.networking.social.responses.UpdateFacebookStatusResponse.Result\"\x81\x01\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x11\n\rERROR_UNKNOWN\x10\x02\x12\x1a\n\x16\x45RROR_PLAYER_NOT_FOUND\x10\x03\x12\x16\n\x12\x45RROR_FACEBOOK_API\x10\x04\x12\x18\n\x14\x45RROR_ALREADY_EXISTS\x10\x05\x62\x06proto3'
)



_UPDATEFACEBOOKSTATUSRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.social.responses.UpdateFacebookStatusResponse.Result',
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
      name='ERROR_PLAYER_NOT_FOUND', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_FACEBOOK_API', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_ALREADY_EXISTS', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=247,
  serialized_end=376,
)
_sym_db.RegisterEnumDescriptor(_UPDATEFACEBOOKSTATUSRESPONSE_RESULT)


_UPDATEFACEBOOKSTATUSRESPONSE = _descriptor.Descriptor(
  name='UpdateFacebookStatusResponse',
  full_name='pogoprotos.networking.social.responses.UpdateFacebookStatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.social.responses.UpdateFacebookStatusResponse.result', index=0,
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
    _UPDATEFACEBOOKSTATUSRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=376,
)

_UPDATEFACEBOOKSTATUSRESPONSE.fields_by_name['result'].enum_type = _UPDATEFACEBOOKSTATUSRESPONSE_RESULT
_UPDATEFACEBOOKSTATUSRESPONSE_RESULT.containing_type = _UPDATEFACEBOOKSTATUSRESPONSE
DESCRIPTOR.message_types_by_name['UpdateFacebookStatusResponse'] = _UPDATEFACEBOOKSTATUSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateFacebookStatusResponse = _reflection.GeneratedProtocolMessageType('UpdateFacebookStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEFACEBOOKSTATUSRESPONSE,
  '__module__' : 'pogoprotos.networking.social.responses.update_facebook_status_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.social.responses.UpdateFacebookStatusResponse)
  })
_sym_db.RegisterMessage(UpdateFacebookStatusResponse)


# @@protoc_insertion_point(module_scope)
