# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/item/user_attributes.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/item/user_attributes.proto',
  package='pogoprotos.settings.master.item',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n5pogoprotos/settings/master/item/user_attributes.proto\x12\x1fpogoprotos.settings.master.item\"\xc9\x0b\n\x0eUserAttributes\x12\r\n\x05level\x18\x01 \x01(\x05\x12\x15\n\rxp_percentage\x18\x02 \x01(\x03\x12\x16\n\x0epokecoin_count\x18\x03 \x01(\x03\x12\x0c\n\x04team\x18\x04 \x01(\x05\x12\x14\n\x0c\x63\x61tch_streak\x18\x05 \x01(\x05\x12\x13\n\x0bspin_streak\x18\x06 \x01(\x05\x12\x12\n\nbuddy_name\x18\x07 \x01(\t\x12\x19\n\x11is_egg_incubating\x18\x08 \x01(\x08\x12\x10\n\x08has_eggs\x18\t \x01(\x08\x12\x18\n\x10star_piece_count\x18\n \x01(\x05\x12\x17\n\x0flucky_egg_count\x18\x0b \x01(\x05\x12\x1e\n\x16incense_ordinary_count\x18\x0c \x01(\x05\x12\x1b\n\x13incense_spicy_count\x18\r \x01(\x05\x12\x1a\n\x12incense_cool_count\x18\x0e \x01(\x05\x12\x1c\n\x14incense_floral_count\x18\x0f \x01(\x05\x12\x1b\n\x13lure_ordinary_count\x18\x10 \x01(\x05\x12\x18\n\x10lure_mossy_count\x18\x11 \x01(\x05\x12\x1a\n\x12lure_glacial_count\x18\x12 \x01(\x05\x12\x1b\n\x13lure_magnetic_count\x18\x13 \x01(\x05\x12\x18\n\x10using_star_piece\x18\x14 \x01(\x08\x12\x17\n\x0fusing_lucky_egg\x18\x15 \x01(\x08\x12\x1e\n\x16using_incense_ordinary\x18\x16 \x01(\x08\x12\x1b\n\x13using_incense_spicy\x18\x17 \x01(\x08\x12\x1a\n\x12using_incense_cool\x18\x18 \x01(\x08\x12\x1c\n\x14using_incense_floral\x18\x19 \x01(\x08\x12\x1b\n\x13using_lure_ordinary\x18\x1a \x01(\x08\x12\x18\n\x10using_lure_mossy\x18\x1b \x01(\x08\x12\x1a\n\x12using_lure_glacial\x18\x1c \x01(\x08\x12\x1b\n\x13using_lure_magnetic\x18\x1d \x01(\x08\x12\x1d\n\x15\x61\x64venture_sync_opt_in\x18\x1e \x01(\x08\x12\x18\n\x10geo_fence_opt_in\x18\x1f \x01(\x08\x12\x17\n\x0fkanto_dex_count\x18  \x01(\x05\x12\x17\n\x0fjohto_dex_count\x18! \x01(\x05\x12\x17\n\x0fhoenn_dex_count\x18\" \x01(\x05\x12\x18\n\x10sinnoh_dex_count\x18# \x01(\x05\x12\x14\n\x0c\x66riend_count\x18$ \x01(\x05\x12%\n\x1d\x66ield_research_stamp_progress\x18% \x01(\x05\x12\x10\n\x08level_up\x18& \x01(\x05\x12\x1b\n\x13sent_friend_request\x18\' \x01(\x08\x12\x1c\n\x14is_egg_incubating_v2\x18( \x01(\t\x12\x13\n\x0bhas_eggs_v2\x18) \x01(\t\x12\x1b\n\x13using_star_piece_v2\x18* \x01(\t\x12\x1a\n\x12using_lucky_egg_v2\x18+ \x01(\t\x12!\n\x19using_incense_ordinary_v2\x18, \x01(\t\x12\x1e\n\x16using_incense_spicy_v2\x18- \x01(\t\x12\x1d\n\x15using_incense_cool_v2\x18. \x01(\t\x12\x1f\n\x17using_incense_floral_v2\x18/ \x01(\t\x12\x1e\n\x16using_lure_ordinary_v2\x18\x30 \x01(\t\x12\x1b\n\x13using_lure_mossy_v2\x18\x31 \x01(\t\x12\x1d\n\x15using_lure_glacial_v2\x18\x32 \x01(\t\x12\x1e\n\x16using_lure_magnetic_v2\x18\x33 \x01(\t\x12 \n\x18\x61\x64venture_sync_opt_in_v2\x18\x34 \x01(\t\x12\x1b\n\x13geo_fence_opt_in_v2\x18\x35 \x01(\t\x12\x17\n\x0funova_dex_count\x18\x36 \x01(\x05\x62\x06proto3'
)




