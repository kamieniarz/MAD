# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/camera_interpolation.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/camera_interpolation.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n+pogoprotos/enums/camera_interpolation.proto\x12\x10pogoprotos.enums*\x96\x01\n\x13\x43\x61meraInterpolation\x12\x12\n\x0e\x43\x41M_INTERP_CUT\x10\x00\x12\x15\n\x11\x43\x41M_INTERP_LINEAR\x10\x01\x12\x15\n\x11\x43\x41M_INTERP_SMOOTH\x10\x02\x12%\n!CAM_INTERP_SMOOTH_ROT_LINEAR_MOVE\x10\x03\x12\x16\n\x12\x43\x41M_INTERP_DEPENDS\x10\x04\x62\x06proto3'
)

_CAMERAINTERPOLATION = _descriptor.EnumDescriptor(
  name='CameraInterpolation',
  full_name='pogoprotos.enums.CameraInterpolation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CAM_INTERP_CUT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAM_INTERP_LINEAR', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAM_INTERP_SMOOTH', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAM_INTERP_SMOOTH_ROT_LINEAR_MOVE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAM_INTERP_DEPENDS', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=66,
  serialized_end=216,
)
_sym_db.RegisterEnumDescriptor(_CAMERAINTERPOLATION)

CameraInterpolation = enum_type_wrapper.EnumTypeWrapper(_CAMERAINTERPOLATION)
CAM_INTERP_CUT = 0
CAM_INTERP_LINEAR = 1
CAM_INTERP_SMOOTH = 2
CAM_INTERP_SMOOTH_ROT_LINEAR_MOVE = 3
CAM_INTERP_DEPENDS = 4


DESCRIPTOR.enum_types_by_name['CameraInterpolation'] = _CAMERAINTERPOLATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
