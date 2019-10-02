# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/core/CoreService.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from feast.core import FeatureSet_pb2 as feast_dot_core_dot_FeatureSet__pb2
from feast.core import Store_pb2 as feast_dot_core_dot_Store__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="feast/core/CoreService.proto",
    package="feast.core",
    syntax="proto3",
    serialized_options=_b(
        "\n\nfeast.coreB\020CoreServiceProtoZ/github.com/gojek/feast/sdk/go/protos/feast/core"
    ),
    serialized_pb=_b(
        '\n\x1c\x66\x65\x61st/core/CoreService.proto\x12\nfeast.core\x1a\x1b\x66\x65\x61st/core/FeatureSet.proto\x1a\x16\x66\x65\x61st/core/Store.proto"\x92\x01\n\x15GetFeatureSetsRequest\x12\x38\n\x06\x66ilter\x18\x01 \x01(\x0b\x32(.feast.core.GetFeatureSetsRequest.Filter\x1a?\n\x06\x46ilter\x12\x18\n\x10\x66\x65\x61ture_set_name\x18\x01 \x01(\t\x12\x1b\n\x13\x66\x65\x61ture_set_version\x18\x02 \x01(\t"J\n\x16GetFeatureSetsResponse\x12\x30\n\x0c\x66\x65\x61ture_sets\x18\x01 \x03(\x0b\x32\x1a.feast.core.FeatureSetSpec"_\n\x10GetStoresRequest\x12\x33\n\x06\x66ilter\x18\x01 \x01(\x0b\x32#.feast.core.GetStoresRequest.Filter\x1a\x16\n\x06\x46ilter\x12\x0c\n\x04name\x18\x01 \x01(\t"5\n\x11GetStoresResponse\x12 \n\x05store\x18\x01 \x03(\x0b\x32\x11.feast.core.Store"I\n\x16\x41pplyFeatureSetRequest\x12/\n\x0b\x66\x65\x61ture_set\x18\x01 \x01(\x0b\x32\x1a.feast.core.FeatureSetSpec"\xb7\x01\n\x17\x41pplyFeatureSetResponse\x12/\n\x0b\x66\x65\x61ture_set\x18\x01 \x01(\x0b\x32\x1a.feast.core.FeatureSetSpec\x12:\n\x06status\x18\x02 \x01(\x0e\x32*.feast.core.ApplyFeatureSetResponse.Status"/\n\x06Status\x12\r\n\tNO_CHANGE\x10\x00\x12\x0b\n\x07\x43REATED\x10\x01\x12\t\n\x05\x45RROR\x10\x02"\x1c\n\x1aGetFeastCoreVersionRequest".\n\x1bGetFeastCoreVersionResponse\x12\x0f\n\x07version\x18\x01 \x01(\t2\xf4\x02\n\x0b\x43oreService\x12\x66\n\x13GetFeastCoreVersion\x12&.feast.core.GetFeastCoreVersionRequest\x1a\'.feast.core.GetFeastCoreVersionResponse\x12W\n\x0eGetFeatureSets\x12!.feast.core.GetFeatureSetsRequest\x1a".feast.core.GetFeatureSetsResponse\x12H\n\tGetStores\x12\x1c.feast.core.GetStoresRequest\x1a\x1d.feast.core.GetStoresResponse\x12Z\n\x0f\x41pplyFeatureSet\x12".feast.core.ApplyFeatureSetRequest\x1a#.feast.core.ApplyFeatureSetResponseBO\n\nfeast.coreB\x10\x43oreServiceProtoZ/github.com/gojek/feast/sdk/go/protos/feast/coreb\x06proto3'
    ),
    dependencies=[
        feast_dot_core_dot_FeatureSet__pb2.DESCRIPTOR,
        feast_dot_core_dot_Store__pb2.DESCRIPTOR,
    ],
)


