# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/item/pokeball_attributes.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import item_effect_pb2 as pogoprotos_dot_enums_dot_item__effect__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/item/pokeball_attributes.proto',
  package='pogoprotos.settings.master.item',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n9pogoprotos/settings/master/item/pokeball_attributes.proto\x12\x1fpogoprotos.settings.master.item\x1a\"pogoprotos/enums/item_effect.proto\"\x95\x01\n\x12PokeballAttributes\x12\x31\n\x0bitem_effect\x18\x01 \x01(\x0e\x32\x1c.pogoprotos.enums.ItemEffect\x12\x15\n\rcapture_multi\x18\x02 \x01(\x02\x12\x1c\n\x14\x63\x61pture_multi_effect\x18\x03 \x01(\x02\x12\x17\n\x0fitem_effect_mod\x18\x04 \x01(\x02\x62\x06proto3'
  ,
  dependencies=[pogoprotos_dot_enums_dot_item__effect__pb2.DESCRIPTOR,])




_POKEBALLATTRIBUTES = _descriptor.Descriptor(
  name='PokeballAttributes',
  full_name='pogoprotos.settings.master.item.PokeballAttributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_effect', full_name='pogoprotos.settings.master.item.PokeballAttributes.item_effect', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='capture_multi', full_name='pogoprotos.settings.master.item.PokeballAttributes.capture_multi', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='capture_multi_effect', full_name='pogoprotos.settings.master.item.PokeballAttributes.capture_multi_effect', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_effect_mod', full_name='pogoprotos.settings.master.item.PokeballAttributes.item_effect_mod', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=131,
  serialized_end=280,
)

_POKEBALLATTRIBUTES.fields_by_name['item_effect'].enum_type = pogoprotos_dot_enums_dot_item__effect__pb2._ITEMEFFECT
DESCRIPTOR.message_types_by_name['PokeballAttributes'] = _POKEBALLATTRIBUTES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PokeballAttributes = _reflection.GeneratedProtocolMessageType('PokeballAttributes', (_message.Message,), {
  'DESCRIPTOR' : _POKEBALLATTRIBUTES,
  '__module__' : 'pogoprotos.settings.master.item.pokeball_attributes_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.item.PokeballAttributes)
  })
_sym_db.RegisterMessage(PokeballAttributes)


# @@protoc_insertion_point(module_scope)
