# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/device_service_toggle_telemetry.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import telemetry_ids_pb2 as pogoprotos_dot_enums_dot_telemetry__ids__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/device_service_toggle_telemetry.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n?pogoprotos/data/telemetry/device_service_toggle_telemetry.proto\x12\x19pogoprotos.data.telemetry\x1a$pogoprotos/enums/telemetry_ids.proto\"\x9d\x01\n\x1c\x44\x65viceServiceToggleTelemetry\x12P\n\x1b\x64\x65vice_service_telemetry_id\x18\x01 \x01(\x0e\x32+.pogoprotos.enums.DeviceServiceTelemetryIds\x12\x13\n\x0bwas_enabled\x18\x02 \x01(\x08\x12\x16\n\x0ewas_subsequent\x18\x03 \x01(\x08\x62\x06proto3'
  ,
  dependencies=[pogoprotos_dot_enums_dot_telemetry__ids__pb2.DESCRIPTOR,])




_DEVICESERVICETOGGLETELEMETRY = _descriptor.Descriptor(
  name='DeviceServiceToggleTelemetry',
  full_name='pogoprotos.data.telemetry.DeviceServiceToggleTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_service_telemetry_id', full_name='pogoprotos.data.telemetry.DeviceServiceToggleTelemetry.device_service_telemetry_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='was_enabled', full_name='pogoprotos.data.telemetry.DeviceServiceToggleTelemetry.was_enabled', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='was_subsequent', full_name='pogoprotos.data.telemetry.DeviceServiceToggleTelemetry.was_subsequent', index=2,
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
  serialized_start=133,
  serialized_end=290,
)

_DEVICESERVICETOGGLETELEMETRY.fields_by_name['device_service_telemetry_id'].enum_type = pogoprotos_dot_enums_dot_telemetry__ids__pb2._DEVICESERVICETELEMETRYIDS
DESCRIPTOR.message_types_by_name['DeviceServiceToggleTelemetry'] = _DEVICESERVICETOGGLETELEMETRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeviceServiceToggleTelemetry = _reflection.GeneratedProtocolMessageType('DeviceServiceToggleTelemetry', (_message.Message,), {
  'DESCRIPTOR' : _DEVICESERVICETOGGLETELEMETRY,
  '__module__' : 'pogoprotos.data.telemetry.device_service_toggle_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.DeviceServiceToggleTelemetry)
  })
_sym_db.RegisterMessage(DeviceServiceToggleTelemetry)


# @@protoc_insertion_point(module_scope)
