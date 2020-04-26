# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/social/responses/remove_friend_response.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/social/responses/remove_friend_response.proto',
  package='pogoprotos.networking.social.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\nCpogoprotos/networking/social/responses/remove_friend_response.proto\x12&pogoprotos.networking.social.responses\"\xd5\x01\n\x14RemoveFriendResponse\x12S\n\x06result\x18\x01 \x01(\x0e\x32\x43.pogoprotos.networking.social.responses.RemoveFriendResponse.Result\"h\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\'\n#ERROR_PLAYER_DOES_NOT_EXIST_DELETED\x10\x02\x12\x1d\n\x19\x45RROR_PLAYER_NOT_A_FRIEND\x10\x03\x62\x06proto3'
)



_REMOVEFRIENDRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.social.responses.RemoveFriendResponse.Result',
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
      name='ERROR_PLAYER_DOES_NOT_EXIST_DELETED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_NOT_A_FRIEND', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=221,
  serialized_end=325,
)
_sym_db.RegisterEnumDescriptor(_REMOVEFRIENDRESPONSE_RESULT)


_REMOVEFRIENDRESPONSE = _descriptor.Descriptor(
  name='RemoveFriendResponse',
  full_name='pogoprotos.networking.social.responses.RemoveFriendResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.social.responses.RemoveFriendResponse.result', index=0,
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
    _REMOVEFRIENDRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=325,
)

_REMOVEFRIENDRESPONSE.fields_by_name['result'].enum_type = _REMOVEFRIENDRESPONSE_RESULT
_REMOVEFRIENDRESPONSE_RESULT.containing_type = _REMOVEFRIENDRESPONSE
DESCRIPTOR.message_types_by_name['RemoveFriendResponse'] = _REMOVEFRIENDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RemoveFriendResponse = _reflection.GeneratedProtocolMessageType('RemoveFriendResponse', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEFRIENDRESPONSE,
  '__module__' : 'pogoprotos.networking.social.responses.remove_friend_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.social.responses.RemoveFriendResponse)
  })
_sym_db.RegisterMessage(RemoveFriendResponse)


# @@protoc_insertion_point(module_scope)
