# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/game/gameiap/responses/set_in_game_currency_exchange_rate_response.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/game/gameiap/responses/set_in_game_currency_exchange_rate_response.proto',
  package='pogoprotos.networking.game.gameiap.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n^pogoprotos/networking/game/gameiap/responses/set_in_game_currency_exchange_rate_response.proto\x12,pogoprotos.networking.game.gameiap.responses\"\xc2\x01\n%SetInGameCurrencyExchangeRateResponse\x12j\n\x06status\x18\x01 \x01(\x0e\x32Z.pogoprotos.networking.game.gameiap.responses.SetInGameCurrencyExchangeRateResponse.Status\"-\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0b\n\x07\x46\x41ILURE\x10\x02\x62\x06proto3'
)



_SETINGAMECURRENCYEXCHANGERATERESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.game.gameiap.responses.SetInGameCurrencyExchangeRateResponse.Status',
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
      name='FAILURE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=294,
  serialized_end=339,
)
_sym_db.RegisterEnumDescriptor(_SETINGAMECURRENCYEXCHANGERATERESPONSE_STATUS)


_SETINGAMECURRENCYEXCHANGERATERESPONSE = _descriptor.Descriptor(
  name='SetInGameCurrencyExchangeRateResponse',
  full_name='pogoprotos.networking.game.gameiap.responses.SetInGameCurrencyExchangeRateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.game.gameiap.responses.SetInGameCurrencyExchangeRateResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SETINGAMECURRENCYEXCHANGERATERESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=145,
  serialized_end=339,
)

_SETINGAMECURRENCYEXCHANGERATERESPONSE.fields_by_name['status'].enum_type = _SETINGAMECURRENCYEXCHANGERATERESPONSE_STATUS
_SETINGAMECURRENCYEXCHANGERATERESPONSE_STATUS.containing_type = _SETINGAMECURRENCYEXCHANGERATERESPONSE
DESCRIPTOR.message_types_by_name['SetInGameCurrencyExchangeRateResponse'] = _SETINGAMECURRENCYEXCHANGERATERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SetInGameCurrencyExchangeRateResponse = _reflection.GeneratedProtocolMessageType('SetInGameCurrencyExchangeRateResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETINGAMECURRENCYEXCHANGERATERESPONSE,
  '__module__' : 'pogoprotos.networking.game.gameiap.responses.set_in_game_currency_exchange_rate_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.game.gameiap.responses.SetInGameCurrencyExchangeRateResponse)
  })
_sym_db.RegisterMessage(SetInGameCurrencyExchangeRateResponse)


# @@protoc_insertion_point(module_scope)
