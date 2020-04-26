# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/get_map_objects_message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/get_map_objects_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\nEpogoprotos/networking/requests/messages/get_map_objects_message.proto\x12\'pogoprotos.networking.requests.messages\"p\n\x14GetMapObjectsMessage\x12\x13\n\x07\x63\x65ll_id\x18\x01 \x03(\x04\x42\x02\x10\x01\x12\x1e\n\x12since_timestamp_ms\x18\x02 \x03(\x03\x42\x02\x10\x01\x12\x10\n\x08latitude\x18\x03 \x01(\x01\x12\x11\n\tlongitude\x18\x04 \x01(\x01\x62\x06proto3'
)




_GETMAPOBJECTSMESSAGE = _descriptor.Descriptor(
  name='GetMapObjectsMessage',
  full_name='pogoprotos.networking.requests.messages.GetMapObjectsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cell_id', full_name='pogoprotos.networking.requests.messages.GetMapObjectsMessage.cell_id', index=0,
      number=1, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='since_timestamp_ms', full_name='pogoprotos.networking.requests.messages.GetMapObjectsMessage.since_timestamp_ms', index=1,
      number=2, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='pogoprotos.networking.requests.messages.GetMapObjectsMessage.latitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='pogoprotos.networking.requests.messages.GetMapObjectsMessage.longitude', index=3,
      number=4, type=1, cpp_type=5, label=1,
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
  serialized_start=114,
  serialized_end=226,
)

DESCRIPTOR.message_types_by_name['GetMapObjectsMessage'] = _GETMAPOBJECTSMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetMapObjectsMessage = _reflection.GeneratedProtocolMessageType('GetMapObjectsMessage', (_message.Message,), {
  'DESCRIPTOR' : _GETMAPOBJECTSMESSAGE,
  '__module__' : 'pogoprotos.networking.requests.messages.get_map_objects_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.GetMapObjectsMessage)
  })
_sym_db.RegisterMessage(GetMapObjectsMessage)


_GETMAPOBJECTSMESSAGE.fields_by_name['cell_id']._options = None
_GETMAPOBJECTSMESSAGE.fields_by_name['since_timestamp_ms']._options = None
# @@protoc_insertion_point(module_scope)
