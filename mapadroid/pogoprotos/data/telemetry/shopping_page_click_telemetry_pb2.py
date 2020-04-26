# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/shopping_page_click_telemetry.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import telemetry_ids_pb2 as pogoprotos_dot_enums_dot_telemetry__ids__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/shopping_page_click_telemetry.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n=pogoprotos/data/telemetry/shopping_page_click_telemetry.proto\x12\x19pogoprotos.data.telemetry\x1a$pogoprotos/enums/telemetry_ids.proto\"\x85\x07\n\x1aShoppingPageClickTelemetry\x12J\n\x16shopping_page_click_id\x18\x01 \x01(\x0e\x32*.pogoprotos.enums.ShoppingPageTelemetryIds\x12u\n\x1ashopping_page_click_source\x18\x02 \x01(\x0e\x32Q.pogoprotos.data.telemetry.ShoppingPageClickTelemetry.ShoppingPageTelemetrySource\x12\x10\n\x08item_sku\x18\x03 \x01(\t\x12\x10\n\x08has_item\x18\x04 \x01(\x08\"\xff\x04\n\x1bShoppingPageTelemetrySource\x12\"\n\x1eUNDEFINED_SHOPPING_PAGE_SOURCE\x10\x00\x12\x14\n\x10SOURCE_MAIN_MENU\x10\x01\x12\x1b\n\x17SOURCE_POKEMON_BAG_FULL\x10\x02\x12\x1d\n\x19SOURCE_INCUBATOR_SELECTOR\x10\x03\x12$\n SOURCE_POKESTOP_DISK_INTERACTION\x10\x04\x12\x1d\n\x19SOURCE_OPEN_GIFT_BAG_FULL\x10\x05\x12(\n$SOURCE_QUICK_SHOP_BAG_FULL_ENCOUNTER\x10\x06\x12#\n\x1fSOURCE_QUICK_SHOP_BAG_FULL_RAID\x10\x07\x12\x1a\n\x16SOURCE_QUICK_SHOP_MORE\x10\x08\x12\x16\n\x12SOURCE_AVATAR_ITEM\x10\t\x12\x1c\n\x18SOURCE_POKEMON_ENCOUNTER\x10\n\x12\x1e\n\x1aSOURCE_PLAYER_PROFILE_PAGE\x10\x0b\x12\x16\n\x12SOURCE_STORE_FRONT\x10\x0c\x12%\n!SOURCE_AVATAR_CUSTOMIZATION_AWARD\x10\r\x12\x1f\n\x1bSOURCE_FIRST_TIME_USER_FLOW\x10\x0e\x12%\n!SOURCE_BADGE_DETAIL_AVATAR_REWARD\x10\x0f\x12.\n*SOURCE_QUICK_SHOP_BUDDY_INTERACTION_POFFIN\x10\x64\x12-\n)SOURCE_QUICK_SHOP_BUDDY_QUICK_FEED_POFFIN\x10\x65\x62\x06proto3'
  ,
  dependencies=[pogoprotos_dot_enums_dot_telemetry__ids__pb2.DESCRIPTOR,])



_SHOPPINGPAGECLICKTELEMETRY_SHOPPINGPAGETELEMETRYSOURCE = _descriptor.EnumDescriptor(
  name='ShoppingPageTelemetrySource',
  full_name='pogoprotos.data.telemetry.ShoppingPageClickTelemetry.ShoppingPageTelemetrySource',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED_SHOPPING_PAGE_SOURCE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOURCE_MAIN_MENU', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOURCE_POKEMON_BAG_FULL', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOURCE_INCUBATOR_SELECTOR', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOURCE_POKESTOP_DISK_INTERACTION', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOURCE_OPEN_GIFT_BAG_FULL', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOURCE_QUICK_SHOP_BAG_FULL_ENCOUNTER', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOURCE_QUICK_SHOP_BAG_FULL_RAID', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOURCE_QUICK_SHOP_MORE', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOURCE_AVATAR_ITEM', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOURCE_POKEMON_ENCOUNTER', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOURCE_PLAYER_PROFILE_PAGE', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOURCE_STORE_FRONT', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOURCE_AVATAR_CUSTOMIZATION_AWARD', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOURCE_FIRST_TIME_USER_FLOW', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOURCE_BADGE_DETAIL_AVATAR_REWARD', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOURCE_QUICK_SHOP_BUDDY_INTERACTION_POFFIN', index=16, number=100,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOURCE_QUICK_SHOP_BUDDY_QUICK_FEED_POFFIN', index=17, number=101,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=393,
  serialized_end=1032,
)
_sym_db.RegisterEnumDescriptor(_SHOPPINGPAGECLICKTELEMETRY_SHOPPINGPAGETELEMETRYSOURCE)


_SHOPPINGPAGECLICKTELEMETRY = _descriptor.Descriptor(
  name='ShoppingPageClickTelemetry',
  full_name='pogoprotos.data.telemetry.ShoppingPageClickTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shopping_page_click_id', full_name='pogoprotos.data.telemetry.ShoppingPageClickTelemetry.shopping_page_click_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shopping_page_click_source', full_name='pogoprotos.data.telemetry.ShoppingPageClickTelemetry.shopping_page_click_source', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_sku', full_name='pogoprotos.data.telemetry.ShoppingPageClickTelemetry.item_sku', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='has_item', full_name='pogoprotos.data.telemetry.ShoppingPageClickTelemetry.has_item', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SHOPPINGPAGECLICKTELEMETRY_SHOPPINGPAGETELEMETRYSOURCE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=131,
  serialized_end=1032,
)

_SHOPPINGPAGECLICKTELEMETRY.fields_by_name['shopping_page_click_id'].enum_type = pogoprotos_dot_enums_dot_telemetry__ids__pb2._SHOPPINGPAGETELEMETRYIDS
_SHOPPINGPAGECLICKTELEMETRY.fields_by_name['shopping_page_click_source'].enum_type = _SHOPPINGPAGECLICKTELEMETRY_SHOPPINGPAGETELEMETRYSOURCE
_SHOPPINGPAGECLICKTELEMETRY_SHOPPINGPAGETELEMETRYSOURCE.containing_type = _SHOPPINGPAGECLICKTELEMETRY
DESCRIPTOR.message_types_by_name['ShoppingPageClickTelemetry'] = _SHOPPINGPAGECLICKTELEMETRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ShoppingPageClickTelemetry = _reflection.GeneratedProtocolMessageType('ShoppingPageClickTelemetry', (_message.Message,), {
  'DESCRIPTOR' : _SHOPPINGPAGECLICKTELEMETRY,
  '__module__' : 'pogoprotos.data.telemetry.shopping_page_click_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.ShoppingPageClickTelemetry)
  })
_sym_db.RegisterMessage(ShoppingPageClickTelemetry)


# @@protoc_insertion_point(module_scope)
