# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/join_buddy_multiplayer_session_message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/join_buddy_multiplayer_session_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\nTpogoprotos/networking/requests/messages/join_buddy_multiplayer_session_message.proto\x12\'pogoprotos.networking.requests.messages\"=\n\"JoinBuddyMultiplayerSessionMessage\x12\x17\n\x0fplfe_session_id\x18\x01 \x01(\tb\x06proto3'
)




_JOINBUDDYMULTIPLAYERSESSIONMESSAGE = _descriptor.Descriptor(
  name='JoinBuddyMultiplayerSessionMessage',
  full_name='pogoprotos.networking.requests.messages.JoinBuddyMultiplayerSessionMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='plfe_session_id', full_name='pogoprotos.networking.requests.messages.JoinBuddyMultiplayerSessionMessage.plfe_session_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=129,
  serialized_end=190,
)

DESCRIPTOR.message_types_by_name['JoinBuddyMultiplayerSessionMessage'] = _JOINBUDDYMULTIPLAYERSESSIONMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

JoinBuddyMultiplayerSessionMessage = _reflection.GeneratedProtocolMessageType('JoinBuddyMultiplayerSessionMessage', (_message.Message,), {
  'DESCRIPTOR' : _JOINBUDDYMULTIPLAYERSESSIONMESSAGE,
  '__module__' : 'pogoprotos.networking.requests.messages.join_buddy_multiplayer_session_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.JoinBuddyMultiplayerSessionMessage)
  })
_sym_db.RegisterMessage(JoinBuddyMultiplayerSessionMessage)


# @@protoc_insertion_point(module_scope)
