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
from ._inputs import *

__all__ = ['FirewallSecurityGroupArgs', 'FirewallSecurityGroup']

@pulumi.input_type
class FirewallSecurityGroupArgs:
    def __init__(__self__, *,
                 rules: pulumi.Input[Sequence[pulumi.Input['FirewallSecurityGroupRuleArgs']]],
                 comment: Optional[pulumi.Input[str]] = None,
                 container_id: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_name: Optional[pulumi.Input[str]] = None,
                 vm_id: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a FirewallSecurityGroup resource.
        :param pulumi.Input[Sequence[pulumi.Input['FirewallSecurityGroupRuleArgs']]] rules: Firewall rule block (multiple blocks supported).
        :param pulumi.Input[str] comment: Rule comment.
        :param pulumi.Input[int] container_id: The ID of the container to manage the firewall for.
        :param pulumi.Input[str] name: Security group name.
        :param pulumi.Input[str] node_name: The name of the node.
        :param pulumi.Input[int] vm_id: The ID of the VM to manage the firewall for.
        """
        pulumi.set(__self__, "rules", rules)
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
    def rules(self) -> pulumi.Input[Sequence[pulumi.Input['FirewallSecurityGroupRuleArgs']]]:
        """
        Firewall rule block (multiple blocks supported).
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: pulumi.Input[Sequence[pulumi.Input['FirewallSecurityGroupRuleArgs']]]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        """
        Rule comment.
        """
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter(name="containerId")
    def container_id(self) -> Optional[pulumi.Input[int]]:
        """
        The ID of the container to manage the firewall for.
        """
        return pulumi.get(self, "container_id")

    @container_id.setter
    def container_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "container_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Security group name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="nodeName")
    def node_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the node.
        """
        return pulumi.get(self, "node_name")

    @node_name.setter
    def node_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "node_name", value)

    @property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> Optional[pulumi.Input[int]]:
        """
        The ID of the VM to manage the firewall for.
        """
        return pulumi.get(self, "vm_id")

    @vm_id.setter
    def vm_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "vm_id", value)


@pulumi.input_type
class _FirewallSecurityGroupState:
    def __init__(__self__, *,
                 comment: Optional[pulumi.Input[str]] = None,
                 container_id: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input['FirewallSecurityGroupRuleArgs']]]] = None,
                 vm_id: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering FirewallSecurityGroup resources.
        :param pulumi.Input[str] comment: Rule comment.
        :param pulumi.Input[int] container_id: The ID of the container to manage the firewall for.
        :param pulumi.Input[str] name: Security group name.
        :param pulumi.Input[str] node_name: The name of the node.
        :param pulumi.Input[Sequence[pulumi.Input['FirewallSecurityGroupRuleArgs']]] rules: Firewall rule block (multiple blocks supported).
        :param pulumi.Input[int] vm_id: The ID of the VM to manage the firewall for.
        """
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if container_id is not None:
            pulumi.set(__self__, "container_id", container_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if node_name is not None:
            pulumi.set(__self__, "node_name", node_name)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)
        if vm_id is not None:
            pulumi.set(__self__, "vm_id", vm_id)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        """
        Rule comment.
        """
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter(name="containerId")
    def container_id(self) -> Optional[pulumi.Input[int]]:
        """
        The ID of the container to manage the firewall for.
        """
        return pulumi.get(self, "container_id")

    @container_id.setter
    def container_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "container_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Security group name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="nodeName")
    def node_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the node.
        """
        return pulumi.get(self, "node_name")

    @node_name.setter
    def node_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "node_name", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FirewallSecurityGroupRuleArgs']]]]:
        """
        Firewall rule block (multiple blocks supported).
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FirewallSecurityGroupRuleArgs']]]]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> Optional[pulumi.Input[int]]:
        """
        The ID of the VM to manage the firewall for.
        """
        return pulumi.get(self, "vm_id")

    @vm_id.setter
    def vm_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "vm_id", value)


class FirewallSecurityGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 container_id: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallSecurityGroupRuleArgs']]]]] = None,
                 vm_id: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        A security group is a collection of rules, defined at cluster level, which can
        be used in all VMs' rules. For example, you can define a group named “webserver”
        with rules to open the http and https ports.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_proxmoxve as proxmoxve

        webserver = proxmoxve.network.FirewallSecurityGroup("webserver",
            comment="Managed by Terraform",
            rules=[
                proxmoxve.network.FirewallSecurityGroupRuleArgs(
                    action="ACCEPT",
                    comment="Allow HTTP",
                    dest="192.168.1.5",
                    dport="80",
                    log="info",
                    proto="tcp",
                    type="in",
                ),
                proxmoxve.network.FirewallSecurityGroupRuleArgs(
                    action="ACCEPT",
                    comment="Allow HTTPS",
                    dest="192.168.1.5",
                    dport="443",
                    log="info",
                    proto="tcp",
                    type="in",
                ),
            ])
        ```

        ## Import

        Instances can be imported using the `name`, e.g., bash

        ```sh
         $ pulumi import proxmoxve:Network/firewallSecurityGroup:FirewallSecurityGroup webserver webserver
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] comment: Rule comment.
        :param pulumi.Input[int] container_id: The ID of the container to manage the firewall for.
        :param pulumi.Input[str] name: Security group name.
        :param pulumi.Input[str] node_name: The name of the node.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallSecurityGroupRuleArgs']]]] rules: Firewall rule block (multiple blocks supported).
        :param pulumi.Input[int] vm_id: The ID of the VM to manage the firewall for.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FirewallSecurityGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A security group is a collection of rules, defined at cluster level, which can
        be used in all VMs' rules. For example, you can define a group named “webserver”
        with rules to open the http and https ports.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_proxmoxve as proxmoxve

        webserver = proxmoxve.network.FirewallSecurityGroup("webserver",
            comment="Managed by Terraform",
            rules=[
                proxmoxve.network.FirewallSecurityGroupRuleArgs(
                    action="ACCEPT",
                    comment="Allow HTTP",
                    dest="192.168.1.5",
                    dport="80",
                    log="info",
                    proto="tcp",
                    type="in",
                ),
                proxmoxve.network.FirewallSecurityGroupRuleArgs(
                    action="ACCEPT",
                    comment="Allow HTTPS",
                    dest="192.168.1.5",
                    dport="443",
                    log="info",
                    proto="tcp",
                    type="in",
                ),
            ])
        ```

        ## Import

        Instances can be imported using the `name`, e.g., bash

        ```sh
         $ pulumi import proxmoxve:Network/firewallSecurityGroup:FirewallSecurityGroup webserver webserver
        ```

        :param str resource_name: The name of the resource.
        :param FirewallSecurityGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FirewallSecurityGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 container_id: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallSecurityGroupRuleArgs']]]]] = None,
                 vm_id: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FirewallSecurityGroupArgs.__new__(FirewallSecurityGroupArgs)

            __props__.__dict__["comment"] = comment
            __props__.__dict__["container_id"] = container_id
            __props__.__dict__["name"] = name
            __props__.__dict__["node_name"] = node_name
            if rules is None and not opts.urn:
                raise TypeError("Missing required property 'rules'")
            __props__.__dict__["rules"] = rules
            __props__.__dict__["vm_id"] = vm_id
        super(FirewallSecurityGroup, __self__).__init__(
            'proxmoxve:Network/firewallSecurityGroup:FirewallSecurityGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            comment: Optional[pulumi.Input[str]] = None,
            container_id: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            node_name: Optional[pulumi.Input[str]] = None,
            rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallSecurityGroupRuleArgs']]]]] = None,
            vm_id: Optional[pulumi.Input[int]] = None) -> 'FirewallSecurityGroup':
        """
        Get an existing FirewallSecurityGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] comment: Rule comment.
        :param pulumi.Input[int] container_id: The ID of the container to manage the firewall for.
        :param pulumi.Input[str] name: Security group name.
        :param pulumi.Input[str] node_name: The name of the node.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallSecurityGroupRuleArgs']]]] rules: Firewall rule block (multiple blocks supported).
        :param pulumi.Input[int] vm_id: The ID of the VM to manage the firewall for.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FirewallSecurityGroupState.__new__(_FirewallSecurityGroupState)

        __props__.__dict__["comment"] = comment
        __props__.__dict__["container_id"] = container_id
        __props__.__dict__["name"] = name
        __props__.__dict__["node_name"] = node_name
        __props__.__dict__["rules"] = rules
        __props__.__dict__["vm_id"] = vm_id
        return FirewallSecurityGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def comment(self) -> pulumi.Output[Optional[str]]:
        """
        Rule comment.
        """
        return pulumi.get(self, "comment")

    @property
    @pulumi.getter(name="containerId")
    def container_id(self) -> pulumi.Output[Optional[int]]:
        """
        The ID of the container to manage the firewall for.
        """
        return pulumi.get(self, "container_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Security group name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeName")
    def node_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the node.
        """
        return pulumi.get(self, "node_name")

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Sequence['outputs.FirewallSecurityGroupRule']]:
        """
        Firewall rule block (multiple blocks supported).
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> pulumi.Output[Optional[int]]:
        """
        The ID of the VM to manage the firewall for.
        """
        return pulumi.get(self, "vm_id")

