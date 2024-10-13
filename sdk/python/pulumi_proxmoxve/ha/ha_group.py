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

__all__ = ['HAGroupArgs', 'HAGroup']

@pulumi.input_type
class HAGroupArgs:
    def __init__(__self__, *,
                 group: pulumi.Input[str],
                 nodes: pulumi.Input[Mapping[str, pulumi.Input[int]]],
                 comment: Optional[pulumi.Input[str]] = None,
                 no_failback: Optional[pulumi.Input[bool]] = None,
                 restricted: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a HAGroup resource.
        :param pulumi.Input[str] group: The identifier of the High Availability group to manage.
        :param pulumi.Input[Mapping[str, pulumi.Input[int]]] nodes: The member nodes for this group. They are provided as a map, where the keys are the node names and the values represent their priority: integers for known priorities or `null` for unset priorities.
        :param pulumi.Input[str] comment: The comment associated with this group
        :param pulumi.Input[bool] no_failback: A flag that indicates that failing back to a higher priority node is disabled for this HA group. Defaults to `false`.
        :param pulumi.Input[bool] restricted: A flag that indicates that other nodes may not be used to run resources associated to this HA group. Defaults to `false`.
        """
        pulumi.set(__self__, "group", group)
        pulumi.set(__self__, "nodes", nodes)
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if no_failback is not None:
            pulumi.set(__self__, "no_failback", no_failback)
        if restricted is not None:
            pulumi.set(__self__, "restricted", restricted)

    @property
    @pulumi.getter
    def group(self) -> pulumi.Input[str]:
        """
        The identifier of the High Availability group to manage.
        """
        return pulumi.get(self, "group")

    @group.setter
    def group(self, value: pulumi.Input[str]):
        pulumi.set(self, "group", value)

    @property
    @pulumi.getter
    def nodes(self) -> pulumi.Input[Mapping[str, pulumi.Input[int]]]:
        """
        The member nodes for this group. They are provided as a map, where the keys are the node names and the values represent their priority: integers for known priorities or `null` for unset priorities.
        """
        return pulumi.get(self, "nodes")

    @nodes.setter
    def nodes(self, value: pulumi.Input[Mapping[str, pulumi.Input[int]]]):
        pulumi.set(self, "nodes", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        """
        The comment associated with this group
        """
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter(name="noFailback")
    def no_failback(self) -> Optional[pulumi.Input[bool]]:
        """
        A flag that indicates that failing back to a higher priority node is disabled for this HA group. Defaults to `false`.
        """
        return pulumi.get(self, "no_failback")

    @no_failback.setter
    def no_failback(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "no_failback", value)

    @property
    @pulumi.getter
    def restricted(self) -> Optional[pulumi.Input[bool]]:
        """
        A flag that indicates that other nodes may not be used to run resources associated to this HA group. Defaults to `false`.
        """
        return pulumi.get(self, "restricted")

    @restricted.setter
    def restricted(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "restricted", value)


@pulumi.input_type
class _HAGroupState:
    def __init__(__self__, *,
                 comment: Optional[pulumi.Input[str]] = None,
                 group: Optional[pulumi.Input[str]] = None,
                 no_failback: Optional[pulumi.Input[bool]] = None,
                 nodes: Optional[pulumi.Input[Mapping[str, pulumi.Input[int]]]] = None,
                 restricted: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering HAGroup resources.
        :param pulumi.Input[str] comment: The comment associated with this group
        :param pulumi.Input[str] group: The identifier of the High Availability group to manage.
        :param pulumi.Input[bool] no_failback: A flag that indicates that failing back to a higher priority node is disabled for this HA group. Defaults to `false`.
        :param pulumi.Input[Mapping[str, pulumi.Input[int]]] nodes: The member nodes for this group. They are provided as a map, where the keys are the node names and the values represent their priority: integers for known priorities or `null` for unset priorities.
        :param pulumi.Input[bool] restricted: A flag that indicates that other nodes may not be used to run resources associated to this HA group. Defaults to `false`.
        """
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if group is not None:
            pulumi.set(__self__, "group", group)
        if no_failback is not None:
            pulumi.set(__self__, "no_failback", no_failback)
        if nodes is not None:
            pulumi.set(__self__, "nodes", nodes)
        if restricted is not None:
            pulumi.set(__self__, "restricted", restricted)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        """
        The comment associated with this group
        """
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter
    def group(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier of the High Availability group to manage.
        """
        return pulumi.get(self, "group")

    @group.setter
    def group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group", value)

    @property
    @pulumi.getter(name="noFailback")
    def no_failback(self) -> Optional[pulumi.Input[bool]]:
        """
        A flag that indicates that failing back to a higher priority node is disabled for this HA group. Defaults to `false`.
        """
        return pulumi.get(self, "no_failback")

    @no_failback.setter
    def no_failback(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "no_failback", value)

    @property
    @pulumi.getter
    def nodes(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[int]]]]:
        """
        The member nodes for this group. They are provided as a map, where the keys are the node names and the values represent their priority: integers for known priorities or `null` for unset priorities.
        """
        return pulumi.get(self, "nodes")

    @nodes.setter
    def nodes(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[int]]]]):
        pulumi.set(self, "nodes", value)

    @property
    @pulumi.getter
    def restricted(self) -> Optional[pulumi.Input[bool]]:
        """
        A flag that indicates that other nodes may not be used to run resources associated to this HA group. Defaults to `false`.
        """
        return pulumi.get(self, "restricted")

    @restricted.setter
    def restricted(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "restricted", value)


class HAGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 group: Optional[pulumi.Input[str]] = None,
                 no_failback: Optional[pulumi.Input[bool]] = None,
                 nodes: Optional[pulumi.Input[Mapping[str, pulumi.Input[int]]]] = None,
                 restricted: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Manages a High Availability group in a Proxmox VE cluster.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_proxmoxve as proxmoxve

        example = proxmoxve.ha.HAGroup("example",
            group="example",
            comment="This is a comment.",
            nodes={
                "node1": None,
                "node2": 2,
                "node3": 1,
            },
            restricted=True,
            no_failback=False)
        ```

        ## Import

        #!/usr/bin/env sh

        HA groups can be imported using their name, e.g.:

        ```sh
        $ pulumi import proxmoxve:HA/hAGroup:HAGroup example example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] comment: The comment associated with this group
        :param pulumi.Input[str] group: The identifier of the High Availability group to manage.
        :param pulumi.Input[bool] no_failback: A flag that indicates that failing back to a higher priority node is disabled for this HA group. Defaults to `false`.
        :param pulumi.Input[Mapping[str, pulumi.Input[int]]] nodes: The member nodes for this group. They are provided as a map, where the keys are the node names and the values represent their priority: integers for known priorities or `null` for unset priorities.
        :param pulumi.Input[bool] restricted: A flag that indicates that other nodes may not be used to run resources associated to this HA group. Defaults to `false`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: HAGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a High Availability group in a Proxmox VE cluster.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_proxmoxve as proxmoxve

        example = proxmoxve.ha.HAGroup("example",
            group="example",
            comment="This is a comment.",
            nodes={
                "node1": None,
                "node2": 2,
                "node3": 1,
            },
            restricted=True,
            no_failback=False)
        ```

        ## Import

        #!/usr/bin/env sh

        HA groups can be imported using their name, e.g.:

        ```sh
        $ pulumi import proxmoxve:HA/hAGroup:HAGroup example example
        ```

        :param str resource_name: The name of the resource.
        :param HAGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HAGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 group: Optional[pulumi.Input[str]] = None,
                 no_failback: Optional[pulumi.Input[bool]] = None,
                 nodes: Optional[pulumi.Input[Mapping[str, pulumi.Input[int]]]] = None,
                 restricted: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = HAGroupArgs.__new__(HAGroupArgs)

            __props__.__dict__["comment"] = comment
            if group is None and not opts.urn:
                raise TypeError("Missing required property 'group'")
            __props__.__dict__["group"] = group
            __props__.__dict__["no_failback"] = no_failback
            if nodes is None and not opts.urn:
                raise TypeError("Missing required property 'nodes'")
            __props__.__dict__["nodes"] = nodes
            __props__.__dict__["restricted"] = restricted
        super(HAGroup, __self__).__init__(
            'proxmoxve:HA/hAGroup:HAGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            comment: Optional[pulumi.Input[str]] = None,
            group: Optional[pulumi.Input[str]] = None,
            no_failback: Optional[pulumi.Input[bool]] = None,
            nodes: Optional[pulumi.Input[Mapping[str, pulumi.Input[int]]]] = None,
            restricted: Optional[pulumi.Input[bool]] = None) -> 'HAGroup':
        """
        Get an existing HAGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] comment: The comment associated with this group
        :param pulumi.Input[str] group: The identifier of the High Availability group to manage.
        :param pulumi.Input[bool] no_failback: A flag that indicates that failing back to a higher priority node is disabled for this HA group. Defaults to `false`.
        :param pulumi.Input[Mapping[str, pulumi.Input[int]]] nodes: The member nodes for this group. They are provided as a map, where the keys are the node names and the values represent their priority: integers for known priorities or `null` for unset priorities.
        :param pulumi.Input[bool] restricted: A flag that indicates that other nodes may not be used to run resources associated to this HA group. Defaults to `false`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _HAGroupState.__new__(_HAGroupState)

        __props__.__dict__["comment"] = comment
        __props__.__dict__["group"] = group
        __props__.__dict__["no_failback"] = no_failback
        __props__.__dict__["nodes"] = nodes
        __props__.__dict__["restricted"] = restricted
        return HAGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def comment(self) -> pulumi.Output[Optional[str]]:
        """
        The comment associated with this group
        """
        return pulumi.get(self, "comment")

    @property
    @pulumi.getter
    def group(self) -> pulumi.Output[str]:
        """
        The identifier of the High Availability group to manage.
        """
        return pulumi.get(self, "group")

    @property
    @pulumi.getter(name="noFailback")
    def no_failback(self) -> pulumi.Output[bool]:
        """
        A flag that indicates that failing back to a higher priority node is disabled for this HA group. Defaults to `false`.
        """
        return pulumi.get(self, "no_failback")

    @property
    @pulumi.getter
    def nodes(self) -> pulumi.Output[Mapping[str, int]]:
        """
        The member nodes for this group. They are provided as a map, where the keys are the node names and the values represent their priority: integers for known priorities or `null` for unset priorities.
        """
        return pulumi.get(self, "nodes")

    @property
    @pulumi.getter
    def restricted(self) -> pulumi.Output[bool]:
        """
        A flag that indicates that other nodes may not be used to run resources associated to this HA group. Defaults to `false`.
        """
        return pulumi.get(self, "restricted")

