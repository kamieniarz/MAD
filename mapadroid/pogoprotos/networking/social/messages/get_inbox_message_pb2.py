# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/social/messages/get_inbox_message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/social/messages/get_inbox_message.proto',
  package='pogoprotos.networking.social.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n=pogoprotos/networking/social/messages/get_inbox_message.proto\x12%pogoprotos.networking.social.messages\"P\n\x0fGetInboxMessage\x12\x12\n\nis_history\x18\x01 \x01(\x08\x12\x12\n\nis_reverse\x18\x02 \x01(\x08\x12\x15\n\rnot_before_ms\x18\x03 \x01(\x03\x62\x06proto3'
)




_GETINBOXMESSAGE = _descriptor.Descriptor(
  name='GetInboxMessage',
  full_name='pogoprotos.networking.social.messages.GetInboxMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_history', full_name='pogoprotos.networking.social.messages.GetInboxMessage.is_history', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_reverse', full_name='pogoprotos.networking.social.messages.GetInboxMessage.is_reverse', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='not_before_ms', full_name='pogoprotos.networking.social.messages.GetInboxMessage.not_before_ms', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=104,
  serialized_end=184,
)

DESCRIPTOR.message_types_by_name['GetInboxMessage'] = _GETINBOXMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetInboxMessage = _reflection.GeneratedProtocolMessageType('GetInboxMessage', (_message.Message,), {
  'DESCRIPTOR' : _GETINBOXMESSAGE,
  '__module__' : 'pogoprotos.networking.social.messages.get_inbox_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.social.messages.GetInboxMessage)
  })
_sym_db.RegisterMessage(GetInboxMessage)


# @@protoc_insertion_point(module_scope)
