# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/adventure_sync_v2_gmt.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/adventure_sync_v2_gmt.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n6pogoprotos/settings/master/adventure_sync_v2_gmt.proto\x12\x1apogoprotos.settings.master\"-\n\x12\x41\x64ventureSyncV2Gmt\x12\x17\n\x0f\x66\x65\x61ture_enabled\x18\x01 \x01(\x08\x62\x06proto3'
)




_ADVENTURESYNCV2GMT = _descriptor.Descriptor(
  name='AdventureSyncV2Gmt',
  full_name='pogoprotos.settings.master.AdventureSyncV2Gmt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_enabled', full_name='pogoprotos.settings.master.AdventureSyncV2Gmt.feature_enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
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
  serialized_start=86,
  serialized_end=131,
)

DESCRIPTOR.message_types_by_name['AdventureSyncV2Gmt'] = _ADVENTURESYNCV2GMT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdventureSyncV2Gmt = _reflection.GeneratedProtocolMessageType('AdventureSyncV2Gmt', (_message.Message,), {
  'DESCRIPTOR' : _ADVENTURESYNCV2GMT,
  '__module__' : 'pogoprotos.settings.master.adventure_sync_v2_gmt_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.AdventureSyncV2Gmt)
  })
_sym_db.RegisterMessage(AdventureSyncV2Gmt)


# @@protoc_insertion_point(module_scope)