_APPLYFEATURESETRESPONSE_STATUS = _descriptor.EnumDescriptor(
    name="Status",
    full_name="feast.core.ApplyFeatureSetResponse.Status",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="NO_CHANGE", index=0, number=0, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="CREATED", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR", index=2, number=2, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=686,
    serialized_end=733,
)
_sym_db.RegisterEnumDescriptor(_APPLYFEATURESETRESPONSE_STATUS)


_GETFEATURESETSREQUEST_FILTER = _descriptor.Descriptor(
    name="Filter",
    full_name="feast.core.GetFeatureSetsRequest.Filter",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="feature_set_name",
            full_name="feast.core.GetFeatureSetsRequest.Filter.feature_set_name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="feature_set_version",
            full_name="feast.core.GetFeatureSetsRequest.Filter.feature_set_version",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=181,
    serialized_end=244,
)

_GETFEATURESETSREQUEST = _descriptor.Descriptor(
    name="GetFeatureSetsRequest",
    full_name="feast.core.GetFeatureSetsRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="filter",
            full_name="feast.core.GetFeatureSetsRequest.filter",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[_GETFEATURESETSREQUEST_FILTER],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=98,
    serialized_end=244,
)


_GETFEATURESETSRESPONSE = _descriptor.Descriptor(
    name="GetFeatureSetsResponse",
    full_name="feast.core.GetFeatureSetsResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="feature_sets",
            full_name="feast.core.GetFeatureSetsResponse.feature_sets",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=246,
    serialized_end=320,
)


_GETSTORESREQUEST_FILTER = _descriptor.Descriptor(
    name="Filter",
    full_name="feast.core.GetStoresRequest.Filter",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="feast.core.GetStoresRequest.Filter.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=395,
    serialized_end=417,
)

_GETSTORESREQUEST = _descriptor.Descriptor(
    name="GetStoresRequest",
    full_name="feast.core.GetStoresRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="filter",
            full_name="feast.core.GetStoresRequest.filter",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[_GETSTORESREQUEST_FILTER],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=322,
    serialized_end=417,
)


_GETSTORESRESPONSE = _descriptor.Descriptor(
    name="GetStoresResponse",
    full_name="feast.core.GetStoresResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="store",
            full_name="feast.core.GetStoresResponse.store",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=419,
    serialized_end=472,
)


_APPLYFEATURESETREQUEST = _descriptor.Descriptor(
    name="ApplyFeatureSetRequest",
    full_name="feast.core.ApplyFeatureSetRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="feature_set",
            full_name="feast.core.ApplyFeatureSetRequest.feature_set",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=474,
    serialized_end=547,
)


_APPLYFEATURESETRESPONSE = _descriptor.Descriptor(
    name="ApplyFeatureSetResponse",
    full_name="feast.core.ApplyFeatureSetResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="feature_set",
            full_name="feast.core.ApplyFeatureSetResponse.feature_set",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="status",
            full_name="feast.core.ApplyFeatureSetResponse.status",
            index=1,
            number=2,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_APPLYFEATURESETRESPONSE_STATUS],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=550,
    serialized_end=733,
)


_GETFEASTCOREVERSIONREQUEST = _descriptor.Descriptor(
    name="GetFeastCoreVersionRequest",
    full_name="feast.core.GetFeastCoreVersionRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=735,
    serialized_end=763,
)


_GETFEASTCOREVERSIONRESPONSE = _descriptor.Descriptor(
    name="GetFeastCoreVersionResponse",
    full_name="feast.core.GetFeastCoreVersionResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="version",
            full_name="feast.core.GetFeastCoreVersionResponse.version",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=765,
    serialized_end=811,
)

