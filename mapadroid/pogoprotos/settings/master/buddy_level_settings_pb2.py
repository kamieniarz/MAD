# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/buddy_level_settings.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import buddy_level_pb2 as pogoprotos_dot_enums_dot_buddy__level__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/buddy_level_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n5pogoprotos/settings/master/buddy_level_settings.proto\x12\x1apogoprotos.settings.master\x1a\"pogoprotos/enums/buddy_level.proto\"\x85\x03\n\x12\x42uddyLevelSettings\x12+\n\x05level\x18\x01 \x01(\x0e\x32\x1c.pogoprotos.enums.BuddyLevel\x12*\n\"min_non_cumulative_points_required\x18\x02 \x01(\x05\x12R\n\x0funlocked_traits\x18\x03 \x03(\x0e\x32\x39.pogoprotos.settings.master.BuddyLevelSettings.BuddyTrait\"\xc1\x01\n\nBuddyTrait\x12\t\n\x05UNSET\x10\x00\x12\x0e\n\nMAP_DEPLOY\x10\x01\x12\x13\n\x0f\x45NCOUNTER_CAMEO\x10\x02\x12\x15\n\x11\x45MOTION_INDICATOR\x10\x03\x12\x17\n\x13PICK_UP_CONSUMABLES\x10\x04\x12\x15\n\x11PICK_UP_SOUVENIRS\x10\x05\x12\x18\n\x14\x46IND_ATTRACTIVE_POIS\x10\x06\x12\x14\n\x10\x42\x45ST_BUDDY_ASSET\x10\x07\x12\x0c\n\x08\x43P_BOOST\x10\x08\x62\x06proto3'
  ,
  dependencies=[pogoprotos_dot_enums_dot_buddy__level__pb2.DESCRIPTOR,])



_BUDDYLEVELSETTINGS_BUDDYTRAIT = _descriptor.EnumDescriptor(
  name='BuddyTrait',
  full_name='pogoprotos.settings.master.BuddyLevelSettings.BuddyTrait',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAP_DEPLOY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENCOUNTER_CAMEO', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMOTION_INDICATOR', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PICK_UP_CONSUMABLES', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PICK_UP_SOUVENIRS', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIND_ATTRACTIVE_POIS', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BEST_BUDDY_ASSET', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CP_BOOST', index=8, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=318,
  serialized_end=511,
)
_sym_db.RegisterEnumDescriptor(_BUDDYLEVELSETTINGS_BUDDYTRAIT)


_BUDDYLEVELSETTINGS = _descriptor.Descriptor(
  name='BuddyLevelSettings',
  full_name='pogoprotos.settings.master.BuddyLevelSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='pogoprotos.settings.master.BuddyLevelSettings.level', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_non_cumulative_points_required', full_name='pogoprotos.settings.master.BuddyLevelSettings.min_non_cumulative_points_required', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unlocked_traits', full_name='pogoprotos.settings.master.BuddyLevelSettings.unlocked_traits', index=2,
      number=3, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BUDDYLEVELSETTINGS_BUDDYTRAIT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=511,
)

_BUDDYLEVELSETTINGS.fields_by_name['level'].enum_type = pogoprotos_dot_enums_dot_buddy__level__pb2._BUDDYLEVEL
_BUDDYLEVELSETTINGS.fields_by_name['unlocked_traits'].enum_type = _BUDDYLEVELSETTINGS_BUDDYTRAIT
_BUDDYLEVELSETTINGS_BUDDYTRAIT.containing_type = _BUDDYLEVELSETTINGS
DESCRIPTOR.message_types_by_name['BuddyLevelSettings'] = _BUDDYLEVELSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BuddyLevelSettings = _reflection.GeneratedProtocolMessageType('BuddyLevelSettings', (_message.Message,), {
  'DESCRIPTOR' : _BUDDYLEVELSETTINGS,
  '__module__' : 'pogoprotos.settings.master.buddy_level_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.BuddyLevelSettings)
  })
_sym_db.RegisterMessage(BuddyLevelSettings)


# @@protoc_insertion_point(module_scope)
