# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'PciMapArgs',
    'UsbMapArgs',
]

@pulumi.input_type
class PciMapArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str],
                 node: pulumi.Input[str],
                 path: pulumi.Input[str],
                 comment: Optional[pulumi.Input[str]] = None,
                 iommu_group: Optional[pulumi.Input[int]] = None,
                 subsystem_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] id: The ID of the map.
        :param pulumi.Input[str] node: The node name of the map.
        :param pulumi.Input[str] path: The path of the map.
        :param pulumi.Input[str] comment: The comment of the mapped PCI device.
        :param pulumi.Input[int] iommu_group: The IOMMU group of the map. Not mandatory for the Proxmox VE API call, but causes a PCI hardware mapping to be incomplete when not set
        :param pulumi.Input[str] subsystem_id: The subsystem ID group of the map. Not mandatory for the Proxmox VE API call, but causes a PCI hardware mapping to be incomplete when not set
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "node", node)
        pulumi.set(__self__, "path", path)
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if iommu_group is not None:
            pulumi.set(__self__, "iommu_group", iommu_group)
        if subsystem_id is not None:
            pulumi.set(__self__, "subsystem_id", subsystem_id)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        The ID of the map.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def node(self) -> pulumi.Input[str]:
        """
        The node name of the map.
        """
        return pulumi.get(self, "node")

    @node.setter
    def node(self, value: pulumi.Input[str]):
        pulumi.set(self, "node", value)

    @property
    @pulumi.getter
    def path(self) -> pulumi.Input[str]:
        """
        The path of the map.
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: pulumi.Input[str]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        """
        The comment of the mapped PCI device.
        """
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter(name="iommuGroup")
    def iommu_group(self) -> Optional[pulumi.Input[int]]:
        """
        The IOMMU group of the map. Not mandatory for the Proxmox VE API call, but causes a PCI hardware mapping to be incomplete when not set
        """
        return pulumi.get(self, "iommu_group")

    @iommu_group.setter
    def iommu_group(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "iommu_group", value)

    @property
    @pulumi.getter(name="subsystemId")
    def subsystem_id(self) -> Optional[pulumi.Input[str]]:
        """
        The subsystem ID group of the map. Not mandatory for the Proxmox VE API call, but causes a PCI hardware mapping to be incomplete when not set
        """
        return pulumi.get(self, "subsystem_id")

    @subsystem_id.setter
    def subsystem_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subsystem_id", value)


@pulumi.input_type
class UsbMapArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str],
                 node: pulumi.Input[str],
                 comment: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] id: The ID of the map.
        :param pulumi.Input[str] node: The node name of the map.
        :param pulumi.Input[str] comment: The comment of the mapped USB device.
        :param pulumi.Input[str] path: The path of the map. For hardware mappings of type USB the path is optional and indicates that the device is mapped through the device ID instead of ports.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "node", node)
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if path is not None:
            pulumi.set(__self__, "path", path)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        The ID of the map.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def node(self) -> pulumi.Input[str]:
        """
        The node name of the map.
        """
        return pulumi.get(self, "node")

    @node.setter
    def node(self, value: pulumi.Input[str]):
        pulumi.set(self, "node", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        """
        The comment of the mapped USB device.
        """
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        """
        The path of the map. For hardware mappings of type USB the path is optional and indicates that the device is mapped through the device ID instead of ports.
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)

