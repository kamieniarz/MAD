# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/platform/responses/get_available_skus_and_balances_response.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.store import currency_quantity_pb2 as pogoprotos_dot_data_dot_store_dot_currency__quantity__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/platform/responses/get_available_skus_and_balances_response.proto',
  package='pogoprotos.networking.platform.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\nWpogoprotos/networking/platform/responses/get_available_skus_and_balances_response.proto\x12(pogoprotos.networking.platform.responses\x1a-pogoprotos/data/store/currency_quantity.proto\"\xb3\x07\n#GetAvailableSkusAndBalancesResponse\x12\x64\n\x06status\x18\x01 \x01(\x0e\x32T.pogoprotos.networking.platform.responses.GetAvailableSkusAndBalancesResponse.Status\x12q\n\ravailable_sku\x18\x02 \x03(\x0b\x32Z.pogoprotos.networking.platform.responses.GetAvailableSkusAndBalancesResponse.AvailableSku\x12\x42\n\x11player_currencies\x18\x03 \x03(\x0b\x32\'.pogoprotos.data.store.CurrencyQuantity\x12\x14\n\x0cplayer_token\x18\x04 \x01(\t\x1a\xc7\x03\n\x0c\x41vailableSku\x12\n\n\x02id\x18\x01 \x01(\t\x12\"\n\x1ais_third_party_vendor_item\x18\x02 \x01(\x08\x12\x36\n\x05price\x18\x03 \x01(\x0b\x32\'.pogoprotos.data.store.CurrencyQuantity\x12\x41\n\x10\x63urrency_granted\x18\x04 \x01(\x0b\x32\'.pogoprotos.data.store.CurrencyQuantity\x12x\n\x11game_item_content\x18\x05 \x03(\x0b\x32].pogoprotos.networking.platform.responses.GetAvailableSkusAndBalancesResponse.GameItemContent\x12x\n\x11presentation_data\x18\x06 \x03(\x0b\x32].pogoprotos.networking.platform.responses.GetAvailableSkusAndBalancesResponse.SkuPresentation\x12\x18\n\x10\x63\x61n_be_purchased\x18\x07 \x01(\x08\x1a\x31\n\x0fGameItemContent\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\x05\x1a-\n\x0fSkuPresentation\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"-\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0b\n\x07\x46\x41ILURE\x10\x02\x62\x06proto3'
  ,
  dependencies=[pogoprotos_dot_data_dot_store_dot_currency__quantity__pb2.DESCRIPTOR,])



_GETAVAILABLESKUSANDBALANCESRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.platform.responses.GetAvailableSkusAndBalancesResponse.Status',
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
  serialized_start=1083,
  serialized_end=1128,
)
_sym_db.RegisterEnumDescriptor(_GETAVAILABLESKUSANDBALANCESRESPONSE_STATUS)


_GETAVAILABLESKUSANDBALANCESRESPONSE_AVAILABLESKU = _descriptor.Descriptor(
  name='AvailableSku',
  full_name='pogoprotos.networking.platform.responses.GetAvailableSkusAndBalancesResponse.AvailableSku',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pogoprotos.networking.platform.responses.GetAvailableSkusAndBalancesResponse.AvailableSku.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_third_party_vendor_item', full_name='pogoprotos.networking.platform.responses.GetAvailableSkusAndBalancesResponse.AvailableSku.is_third_party_vendor_item', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='pogoprotos.networking.platform.responses.GetAvailableSkusAndBalancesResponse.AvailableSku.price', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currency_granted', full_name='pogoprotos.networking.platform.responses.GetAvailableSkusAndBalancesResponse.AvailableSku.currency_granted', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='game_item_content', full_name='pogoprotos.networking.platform.responses.GetAvailableSkusAndBalancesResponse.AvailableSku.game_item_content', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='presentation_data', full_name='pogoprotos.networking.platform.responses.GetAvailableSkusAndBalancesResponse.AvailableSku.presentation_data', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='can_be_purchased', full_name='pogoprotos.networking.platform.responses.GetAvailableSkusAndBalancesResponse.AvailableSku.can_be_purchased', index=6,
      number=7, type=8, cpp_type=7, label=1,
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
  serialized_start=528,
  serialized_end=983,
)

_GETAVAILABLESKUSANDBALANCESRESPONSE_GAMEITEMCONTENT = _descriptor.Descriptor(
  name='GameItemContent',
  full_name='pogoprotos.networking.platform.responses.GetAvailableSkusAndBalancesResponse.GameItemContent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='pogoprotos.networking.platform.responses.GetAvailableSkusAndBalancesResponse.GameItemContent.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='pogoprotos.networking.platform.responses.GetAvailableSkusAndBalancesResponse.GameItemContent.quantity', index=1,
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
  serialized_start=985,
  serialized_end=1034,
)

_GETAVAILABLESKUSANDBALANCESRESPONSE_SKUPRESENTATION = _descriptor.Descriptor(
  name='SkuPresentation',
  full_name='pogoprotos.networking.platform.responses.GetAvailableSkusAndBalancesResponse.SkuPresentation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='pogoprotos.networking.platform.responses.GetAvailableSkusAndBalancesResponse.SkuPresentation.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='pogoprotos.networking.platform.responses.GetAvailableSkusAndBalancesResponse.SkuPresentation.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=1036,
  serialized_end=1081,
)