_GETFEATURESETSREQUEST_FILTER.containing_type = _GETFEATURESETSREQUEST
_GETFEATURESETSREQUEST.fields_by_name[
    "filter"
].message_type = _GETFEATURESETSREQUEST_FILTER
_GETFEATURESETSRESPONSE.fields_by_name[
    "feature_sets"
].message_type = feast_dot_core_dot_FeatureSet__pb2._FEATURESETSPEC
_GETSTORESREQUEST_FILTER.containing_type = _GETSTORESREQUEST
_GETSTORESREQUEST.fields_by_name["filter"].message_type = _GETSTORESREQUEST_FILTER
_GETSTORESRESPONSE.fields_by_name[
    "store"
].message_type = feast_dot_core_dot_Store__pb2._STORE
_APPLYFEATURESETREQUEST.fields_by_name[
    "feature_set"
].message_type = feast_dot_core_dot_FeatureSet__pb2._FEATURESETSPEC
_APPLYFEATURESETRESPONSE.fields_by_name[
    "feature_set"
].message_type = feast_dot_core_dot_FeatureSet__pb2._FEATURESETSPEC
_APPLYFEATURESETRESPONSE.fields_by_name[
    "status"
].enum_type = _APPLYFEATURESETRESPONSE_STATUS
_APPLYFEATURESETRESPONSE_STATUS.containing_type = _APPLYFEATURESETRESPONSE
DESCRIPTOR.message_types_by_name["GetFeatureSetsRequest"] = _GETFEATURESETSREQUEST
DESCRIPTOR.message_types_by_name["GetFeatureSetsResponse"] = _GETFEATURESETSRESPONSE
DESCRIPTOR.message_types_by_name["GetStoresRequest"] = _GETSTORESREQUEST
DESCRIPTOR.message_types_by_name["GetStoresResponse"] = _GETSTORESRESPONSE
DESCRIPTOR.message_types_by_name["ApplyFeatureSetRequest"] = _APPLYFEATURESETREQUEST
DESCRIPTOR.message_types_by_name["ApplyFeatureSetResponse"] = _APPLYFEATURESETRESPONSE
DESCRIPTOR.message_types_by_name[
    "GetFeastCoreVersionRequest"
] = _GETFEASTCOREVERSIONREQUEST
DESCRIPTOR.message_types_by_name[
    "GetFeastCoreVersionResponse"
] = _GETFEASTCOREVERSIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetFeatureSetsRequest = _reflection.GeneratedProtocolMessageType(
    "GetFeatureSetsRequest",
    (_message.Message,),
    {
        "Filter": _reflection.GeneratedProtocolMessageType(
            "Filter",
            (_message.Message,),
            {
                "DESCRIPTOR": _GETFEATURESETSREQUEST_FILTER,
                "__module__": "feast.core.CoreService_pb2"
                # @@protoc_insertion_point(class_scope:feast.core.GetFeatureSetsRequest.Filter)
            },
        ),
        "DESCRIPTOR": _GETFEATURESETSREQUEST,
        "__module__": "feast.core.CoreService_pb2"
        # @@protoc_insertion_point(class_scope:feast.core.GetFeatureSetsRequest)
    },
)
_sym_db.RegisterMessage(GetFeatureSetsRequest)
_sym_db.RegisterMessage(GetFeatureSetsRequest.Filter)

GetFeatureSetsResponse = _reflection.GeneratedProtocolMessageType(
    "GetFeatureSetsResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETFEATURESETSRESPONSE,
        "__module__": "feast.core.CoreService_pb2"
        # @@protoc_insertion_point(class_scope:feast.core.GetFeatureSetsResponse)
    },
)
_sym_db.RegisterMessage(GetFeatureSetsResponse)

GetStoresRequest = _reflection.GeneratedProtocolMessageType(
    "GetStoresRequest",
    (_message.Message,),
    {
        "Filter": _reflection.GeneratedProtocolMessageType(
            "Filter",
            (_message.Message,),
            {
                "DESCRIPTOR": _GETSTORESREQUEST_FILTER,
                "__module__": "feast.core.CoreService_pb2"
                # @@protoc_insertion_point(class_scope:feast.core.GetStoresRequest.Filter)
            },
        ),
        "DESCRIPTOR": _GETSTORESREQUEST,
        "__module__": "feast.core.CoreService_pb2"
        # @@protoc_insertion_point(class_scope:feast.core.GetStoresRequest)
    },
)
_sym_db.RegisterMessage(GetStoresRequest)
_sym_db.RegisterMessage(GetStoresRequest.Filter)

