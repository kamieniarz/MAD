# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/redeem/redeem_passcode_reward.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import badge_type_pb2 as pogoprotos_dot_enums_dot_badge__type__pb2
from pogoprotos.data import pokemon_data_pb2 as pogoprotos_dot_data_dot_pokemon__data__pb2
from pogoprotos.data.redeem import poke_candy_pb2 as pogoprotos_dot_data_dot_redeem_dot_poke__candy__pb2
from pogoprotos.data.redeem import redeemed_avatar_item_pb2 as pogoprotos_dot_data_dot_redeem_dot_redeemed__avatar__item__pb2
from pogoprotos.data.redeem import redeemed_item_pb2 as pogoprotos_dot_data_dot_redeem_dot_redeemed__item__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/redeem/redeem_passcode_reward.proto',
  package='pogoprotos.data.redeem',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n3pogoprotos/data/redeem/redeem_passcode_reward.proto\x12\x16pogoprotos.data.redeem\x1a!pogoprotos/enums/badge_type.proto\x1a\"pogoprotos/data/pokemon_data.proto\x1a\'pogoprotos/data/redeem/poke_candy.proto\x1a\x31pogoprotos/data/redeem/redeemed_avatar_item.proto\x1a*pogoprotos/data/redeem/redeemed_item.proto\"\xf8\x02\n\x14RedeemPasscodeReward\x12\x33\n\x05items\x18\x01 \x03(\x0b\x32$.pogoprotos.data.redeem.RedeemedItem\x12@\n\x0c\x61vatar_items\x18\x02 \x03(\x0b\x32*.pogoprotos.data.redeem.RedeemedAvatarItem\x12\x31\n\x0b\x65gg_pokemon\x18\x03 \x03(\x0b\x32\x1c.pogoprotos.data.PokemonData\x12-\n\x07pokemon\x18\x04 \x03(\x0b\x32\x1c.pogoprotos.data.PokemonData\x12\x35\n\npoke_candy\x18\x05 \x03(\x0b\x32!.pogoprotos.data.redeem.PokeCandy\x12\x10\n\x08stardust\x18\x06 \x01(\x05\x12\x11\n\tpokecoins\x18\x07 \x01(\x05\x12+\n\x06\x62\x61\x64ges\x18\x08 \x03(\x0e\x32\x1b.pogoprotos.enums.BadgeTypeb\x06proto3'
  ,
  dependencies=[pogoprotos_dot_enums_dot_badge__type__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_pokemon__data__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_redeem_dot_poke__candy__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_redeem_dot_redeemed__avatar__item__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_redeem_dot_redeemed__item__pb2.DESCRIPTOR,])




_REDEEMPASSCODEREWARD = _descriptor.Descriptor(
  name='RedeemPasscodeReward',
  full_name='pogoprotos.data.redeem.RedeemPasscodeReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='pogoprotos.data.redeem.RedeemPasscodeReward.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avatar_items', full_name='pogoprotos.data.redeem.RedeemPasscodeReward.avatar_items', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='egg_pokemon', full_name='pogoprotos.data.redeem.RedeemPasscodeReward.egg_pokemon', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pokemon', full_name='pogoprotos.data.redeem.RedeemPasscodeReward.pokemon', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='poke_candy', full_name='pogoprotos.data.redeem.RedeemPasscodeReward.poke_candy', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stardust', full_name='pogoprotos.data.redeem.RedeemPasscodeReward.stardust', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pokecoins', full_name='pogoprotos.data.redeem.RedeemPasscodeReward.pokecoins', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='badges', full_name='pogoprotos.data.redeem.RedeemPasscodeReward.badges', index=7,
      number=8, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=287,
  serialized_end=663,
)

_REDEEMPASSCODEREWARD.fields_by_name['items'].message_type = pogoprotos_dot_data_dot_redeem_dot_redeemed__item__pb2._REDEEMEDITEM
_REDEEMPASSCODEREWARD.fields_by_name['avatar_items'].message_type = pogoprotos_dot_data_dot_redeem_dot_redeemed__avatar__item__pb2._REDEEMEDAVATARITEM
_REDEEMPASSCODEREWARD.fields_by_name['egg_pokemon'].message_type = pogoprotos_dot_data_dot_pokemon__data__pb2._POKEMONDATA
_REDEEMPASSCODEREWARD.fields_by_name['pokemon'].message_type = pogoprotos_dot_data_dot_pokemon__data__pb2._POKEMONDATA
_REDEEMPASSCODEREWARD.fields_by_name['poke_candy'].message_type = pogoprotos_dot_data_dot_redeem_dot_poke__candy__pb2._POKECANDY
_REDEEMPASSCODEREWARD.fields_by_name['badges'].enum_type = pogoprotos_dot_enums_dot_badge__type__pb2._BADGETYPE
DESCRIPTOR.message_types_by_name['RedeemPasscodeReward'] = _REDEEMPASSCODEREWARD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RedeemPasscodeReward = _reflection.GeneratedProtocolMessageType('RedeemPasscodeReward', (_message.Message,), {
  'DESCRIPTOR' : _REDEEMPASSCODEREWARD,
  '__module__' : 'pogoprotos.data.redeem.redeem_passcode_reward_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.redeem.RedeemPasscodeReward)
  })
_sym_db.RegisterMessage(RedeemPasscodeReward)


# @@protoc_insertion_point(module_scope)
