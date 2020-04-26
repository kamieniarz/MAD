# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/quests/quest_pokemon_encounter.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import encounter_type_pb2 as pogoprotos_dot_enums_dot_encounter__type__pb2
from pogoprotos.data import pokemon_data_pb2 as pogoprotos_dot_data_dot_pokemon__data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/quests/quest_pokemon_encounter.proto',
  package='pogoprotos.data.quests',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n4pogoprotos/data/quests/quest_pokemon_encounter.proto\x12\x16pogoprotos.data.quests\x1a%pogoprotos/enums/encounter_type.proto\x1a\"pogoprotos/data/pokemon_data.proto\"\xd7\x01\n\x15QuestPokemonEncounter\x12\x10\n\x08quest_id\x18\x01 \x01(\t\x12-\n\x07pokemon\x18\x02 \x01(\x0b\x32\x1c.pogoprotos.data.PokemonData\x12\x37\n\x0e\x65ncounter_type\x18\x03 \x01(\x0e\x32\x1f.pogoprotos.enums.EncounterType\x12\x17\n\x0fis_hidden_ditto\x18\x04 \x01(\x08\x12+\n\x05\x64itto\x18\x05 \x01(\x0b\x32\x1c.pogoprotos.data.PokemonDatab\x06proto3'
  ,
  dependencies=[pogoprotos_dot_enums_dot_encounter__type__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_pokemon__data__pb2.DESCRIPTOR,])




_QUESTPOKEMONENCOUNTER = _descriptor.Descriptor(
  name='QuestPokemonEncounter',
  full_name='pogoprotos.data.quests.QuestPokemonEncounter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='quest_id', full_name='pogoprotos.data.quests.QuestPokemonEncounter.quest_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pokemon', full_name='pogoprotos.data.quests.QuestPokemonEncounter.pokemon', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encounter_type', full_name='pogoprotos.data.quests.QuestPokemonEncounter.encounter_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_hidden_ditto', full_name='pogoprotos.data.quests.QuestPokemonEncounter.is_hidden_ditto', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ditto', full_name='pogoprotos.data.quests.QuestPokemonEncounter.ditto', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=156,
  serialized_end=371,
)

_QUESTPOKEMONENCOUNTER.fields_by_name['pokemon'].message_type = pogoprotos_dot_data_dot_pokemon__data__pb2._POKEMONDATA
_QUESTPOKEMONENCOUNTER.fields_by_name['encounter_type'].enum_type = pogoprotos_dot_enums_dot_encounter__type__pb2._ENCOUNTERTYPE
_QUESTPOKEMONENCOUNTER.fields_by_name['ditto'].message_type = pogoprotos_dot_data_dot_pokemon__data__pb2._POKEMONDATA
DESCRIPTOR.message_types_by_name['QuestPokemonEncounter'] = _QUESTPOKEMONENCOUNTER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QuestPokemonEncounter = _reflection.GeneratedProtocolMessageType('QuestPokemonEncounter', (_message.Message,), {
  'DESCRIPTOR' : _QUESTPOKEMONENCOUNTER,
  '__module__' : 'pogoprotos.data.quests.quest_pokemon_encounter_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.quests.QuestPokemonEncounter)
  })
_sym_db.RegisterMessage(QuestPokemonEncounter)


# @@protoc_insertion_point(module_scope)
