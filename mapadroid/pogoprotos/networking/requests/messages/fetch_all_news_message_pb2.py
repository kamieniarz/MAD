# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/fetch_all_news_message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/fetch_all_news_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\nDpogoprotos/networking/requests/messages/fetch_all_news_message.proto\x12\'pogoprotos.networking.requests.messages\"\x15\n\x13\x46\x65tchAllNewsMessageb\x06proto3'
)




_FETCHALLNEWSMESSAGE = _descriptor.Descriptor(
  name='FetchAllNewsMessage',
  full_name='pogoprotos.networking.requests.messages.FetchAllNewsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=113,
  serialized_end=134,
)

DESCRIPTOR.message_types_by_name['FetchAllNewsMessage'] = _FETCHALLNEWSMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FetchAllNewsMessage = _reflection.GeneratedProtocolMessageType('FetchAllNewsMessage', (_message.Message,), {
  'DESCRIPTOR' : _FETCHALLNEWSMESSAGE,
  '__module__' : 'pogoprotos.networking.requests.messages.fetch_all_news_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.FetchAllNewsMessage)
  })
_sym_db.RegisterMessage(FetchAllNewsMessage)


# @@protoc_insertion_point(module_scope)
