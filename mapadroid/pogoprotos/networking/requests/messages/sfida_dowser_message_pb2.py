# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/sfida_dowser_message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/sfida_dowser_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\nBpogoprotos/networking/requests/messages/sfida_dowser_message.proto\x12\'pogoprotos.networking.requests.messages\"*\n\x12SfidaDowserMessage\x12\x14\n\x0c\x65ncounter_id\x18\x01 \x01(\x03\x62\x06proto3'
)




_SFIDADOWSERMESSAGE = _descriptor.Descriptor(
  name='SfidaDowserMessage',
  full_name='pogoprotos.networking.requests.messages.SfidaDowserMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='encounter_id', full_name='pogoprotos.networking.requests.messages.SfidaDowserMessage.encounter_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=111,
  serialized_end=153,
)

DESCRIPTOR.message_types_by_name['SfidaDowserMessage'] = _SFIDADOWSERMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SfidaDowserMessage = _reflection.GeneratedProtocolMessageType('SfidaDowserMessage', (_message.Message,), {
  'DESCRIPTOR' : _SFIDADOWSERMESSAGE,
  '__module__' : 'pogoprotos.networking.requests.messages.sfida_dowser_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.SfidaDowserMessage)
  })
_sym_db.RegisterMessage(SfidaDowserMessage)


# @@protoc_insertion_point(module_scope)
