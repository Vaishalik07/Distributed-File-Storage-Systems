# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fileService.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='fileService.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11\x66ileService.proto\"v\n\x08\x46ileData\x12\x1c\n\x14initialReplicaServer\x18\x01 \x01(\t\x12\x11\n\tbytearray\x18\x02 \x01(\x0c\x12\x0e\n\x06vClock\x18\x03 \x01(\t\x12\x15\n\rshortest_path\x18\x04 \x03(\t\x12\x12\n\ncurrentpos\x18\x05 \x01(\x05\"\'\n\x03\x61\x63k\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2/\n\x0b\x46ileservice\x12 \n\rReplicateFile\x12\t.FileData\x1a\x04.ackb\x06proto3')
)




_FILEDATA = _descriptor.Descriptor(
  name='FileData',
  full_name='FileData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='initialReplicaServer', full_name='FileData.initialReplicaServer', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytearray', full_name='FileData.bytearray', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vClock', full_name='FileData.vClock', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shortest_path', full_name='FileData.shortest_path', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currentpos', full_name='FileData.currentpos', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_start=21,
  serialized_end=139,
)


_ACK = _descriptor.Descriptor(
  name='ack',
  full_name='ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='ack.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='ack.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=141,
  serialized_end=180,
)

DESCRIPTOR.message_types_by_name['FileData'] = _FILEDATA
DESCRIPTOR.message_types_by_name['ack'] = _ACK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FileData = _reflection.GeneratedProtocolMessageType('FileData', (_message.Message,), {
  'DESCRIPTOR' : _FILEDATA,
  '__module__' : 'fileService_pb2'
  # @@protoc_insertion_point(class_scope:FileData)
  })
_sym_db.RegisterMessage(FileData)

ack = _reflection.GeneratedProtocolMessageType('ack', (_message.Message,), {
  'DESCRIPTOR' : _ACK,
  '__module__' : 'fileService_pb2'
  # @@protoc_insertion_point(class_scope:ack)
  })
_sym_db.RegisterMessage(ack)



_FILESERVICE = _descriptor.ServiceDescriptor(
  name='Fileservice',
  full_name='Fileservice',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=182,
  serialized_end=229,
  methods=[
  _descriptor.MethodDescriptor(
    name='ReplicateFile',
    full_name='Fileservice.ReplicateFile',
    index=0,
    containing_service=None,
    input_type=_FILEDATA,
    output_type=_ACK,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FILESERVICE)

DESCRIPTOR.services_by_name['Fileservice'] = _FILESERVICE

# @@protoc_insertion_point(module_scope)