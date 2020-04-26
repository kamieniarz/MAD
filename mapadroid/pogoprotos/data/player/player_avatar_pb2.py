# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/player/player_avatar.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/player/player_avatar.proto',
  package='pogoprotos.data.player',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n*pogoprotos/data/player/player_avatar.proto\x12\x16pogoprotos.data.player\"\xca\x03\n\x0cPlayerAvatar\x12\x0c\n\x04skin\x18\x02 \x01(\x05\x12\x0c\n\x04hair\x18\x03 \x01(\x05\x12\r\n\x05shirt\x18\x04 \x01(\x05\x12\r\n\x05pants\x18\x05 \x01(\x05\x12\x0b\n\x03hat\x18\x06 \x01(\x05\x12\r\n\x05shoes\x18\x07 \x01(\x05\x12\x0e\n\x06\x61vatar\x18\x08 \x01(\x05\x12\x0c\n\x04\x65yes\x18\t \x01(\x05\x12\x10\n\x08\x62\x61\x63kpack\x18\n \x01(\x05\x12\x13\n\x0b\x61vatar_hair\x18\x0b \x01(\t\x12\x14\n\x0c\x61vatar_shirt\x18\x0c \x01(\t\x12\x14\n\x0c\x61vatar_pants\x18\r \x01(\t\x12\x12\n\navatar_hat\x18\x0e \x01(\t\x12\x14\n\x0c\x61vatar_shoes\x18\x0f \x01(\t\x12\x13\n\x0b\x61vatar_eyes\x18\x10 \x01(\t\x12\x17\n\x0f\x61vatar_backpack\x18\x11 \x01(\t\x12\x15\n\ravatar_gloves\x18\x12 \x01(\t\x12\x14\n\x0c\x61vatar_socks\x18\x13 \x01(\t\x12\x13\n\x0b\x61vatar_belt\x18\x14 \x01(\t\x12\x16\n\x0e\x61vatar_glasses\x18\x15 \x01(\t\x12\x17\n\x0f\x61vatar_necklace\x18\x16 \x01(\t\x12\x13\n\x0b\x61vatar_skin\x18\x17 \x01(\t\x12\x13\n\x0b\x61vatar_pose\x18\x18 \x01(\tb\x06proto3'
)




_PLAYERAVATAR = _descriptor.Descriptor(
  name='PlayerAvatar',
  full_name='pogoprotos.data.player.PlayerAvatar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='skin', full_name='pogoprotos.data.player.PlayerAvatar.skin', index=0,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hair', full_name='pogoprotos.data.player.PlayerAvatar.hair', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shirt', full_name='pogoprotos.data.player.PlayerAvatar.shirt', index=2,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pants', full_name='pogoprotos.data.player.PlayerAvatar.pants', index=3,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hat', full_name='pogoprotos.data.player.PlayerAvatar.hat', index=4,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shoes', full_name='pogoprotos.data.player.PlayerAvatar.shoes', index=5,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avatar', full_name='pogoprotos.data.player.PlayerAvatar.avatar', index=6,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eyes', full_name='pogoprotos.data.player.PlayerAvatar.eyes', index=7,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='backpack', full_name='pogoprotos.data.player.PlayerAvatar.backpack', index=8,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avatar_hair', full_name='pogoprotos.data.player.PlayerAvatar.avatar_hair', index=9,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avatar_shirt', full_name='pogoprotos.data.player.PlayerAvatar.avatar_shirt', index=10,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avatar_pants', full_name='pogoprotos.data.player.PlayerAvatar.avatar_pants', index=11,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avatar_hat', full_name='pogoprotos.data.player.PlayerAvatar.avatar_hat', index=12,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avatar_shoes', full_name='pogoprotos.data.player.PlayerAvatar.avatar_shoes', index=13,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avatar_eyes', full_name='pogoprotos.data.player.PlayerAvatar.avatar_eyes', index=14,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avatar_backpack', full_name='pogoprotos.data.player.PlayerAvatar.avatar_backpack', index=15,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avatar_gloves', full_name='pogoprotos.data.player.PlayerAvatar.avatar_gloves', index=16,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avatar_socks', full_name='pogoprotos.data.player.PlayerAvatar.avatar_socks', index=17,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avatar_belt', full_name='pogoprotos.data.player.PlayerAvatar.avatar_belt', index=18,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avatar_glasses', full_name='pogoprotos.data.player.PlayerAvatar.avatar_glasses', index=19,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avatar_necklace', full_name='pogoprotos.data.player.PlayerAvatar.avatar_necklace', index=20,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avatar_skin', full_name='pogoprotos.data.player.PlayerAvatar.avatar_skin', index=21,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avatar_pose', full_name='pogoprotos.data.player.PlayerAvatar.avatar_pose', index=22,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=71,
  serialized_end=529,
)

DESCRIPTOR.message_types_by_name['PlayerAvatar'] = _PLAYERAVATAR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlayerAvatar = _reflection.GeneratedProtocolMessageType('PlayerAvatar', (_message.Message,), {
  'DESCRIPTOR' : _PLAYERAVATAR,
  '__module__' : 'pogoprotos.data.player.player_avatar_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.player.PlayerAvatar)
  })
_sym_db.RegisterMessage(PlayerAvatar)


# @@protoc_insertion_point(module_scope)
