# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/map/pokemon/motivated_pokemon.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data import pokemon_data_pb2 as pogoprotos_dot_data_dot_pokemon__data__pb2
from pogoprotos.inventory.item import item_id_pb2 as pogoprotos_dot_inventory_dot_item_dot_item__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/map/pokemon/motivated_pokemon.proto',
  package='pogoprotos.map.pokemon',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n.pogoprotos/map/pokemon/motivated_pokemon.proto\x12\x16pogoprotos.map.pokemon\x1a\"pogoprotos/data/pokemon_data.proto\x1a\'pogoprotos/inventory/item/item_id.proto\"\x8f\x03\n\x10MotivatedPokemon\x12-\n\x07pokemon\x18\x01 \x01(\x0b\x32\x1c.pogoprotos.data.PokemonData\x12\x11\n\tdeploy_ms\x18\x02 \x01(\x03\x12\x18\n\x10\x63p_when_deployed\x18\x03 \x01(\x05\x12\x16\n\x0emotivation_now\x18\x04 \x01(\x01\x12\x0e\n\x06\x63p_now\x18\x05 \x01(\x05\x12\x13\n\x0b\x62\x65rry_value\x18\x06 \x01(\x02\x12%\n\x1d\x66\x65\x65\x64_cooldown_duration_millis\x18\x07 \x01(\x03\x12\x46\n\nfood_value\x18\x08 \x03(\x0b\x32\x32.pogoprotos.map.pokemon.MotivatedPokemon.FoodValue\x1as\n\tFoodValue\x12\x1b\n\x13motivation_increase\x18\x01 \x01(\x02\x12\x13\n\x0b\x63p_increase\x18\x02 \x01(\x05\x12\x34\n\tfood_item\x18\x03 \x01(\x0e\x32!.pogoprotos.inventory.item.ItemIdb\x06proto3'
  ,
  dependencies=[pogoprotos_dot_data_dot_pokemon__data__pb2.DESCRIPTOR,pogoprotos_dot_inventory_dot_item_dot_item__id__pb2.DESCRIPTOR,])




_MOTIVATEDPOKEMON_FOODVALUE = _descriptor.Descriptor(
  name='FoodValue',
  full_name='pogoprotos.map.pokemon.MotivatedPokemon.FoodValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='motivation_increase', full_name='pogoprotos.map.pokemon.MotivatedPokemon.FoodValue.motivation_increase', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cp_increase', full_name='pogoprotos.map.pokemon.MotivatedPokemon.FoodValue.cp_increase', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='food_item', full_name='pogoprotos.map.pokemon.MotivatedPokemon.FoodValue.food_item', index=2,
      number=3, type=14, cpp_type=8, label=1,
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
  serialized_start=436,
  serialized_end=551,
)

_MOTIVATEDPOKEMON = _descriptor.Descriptor(
  name='MotivatedPokemon',
  full_name='pogoprotos.map.pokemon.MotivatedPokemon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon', full_name='pogoprotos.map.pokemon.MotivatedPokemon.pokemon', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deploy_ms', full_name='pogoprotos.map.pokemon.MotivatedPokemon.deploy_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cp_when_deployed', full_name='pogoprotos.map.pokemon.MotivatedPokemon.cp_when_deployed', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='motivation_now', full_name='pogoprotos.map.pokemon.MotivatedPokemon.motivation_now', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cp_now', full_name='pogoprotos.map.pokemon.MotivatedPokemon.cp_now', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='berry_value', full_name='pogoprotos.map.pokemon.MotivatedPokemon.berry_value', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feed_cooldown_duration_millis', full_name='pogoprotos.map.pokemon.MotivatedPokemon.feed_cooldown_duration_millis', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='food_value', full_name='pogoprotos.map.pokemon.MotivatedPokemon.food_value', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MOTIVATEDPOKEMON_FOODVALUE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=152,
  serialized_end=551,
)

_MOTIVATEDPOKEMON_FOODVALUE.fields_by_name['food_item'].enum_type = pogoprotos_dot_inventory_dot_item_dot_item__id__pb2._ITEMID
_MOTIVATEDPOKEMON_FOODVALUE.containing_type = _MOTIVATEDPOKEMON
_MOTIVATEDPOKEMON.fields_by_name['pokemon'].message_type = pogoprotos_dot_data_dot_pokemon__data__pb2._POKEMONDATA
_MOTIVATEDPOKEMON.fields_by_name['food_value'].message_type = _MOTIVATEDPOKEMON_FOODVALUE
DESCRIPTOR.message_types_by_name['MotivatedPokemon'] = _MOTIVATEDPOKEMON
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MotivatedPokemon = _reflection.GeneratedProtocolMessageType('MotivatedPokemon', (_message.Message,), {

  'FoodValue' : _reflection.GeneratedProtocolMessageType('FoodValue', (_message.Message,), {
    'DESCRIPTOR' : _MOTIVATEDPOKEMON_FOODVALUE,
    '__module__' : 'pogoprotos.map.pokemon.motivated_pokemon_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.map.pokemon.MotivatedPokemon.FoodValue)
    })
  ,
  'DESCRIPTOR' : _MOTIVATEDPOKEMON,
  '__module__' : 'pogoprotos.map.pokemon.motivated_pokemon_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.map.pokemon.MotivatedPokemon)
  })
_sym_db.RegisterMessage(MotivatedPokemon)
_sym_db.RegisterMessage(MotivatedPokemon.FoodValue)


# @@protoc_insertion_point(module_scope)
