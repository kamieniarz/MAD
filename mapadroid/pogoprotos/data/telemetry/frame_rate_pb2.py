# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/frame_rate.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.telemetry import platform_metric_data_pb2 as pogoprotos_dot_data_dot_telemetry_dot_platform__metric__data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/frame_rate.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n*pogoprotos/data/telemetry/frame_rate.proto\x12\x19pogoprotos.data.telemetry\x1a\x34pogoprotos/data/telemetry/platform_metric_data.proto\"V\n\tFrameRate\x12I\n\x12sampled_frame_rate\x18\x01 \x01(\x0b\x32-.pogoprotos.data.telemetry.PlatformMetricDatab\x06proto3'
  ,
  dependencies=[pogoprotos_dot_data_dot_telemetry_dot_platform__metric__data__pb2.DESCRIPTOR,])




_FRAMERATE = _descriptor.Descriptor(
  name='FrameRate',
  full_name='pogoprotos.data.telemetry.FrameRate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sampled_frame_rate', full_name='pogoprotos.data.telemetry.FrameRate.sampled_frame_rate', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=127,
  serialized_end=213,
)

_FRAMERATE.fields_by_name['sampled_frame_rate'].message_type = pogoprotos_dot_data_dot_telemetry_dot_platform__metric__data__pb2._PLATFORMMETRICDATA
DESCRIPTOR.message_types_by_name['FrameRate'] = _FRAMERATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FrameRate = _reflection.GeneratedProtocolMessageType('FrameRate', (_message.Message,), {
  'DESCRIPTOR' : _FRAMERATE,
  '__module__' : 'pogoprotos.data.telemetry.frame_rate_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.FrameRate)
  })
_sym_db.RegisterMessage(FrameRate)


# @@protoc_insertion_point(module_scope)
