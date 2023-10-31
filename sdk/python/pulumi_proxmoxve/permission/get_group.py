# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetGroupResult',
    'AwaitableGetGroupResult',
    'get_group',
    'get_group_output',
]

@pulumi.output_type
class GetGroupResult:
    """
    A collection of values returned by getGroup.
    """
    def __init__(__self__, acls=None, comment=None, group_id=None, id=None, members=None):
        if acls and not isinstance(acls, list):
            raise TypeError("Expected argument 'acls' to be a list")
        pulumi.set(__self__, "acls", acls)
        if comment and not isinstance(comment, str):
            raise TypeError("Expected argument 'comment' to be a str")
        pulumi.set(__self__, "comment", comment)
        if group_id and not isinstance(group_id, str):
            raise TypeError("Expected argument 'group_id' to be a str")
        pulumi.set(__self__, "group_id", group_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if members and not isinstance(members, list):
            raise TypeError("Expected argument 'members' to be a list")
        pulumi.set(__self__, "members", members)

    @property
    @pulumi.getter
    def acls(self) -> Sequence['outputs.GetGroupAclResult']:
        """
        The access control list.
        """
        return pulumi.get(self, "acls")

    @property
    @pulumi.getter
    def comment(self) -> str:
        """
        The group comment.
        """
        return pulumi.get(self, "comment")

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> str:
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def members(self) -> Sequence[str]:
        """
        The group members as a list with `username@realm` entries.
        """
        return pulumi.get(self, "members")


class AwaitableGetGroupResult(GetGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGroupResult(
            acls=self.acls,
            comment=self.comment,
            group_id=self.group_id,
            id=self.id,
            members=self.members)


def get_group(group_id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGroupResult:
    """
    Retrieves information about a specific user group.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_proxmoxve as proxmoxve

    operations_team = proxmoxve.Permission.get_group(group_id="operations-team")
    ```


    :param str group_id: The group identifier.
    """
    __args__ = dict()
    __args__['groupId'] = group_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('proxmoxve:Permission/getGroup:getGroup', __args__, opts=opts, typ=GetGroupResult).value

    return AwaitableGetGroupResult(
        acls=pulumi.get(__ret__, 'acls'),
        comment=pulumi.get(__ret__, 'comment'),
        group_id=pulumi.get(__ret__, 'group_id'),
        id=pulumi.get(__ret__, 'id'),
        members=pulumi.get(__ret__, 'members'))


@_utilities.lift_output_func(get_group)
def get_group_output(group_id: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGroupResult]:
    """
    Retrieves information about a specific user group.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_proxmoxve as proxmoxve

    operations_team = proxmoxve.Permission.get_group(group_id="operations-team")
    ```


    :param str group_id: The group identifier.
    """
    ...
