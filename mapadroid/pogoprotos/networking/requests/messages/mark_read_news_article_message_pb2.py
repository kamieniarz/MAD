# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/mark_read_news_article_message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/mark_read_news_article_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\nLpogoprotos/networking/requests/messages/mark_read_news_article_message.proto\x12\'pogoprotos.networking.requests.messages\".\n\x1aMarkReadNewsArticleMessage\x12\x10\n\x08news_ids\x18\x01 \x03(\tb\x06proto3'
)




_MARKREADNEWSARTICLEMESSAGE = _descriptor.Descriptor(
  name='MarkReadNewsArticleMessage',
  full_name='pogoprotos.networking.requests.messages.MarkReadNewsArticleMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='news_ids', full_name='pogoprotos.networking.requests.messages.MarkReadNewsArticleMessage.news_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=121,
  serialized_end=167,
)

DESCRIPTOR.message_types_by_name['MarkReadNewsArticleMessage'] = _MARKREADNEWSARTICLEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MarkReadNewsArticleMessage = _reflection.GeneratedProtocolMessageType('MarkReadNewsArticleMessage', (_message.Message,), {
  'DESCRIPTOR' : _MARKREADNEWSARTICLEMESSAGE,
  '__module__' : 'pogoprotos.networking.requests.messages.mark_read_news_article_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.MarkReadNewsArticleMessage)
  })
_sym_db.RegisterMessage(MarkReadNewsArticleMessage)


# @@protoc_insertion_point(module_scope)
