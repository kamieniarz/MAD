# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/probe_settings.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/probe_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n(pogoprotos/settings/probe_settings.proto\x12\x13pogoprotos.settings\"^\n\rProbeSettings\x12\x1a\n\x12\x65nable_sidechannel\x18\x01 \x01(\x08\x12\x14\n\x0c\x65nable_adhoc\x18\x02 \x01(\x08\x12\x1b\n\x13\x61\x64hoc_frequency_sec\x18\x03 \x01(\x05\x62\x06proto3'
)




_PROBESETTINGS = _descriptor.Descriptor(
  name='ProbeSettings',
  full_name='pogoprotos.settings.ProbeSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enable_sidechannel', full_name='pogoprotos.settings.ProbeSettings.enable_sidechannel', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_adhoc', full_name='pogoprotos.settings.ProbeSettings.enable_adhoc', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adhoc_frequency_sec', full_name='pogoprotos.settings.ProbeSettings.adhoc_frequency_sec', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=65,
  serialized_end=159,
)

DESCRIPTOR.message_types_by_name['ProbeSettings'] = _PROBESETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProbeSettings = _reflection.GeneratedProtocolMessageType('ProbeSettings', (_message.Message,), {
  'DESCRIPTOR' : _PROBESETTINGS,
  '__module__' : 'pogoprotos.settings.probe_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.ProbeSettings)
  })
_sym_db.RegisterMessage(ProbeSettings)


# @@protoc_insertion_point(module_scope)
