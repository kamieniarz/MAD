# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/platform/requests/send_encrypted_signature_message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/platform/requests/send_encrypted_signature_message.proto',
  package='pogoprotos.networking.platform.requests',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\nNpogoprotos/networking/platform/requests/send_encrypted_signature_message.proto\x12\'pogoprotos.networking.platform.requests\"<\n\x1dSendEncryptedSignatureMessage\x12\x1b\n\x13\x65ncrypted_signature\x18\x01 \x01(\x0c\x62\x06proto3'
)




_SENDENCRYPTEDSIGNATUREMESSAGE = _descriptor.Descriptor(
  name='SendEncryptedSignatureMessage',
  full_name='pogoprotos.networking.platform.requests.SendEncryptedSignatureMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='encrypted_signature', full_name='pogoprotos.networking.platform.requests.SendEncryptedSignatureMessage.encrypted_signature', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=123,
  serialized_end=183,
)

DESCRIPTOR.message_types_by_name['SendEncryptedSignatureMessage'] = _SENDENCRYPTEDSIGNATUREMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SendEncryptedSignatureMessage = _reflection.GeneratedProtocolMessageType('SendEncryptedSignatureMessage', (_message.Message,), {
  'DESCRIPTOR' : _SENDENCRYPTEDSIGNATUREMESSAGE,
  '__module__' : 'pogoprotos.networking.platform.requests.send_encrypted_signature_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.requests.SendEncryptedSignatureMessage)
  })
_sym_db.RegisterMessage(SendEncryptedSignatureMessage)


# @@protoc_insertion_point(module_scope)
