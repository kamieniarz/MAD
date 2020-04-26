# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/game/gamepoi/game_poi_action.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/game/gamepoi/game_poi_action.proto',
  package='pogoprotos.networking.game.gamepoi',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n8pogoprotos/networking/game/gamepoi/game_poi_action.proto\x12\"pogoprotos.networking.game.gamepoi*\x8f\x04\n\rGamePoiAction\x12\x1b\n\x17UNKNOWN_GAME_POI_ACTION\x10\x00\x12\x11\n\x0b\x41\x44\x44_NEW_POI\x10\xe0\xeb%\x12\x1f\n\x19GET_AVAILABLE_SUBMISSIONS\x10\xe1\xeb%\x12%\n\x1fGET_SIGNED_URL_FOR_PHOTO_UPLOAD\x10\xe2\xeb%\x12\x16\n\x10SUBMIT_POI_IMAGE\x10\xc4\xec%\x12%\n\x1fSUBMIT_POI_TEXT_METADATA_UPDATE\x10\xc5\xec%\x12 \n\x1aSUBMIT_POI_LOCATION_UPDATE\x10\xc6\xec%\x12!\n\x1bSUBMIT_POI_TAKEDOWN_REQUEST\x10\xc7\xec%\x12\x1f\n\x19SUBMIT_SPONSOR_POI_REPORT\x10\xc8\xec%\x12(\n\"SUBMIT_SPONSOR_POI_LOCATION_UPDATE\x10\xc9\xec%\x12\x13\n\rADD_NEW_ROUTE\x10\xa8\xed%\x12\x1e\n\x18GENERATE_GMAP_SIGNED_URL\x10\x8c\xee%\x12\x17\n\x11GET_GMAP_SETTINGS\x10\x8d\xee%\x12\"\n\x1cSUBMIT_POI_AR_VIDEO_METADATA\x10\xf0\xee%\x12#\n\x1dGET_GRAPESHOT_FILE_UPLOAD_URL\x10\xf1\xee%\x12 \n\x1a\x41SYNC_FILE_UPLOAD_COMPLETE\x10\xf2\xee%b\x06proto3'
)

_GAMEPOIACTION = _descriptor.EnumDescriptor(
  name='GamePoiAction',
  full_name='pogoprotos.networking.game.gamepoi.GamePoiAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_GAME_POI_ACTION', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADD_NEW_POI', index=1, number=620000,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_AVAILABLE_SUBMISSIONS', index=2, number=620001,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_SIGNED_URL_FOR_PHOTO_UPLOAD', index=3, number=620002,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBMIT_POI_IMAGE', index=4, number=620100,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBMIT_POI_TEXT_METADATA_UPDATE', index=5, number=620101,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBMIT_POI_LOCATION_UPDATE', index=6, number=620102,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBMIT_POI_TAKEDOWN_REQUEST', index=7, number=620103,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBMIT_SPONSOR_POI_REPORT', index=8, number=620104,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBMIT_SPONSOR_POI_LOCATION_UPDATE', index=9, number=620105,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADD_NEW_ROUTE', index=10, number=620200,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GENERATE_GMAP_SIGNED_URL', index=11, number=620300,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_GMAP_SETTINGS', index=12, number=620301,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBMIT_POI_AR_VIDEO_METADATA', index=13, number=620400,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_GRAPESHOT_FILE_UPLOAD_URL', index=14, number=620401,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ASYNC_FILE_UPLOAD_COMPLETE', index=15, number=620402,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=97,
  serialized_end=624,
)
_sym_db.RegisterEnumDescriptor(_GAMEPOIACTION)

GamePoiAction = enum_type_wrapper.EnumTypeWrapper(_GAMEPOIACTION)
UNKNOWN_GAME_POI_ACTION = 0
ADD_NEW_POI = 620000
GET_AVAILABLE_SUBMISSIONS = 620001
GET_SIGNED_URL_FOR_PHOTO_UPLOAD = 620002
SUBMIT_POI_IMAGE = 620100
SUBMIT_POI_TEXT_METADATA_UPDATE = 620101
SUBMIT_POI_LOCATION_UPDATE = 620102
SUBMIT_POI_TAKEDOWN_REQUEST = 620103
SUBMIT_SPONSOR_POI_REPORT = 620104
SUBMIT_SPONSOR_POI_LOCATION_UPDATE = 620105
ADD_NEW_ROUTE = 620200
GENERATE_GMAP_SIGNED_URL = 620300
GET_GMAP_SETTINGS = 620301
SUBMIT_POI_AR_VIDEO_METADATA = 620400
GET_GRAPESHOT_FILE_UPLOAD_URL = 620401
ASYNC_FILE_UPLOAD_COMPLETE = 620402


DESCRIPTOR.enum_types_by_name['GamePoiAction'] = _GAMEPOIACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
