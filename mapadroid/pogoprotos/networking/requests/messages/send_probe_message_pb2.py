# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/send_probe_message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/send_probe_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n@pogoprotos/networking/requests/messages/send_probe_message.proto\x12\'pogoprotos.networking.requests.messages\"\x12\n\x10SendProbeMessageb\x06proto3'
)




_SENDPROBEMESSAGE = _descriptor.Descriptor(
  name='SendProbeMessage',
  full_name='pogoprotos.networking.requests.messages.SendProbeMessage',
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
  serialized_start=109,
  serialized_end=127,
)

DESCRIPTOR.message_types_by_name['SendProbeMessage'] = _SENDPROBEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SendProbeMessage = _reflection.GeneratedProtocolMessageType('SendProbeMessage', (_message.Message,), {
  'DESCRIPTOR' : _SENDPROBEMESSAGE,
  '__module__' : 'pogoprotos.networking.requests.messages.send_probe_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.SendProbeMessage)
  })
_sym_db.RegisterMessage(SendProbeMessage)


# @@protoc_insertion_point(module_scope)
