# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/get_photobomb_response.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import pokemon_id_pb2 as pogoprotos_dot_enums_dot_pokemon__id__pb2
from pogoprotos.data import pokemon_display_pb2 as pogoprotos_dot_data_dot_pokemon__display__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/get_photobomb_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n<pogoprotos/networking/responses/get_photobomb_response.proto\x12\x1fpogoprotos.networking.responses\x1a!pogoprotos/enums/pokemon_id.proto\x1a%pogoprotos/data/pokemon_display.proto\"\xa9\x03\n\x14GetPhotobombResponse\x12L\n\x06status\x18\x01 \x01(\x0e\x32<.pogoprotos.networking.responses.GetPhotobombResponse.Status\x12/\n\npokemon_id\x18\x02 \x01(\x0e\x32\x1b.pogoprotos.enums.PokemonId\x12\x0b\n\x03lat\x18\x03 \x01(\x01\x12\x0b\n\x03lng\x18\x04 \x01(\x01\x12\x1a\n\x12\x65ncounter_location\x18\x05 \x01(\t\x12\x14\n\x0c\x65ncounter_id\x18\x06 \x01(\x06\x12\x19\n\x11\x64isappear_time_ms\x18\x07 \x01(\x03\x12\x38\n\x0fpokemon_display\x18\x08 \x01(\x0b\x32\x1f.pogoprotos.data.PokemonDisplay\"q\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x1b\n\x17PHOTOBOMB_NOT_AVAILABLE\x10\x02\x12\x1f\n\x1b\x45NCOUNTER_ALREADY_COMPLETED\x10\x03\x12\x11\n\rERROR_UNKNOWN\x10\x04\x62\x06proto3'
  ,
  dependencies=[pogoprotos_dot_enums_dot_pokemon__id__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_pokemon__display__pb2.DESCRIPTOR,])



_GETPHOTOBOMBRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.responses.GetPhotobombResponse.Status',
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
      name='PHOTOBOMB_NOT_AVAILABLE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENCOUNTER_ALREADY_COMPLETED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_UNKNOWN', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=484,
  serialized_end=597,
)
_sym_db.RegisterEnumDescriptor(_GETPHOTOBOMBRESPONSE_STATUS)


_GETPHOTOBOMBRESPONSE = _descriptor.Descriptor(
  name='GetPhotobombResponse',
  full_name='pogoprotos.networking.responses.GetPhotobombResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.responses.GetPhotobombResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='pogoprotos.networking.responses.GetPhotobombResponse.pokemon_id', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lat', full_name='pogoprotos.networking.responses.GetPhotobombResponse.lat', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lng', full_name='pogoprotos.networking.responses.GetPhotobombResponse.lng', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encounter_location', full_name='pogoprotos.networking.responses.GetPhotobombResponse.encounter_location', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encounter_id', full_name='pogoprotos.networking.responses.GetPhotobombResponse.encounter_id', index=5,
      number=6, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disappear_time_ms', full_name='pogoprotos.networking.responses.GetPhotobombResponse.disappear_time_ms', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pokemon_display', full_name='pogoprotos.networking.responses.GetPhotobombResponse.pokemon_display', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETPHOTOBOMBRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=172,
  serialized_end=597,
)

_GETPHOTOBOMBRESPONSE.fields_by_name['status'].enum_type = _GETPHOTOBOMBRESPONSE_STATUS
_GETPHOTOBOMBRESPONSE.fields_by_name['pokemon_id'].enum_type = pogoprotos_dot_enums_dot_pokemon__id__pb2._POKEMONID
_GETPHOTOBOMBRESPONSE.fields_by_name['pokemon_display'].message_type = pogoprotos_dot_data_dot_pokemon__display__pb2._POKEMONDISPLAY
_GETPHOTOBOMBRESPONSE_STATUS.containing_type = _GETPHOTOBOMBRESPONSE
DESCRIPTOR.message_types_by_name['GetPhotobombResponse'] = _GETPHOTOBOMBRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetPhotobombResponse = _reflection.GeneratedProtocolMessageType('GetPhotobombResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPHOTOBOMBRESPONSE,
  '__module__' : 'pogoprotos.networking.responses.get_photobomb_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GetPhotobombResponse)
  })
_sym_db.RegisterMessage(GetPhotobombResponse)


# @@protoc_insertion_point(module_scope)
