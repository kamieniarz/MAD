# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/claim_codename_message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/claim_codename_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\nDpogoprotos/networking/requests/messages/claim_codename_message.proto\x12\'pogoprotos.networking.requests.messages\"]\n\x14\x43laimCodenameMessage\x12\x10\n\x08\x63odename\x18\x01 \x01(\t\x12\r\n\x05\x66orce\x18\x02 \x01(\x08\x12$\n\x1cgenerate_suggested_codenames\x18\x03 \x01(\x08\x62\x06proto3'
)




_CLAIMCODENAMEMESSAGE = _descriptor.Descriptor(
  name='ClaimCodenameMessage',
  full_name='pogoprotos.networking.requests.messages.ClaimCodenameMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='codename', full_name='pogoprotos.networking.requests.messages.ClaimCodenameMessage.codename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='force', full_name='pogoprotos.networking.requests.messages.ClaimCodenameMessage.force', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='generate_suggested_codenames', full_name='pogoprotos.networking.requests.messages.ClaimCodenameMessage.generate_suggested_codenames', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=113,
  serialized_end=206,
)

DESCRIPTOR.message_types_by_name['ClaimCodenameMessage'] = _CLAIMCODENAMEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClaimCodenameMessage = _reflection.GeneratedProtocolMessageType('ClaimCodenameMessage', (_message.Message,), {
  'DESCRIPTOR' : _CLAIMCODENAMEMESSAGE,
  '__module__' : 'pogoprotos.networking.requests.messages.claim_codename_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.ClaimCodenameMessage)
  })
_sym_db.RegisterMessage(ClaimCodenameMessage)


# @@protoc_insertion_point(module_scope)