GetStoresResponse = _reflection.GeneratedProtocolMessageType(
    "GetStoresResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETSTORESRESPONSE,
        "__module__": "feast.core.CoreService_pb2"
        # @@protoc_insertion_point(class_scope:feast.core.GetStoresResponse)
    },
)
_sym_db.RegisterMessage(GetStoresResponse)

ApplyFeatureSetRequest = _reflection.GeneratedProtocolMessageType(
    "ApplyFeatureSetRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _APPLYFEATURESETREQUEST,
        "__module__": "feast.core.CoreService_pb2"
        # @@protoc_insertion_point(class_scope:feast.core.ApplyFeatureSetRequest)
    },
)
_sym_db.RegisterMessage(ApplyFeatureSetRequest)

ApplyFeatureSetResponse = _reflection.GeneratedProtocolMessageType(
    "ApplyFeatureSetResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _APPLYFEATURESETRESPONSE,
        "__module__": "feast.core.CoreService_pb2"
        # @@protoc_insertion_point(class_scope:feast.core.ApplyFeatureSetResponse)
    },
)
_sym_db.RegisterMessage(ApplyFeatureSetResponse)

GetFeastCoreVersionRequest = _reflection.GeneratedProtocolMessageType(
    "GetFeastCoreVersionRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETFEASTCOREVERSIONREQUEST,
        "__module__": "feast.core.CoreService_pb2"
        # @@protoc_insertion_point(class_scope:feast.core.GetFeastCoreVersionRequest)
    },
)
_sym_db.RegisterMessage(GetFeastCoreVersionRequest)

GetFeastCoreVersionResponse = _reflection.GeneratedProtocolMessageType(
    "GetFeastCoreVersionResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETFEASTCOREVERSIONRESPONSE,
        "__module__": "feast.core.CoreService_pb2"
        # @@protoc_insertion_point(class_scope:feast.core.GetFeastCoreVersionResponse)
    },
)
_sym_db.RegisterMessage(GetFeastCoreVersionResponse)


DESCRIPTOR._options = None

_CORESERVICE = _descriptor.ServiceDescriptor(
    name="CoreService",
    full_name="feast.core.CoreService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    serialized_start=814,
    serialized_end=1186,
    methods=[
        _descriptor.MethodDescriptor(
            name="GetFeastCoreVersion",
            full_name="feast.core.CoreService.GetFeastCoreVersion",
            index=0,
            containing_service=None,
            input_type=_GETFEASTCOREVERSIONREQUEST,
            output_type=_GETFEASTCOREVERSIONRESPONSE,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name="GetFeatureSets",
            full_name="feast.core.CoreService.GetFeatureSets",
            index=1,
            containing_service=None,
            input_type=_GETFEATURESETSREQUEST,
            output_type=_GETFEATURESETSRESPONSE,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name="GetStores",
            full_name="feast.core.CoreService.GetStores",
            index=2,
            containing_service=None,
            input_type=_GETSTORESREQUEST,
            output_type=_GETSTORESRESPONSE,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name="ApplyFeatureSet",
            full_name="feast.core.CoreService.ApplyFeatureSet",
            index=3,
            containing_service=None,
            input_type=_APPLYFEATURESETREQUEST,
            output_type=_APPLYFEATURESETRESPONSE,
            serialized_options=None,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_CORESERVICE)

DESCRIPTOR.services_by_name["CoreService"] = _CORESERVICE

# @@protoc_insertion_point(module_scope)
