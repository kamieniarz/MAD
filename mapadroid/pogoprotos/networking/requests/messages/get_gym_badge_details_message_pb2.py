# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/get_gym_badge_details_message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/get_gym_badge_details_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\nKpogoprotos/networking/requests/messages/get_gym_badge_details_message.proto\x12\'pogoprotos.networking.requests.messages\"Q\n\x19GetGymBadgeDetailsMessage\x12\x0f\n\x07\x66ort_id\x18\x01 \x01(\t\x12\x10\n\x08latitude\x18\x02 \x01(\x01\x12\x11\n\tlongitude\x18\x03 \x01(\x01\x62\x06proto3'
)




_GETGYMBADGEDETAILSMESSAGE = _descriptor.Descriptor(
  name='GetGymBadgeDetailsMessage',
  full_name='pogoprotos.networking.requests.messages.GetGymBadgeDetailsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fort_id', full_name='pogoprotos.networking.requests.messages.GetGymBadgeDetailsMessage.fort_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='pogoprotos.networking.requests.messages.GetGymBadgeDetailsMessage.latitude', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='pogoprotos.networking.requests.messages.GetGymBadgeDetailsMessage.longitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=120,
  serialized_end=201,
)

DESCRIPTOR.message_types_by_name['GetGymBadgeDetailsMessage'] = _GETGYMBADGEDETAILSMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetGymBadgeDetailsMessage = _reflection.GeneratedProtocolMessageType('GetGymBadgeDetailsMessage', (_message.Message,), {
  'DESCRIPTOR' : _GETGYMBADGEDETAILSMESSAGE,
  '__module__' : 'pogoprotos.networking.requests.messages.get_gym_badge_details_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.GetGymBadgeDetailsMessage)
  })
_sym_db.RegisterMessage(GetGymBadgeDetailsMessage)


# @@protoc_insertion_point(module_scope)
