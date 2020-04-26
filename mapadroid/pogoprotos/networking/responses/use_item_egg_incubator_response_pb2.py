# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/use_item_egg_incubator_response.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.inventory import egg_incubator_pb2 as pogoprotos_dot_inventory_dot_egg__incubator__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/use_item_egg_incubator_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\nEpogoprotos/networking/responses/use_item_egg_incubator_response.proto\x12\x1fpogoprotos.networking.responses\x1a(pogoprotos/inventory/egg_incubator.proto\"\x9f\x03\n\x1bUseItemEggIncubatorResponse\x12S\n\x06result\x18\x01 \x01(\x0e\x32\x43.pogoprotos.networking.responses.UseItemEggIncubatorResponse.Result\x12\x39\n\regg_incubator\x18\x02 \x01(\x0b\x32\".pogoprotos.inventory.EggIncubator\"\xef\x01\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x1d\n\x19\x45RROR_INCUBATOR_NOT_FOUND\x10\x02\x12\x1f\n\x1b\x45RROR_POKEMON_EGG_NOT_FOUND\x10\x03\x12\x1c\n\x18\x45RROR_POKEMON_ID_NOT_EGG\x10\x04\x12\"\n\x1e\x45RROR_INCUBATOR_ALREADY_IN_USE\x10\x05\x12$\n ERROR_POKEMON_ALREADY_INCUBATING\x10\x06\x12%\n!ERROR_INCUBATOR_NO_USES_REMAINING\x10\x07\x62\x06proto3'
  ,
  dependencies=[pogoprotos_dot_inventory_dot_egg__incubator__pb2.DESCRIPTOR,])



_USEITEMEGGINCUBATORRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.UseItemEggIncubatorResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INCUBATOR_NOT_FOUND', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_EGG_NOT_FOUND', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_ID_NOT_EGG', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INCUBATOR_ALREADY_IN_USE', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_ALREADY_INCUBATING', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INCUBATOR_NO_USES_REMAINING', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=325,
  serialized_end=564,
)
_sym_db.RegisterEnumDescriptor(_USEITEMEGGINCUBATORRESPONSE_RESULT)


_USEITEMEGGINCUBATORRESPONSE = _descriptor.Descriptor(
  name='UseItemEggIncubatorResponse',
  full_name='pogoprotos.networking.responses.UseItemEggIncubatorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.UseItemEggIncubatorResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='egg_incubator', full_name='pogoprotos.networking.responses.UseItemEggIncubatorResponse.egg_incubator', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _USEITEMEGGINCUBATORRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=149,
  serialized_end=564,
)

_USEITEMEGGINCUBATORRESPONSE.fields_by_name['result'].enum_type = _USEITEMEGGINCUBATORRESPONSE_RESULT
_USEITEMEGGINCUBATORRESPONSE.fields_by_name['egg_incubator'].message_type = pogoprotos_dot_inventory_dot_egg__incubator__pb2._EGGINCUBATOR
_USEITEMEGGINCUBATORRESPONSE_RESULT.containing_type = _USEITEMEGGINCUBATORRESPONSE
DESCRIPTOR.message_types_by_name['UseItemEggIncubatorResponse'] = _USEITEMEGGINCUBATORRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UseItemEggIncubatorResponse = _reflection.GeneratedProtocolMessageType('UseItemEggIncubatorResponse', (_message.Message,), {
  'DESCRIPTOR' : _USEITEMEGGINCUBATORRESPONSE,
  '__module__' : 'pogoprotos.networking.responses.use_item_egg_incubator_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.UseItemEggIncubatorResponse)
  })
_sym_db.RegisterMessage(UseItemEggIncubatorResponse)


# @@protoc_insertion_point(module_scope)
