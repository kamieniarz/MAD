# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/buddy_global_settings.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/buddy_global_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n/pogoprotos/settings/buddy_global_settings.proto\x12\x13pogoprotos.settings\"\xd4\x04\n\x13\x42uddyGlobalSettings\x12!\n\x19\x62uddy_v2_min_player_level\x18\x01 \x01(\x05\x12*\n\"buddy_multiplayer_min_player_level\x18\x02 \x01(\x05\x12\x18\n\x10\x65nable_monodepth\x18\x03 \x01(\x08\x12\x19\n\x11monodepth_devices\x18\x04 \x03(\t\x12(\n lobby_status_message_duration_ms\x18\x05 \x01(\x05\x12\'\n\x1fmapping_instruction_duration_ms\x18\x06 \x01(\x05\x12/\n\'group_photo_leader_tracking_interval_ms\x18\x07 \x01(\x05\x12 \n\x18group_photo_countdown_ms\x18\x08 \x01(\x05\x12\x18\n\x10lobby_timeout_ms\x18\t \x01(\x05\x12 \n\x18\x65nable_wallaby_telemetry\x18\n \x01(\x08\x12\x1f\n\x17mapping_hint_timeout_ms\x18\x0b \x01(\x05\x12&\n\x1egroup_photo_simultaneous_shots\x18\x0c \x01(\x05\x12 \n\x18plfe_auth_tokens_enabled\x18\r \x01(\x08\x12$\n\x1cgroup_photo_shot_interval_ms\x18\x0e \x01(\x05\x12\x19\n\x11\x61rbe_endpoint_url\x18\x0f \x01(\t\x12+\n#buddy_on_map_required_to_open_gifts\x18\x10 \x01(\x08\x62\x06proto3'
)




_BUDDYGLOBALSETTINGS = _descriptor.Descriptor(
  name='BuddyGlobalSettings',
  full_name='pogoprotos.settings.BuddyGlobalSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='buddy_v2_min_player_level', full_name='pogoprotos.settings.BuddyGlobalSettings.buddy_v2_min_player_level', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buddy_multiplayer_min_player_level', full_name='pogoprotos.settings.BuddyGlobalSettings.buddy_multiplayer_min_player_level', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_monodepth', full_name='pogoprotos.settings.BuddyGlobalSettings.enable_monodepth', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='monodepth_devices', full_name='pogoprotos.settings.BuddyGlobalSettings.monodepth_devices', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lobby_status_message_duration_ms', full_name='pogoprotos.settings.BuddyGlobalSettings.lobby_status_message_duration_ms', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mapping_instruction_duration_ms', full_name='pogoprotos.settings.BuddyGlobalSettings.mapping_instruction_duration_ms', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='group_photo_leader_tracking_interval_ms', full_name='pogoprotos.settings.BuddyGlobalSettings.group_photo_leader_tracking_interval_ms', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='group_photo_countdown_ms', full_name='pogoprotos.settings.BuddyGlobalSettings.group_photo_countdown_ms', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lobby_timeout_ms', full_name='pogoprotos.settings.BuddyGlobalSettings.lobby_timeout_ms', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_wallaby_telemetry', full_name='pogoprotos.settings.BuddyGlobalSettings.enable_wallaby_telemetry', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mapping_hint_timeout_ms', full_name='pogoprotos.settings.BuddyGlobalSettings.mapping_hint_timeout_ms', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='group_photo_simultaneous_shots', full_name='pogoprotos.settings.BuddyGlobalSettings.group_photo_simultaneous_shots', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='plfe_auth_tokens_enabled', full_name='pogoprotos.settings.BuddyGlobalSettings.plfe_auth_tokens_enabled', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='group_photo_shot_interval_ms', full_name='pogoprotos.settings.BuddyGlobalSettings.group_photo_shot_interval_ms', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arbe_endpoint_url', full_name='pogoprotos.settings.BuddyGlobalSettings.arbe_endpoint_url', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buddy_on_map_required_to_open_gifts', full_name='pogoprotos.settings.BuddyGlobalSettings.buddy_on_map_required_to_open_gifts', index=15,
      number=16, type=8, cpp_type=7, label=1,
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
  serialized_start=73,
  serialized_end=669,
)

DESCRIPTOR.message_types_by_name['BuddyGlobalSettings'] = _BUDDYGLOBALSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BuddyGlobalSettings = _reflection.GeneratedProtocolMessageType('BuddyGlobalSettings', (_message.Message,), {
  'DESCRIPTOR' : _BUDDYGLOBALSETTINGS,
  '__module__' : 'pogoprotos.settings.buddy_global_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.BuddyGlobalSettings)
  })
_sym_db.RegisterMessage(BuddyGlobalSettings)


# @@protoc_insertion_point(module_scope)
