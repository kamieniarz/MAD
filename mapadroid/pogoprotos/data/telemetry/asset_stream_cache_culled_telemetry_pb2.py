# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/asset_stream_cache_culled_telemetry.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import telemetry_ids_pb2 as pogoprotos_dot_enums_dot_telemetry__ids__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/asset_stream_cache_culled_telemetry.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\nCpogoprotos/data/telemetry/asset_stream_cache_culled_telemetry.proto\x12\x19pogoprotos.data.telemetry\x1a$pogoprotos/enums/telemetry_ids.proto\"v\n\x1f\x41ssetStreamCacheCulledTelemetry\x12;\n\x0e\x61sset_event_id\x18\x01 \x01(\x0e\x32#.pogoprotos.enums.AssetTelemetryIds\x12\x16\n\x0espace_released\x18\x02 \x01(\rb\x06proto3'
  ,
  dependencies=[pogoprotos_dot_enums_dot_telemetry__ids__pb2.DESCRIPTOR,])




_ASSETSTREAMCACHECULLEDTELEMETRY = _descriptor.Descriptor(
  name='AssetStreamCacheCulledTelemetry',
  full_name='pogoprotos.data.telemetry.AssetStreamCacheCulledTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='asset_event_id', full_name='pogoprotos.data.telemetry.AssetStreamCacheCulledTelemetry.asset_event_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='space_released', full_name='pogoprotos.data.telemetry.AssetStreamCacheCulledTelemetry.space_released', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=136,
  serialized_end=254,
)

_ASSETSTREAMCACHECULLEDTELEMETRY.fields_by_name['asset_event_id'].enum_type = pogoprotos_dot_enums_dot_telemetry__ids__pb2._ASSETTELEMETRYIDS
DESCRIPTOR.message_types_by_name['AssetStreamCacheCulledTelemetry'] = _ASSETSTREAMCACHECULLEDTELEMETRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AssetStreamCacheCulledTelemetry = _reflection.GeneratedProtocolMessageType('AssetStreamCacheCulledTelemetry', (_message.Message,), {
  'DESCRIPTOR' : _ASSETSTREAMCACHECULLEDTELEMETRY,
  '__module__' : 'pogoprotos.data.telemetry.asset_stream_cache_culled_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.AssetStreamCacheCulledTelemetry)
  })
_sym_db.RegisterMessage(AssetStreamCacheCulledTelemetry)


# @@protoc_insertion_point(module_scope)
