# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/buddy_emotion_level_settings.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import buddy_emotion_level_pb2 as pogoprotos_dot_enums_dot_buddy__emotion__level__pb2
from pogoprotos.enums import buddy_animation_pb2 as pogoprotos_dot_enums_dot_buddy__animation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/buddy_emotion_level_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n=pogoprotos/settings/master/buddy_emotion_level_settings.proto\x12\x1apogoprotos.settings.master\x1a*pogoprotos/enums/buddy_emotion_level.proto\x1a&pogoprotos/enums/buddy_animation.proto\"\xdf\x01\n\x19\x42uddyEmotionLevelSettings\x12:\n\remotion_level\x18\x01 \x01(\x0e\x32#.pogoprotos.enums.BuddyEmotionLevel\x12#\n\x1bmin_emotion_points_required\x18\x02 \x01(\x05\x12;\n\x11\x65motion_animation\x18\x03 \x01(\x0e\x32 .pogoprotos.enums.BuddyAnimation\x12$\n\x1c\x64\x65\x63\x61y_prevention_duration_ms\x18\x04 \x01(\x03\x62\x06proto3'
  ,
  dependencies=[pogoprotos_dot_enums_dot_buddy__emotion__level__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_buddy__animation__pb2.DESCRIPTOR,])




_BUDDYEMOTIONLEVELSETTINGS = _descriptor.Descriptor(
  name='BuddyEmotionLevelSettings',
  full_name='pogoprotos.settings.master.BuddyEmotionLevelSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='emotion_level', full_name='pogoprotos.settings.master.BuddyEmotionLevelSettings.emotion_level', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_emotion_points_required', full_name='pogoprotos.settings.master.BuddyEmotionLevelSettings.min_emotion_points_required', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='emotion_animation', full_name='pogoprotos.settings.master.BuddyEmotionLevelSettings.emotion_animation', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='decay_prevention_duration_ms', full_name='pogoprotos.settings.master.BuddyEmotionLevelSettings.decay_prevention_duration_ms', index=3,
      number=4, type=3, cpp_type=2, label=1,
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
  serialized_start=178,
  serialized_end=401,
)

_BUDDYEMOTIONLEVELSETTINGS.fields_by_name['emotion_level'].enum_type = pogoprotos_dot_enums_dot_buddy__emotion__level__pb2._BUDDYEMOTIONLEVEL
_BUDDYEMOTIONLEVELSETTINGS.fields_by_name['emotion_animation'].enum_type = pogoprotos_dot_enums_dot_buddy__animation__pb2._BUDDYANIMATION
DESCRIPTOR.message_types_by_name['BuddyEmotionLevelSettings'] = _BUDDYEMOTIONLEVELSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BuddyEmotionLevelSettings = _reflection.GeneratedProtocolMessageType('BuddyEmotionLevelSettings', (_message.Message,), {
  'DESCRIPTOR' : _BUDDYEMOTIONLEVELSETTINGS,
  '__module__' : 'pogoprotos.settings.master.buddy_emotion_level_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.BuddyEmotionLevelSettings)
  })
_sym_db.RegisterMessage(BuddyEmotionLevelSettings)


# @@protoc_insertion_point(module_scope)
