# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tinkoff/invest/grpc/users.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import (
    descriptor as _descriptor,
    descriptor_pool as _descriptor_pool,
    symbol_database as _symbol_database,
)
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2

from tinkoff.invest.grpc import (
    common_pb2 as tinkoff_dot_invest_dot_grpc_dot_common__pb2,
)
from tinkoff.invest.grpc.google.api import (
    field_behavior_pb2 as tinkoff_dot_invest_dot_grpc_dot_google_dot_api_dot_field__behavior__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ftinkoff/invest/grpc/users.proto\x12%tinkoff.public.invest.api.contract.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x33tinkoff/invest/grpc/google/api/field_behavior.proto\x1a tinkoff/invest/grpc/common.proto\"j\n\x12GetAccountsRequest\x12I\n\x06status\x18\x01 \x01(\x0e\x32\x34.tinkoff.public.invest.api.contract.v1.AccountStatusH\x00\x88\x01\x01\x42\t\n\x07_status\"W\n\x13GetAccountsResponse\x12@\n\x08\x61\x63\x63ounts\x18\x01 \x03(\x0b\x32..tinkoff.public.invest.api.contract.v1.Account\"\xd7\x02\n\x07\x41\x63\x63ount\x12\n\n\x02id\x18\x01 \x01(\t\x12@\n\x04type\x18\x02 \x01(\x0e\x32\x32.tinkoff.public.invest.api.contract.v1.AccountType\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x44\n\x06status\x18\x04 \x01(\x0e\x32\x34.tinkoff.public.invest.api.contract.v1.AccountStatus\x12/\n\x0bopened_date\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x63losed_date\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12H\n\x0c\x61\x63\x63\x65ss_level\x18\x07 \x01(\x0e\x32\x32.tinkoff.public.invest.api.contract.v1.AccessLevel\"6\n\x1aGetMarginAttributesRequest\x12\x18\n\naccount_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\"\xf5\x03\n\x1bGetMarginAttributesResponse\x12K\n\x10liquid_portfolio\x18\x01 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12J\n\x0fstarting_margin\x18\x02 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12I\n\x0eminimal_margin\x18\x03 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12Q\n\x17\x66unds_sufficiency_level\x18\x04 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12R\n\x17\x61mount_of_missing_funds\x18\x05 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12K\n\x10\x63orrected_margin\x18\x06 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\"\x16\n\x14GetUserTariffRequest\"\xab\x01\n\x15GetUserTariffResponse\x12G\n\x0cunary_limits\x18\x01 \x03(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.UnaryLimit\x12I\n\rstream_limits\x18\x02 \x03(\x0b\x32\x32.tinkoff.public.invest.api.contract.v1.StreamLimit\"7\n\nUnaryLimit\x12\x18\n\x10limit_per_minute\x18\x01 \x01(\x05\x12\x0f\n\x07methods\x18\x02 \x03(\t\";\n\x0bStreamLimit\x12\r\n\x05limit\x18\x01 \x01(\x05\x12\x0f\n\x07streams\x18\x02 \x03(\t\x12\x0c\n\x04open\x18\x03 \x01(\x05\"\x10\n\x0eGetInfoRequest\"\x96\x01\n\x0fGetInfoResponse\x12\x13\n\x0bprem_status\x18\x01 \x01(\x08\x12\x13\n\x0bqual_status\x18\x02 \x01(\x08\x12\x1f\n\x17qualified_for_work_with\x18\x03 \x03(\t\x12\x0e\n\x06tariff\x18\x04 \x01(\t\x12\x0f\n\x07user_id\x18\t \x01(\t\x12\x17\n\x0frisk_level_code\x18\x0c \x01(\t*\x9e\x01\n\x0b\x41\x63\x63ountType\x12\x1c\n\x18\x41\x43\x43OUNT_TYPE_UNSPECIFIED\x10\x00\x12\x18\n\x14\x41\x43\x43OUNT_TYPE_TINKOFF\x10\x01\x12\x1c\n\x18\x41\x43\x43OUNT_TYPE_TINKOFF_IIS\x10\x02\x12\x1b\n\x17\x41\x43\x43OUNT_TYPE_INVEST_BOX\x10\x03\x12\x1c\n\x18\x41\x43\x43OUNT_TYPE_INVEST_FUND\x10\x04*\x93\x01\n\rAccountStatus\x12\x1e\n\x1a\x41\x43\x43OUNT_STATUS_UNSPECIFIED\x10\x00\x12\x16\n\x12\x41\x43\x43OUNT_STATUS_NEW\x10\x01\x12\x17\n\x13\x41\x43\x43OUNT_STATUS_OPEN\x10\x02\x12\x19\n\x15\x41\x43\x43OUNT_STATUS_CLOSED\x10\x03\x12\x16\n\x12\x41\x43\x43OUNT_STATUS_ALL\x10\x04*\xa1\x01\n\x0b\x41\x63\x63\x65ssLevel\x12$\n ACCOUNT_ACCESS_LEVEL_UNSPECIFIED\x10\x00\x12$\n ACCOUNT_ACCESS_LEVEL_FULL_ACCESS\x10\x01\x12\"\n\x1e\x41\x43\x43OUNT_ACCESS_LEVEL_READ_ONLY\x10\x02\x12\"\n\x1e\x41\x43\x43OUNT_ACCESS_LEVEL_NO_ACCESS\x10\x03\x32\xbb\x04\n\x0cUsersService\x12\x84\x01\n\x0bGetAccounts\x12\x39.tinkoff.public.invest.api.contract.v1.GetAccountsRequest\x1a:.tinkoff.public.invest.api.contract.v1.GetAccountsResponse\x12\x9c\x01\n\x13GetMarginAttributes\x12\x41.tinkoff.public.invest.api.contract.v1.GetMarginAttributesRequest\x1a\x42.tinkoff.public.invest.api.contract.v1.GetMarginAttributesResponse\x12\x8a\x01\n\rGetUserTariff\x12;.tinkoff.public.invest.api.contract.v1.GetUserTariffRequest\x1a<.tinkoff.public.invest.api.contract.v1.GetUserTariffResponse\x12x\n\x07GetInfo\x12\x35.tinkoff.public.invest.api.contract.v1.GetInfoRequest\x1a\x36.tinkoff.public.invest.api.contract.v1.GetInfoResponseBa\n\x1cru.tinkoff.piapi.contract.v1P\x01Z\x0c./;investapi\xa2\x02\x05TIAPI\xaa\x02\x14Tinkoff.InvestApi.V1\xca\x02\x11Tinkoff\\Invest\\V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tinkoff.invest.grpc.users_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034ru.tinkoff.piapi.contract.v1P\001Z\014./;investapi\242\002\005TIAPI\252\002\024Tinkoff.InvestApi.V1\312\002\021Tinkoff\\Invest\\V1'
  _globals['_GETMARGINATTRIBUTESREQUEST'].fields_by_name['account_id']._options = None
  _globals['_GETMARGINATTRIBUTESREQUEST'].fields_by_name['account_id']._serialized_options = b'\342A\001\002'
  _globals['_ACCOUNTTYPE']._serialized_start=1785
  _globals['_ACCOUNTTYPE']._serialized_end=1943
  _globals['_ACCOUNTSTATUS']._serialized_start=1946
  _globals['_ACCOUNTSTATUS']._serialized_end=2093
  _globals['_ACCESSLEVEL']._serialized_start=2096
  _globals['_ACCESSLEVEL']._serialized_end=2257
  _globals['_GETACCOUNTSREQUEST']._serialized_start=194
  _globals['_GETACCOUNTSREQUEST']._serialized_end=300
  _globals['_GETACCOUNTSRESPONSE']._serialized_start=302
  _globals['_GETACCOUNTSRESPONSE']._serialized_end=389
  _globals['_ACCOUNT']._serialized_start=392
  _globals['_ACCOUNT']._serialized_end=735
  _globals['_GETMARGINATTRIBUTESREQUEST']._serialized_start=737
  _globals['_GETMARGINATTRIBUTESREQUEST']._serialized_end=791
  _globals['_GETMARGINATTRIBUTESRESPONSE']._serialized_start=794
  _globals['_GETMARGINATTRIBUTESRESPONSE']._serialized_end=1295
  _globals['_GETUSERTARIFFREQUEST']._serialized_start=1297
  _globals['_GETUSERTARIFFREQUEST']._serialized_end=1319
  _globals['_GETUSERTARIFFRESPONSE']._serialized_start=1322
  _globals['_GETUSERTARIFFRESPONSE']._serialized_end=1493
  _globals['_UNARYLIMIT']._serialized_start=1495
  _globals['_UNARYLIMIT']._serialized_end=1550
  _globals['_STREAMLIMIT']._serialized_start=1552
  _globals['_STREAMLIMIT']._serialized_end=1611
  _globals['_GETINFOREQUEST']._serialized_start=1613
  _globals['_GETINFOREQUEST']._serialized_end=1629
  _globals['_GETINFORESPONSE']._serialized_start=1632
  _globals['_GETINFORESPONSE']._serialized_end=1782
  _globals['_USERSSERVICE']._serialized_start=2260
  _globals['_USERSSERVICE']._serialized_end=2831
# @@protoc_insertion_point(module_scope)
