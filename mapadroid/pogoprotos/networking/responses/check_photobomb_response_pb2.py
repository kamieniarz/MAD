# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/check_photobomb_response.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data import pokemon_display_pb2 as pogoprotos_dot_data_dot_pokemon__display__pb2
from pogoprotos.enums import pokemon_id_pb2 as pogoprotos_dot_enums_dot_pokemon__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/check_photobomb_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n>pogoprotos/networking/responses/check_photobomb_response.proto\x12\x1fpogoprotos.networking.responses\x1a%pogoprotos/data/pokemon_display.proto\x1a!pogoprotos/enums/pokemon_id.proto\"\xe0\x02\n\x16\x43heckPhotobombResponse\x12N\n\x06status\x18\x01 \x01(\x0e\x32>.pogoprotos.networking.responses.CheckPhotobombResponse.Status\x12\x39\n\x14photobomb_pokemon_id\x18\x02 \x01(\x0e\x32\x1b.pogoprotos.enums.PokemonId\x12\x42\n\x19photobomb_pokemon_display\x18\x03 \x01(\x0b\x32\x1f.pogoprotos.data.PokemonDisplay\x12\x14\n\x0c\x65ncounter_id\x18\x04 \x01(\x06\x12\x0b\n\x03uri\x18\x05 \x01(\t\"T\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x1f\n\x1b\x45RROR_PHOTO_POKEMON_INVALID\x10\x02\x12\x11\n\rERROR_UNKNOWN\x10\x03\x62\x06proto3'
  ,
  dependencies=[pogoprotos_dot_data_dot_pokemon__display__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_pokemon__id__pb2.DESCRIPTOR,])



_CHECKPHOTOBOMBRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.responses.CheckPhotobombResponse.Status',
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
      name='ERROR_PHOTO_POKEMON_INVALID', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_UNKNOWN', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=442,
  serialized_end=526,
)
_sym_db.RegisterEnumDescriptor(_CHECKPHOTOBOMBRESPONSE_STATUS)


_CHECKPHOTOBOMBRESPONSE = _descriptor.Descriptor(
  name='CheckPhotobombResponse',
  full_name='pogoprotos.networking.responses.CheckPhotobombResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.responses.CheckPhotobombResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='photobomb_pokemon_id', full_name='pogoprotos.networking.responses.CheckPhotobombResponse.photobomb_pokemon_id', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='photobomb_pokemon_display', full_name='pogoprotos.networking.responses.CheckPhotobombResponse.photobomb_pokemon_display', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encounter_id', full_name='pogoprotos.networking.responses.CheckPhotobombResponse.encounter_id', index=3,
      number=4, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uri', full_name='pogoprotos.networking.responses.CheckPhotobombResponse.uri', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CHECKPHOTOBOMBRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=174,
  serialized_end=526,
)

_CHECKPHOTOBOMBRESPONSE.fields_by_name['status'].enum_type = _CHECKPHOTOBOMBRESPONSE_STATUS
_CHECKPHOTOBOMBRESPONSE.fields_by_name['photobomb_pokemon_id'].enum_type = pogoprotos_dot_enums_dot_pokemon__id__pb2._POKEMONID
_CHECKPHOTOBOMBRESPONSE.fields_by_name['photobomb_pokemon_display'].message_type = pogoprotos_dot_data_dot_pokemon__display__pb2._POKEMONDISPLAY
_CHECKPHOTOBOMBRESPONSE_STATUS.containing_type = _CHECKPHOTOBOMBRESPONSE
DESCRIPTOR.message_types_by_name['CheckPhotobombResponse'] = _CHECKPHOTOBOMBRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CheckPhotobombResponse = _reflection.GeneratedProtocolMessageType('CheckPhotobombResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHECKPHOTOBOMBRESPONSE,
  '__module__' : 'pogoprotos.networking.responses.check_photobomb_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.CheckPhotobombResponse)
  })
_sym_db.RegisterMessage(CheckPhotobombResponse)


# @@protoc_insertion_point(module_scope)
