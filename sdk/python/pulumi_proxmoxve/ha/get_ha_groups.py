# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from .. import _utilities

__all__ = [
    'GetHAGroupsResult',
    'AwaitableGetHAGroupsResult',
    'get_ha_groups',
    'get_ha_groups_output',
]

@pulumi.output_type
class GetHAGroupsResult:
    """
    A collection of values returned by getHAGroups.
    """
    def __init__(__self__, group_ids=None, id=None):
        if group_ids and not isinstance(group_ids, list):
            raise TypeError("Expected argument 'group_ids' to be a list")
        pulumi.set(__self__, "group_ids", group_ids)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Sequence[str]:
        """
        The identifiers of the High Availability groups.
        """
        return pulumi.get(self, "group_ids")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The unique identifier of this resource.
        """
        return pulumi.get(self, "id")


class AwaitableGetHAGroupsResult(GetHAGroupsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetHAGroupsResult(
            group_ids=self.group_ids,
            id=self.id)


def get_ha_groups(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetHAGroupsResult:
    """
    Retrieves the list of High Availability groups.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_proxmoxve as proxmoxve

    example = proxmoxve.HA.get_ha_groups()
    pulumi.export("dataProxmoxVirtualEnvironmentHagroups", example.group_ids)
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('proxmoxve:HA/getHAGroups:getHAGroups', __args__, opts=opts, typ=GetHAGroupsResult).value

    return AwaitableGetHAGroupsResult(
        group_ids=pulumi.get(__ret__, 'group_ids'),
        id=pulumi.get(__ret__, 'id'))
def get_ha_groups_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetHAGroupsResult]:
    """
    Retrieves the list of High Availability groups.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_proxmoxve as proxmoxve

    example = proxmoxve.HA.get_ha_groups()
    pulumi.export("dataProxmoxVirtualEnvironmentHagroups", example.group_ids)
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('proxmoxve:HA/getHAGroups:getHAGroups', __args__, opts=opts, typ=GetHAGroupsResult)
    return __ret__.apply(lambda __response__: GetHAGroupsResult(
        group_ids=pulumi.get(__response__, 'group_ids'),
        id=pulumi.get(__response__, 'id')))
