# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/social/responses/send_friend_invite_response.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/social/responses/send_friend_invite_response.proto',
  package='pogoprotos.networking.social.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\nHpogoprotos/networking/social/responses/send_friend_invite_response.proto\x12&pogoprotos.networking.social.responses\"\xdc\x03\n\x18SendFriendInviteResponse\x12W\n\x06result\x18\x01 \x01(\x0e\x32G.pogoprotos.networking.social.responses.SendFriendInviteResponse.Result\"\xe6\x02\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x11\n\rERROR_UNKNOWN\x10\x02\x12\x1a\n\x16\x45RROR_ALREADY_A_FRIEND\x10\x03\x12\'\n#ERROR_PLAYER_DOES_NOT_EXIST_DELETED\x10\x04\x12\x1b\n\x17\x45RROR_PLAYER_INBOX_FULL\x10\x05\x12\x1c\n\x18\x45RROR_PLAYER_OUTBOX_FULL\x10\x06\x12 \n\x1c\x45RROR_SENDER_HAS_MAX_FRIENDS\x10\x07\x12\x1d\n\x19\x45RROR_INVITE_ALREADY_SENT\x10\x08\x12)\n%ERROR_CANNOT_SEND_INVITES_TO_YOURSELF\x10\t\x12!\n\x1d\x45RROR_INVITE_ALREADY_RECEIVED\x10\n\x12\"\n\x1e\x45RROR_RECEIVER_HAS_MAX_FRIENDS\x10\x0b\x62\x06proto3'
)



_SENDFRIENDINVITERESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.social.responses.SendFriendInviteResponse.Result',
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
      name='ERROR_ALREADY_A_FRIEND', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_DOES_NOT_EXIST_DELETED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_INBOX_FULL', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_OUTBOX_FULL', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_SENDER_HAS_MAX_FRIENDS', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVITE_ALREADY_SENT', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_CANNOT_SEND_INVITES_TO_YOURSELF', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVITE_ALREADY_RECEIVED', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_RECEIVER_HAS_MAX_FRIENDS', index=11, number=11,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=235,
  serialized_end=593,
)
_sym_db.RegisterEnumDescriptor(_SENDFRIENDINVITERESPONSE_RESULT)


_SENDFRIENDINVITERESPONSE = _descriptor.Descriptor(
  name='SendFriendInviteResponse',
  full_name='pogoprotos.networking.social.responses.SendFriendInviteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.social.responses.SendFriendInviteResponse.result', index=0,
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
    _SENDFRIENDINVITERESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=593,
)

_SENDFRIENDINVITERESPONSE.fields_by_name['result'].enum_type = _SENDFRIENDINVITERESPONSE_RESULT
_SENDFRIENDINVITERESPONSE_RESULT.containing_type = _SENDFRIENDINVITERESPONSE
DESCRIPTOR.message_types_by_name['SendFriendInviteResponse'] = _SENDFRIENDINVITERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SendFriendInviteResponse = _reflection.GeneratedProtocolMessageType('SendFriendInviteResponse', (_message.Message,), {
  'DESCRIPTOR' : _SENDFRIENDINVITERESPONSE,
  '__module__' : 'pogoprotos.networking.social.responses.send_friend_invite_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.social.responses.SendFriendInviteResponse)
  })
_sym_db.RegisterMessage(SendFriendInviteResponse)


# @@protoc_insertion_point(module_scope)
