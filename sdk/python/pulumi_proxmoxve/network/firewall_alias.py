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

__all__ = ['FirewallAliasArgs', 'FirewallAlias']

@pulumi.input_type
class FirewallAliasArgs:
    def __init__(__self__, *,
                 cidr: pulumi.Input[str],
                 comment: Optional[pulumi.Input[str]] = None,
                 container_id: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_name: Optional[pulumi.Input[str]] = None,
                 vm_id: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a FirewallAlias resource.
        :param pulumi.Input[str] cidr: Network/IP specification in CIDR format.
        :param pulumi.Input[str] comment: Alias comment.
        :param pulumi.Input[int] container_id: Container ID. Leave empty for cluster level aliases.
        :param pulumi.Input[str] name: Alias name.
        :param pulumi.Input[str] node_name: Node name. Leave empty for cluster level aliases.
        :param pulumi.Input[int] vm_id: VM ID. Leave empty for cluster level aliases.
        """
        pulumi.set(__self__, "cidr", cidr)
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if container_id is not None:
            pulumi.set(__self__, "container_id", container_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if node_name is not None:
            pulumi.set(__self__, "node_name", node_name)
        if vm_id is not None:
            pulumi.set(__self__, "vm_id", vm_id)

    @property
    @pulumi.getter
    def cidr(self) -> pulumi.Input[str]:
        """
        Network/IP specification in CIDR format.
        """
        return pulumi.get(self, "cidr")

    @cidr.setter
    def cidr(self, value: pulumi.Input[str]):
        pulumi.set(self, "cidr", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        """
        Alias comment.
        """
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter(name="containerId")
    def container_id(self) -> Optional[pulumi.Input[int]]:
        """
        Container ID. Leave empty for cluster level aliases.
        """
        return pulumi.get(self, "container_id")

    @container_id.setter
    def container_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "container_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Alias name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="nodeName")
    def node_name(self) -> Optional[pulumi.Input[str]]:
        """
        Node name. Leave empty for cluster level aliases.
        """
        return pulumi.get(self, "node_name")

    @node_name.setter
    def node_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "node_name", value)

    @property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> Optional[pulumi.Input[int]]:
        """
        VM ID. Leave empty for cluster level aliases.
        """
        return pulumi.get(self, "vm_id")

    @vm_id.setter
    def vm_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "vm_id", value)


@pulumi.input_type
class _FirewallAliasState:
    def __init__(__self__, *,
                 cidr: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 container_id: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_name: Optional[pulumi.Input[str]] = None,
                 vm_id: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering FirewallAlias resources.
        :param pulumi.Input[str] cidr: Network/IP specification in CIDR format.
        :param pulumi.Input[str] comment: Alias comment.
        :param pulumi.Input[int] container_id: Container ID. Leave empty for cluster level aliases.
        :param pulumi.Input[str] name: Alias name.
        :param pulumi.Input[str] node_name: Node name. Leave empty for cluster level aliases.
        :param pulumi.Input[int] vm_id: VM ID. Leave empty for cluster level aliases.
        """
        if cidr is not None:
            pulumi.set(__self__, "cidr", cidr)
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if container_id is not None:
            pulumi.set(__self__, "container_id", container_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if node_name is not None:
            pulumi.set(__self__, "node_name", node_name)
        if vm_id is not None:
            pulumi.set(__self__, "vm_id", vm_id)

    @property
    @pulumi.getter
    def cidr(self) -> Optional[pulumi.Input[str]]:
        """
        Network/IP specification in CIDR format.
        """
        return pulumi.get(self, "cidr")

    @cidr.setter
    def cidr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cidr", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        """
        Alias comment.
        """
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter(name="containerId")
    def container_id(self) -> Optional[pulumi.Input[int]]:
        """
        Container ID. Leave empty for cluster level aliases.
        """
        return pulumi.get(self, "container_id")

    @container_id.setter
    def container_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "container_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Alias name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="nodeName")
    def node_name(self) -> Optional[pulumi.Input[str]]:
        """
        Node name. Leave empty for cluster level aliases.
        """
        return pulumi.get(self, "node_name")

    @node_name.setter
    def node_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "node_name", value)

    @property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> Optional[pulumi.Input[int]]:
        """
        VM ID. Leave empty for cluster level aliases.
        """
        return pulumi.get(self, "vm_id")

    @vm_id.setter
    def vm_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "vm_id", value)


class FirewallAlias(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cidr: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 container_id: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_name: Optional[pulumi.Input[str]] = None,
                 vm_id: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Aliases are used to see what devices or group of devices are affected by a rule.
        We can create aliases to identify an IP address or a network. Aliases can be
        created on the cluster level, on VM / Container level.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_proxmoxve as proxmoxve

        local_network = proxmoxve.network.FirewallAlias("localNetwork",
            node_name=proxmox_virtual_environment_vm["example"]["node_name"],
            vm_id=proxmox_virtual_environment_vm["example"]["vm_id"],
            cidr="192.168.0.0/23",
            comment="Managed by Terraform",
            opts = pulumi.ResourceOptions(depends_on=[proxmox_virtual_environment_vm["example"]]))
        ubuntu_vm = proxmoxve.network.FirewallAlias("ubuntuVm",
            cidr="192.168.0.1",
            comment="Managed by Terraform")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cidr: Network/IP specification in CIDR format.
        :param pulumi.Input[str] comment: Alias comment.
        :param pulumi.Input[int] container_id: Container ID. Leave empty for cluster level aliases.
        :param pulumi.Input[str] name: Alias name.
        :param pulumi.Input[str] node_name: Node name. Leave empty for cluster level aliases.
        :param pulumi.Input[int] vm_id: VM ID. Leave empty for cluster level aliases.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FirewallAliasArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Aliases are used to see what devices or group of devices are affected by a rule.
        We can create aliases to identify an IP address or a network. Aliases can be
        created on the cluster level, on VM / Container level.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_proxmoxve as proxmoxve

        local_network = proxmoxve.network.FirewallAlias("localNetwork",
            node_name=proxmox_virtual_environment_vm["example"]["node_name"],
            vm_id=proxmox_virtual_environment_vm["example"]["vm_id"],
            cidr="192.168.0.0/23",
            comment="Managed by Terraform",
            opts = pulumi.ResourceOptions(depends_on=[proxmox_virtual_environment_vm["example"]]))
        ubuntu_vm = proxmoxve.network.FirewallAlias("ubuntuVm",
            cidr="192.168.0.1",
            comment="Managed by Terraform")
        ```

        :param str resource_name: The name of the resource.
        :param FirewallAliasArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FirewallAliasArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cidr: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 container_id: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_name: Optional[pulumi.Input[str]] = None,
                 vm_id: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FirewallAliasArgs.__new__(FirewallAliasArgs)

            if cidr is None and not opts.urn:
                raise TypeError("Missing required property 'cidr'")
            __props__.__dict__["cidr"] = cidr
            __props__.__dict__["comment"] = comment
            __props__.__dict__["container_id"] = container_id
            __props__.__dict__["name"] = name
            __props__.__dict__["node_name"] = node_name
            __props__.__dict__["vm_id"] = vm_id
        super(FirewallAlias, __self__).__init__(
            'proxmoxve:Network/firewallAlias:FirewallAlias',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cidr: Optional[pulumi.Input[str]] = None,
            comment: Optional[pulumi.Input[str]] = None,
            container_id: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            node_name: Optional[pulumi.Input[str]] = None,
            vm_id: Optional[pulumi.Input[int]] = None) -> 'FirewallAlias':
        """
        Get an existing FirewallAlias resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cidr: Network/IP specification in CIDR format.
        :param pulumi.Input[str] comment: Alias comment.
        :param pulumi.Input[int] container_id: Container ID. Leave empty for cluster level aliases.
        :param pulumi.Input[str] name: Alias name.
        :param pulumi.Input[str] node_name: Node name. Leave empty for cluster level aliases.
        :param pulumi.Input[int] vm_id: VM ID. Leave empty for cluster level aliases.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FirewallAliasState.__new__(_FirewallAliasState)

        __props__.__dict__["cidr"] = cidr
        __props__.__dict__["comment"] = comment
        __props__.__dict__["container_id"] = container_id
        __props__.__dict__["name"] = name
        __props__.__dict__["node_name"] = node_name
        __props__.__dict__["vm_id"] = vm_id
        return FirewallAlias(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def cidr(self) -> pulumi.Output[str]:
        """
        Network/IP specification in CIDR format.
        """
        return pulumi.get(self, "cidr")

    @property
    @pulumi.getter
    def comment(self) -> pulumi.Output[Optional[str]]:
        """
        Alias comment.
        """
        return pulumi.get(self, "comment")

    @property
    @pulumi.getter(name="containerId")
    def container_id(self) -> pulumi.Output[Optional[int]]:
        """
        Container ID. Leave empty for cluster level aliases.
        """
        return pulumi.get(self, "container_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Alias name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeName")
    def node_name(self) -> pulumi.Output[Optional[str]]:
        """
        Node name. Leave empty for cluster level aliases.
        """
        return pulumi.get(self, "node_name")

    @property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> pulumi.Output[Optional[int]]:
        """
        VM ID. Leave empty for cluster level aliases.
        """
        return pulumi.get(self, "vm_id")

