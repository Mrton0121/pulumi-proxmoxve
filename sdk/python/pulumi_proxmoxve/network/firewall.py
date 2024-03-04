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

__all__ = ['FirewallArgs', 'Firewall']

@pulumi.input_type
class FirewallArgs:
    def __init__(__self__, *,
                 ebtables: Optional[pulumi.Input[bool]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 input_policy: Optional[pulumi.Input[str]] = None,
                 log_ratelimit: Optional[pulumi.Input['FirewallLogRatelimitArgs']] = None,
                 output_policy: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Firewall resource.
        :param pulumi.Input[bool] ebtables: Enable ebtables rules cluster wide.
        :param pulumi.Input[bool] enabled: Enable or disable the log rate limit.
        :param pulumi.Input[str] input_policy: The default input policy (`ACCEPT`, `DROP`, `REJECT`).
        :param pulumi.Input['FirewallLogRatelimitArgs'] log_ratelimit: The log rate limit.
        :param pulumi.Input[str] output_policy: The default output policy (`ACCEPT`, `DROP`, `REJECT`).
        """
        if ebtables is not None:
            pulumi.set(__self__, "ebtables", ebtables)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if input_policy is not None:
            pulumi.set(__self__, "input_policy", input_policy)
        if log_ratelimit is not None:
            pulumi.set(__self__, "log_ratelimit", log_ratelimit)
        if output_policy is not None:
            pulumi.set(__self__, "output_policy", output_policy)

    @property
    @pulumi.getter
    def ebtables(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable ebtables rules cluster wide.
        """
        return pulumi.get(self, "ebtables")

    @ebtables.setter
    def ebtables(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ebtables", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable or disable the log rate limit.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="inputPolicy")
    def input_policy(self) -> Optional[pulumi.Input[str]]:
        """
        The default input policy (`ACCEPT`, `DROP`, `REJECT`).
        """
        return pulumi.get(self, "input_policy")

    @input_policy.setter
    def input_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "input_policy", value)

    @property
    @pulumi.getter(name="logRatelimit")
    def log_ratelimit(self) -> Optional[pulumi.Input['FirewallLogRatelimitArgs']]:
        """
        The log rate limit.
        """
        return pulumi.get(self, "log_ratelimit")

    @log_ratelimit.setter
    def log_ratelimit(self, value: Optional[pulumi.Input['FirewallLogRatelimitArgs']]):
        pulumi.set(self, "log_ratelimit", value)

    @property
    @pulumi.getter(name="outputPolicy")
    def output_policy(self) -> Optional[pulumi.Input[str]]:
        """
        The default output policy (`ACCEPT`, `DROP`, `REJECT`).
        """
        return pulumi.get(self, "output_policy")

    @output_policy.setter
    def output_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "output_policy", value)


@pulumi.input_type
class _FirewallState:
    def __init__(__self__, *,
                 ebtables: Optional[pulumi.Input[bool]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 input_policy: Optional[pulumi.Input[str]] = None,
                 log_ratelimit: Optional[pulumi.Input['FirewallLogRatelimitArgs']] = None,
                 output_policy: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Firewall resources.
        :param pulumi.Input[bool] ebtables: Enable ebtables rules cluster wide.
        :param pulumi.Input[bool] enabled: Enable or disable the log rate limit.
        :param pulumi.Input[str] input_policy: The default input policy (`ACCEPT`, `DROP`, `REJECT`).
        :param pulumi.Input['FirewallLogRatelimitArgs'] log_ratelimit: The log rate limit.
        :param pulumi.Input[str] output_policy: The default output policy (`ACCEPT`, `DROP`, `REJECT`).
        """
        if ebtables is not None:
            pulumi.set(__self__, "ebtables", ebtables)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if input_policy is not None:
            pulumi.set(__self__, "input_policy", input_policy)
        if log_ratelimit is not None:
            pulumi.set(__self__, "log_ratelimit", log_ratelimit)
        if output_policy is not None:
            pulumi.set(__self__, "output_policy", output_policy)

    @property
    @pulumi.getter
    def ebtables(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable ebtables rules cluster wide.
        """
        return pulumi.get(self, "ebtables")

    @ebtables.setter
    def ebtables(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ebtables", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable or disable the log rate limit.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="inputPolicy")
    def input_policy(self) -> Optional[pulumi.Input[str]]:
        """
        The default input policy (`ACCEPT`, `DROP`, `REJECT`).
        """
        return pulumi.get(self, "input_policy")

    @input_policy.setter
    def input_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "input_policy", value)

    @property
    @pulumi.getter(name="logRatelimit")
    def log_ratelimit(self) -> Optional[pulumi.Input['FirewallLogRatelimitArgs']]:
        """
        The log rate limit.
        """
        return pulumi.get(self, "log_ratelimit")

    @log_ratelimit.setter
    def log_ratelimit(self, value: Optional[pulumi.Input['FirewallLogRatelimitArgs']]):
        pulumi.set(self, "log_ratelimit", value)

    @property
    @pulumi.getter(name="outputPolicy")
    def output_policy(self) -> Optional[pulumi.Input[str]]:
        """
        The default output policy (`ACCEPT`, `DROP`, `REJECT`).
        """
        return pulumi.get(self, "output_policy")

    @output_policy.setter
    def output_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "output_policy", value)


class Firewall(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ebtables: Optional[pulumi.Input[bool]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 input_policy: Optional[pulumi.Input[str]] = None,
                 log_ratelimit: Optional[pulumi.Input[pulumi.InputType['FirewallLogRatelimitArgs']]] = None,
                 output_policy: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages firewall options on the cluster level.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_proxmoxve as proxmoxve

        example = proxmoxve.network.Firewall("example",
            ebtables=False,
            enabled=False,
            input_policy="DROP",
            log_ratelimit=proxmoxve.network.FirewallLogRatelimitArgs(
                burst=10,
                enabled=False,
                rate="5/second",
            ),
            output_policy="ACCEPT")
        ```
        ## Important Notes

        Be careful not to use this resource multiple times for the same node.

        ## Import

        Instances can be imported without an ID, but you still need to pass one, e.g., bash

        ```sh
         $ pulumi import proxmoxve:Network/firewall:Firewall example example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] ebtables: Enable ebtables rules cluster wide.
        :param pulumi.Input[bool] enabled: Enable or disable the log rate limit.
        :param pulumi.Input[str] input_policy: The default input policy (`ACCEPT`, `DROP`, `REJECT`).
        :param pulumi.Input[pulumi.InputType['FirewallLogRatelimitArgs']] log_ratelimit: The log rate limit.
        :param pulumi.Input[str] output_policy: The default output policy (`ACCEPT`, `DROP`, `REJECT`).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[FirewallArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages firewall options on the cluster level.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_proxmoxve as proxmoxve

        example = proxmoxve.network.Firewall("example",
            ebtables=False,
            enabled=False,
            input_policy="DROP",
            log_ratelimit=proxmoxve.network.FirewallLogRatelimitArgs(
                burst=10,
                enabled=False,
                rate="5/second",
            ),
            output_policy="ACCEPT")
        ```
        ## Important Notes

        Be careful not to use this resource multiple times for the same node.

        ## Import

        Instances can be imported without an ID, but you still need to pass one, e.g., bash

        ```sh
         $ pulumi import proxmoxve:Network/firewall:Firewall example example
        ```

        :param str resource_name: The name of the resource.
        :param FirewallArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FirewallArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ebtables: Optional[pulumi.Input[bool]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 input_policy: Optional[pulumi.Input[str]] = None,
                 log_ratelimit: Optional[pulumi.Input[pulumi.InputType['FirewallLogRatelimitArgs']]] = None,
                 output_policy: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FirewallArgs.__new__(FirewallArgs)

            __props__.__dict__["ebtables"] = ebtables
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["input_policy"] = input_policy
            __props__.__dict__["log_ratelimit"] = log_ratelimit
            __props__.__dict__["output_policy"] = output_policy
        super(Firewall, __self__).__init__(
            'proxmoxve:Network/firewall:Firewall',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            ebtables: Optional[pulumi.Input[bool]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            input_policy: Optional[pulumi.Input[str]] = None,
            log_ratelimit: Optional[pulumi.Input[pulumi.InputType['FirewallLogRatelimitArgs']]] = None,
            output_policy: Optional[pulumi.Input[str]] = None) -> 'Firewall':
        """
        Get an existing Firewall resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] ebtables: Enable ebtables rules cluster wide.
        :param pulumi.Input[bool] enabled: Enable or disable the log rate limit.
        :param pulumi.Input[str] input_policy: The default input policy (`ACCEPT`, `DROP`, `REJECT`).
        :param pulumi.Input[pulumi.InputType['FirewallLogRatelimitArgs']] log_ratelimit: The log rate limit.
        :param pulumi.Input[str] output_policy: The default output policy (`ACCEPT`, `DROP`, `REJECT`).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FirewallState.__new__(_FirewallState)

        __props__.__dict__["ebtables"] = ebtables
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["input_policy"] = input_policy
        __props__.__dict__["log_ratelimit"] = log_ratelimit
        __props__.__dict__["output_policy"] = output_policy
        return Firewall(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def ebtables(self) -> pulumi.Output[Optional[bool]]:
        """
        Enable ebtables rules cluster wide.
        """
        return pulumi.get(self, "ebtables")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Enable or disable the log rate limit.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="inputPolicy")
    def input_policy(self) -> pulumi.Output[Optional[str]]:
        """
        The default input policy (`ACCEPT`, `DROP`, `REJECT`).
        """
        return pulumi.get(self, "input_policy")

    @property
    @pulumi.getter(name="logRatelimit")
    def log_ratelimit(self) -> pulumi.Output[Optional['outputs.FirewallLogRatelimit']]:
        """
        The log rate limit.
        """
        return pulumi.get(self, "log_ratelimit")

    @property
    @pulumi.getter(name="outputPolicy")
    def output_policy(self) -> pulumi.Output[Optional[str]]:
        """
        The default output policy (`ACCEPT`, `DROP`, `REJECT`).
        """
        return pulumi.get(self, "output_policy")

