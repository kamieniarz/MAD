# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/background_mode_global_settings.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/background_mode_global_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n9pogoprotos/settings/background_mode_global_settings.proto\x12\x13pogoprotos.settings\"e\n\x1c\x42\x61\x63kgroundModeGlobalSettings\x12 \n\x18min_player_level_fitness\x18\x01 \x01(\r\x12#\n\x1bservice_prompt_timestamp_ms\x18\x02 \x01(\x03\x62\x06proto3'
)




_BACKGROUNDMODEGLOBALSETTINGS = _descriptor.Descriptor(
  name='BackgroundModeGlobalSettings',
  full_name='pogoprotos.settings.BackgroundModeGlobalSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min_player_level_fitness', full_name='pogoprotos.settings.BackgroundModeGlobalSettings.min_player_level_fitness', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_prompt_timestamp_ms', full_name='pogoprotos.settings.BackgroundModeGlobalSettings.service_prompt_timestamp_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=82,
  serialized_end=183,
)

DESCRIPTOR.message_types_by_name['BackgroundModeGlobalSettings'] = _BACKGROUNDMODEGLOBALSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BackgroundModeGlobalSettings = _reflection.GeneratedProtocolMessageType('BackgroundModeGlobalSettings', (_message.Message,), {
  'DESCRIPTOR' : _BACKGROUNDMODEGLOBALSETTINGS,
  '__module__' : 'pogoprotos.settings.background_mode_global_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.BackgroundModeGlobalSettings)
  })
_sym_db.RegisterMessage(BackgroundModeGlobalSettings)


# @@protoc_insertion_point(module_scope)
