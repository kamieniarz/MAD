# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/map/spawn_point.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/map/spawn_point.proto',
  package='pogoprotos.map',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n pogoprotos/map/spawn_point.proto\x12\x0epogoprotos.map\"1\n\nSpawnPoint\x12\x10\n\x08latitude\x18\x02 \x01(\x01\x12\x11\n\tlongitude\x18\x03 \x01(\x01\x62\x06proto3'
)




_SPAWNPOINT = _descriptor.Descriptor(
  name='SpawnPoint',
  full_name='pogoprotos.map.SpawnPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='pogoprotos.map.SpawnPoint.latitude', index=0,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='pogoprotos.map.SpawnPoint.longitude', index=1,
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
  serialized_start=52,
  serialized_end=101,
)

DESCRIPTOR.message_types_by_name['SpawnPoint'] = _SPAWNPOINT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SpawnPoint = _reflection.GeneratedProtocolMessageType('SpawnPoint', (_message.Message,), {
  'DESCRIPTOR' : _SPAWNPOINT,
  '__module__' : 'pogoprotos.map.spawn_point_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.map.SpawnPoint)
  })
_sym_db.RegisterMessage(SpawnPoint)


# @@protoc_insertion_point(module_scope)