_USERATTRIBUTES = _descriptor.Descriptor(
  name='UserAttributes',
  full_name='pogoprotos.settings.master.item.UserAttributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='pogoprotos.settings.master.item.UserAttributes.level', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='xp_percentage', full_name='pogoprotos.settings.master.item.UserAttributes.xp_percentage', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pokecoin_count', full_name='pogoprotos.settings.master.item.UserAttributes.pokecoin_count', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='team', full_name='pogoprotos.settings.master.item.UserAttributes.team', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='catch_streak', full_name='pogoprotos.settings.master.item.UserAttributes.catch_streak', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spin_streak', full_name='pogoprotos.settings.master.item.UserAttributes.spin_streak', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buddy_name', full_name='pogoprotos.settings.master.item.UserAttributes.buddy_name', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_egg_incubating', full_name='pogoprotos.settings.master.item.UserAttributes.is_egg_incubating', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='has_eggs', full_name='pogoprotos.settings.master.item.UserAttributes.has_eggs', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='star_piece_count', full_name='pogoprotos.settings.master.item.UserAttributes.star_piece_count', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lucky_egg_count', full_name='pogoprotos.settings.master.item.UserAttributes.lucky_egg_count', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='incense_ordinary_count', full_name='pogoprotos.settings.master.item.UserAttributes.incense_ordinary_count', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='incense_spicy_count', full_name='pogoprotos.settings.master.item.UserAttributes.incense_spicy_count', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='incense_cool_count', full_name='pogoprotos.settings.master.item.UserAttributes.incense_cool_count', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='incense_floral_count', full_name='pogoprotos.settings.master.item.UserAttributes.incense_floral_count', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lure_ordinary_count', full_name='pogoprotos.settings.master.item.UserAttributes.lure_ordinary_count', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lure_mossy_count', full_name='pogoprotos.settings.master.item.UserAttributes.lure_mossy_count', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lure_glacial_count', full_name='pogoprotos.settings.master.item.UserAttributes.lure_glacial_count', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lure_magnetic_count', full_name='pogoprotos.settings.master.item.UserAttributes.lure_magnetic_count', index=18,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='using_star_piece', full_name='pogoprotos.settings.master.item.UserAttributes.using_star_piece', index=19,
      number=20, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='using_lucky_egg', full_name='pogoprotos.settings.master.item.UserAttributes.using_lucky_egg', index=20,
      number=21, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='using_incense_ordinary', full_name='pogoprotos.settings.master.item.UserAttributes.using_incense_ordinary', index=21,
      number=22, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='using_incense_spicy', full_name='pogoprotos.settings.master.item.UserAttributes.using_incense_spicy', index=22,
      number=23, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='using_incense_cool', full_name='pogoprotos.settings.master.item.UserAttributes.using_incense_cool', index=23,
      number=24, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='using_incense_floral', full_name='pogoprotos.settings.master.item.UserAttributes.using_incense_floral', index=24,
      number=25, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='using_lure_ordinary', full_name='pogoprotos.settings.master.item.UserAttributes.using_lure_ordinary', index=25,
      number=26, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='using_lure_mossy', full_name='pogoprotos.settings.master.item.UserAttributes.using_lure_mossy', index=26,
      number=27, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='using_lure_glacial', full_name='pogoprotos.settings.master.item.UserAttributes.using_lure_glacial', index=27,
      number=28, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='using_lure_magnetic', full_name='pogoprotos.settings.master.item.UserAttributes.using_lure_magnetic', index=28,
      number=29, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adventure_sync_opt_in', full_name='pogoprotos.settings.master.item.UserAttributes.adventure_sync_opt_in', index=29,
      number=30, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='geo_fence_opt_in', full_name='pogoprotos.settings.master.item.UserAttributes.geo_fence_opt_in', index=30,
      number=31, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kanto_dex_count', full_name='pogoprotos.settings.master.item.UserAttributes.kanto_dex_count', index=31,
      number=32, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='johto_dex_count', full_name='pogoprotos.settings.master.item.UserAttributes.johto_dex_count', index=32,
      number=33, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hoenn_dex_count', full_name='pogoprotos.settings.master.item.UserAttributes.hoenn_dex_count', index=33,
      number=34, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sinnoh_dex_count', full_name='pogoprotos.settings.master.item.UserAttributes.sinnoh_dex_count', index=34,
      number=35, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='friend_count', full_name='pogoprotos.settings.master.item.UserAttributes.friend_count', index=35,
      number=36, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='field_research_stamp_progress', full_name='pogoprotos.settings.master.item.UserAttributes.field_research_stamp_progress', index=36,
      number=37, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level_up', full_name='pogoprotos.settings.master.item.UserAttributes.level_up', index=37,
      number=38, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sent_friend_request', full_name='pogoprotos.settings.master.item.UserAttributes.sent_friend_request', index=38,
      number=39, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_egg_incubating_v2', full_name='pogoprotos.settings.master.item.UserAttributes.is_egg_incubating_v2', index=39,
      number=40, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='has_eggs_v2', full_name='pogoprotos.settings.master.item.UserAttributes.has_eggs_v2', index=40,
      number=41, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='using_star_piece_v2', full_name='pogoprotos.settings.master.item.UserAttributes.using_star_piece_v2', index=41,
      number=42, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='using_lucky_egg_v2', full_name='pogoprotos.settings.master.item.UserAttributes.using_lucky_egg_v2', index=42,
      number=43, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='using_incense_ordinary_v2', full_name='pogoprotos.settings.master.item.UserAttributes.using_incense_ordinary_v2', index=43,
      number=44, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='using_incense_spicy_v2', full_name='pogoprotos.settings.master.item.UserAttributes.using_incense_spicy_v2', index=44,
      number=45, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='using_incense_cool_v2', full_name='pogoprotos.settings.master.item.UserAttributes.using_incense_cool_v2', index=45,
      number=46, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='using_incense_floral_v2', full_name='pogoprotos.settings.master.item.UserAttributes.using_incense_floral_v2', index=46,
      number=47, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='using_lure_ordinary_v2', full_name='pogoprotos.settings.master.item.UserAttributes.using_lure_ordinary_v2', index=47,
      number=48, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='using_lure_mossy_v2', full_name='pogoprotos.settings.master.item.UserAttributes.using_lure_mossy_v2', index=48,
      number=49, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='using_lure_glacial_v2', full_name='pogoprotos.settings.master.item.UserAttributes.using_lure_glacial_v2', index=49,
      number=50, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='using_lure_magnetic_v2', full_name='pogoprotos.settings.master.item.UserAttributes.using_lure_magnetic_v2', index=50,
      number=51, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adventure_sync_opt_in_v2', full_name='pogoprotos.settings.master.item.UserAttributes.adventure_sync_opt_in_v2', index=51,
      number=52, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='geo_fence_opt_in_v2', full_name='pogoprotos.settings.master.item.UserAttributes.geo_fence_opt_in_v2', index=52,
      number=53, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unova_dex_count', full_name='pogoprotos.settings.master.item.UserAttributes.unova_dex_count', index=53,
      number=54, type=5, cpp_type=1, label=1,
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
  serialized_start=91,
  serialized_end=1572,
)

DESCRIPTOR.message_types_by_name['UserAttributes'] = _USERATTRIBUTES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserAttributes = _reflection.GeneratedProtocolMessageType('UserAttributes', (_message.Message,), {
  'DESCRIPTOR' : _USERATTRIBUTES,
  '__module__' : 'pogoprotos.settings.master.item.user_attributes_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.item.UserAttributes)
  })
_sym_db.RegisterMessage(UserAttributes)


# @@protoc_insertion_point(module_scope)
