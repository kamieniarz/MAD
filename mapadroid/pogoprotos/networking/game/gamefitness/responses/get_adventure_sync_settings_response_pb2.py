# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/game/gamefitness/responses/get_adventure_sync_settings_response.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.settings import adventure_sync_settings_pb2 as pogoprotos_dot_settings_dot_adventure__sync__settings__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/game/gamefitness/responses/get_adventure_sync_settings_response.proto',
  package='pogoprotos.networking.game.gamefitness.response',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n[pogoprotos/networking/game/gamefitness/responses/get_adventure_sync_settings_response.proto\x12/pogoprotos.networking.game.gamefitness.response\x1a\x31pogoprotos/settings/adventure_sync_settings.proto\"\xaa\x02\n GetAdventureSyncSettingsResponse\x12h\n\x06status\x18\x01 \x01(\x0e\x32X.pogoprotos.networking.game.gamefitness.response.GetAdventureSyncSettingsResponse.Status\x12K\n\x17\x61\x64venture_sync_settings\x18\x02 \x01(\x0b\x32*.pogoprotos.settings.AdventureSyncSettings\"O\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x11\n\rERROR_UNKNOWN\x10\x02\x12\x1a\n\x16\x45RROR_PLAYER_NOT_FOUND\x10\x03\x62\x06proto3'
  ,
  dependencies=[pogoprotos_dot_settings_dot_adventure__sync__settings__pb2.DESCRIPTOR,])



_GETADVENTURESYNCSETTINGSRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.game.gamefitness.response.GetAdventureSyncSettingsResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_UNKNOWN', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_NOT_FOUND', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=415,
  serialized_end=494,
)
_sym_db.RegisterEnumDescriptor(_GETADVENTURESYNCSETTINGSRESPONSE_STATUS)


_GETADVENTURESYNCSETTINGSRESPONSE = _descriptor.Descriptor(
  name='GetAdventureSyncSettingsResponse',
  full_name='pogoprotos.networking.game.gamefitness.response.GetAdventureSyncSettingsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.game.gamefitness.response.GetAdventureSyncSettingsResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adventure_sync_settings', full_name='pogoprotos.networking.game.gamefitness.response.GetAdventureSyncSettingsResponse.adventure_sync_settings', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETADVENTURESYNCSETTINGSRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=196,
  serialized_end=494,
)

_GETADVENTURESYNCSETTINGSRESPONSE.fields_by_name['status'].enum_type = _GETADVENTURESYNCSETTINGSRESPONSE_STATUS
_GETADVENTURESYNCSETTINGSRESPONSE.fields_by_name['adventure_sync_settings'].message_type = pogoprotos_dot_settings_dot_adventure__sync__settings__pb2._ADVENTURESYNCSETTINGS
_GETADVENTURESYNCSETTINGSRESPONSE_STATUS.containing_type = _GETADVENTURESYNCSETTINGSRESPONSE
DESCRIPTOR.message_types_by_name['GetAdventureSyncSettingsResponse'] = _GETADVENTURESYNCSETTINGSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAdventureSyncSettingsResponse = _reflection.GeneratedProtocolMessageType('GetAdventureSyncSettingsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETADVENTURESYNCSETTINGSRESPONSE,
  '__module__' : 'pogoprotos.networking.game.gamefitness.responses.get_adventure_sync_settings_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.game.gamefitness.response.GetAdventureSyncSettingsResponse)
  })
_sym_db.RegisterMessage(GetAdventureSyncSettingsResponse)


# @@protoc_insertion_point(module_scope)
