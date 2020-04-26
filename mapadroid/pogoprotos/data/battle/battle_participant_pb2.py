# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/battle/battle_participant.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.battle import battle_pokemon_info_pb2 as pogoprotos_dot_data_dot_battle_dot_battle__pokemon__info__pb2
from pogoprotos.data.player import player_public_profile_pb2 as pogoprotos_dot_data_dot_player_dot_player__public__profile__pb2
from pogoprotos.map.pokemon import lobby_pokemon_pb2 as pogoprotos_dot_map_dot_pokemon_dot_lobby__pokemon__pb2
from pogoprotos.enums import friendship_level_milestone_pb2 as pogoprotos_dot_enums_dot_friendship__level__milestone__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/battle/battle_participant.proto',
  package='pogoprotos.data.battle',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n/pogoprotos/data/battle/battle_participant.proto\x12\x16pogoprotos.data.battle\x1a\x30pogoprotos/data/battle/battle_pokemon_info.proto\x1a\x32pogoprotos/data/player/player_public_profile.proto\x1a*pogoprotos/map/pokemon/lobby_pokemon.proto\x1a\x31pogoprotos/enums/friendship_level_milestone.proto\"\xd5\x04\n\x11\x42\x61ttleParticipant\x12\x41\n\x0e\x61\x63tive_pokemon\x18\x01 \x01(\x0b\x32).pogoprotos.data.battle.BattlePokemonInfo\x12K\n\x16trainer_public_profile\x18\x02 \x01(\x0b\x32+.pogoprotos.data.player.PlayerPublicProfile\x12\x42\n\x0freverse_pokemon\x18\x03 \x03(\x0b\x32).pogoprotos.data.battle.BattlePokemonInfo\x12\x43\n\x10\x64\x65\x66\x65\x61ted_pokemon\x18\x04 \x03(\x0b\x32).pogoprotos.data.battle.BattlePokemonInfo\x12;\n\rlobby_pokemon\x18\x05 \x03(\x0b\x32$.pogoprotos.map.pokemon.LobbyPokemon\x12\x14\n\x0c\x64\x61mage_dealt\x18\x06 \x01(\x05\x12#\n\x1bsuper_effective_charge_move\x18\x07 \x01(\x08\x12\x17\n\x0fweather_boosted\x18\x08 \x01(\x08\x12P\n\x1chighest_friendship_milestone\x18\t \x01(\x0e\x32*.pogoprotos.enums.FriendshipLevelMilestone\x12\x17\n\x0f\x66riend_codename\x18\n \x03(\t\x12\x11\n\tis_remote\x18\x0b \x01(\x08\x12\x18\n\x10is_social_invite\x18\x0c \x01(\x08\x62\x06proto3'
  ,
  dependencies=[pogoprotos_dot_data_dot_battle_dot_battle__pokemon__info__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_player_dot_player__public__profile__pb2.DESCRIPTOR,pogoprotos_dot_map_dot_pokemon_dot_lobby__pokemon__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_friendship__level__milestone__pb2.DESCRIPTOR,])




_BATTLEPARTICIPANT = _descriptor.Descriptor(
  name='BattleParticipant',
  full_name='pogoprotos.data.battle.BattleParticipant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='active_pokemon', full_name='pogoprotos.data.battle.BattleParticipant.active_pokemon', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trainer_public_profile', full_name='pogoprotos.data.battle.BattleParticipant.trainer_public_profile', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reverse_pokemon', full_name='pogoprotos.data.battle.BattleParticipant.reverse_pokemon', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='defeated_pokemon', full_name='pogoprotos.data.battle.BattleParticipant.defeated_pokemon', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lobby_pokemon', full_name='pogoprotos.data.battle.BattleParticipant.lobby_pokemon', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='damage_dealt', full_name='pogoprotos.data.battle.BattleParticipant.damage_dealt', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='super_effective_charge_move', full_name='pogoprotos.data.battle.BattleParticipant.super_effective_charge_move', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weather_boosted', full_name='pogoprotos.data.battle.BattleParticipant.weather_boosted', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='highest_friendship_milestone', full_name='pogoprotos.data.battle.BattleParticipant.highest_friendship_milestone', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='friend_codename', full_name='pogoprotos.data.battle.BattleParticipant.friend_codename', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_remote', full_name='pogoprotos.data.battle.BattleParticipant.is_remote', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_social_invite', full_name='pogoprotos.data.battle.BattleParticipant.is_social_invite', index=11,
      number=12, type=8, cpp_type=7, label=1,
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
  serialized_start=273,
  serialized_end=870,
)

_BATTLEPARTICIPANT.fields_by_name['active_pokemon'].message_type = pogoprotos_dot_data_dot_battle_dot_battle__pokemon__info__pb2._BATTLEPOKEMONINFO
_BATTLEPARTICIPANT.fields_by_name['trainer_public_profile'].message_type = pogoprotos_dot_data_dot_player_dot_player__public__profile__pb2._PLAYERPUBLICPROFILE
_BATTLEPARTICIPANT.fields_by_name['reverse_pokemon'].message_type = pogoprotos_dot_data_dot_battle_dot_battle__pokemon__info__pb2._BATTLEPOKEMONINFO
_BATTLEPARTICIPANT.fields_by_name['defeated_pokemon'].message_type = pogoprotos_dot_data_dot_battle_dot_battle__pokemon__info__pb2._BATTLEPOKEMONINFO
_BATTLEPARTICIPANT.fields_by_name['lobby_pokemon'].message_type = pogoprotos_dot_map_dot_pokemon_dot_lobby__pokemon__pb2._LOBBYPOKEMON
_BATTLEPARTICIPANT.fields_by_name['highest_friendship_milestone'].enum_type = pogoprotos_dot_enums_dot_friendship__level__milestone__pb2._FRIENDSHIPLEVELMILESTONE
DESCRIPTOR.message_types_by_name['BattleParticipant'] = _BATTLEPARTICIPANT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BattleParticipant = _reflection.GeneratedProtocolMessageType('BattleParticipant', (_message.Message,), {
  'DESCRIPTOR' : _BATTLEPARTICIPANT,
  '__module__' : 'pogoprotos.data.battle.battle_participant_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.battle.BattleParticipant)
  })
_sym_db.RegisterMessage(BattleParticipant)


# @@protoc_insertion_point(module_scope)
