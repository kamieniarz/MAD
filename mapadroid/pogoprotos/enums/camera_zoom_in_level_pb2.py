# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/camera_zoom_in_level.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/camera_zoom_in_level.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n+pogoprotos/enums/camera_zoom_in_level.proto\x12\x10pogoprotos.enums*\x98\x01\n\x11\x43\x61meraZoomInLevel\x12 \n\x1c\x44\x45\x46\x41ULT_CAMERA_ZOOM_IN_LEVEL\x10\x00\x12\x1d\n\x19NICE_CAMERA_ZOOM_IN_LEVEL\x10\x01\x12\x1e\n\x1aGREAT_CAMERA_ZOOM_IN_LEVEL\x10\x02\x12\"\n\x1e\x45XCELLENT_CAMERA_ZOOM_IN_LEVEL\x10\x03\x62\x06proto3'
)

_CAMERAZOOMINLEVEL = _descriptor.EnumDescriptor(
  name='CameraZoomInLevel',
  full_name='pogoprotos.enums.CameraZoomInLevel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT_CAMERA_ZOOM_IN_LEVEL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NICE_CAMERA_ZOOM_IN_LEVEL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GREAT_CAMERA_ZOOM_IN_LEVEL', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXCELLENT_CAMERA_ZOOM_IN_LEVEL', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=66,
  serialized_end=218,
)
_sym_db.RegisterEnumDescriptor(_CAMERAZOOMINLEVEL)

CameraZoomInLevel = enum_type_wrapper.EnumTypeWrapper(_CAMERAZOOMINLEVEL)
DEFAULT_CAMERA_ZOOM_IN_LEVEL = 0
NICE_CAMERA_ZOOM_IN_LEVEL = 1
GREAT_CAMERA_ZOOM_IN_LEVEL = 2
EXCELLENT_CAMERA_ZOOM_IN_LEVEL = 3


DESCRIPTOR.enum_types_by_name['CameraZoomInLevel'] = _CAMERAZOOMINLEVEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