_GETAVAILABLESKUSANDBALANCESRESPONSE = _descriptor.Descriptor(
  name='GetAvailableSkusAndBalancesResponse',
  full_name='pogoprotos.networking.platform.responses.GetAvailableSkusAndBalancesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.platform.responses.GetAvailableSkusAndBalancesResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='available_sku', full_name='pogoprotos.networking.platform.responses.GetAvailableSkusAndBalancesResponse.available_sku', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_currencies', full_name='pogoprotos.networking.platform.responses.GetAvailableSkusAndBalancesResponse.player_currencies', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_token', full_name='pogoprotos.networking.platform.responses.GetAvailableSkusAndBalancesResponse.player_token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETAVAILABLESKUSANDBALANCESRESPONSE_AVAILABLESKU, _GETAVAILABLESKUSANDBALANCESRESPONSE_GAMEITEMCONTENT, _GETAVAILABLESKUSANDBALANCESRESPONSE_SKUPRESENTATION, ],
  enum_types=[
    _GETAVAILABLESKUSANDBALANCESRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=181,
  serialized_end=1128,
)

_GETAVAILABLESKUSANDBALANCESRESPONSE_AVAILABLESKU.fields_by_name['price'].message_type = pogoprotos_dot_data_dot_store_dot_currency__quantity__pb2._CURRENCYQUANTITY
_GETAVAILABLESKUSANDBALANCESRESPONSE_AVAILABLESKU.fields_by_name['currency_granted'].message_type = pogoprotos_dot_data_dot_store_dot_currency__quantity__pb2._CURRENCYQUANTITY
_GETAVAILABLESKUSANDBALANCESRESPONSE_AVAILABLESKU.fields_by_name['game_item_content'].message_type = _GETAVAILABLESKUSANDBALANCESRESPONSE_GAMEITEMCONTENT
_GETAVAILABLESKUSANDBALANCESRESPONSE_AVAILABLESKU.fields_by_name['presentation_data'].message_type = _GETAVAILABLESKUSANDBALANCESRESPONSE_SKUPRESENTATION
_GETAVAILABLESKUSANDBALANCESRESPONSE_AVAILABLESKU.containing_type = _GETAVAILABLESKUSANDBALANCESRESPONSE
_GETAVAILABLESKUSANDBALANCESRESPONSE_GAMEITEMCONTENT.containing_type = _GETAVAILABLESKUSANDBALANCESRESPONSE
_GETAVAILABLESKUSANDBALANCESRESPONSE_SKUPRESENTATION.containing_type = _GETAVAILABLESKUSANDBALANCESRESPONSE
_GETAVAILABLESKUSANDBALANCESRESPONSE.fields_by_name['status'].enum_type = _GETAVAILABLESKUSANDBALANCESRESPONSE_STATUS
_GETAVAILABLESKUSANDBALANCESRESPONSE.fields_by_name['available_sku'].message_type = _GETAVAILABLESKUSANDBALANCESRESPONSE_AVAILABLESKU
_GETAVAILABLESKUSANDBALANCESRESPONSE.fields_by_name['player_currencies'].message_type = pogoprotos_dot_data_dot_store_dot_currency__quantity__pb2._CURRENCYQUANTITY
_GETAVAILABLESKUSANDBALANCESRESPONSE_STATUS.containing_type = _GETAVAILABLESKUSANDBALANCESRESPONSE
DESCRIPTOR.message_types_by_name['GetAvailableSkusAndBalancesResponse'] = _GETAVAILABLESKUSANDBALANCESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAvailableSkusAndBalancesResponse = _reflection.GeneratedProtocolMessageType('GetAvailableSkusAndBalancesResponse', (_message.Message,), {

  'AvailableSku' : _reflection.GeneratedProtocolMessageType('AvailableSku', (_message.Message,), {
    'DESCRIPTOR' : _GETAVAILABLESKUSANDBALANCESRESPONSE_AVAILABLESKU,
    '__module__' : 'pogoprotos.networking.platform.responses.get_available_skus_and_balances_response_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.responses.GetAvailableSkusAndBalancesResponse.AvailableSku)
    })
  ,

  'GameItemContent' : _reflection.GeneratedProtocolMessageType('GameItemContent', (_message.Message,), {
    'DESCRIPTOR' : _GETAVAILABLESKUSANDBALANCESRESPONSE_GAMEITEMCONTENT,
    '__module__' : 'pogoprotos.networking.platform.responses.get_available_skus_and_balances_response_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.responses.GetAvailableSkusAndBalancesResponse.GameItemContent)
    })
  ,

  'SkuPresentation' : _reflection.GeneratedProtocolMessageType('SkuPresentation', (_message.Message,), {
    'DESCRIPTOR' : _GETAVAILABLESKUSANDBALANCESRESPONSE_SKUPRESENTATION,
    '__module__' : 'pogoprotos.networking.platform.responses.get_available_skus_and_balances_response_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.responses.GetAvailableSkusAndBalancesResponse.SkuPresentation)
    })
  ,
  'DESCRIPTOR' : _GETAVAILABLESKUSANDBALANCESRESPONSE,
  '__module__' : 'pogoprotos.networking.platform.responses.get_available_skus_and_balances_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.responses.GetAvailableSkusAndBalancesResponse)
  })
_sym_db.RegisterMessage(GetAvailableSkusAndBalancesResponse)
_sym_db.RegisterMessage(GetAvailableSkusAndBalancesResponse.AvailableSku)
_sym_db.RegisterMessage(GetAvailableSkusAndBalancesResponse.GameItemContent)
_sym_db.RegisterMessage(GetAvailableSkusAndBalancesResponse.SkuPresentation)


# @@protoc_insertion_point(module_scope)
