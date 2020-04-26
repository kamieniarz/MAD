# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/trading_global_settings.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/trading_global_settings.proto',
  package='pogoprotos.settings',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n1pogoprotos/settings/trading_global_settings.proto\x12\x13pogoprotos.settings\"I\n\x15TradingGlobalSettings\x12\x16\n\x0e\x65nable_trading\x18\x01 \x01(\x08\x12\x18\n\x10min_player_level\x18\x02 \x01(\rb\x06proto3'
)




_TRADINGGLOBALSETTINGS = _descriptor.Descriptor(
  name='TradingGlobalSettings',
  full_name='pogoprotos.settings.TradingGlobalSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enable_trading', full_name='pogoprotos.settings.TradingGlobalSettings.enable_trading', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_player_level', full_name='pogoprotos.settings.TradingGlobalSettings.min_player_level', index=1,
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
  serialized_start=74,
  serialized_end=147,
)

DESCRIPTOR.message_types_by_name['TradingGlobalSettings'] = _TRADINGGLOBALSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TradingGlobalSettings = _reflection.GeneratedProtocolMessageType('TradingGlobalSettings', (_message.Message,), {
  'DESCRIPTOR' : _TRADINGGLOBALSETTINGS,
  '__module__' : 'pogoprotos.settings.trading_global_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.TradingGlobalSettings)
  })
_sym_db.RegisterMessage(TradingGlobalSettings)


# @@protoc_insertion_point(module_scope)
