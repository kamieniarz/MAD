# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/platform/requests/submit_poi_image_message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/platform/requests/submit_poi_image_message.proto',
  package='pogoprotos.networking.platform.requests',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\nFpogoprotos/networking/platform/requests/submit_poi_image_message.proto\x12\'pogoprotos.networking.platform.requests\"B\n\x15SubmitPoiImageMessage\x12\x0e\n\x06poi_id\x18\x01 \x01(\t\x12\x19\n\x11\x61sync_file_upload\x18\x02 \x01(\x08\x62\x06proto3'
)




_SUBMITPOIIMAGEMESSAGE = _descriptor.Descriptor(
  name='SubmitPoiImageMessage',
  full_name='pogoprotos.networking.platform.requests.SubmitPoiImageMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='poi_id', full_name='pogoprotos.networking.platform.requests.SubmitPoiImageMessage.poi_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='async_file_upload', full_name='pogoprotos.networking.platform.requests.SubmitPoiImageMessage.async_file_upload', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=115,
  serialized_end=181,
)

DESCRIPTOR.message_types_by_name['SubmitPoiImageMessage'] = _SUBMITPOIIMAGEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubmitPoiImageMessage = _reflection.GeneratedProtocolMessageType('SubmitPoiImageMessage', (_message.Message,), {
  'DESCRIPTOR' : _SUBMITPOIIMAGEMESSAGE,
  '__module__' : 'pogoprotos.networking.platform.requests.submit_poi_image_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.requests.SubmitPoiImageMessage)
  })
_sym_db.RegisterMessage(SubmitPoiImageMessage)


# @@protoc_insertion_point(module_scope)
