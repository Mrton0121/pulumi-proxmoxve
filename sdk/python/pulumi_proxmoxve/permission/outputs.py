# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GroupAcl',
    'PoolMember',
    'UserAcl',
    'GetGroupAclResult',
    'GetPoolMemberResult',
    'GetUserAclResult',
]

@pulumi.output_type
class GroupAcl(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "roleId":
            suggest = "role_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GroupAcl. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GroupAcl.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GroupAcl.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 path: str,
                 role_id: str,
                 propagate: Optional[bool] = None):
        pulumi.set(__self__, "path", path)
        pulumi.set(__self__, "role_id", role_id)
        if propagate is not None:
            pulumi.set(__self__, "propagate", propagate)

    @property
    @pulumi.getter
    def path(self) -> str:
        return pulumi.get(self, "path")

    @property
    @pulumi.getter(name="roleId")
    def role_id(self) -> str:
        return pulumi.get(self, "role_id")

    @property
    @pulumi.getter
    def propagate(self) -> Optional[bool]:
        return pulumi.get(self, "propagate")


@pulumi.output_type
class PoolMember(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "datastoreId":
            suggest = "datastore_id"
        elif key == "nodeName":
            suggest = "node_name"
        elif key == "vmId":
            suggest = "vm_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PoolMember. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PoolMember.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PoolMember.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 datastore_id: Optional[str] = None,
                 id: Optional[str] = None,
                 node_name: Optional[str] = None,
                 type: Optional[str] = None,
                 vm_id: Optional[int] = None):
        if datastore_id is not None:
            pulumi.set(__self__, "datastore_id", datastore_id)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if node_name is not None:
            pulumi.set(__self__, "node_name", node_name)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if vm_id is not None:
            pulumi.set(__self__, "vm_id", vm_id)

    @property
    @pulumi.getter(name="datastoreId")
    def datastore_id(self) -> Optional[str]:
        return pulumi.get(self, "datastore_id")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="nodeName")
    def node_name(self) -> Optional[str]:
        return pulumi.get(self, "node_name")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> Optional[int]:
        return pulumi.get(self, "vm_id")


@pulumi.output_type
class UserAcl(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "roleId":
            suggest = "role_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in UserAcl. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        UserAcl.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        UserAcl.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 path: str,
                 role_id: str,
                 propagate: Optional[bool] = None):
        pulumi.set(__self__, "path", path)
        pulumi.set(__self__, "role_id", role_id)
        if propagate is not None:
            pulumi.set(__self__, "propagate", propagate)

    @property
    @pulumi.getter
    def path(self) -> str:
        return pulumi.get(self, "path")

    @property
    @pulumi.getter(name="roleId")
    def role_id(self) -> str:
        return pulumi.get(self, "role_id")

    @property
    @pulumi.getter
    def propagate(self) -> Optional[bool]:
        return pulumi.get(self, "propagate")


@pulumi.output_type
class GetGroupAclResult(dict):
    def __init__(__self__, *,
                 path: str,
                 propagate: bool,
                 role_id: str):
        pulumi.set(__self__, "path", path)
        pulumi.set(__self__, "propagate", propagate)
        pulumi.set(__self__, "role_id", role_id)

    @property
    @pulumi.getter
    def path(self) -> str:
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def propagate(self) -> bool:
        return pulumi.get(self, "propagate")

    @property
    @pulumi.getter(name="roleId")
    def role_id(self) -> str:
        return pulumi.get(self, "role_id")


@pulumi.output_type
class GetPoolMemberResult(dict):
    def __init__(__self__, *,
                 datastore_id: str,
                 id: str,
                 node_name: str,
                 type: str,
                 vm_id: int):
        pulumi.set(__self__, "datastore_id", datastore_id)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "node_name", node_name)
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "vm_id", vm_id)

    @property
    @pulumi.getter(name="datastoreId")
    def datastore_id(self) -> str:
        return pulumi.get(self, "datastore_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="nodeName")
    def node_name(self) -> str:
        return pulumi.get(self, "node_name")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> int:
        return pulumi.get(self, "vm_id")


@pulumi.output_type
class GetUserAclResult(dict):
    def __init__(__self__, *,
                 path: str,
                 propagate: bool,
                 role_id: str):
        pulumi.set(__self__, "path", path)
        pulumi.set(__self__, "propagate", propagate)
        pulumi.set(__self__, "role_id", role_id)

    @property
    @pulumi.getter
    def path(self) -> str:
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def propagate(self) -> bool:
        return pulumi.get(self, "propagate")

    @property
    @pulumi.getter(name="roleId")
    def role_id(self) -> str:
        return pulumi.get(self, "role_id")


