# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/background_mode_settings.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/background_mode_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n9pogoprotos/settings/master/background_mode_settings.proto\x12\x1apogoprotos.settings.master\"\xd8\x01\n\x16\x42\x61\x63kgroundModeSettings\x12.\n&weekly_fitness_goal_level1_distance_km\x18\x01 \x01(\x01\x12.\n&weekly_fitness_goal_level2_distance_km\x18\x02 \x01(\x01\x12.\n&weekly_fitness_goal_level3_distance_km\x18\x03 \x01(\x01\x12.\n&weekly_fitness_goal_level4_distance_km\x18\x04 \x01(\x01\x62\x06proto3'
)




_BACKGROUNDMODESETTINGS = _descriptor.Descriptor(
  name='BackgroundModeSettings',
  full_name='pogoprotos.settings.master.BackgroundModeSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='weekly_fitness_goal_level1_distance_km', full_name='pogoprotos.settings.master.BackgroundModeSettings.weekly_fitness_goal_level1_distance_km', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weekly_fitness_goal_level2_distance_km', full_name='pogoprotos.settings.master.BackgroundModeSettings.weekly_fitness_goal_level2_distance_km', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weekly_fitness_goal_level3_distance_km', full_name='pogoprotos.settings.master.BackgroundModeSettings.weekly_fitness_goal_level3_distance_km', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weekly_fitness_goal_level4_distance_km', full_name='pogoprotos.settings.master.BackgroundModeSettings.weekly_fitness_goal_level4_distance_km', index=3,
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
  serialized_start=90,
  serialized_end=306,
)

DESCRIPTOR.message_types_by_name['BackgroundModeSettings'] = _BACKGROUNDMODESETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BackgroundModeSettings = _reflection.GeneratedProtocolMessageType('BackgroundModeSettings', (_message.Message,), {
  'DESCRIPTOR' : _BACKGROUNDMODESETTINGS,
  '__module__' : 'pogoprotos.settings.master.background_mode_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.BackgroundModeSettings)
  })
_sym_db.RegisterMessage(BackgroundModeSettings)


# @@protoc_insertion_point(module_scope)
