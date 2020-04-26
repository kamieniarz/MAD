# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/inventory/candy.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import pokemon_family_id_pb2 as pogoprotos_dot_enums_dot_pokemon__family__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/inventory/candy.proto',
  package='pogoprotos.inventory',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n pogoprotos/inventory/candy.proto\x12\x14pogoprotos.inventory\x1a(pogoprotos/enums/pokemon_family_id.proto\"L\n\x05\x43\x61ndy\x12\x34\n\tfamily_id\x18\x01 \x01(\x0e\x32!.pogoprotos.enums.PokemonFamilyId\x12\r\n\x05\x63\x61ndy\x18\x02 \x01(\x05\x62\x06proto3'
  ,
  dependencies=[pogoprotos_dot_enums_dot_pokemon__family__id__pb2.DESCRIPTOR,])




_CANDY = _descriptor.Descriptor(
  name='Candy',
  full_name='pogoprotos.inventory.Candy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='family_id', full_name='pogoprotos.inventory.Candy.family_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='candy', full_name='pogoprotos.inventory.Candy.candy', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=100,
  serialized_end=176,
)

_CANDY.fields_by_name['family_id'].enum_type = pogoprotos_dot_enums_dot_pokemon__family__id__pb2._POKEMONFAMILYID
DESCRIPTOR.message_types_by_name['Candy'] = _CANDY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Candy = _reflection.GeneratedProtocolMessageType('Candy', (_message.Message,), {
  'DESCRIPTOR' : _CANDY,
  '__module__' : 'pogoprotos.inventory.candy_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.inventory.Candy)
  })
_sym_db.RegisterMessage(Candy)


# @@protoc_insertion_point(module_scope)
