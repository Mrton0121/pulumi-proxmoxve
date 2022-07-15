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

__all__ = ['ContainerArgs', 'Container']

@pulumi.input_type
class ContainerArgs:
    def __init__(__self__, *,
                 node_name: pulumi.Input[str],
                 clone: Optional[pulumi.Input['ContainerCloneArgs']] = None,
                 console: Optional[pulumi.Input['ContainerConsoleArgs']] = None,
                 cpu: Optional[pulumi.Input['ContainerCpuArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 disk: Optional[pulumi.Input['ContainerDiskArgs']] = None,
                 initialization: Optional[pulumi.Input['ContainerInitializationArgs']] = None,
                 memory: Optional[pulumi.Input['ContainerMemoryArgs']] = None,
                 network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input['ContainerNetworkInterfaceArgs']]]] = None,
                 operating_system: Optional[pulumi.Input['ContainerOperatingSystemArgs']] = None,
                 pool_id: Optional[pulumi.Input[str]] = None,
                 started: Optional[pulumi.Input[bool]] = None,
                 template: Optional[pulumi.Input[bool]] = None,
                 vm_id: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a Container resource.
        :param pulumi.Input[str] node_name: The node name
        :param pulumi.Input['ContainerCloneArgs'] clone: The cloning configuration
        :param pulumi.Input['ContainerConsoleArgs'] console: The console configuration
        :param pulumi.Input['ContainerCpuArgs'] cpu: The CPU allocation
        :param pulumi.Input[str] description: The description
        :param pulumi.Input['ContainerDiskArgs'] disk: The disks
        :param pulumi.Input['ContainerInitializationArgs'] initialization: The initialization configuration
        :param pulumi.Input['ContainerMemoryArgs'] memory: The memory allocation
        :param pulumi.Input[Sequence[pulumi.Input['ContainerNetworkInterfaceArgs']]] network_interfaces: The network interfaces
        :param pulumi.Input['ContainerOperatingSystemArgs'] operating_system: The operating system configuration
        :param pulumi.Input[str] pool_id: The ID of the pool to assign the container to
        :param pulumi.Input[bool] started: Whether to start the container
        :param pulumi.Input[bool] template: Whether to create a template
        :param pulumi.Input[int] vm_id: The VM identifier
        """
        pulumi.set(__self__, "node_name", node_name)
        if clone is not None:
            pulumi.set(__self__, "clone", clone)
        if console is not None:
            pulumi.set(__self__, "console", console)
        if cpu is not None:
            pulumi.set(__self__, "cpu", cpu)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if disk is not None:
            pulumi.set(__self__, "disk", disk)
        if initialization is not None:
            pulumi.set(__self__, "initialization", initialization)
        if memory is not None:
            pulumi.set(__self__, "memory", memory)
        if network_interfaces is not None:
            pulumi.set(__self__, "network_interfaces", network_interfaces)
        if operating_system is not None:
            pulumi.set(__self__, "operating_system", operating_system)
        if pool_id is not None:
            pulumi.set(__self__, "pool_id", pool_id)
        if started is not None:
            pulumi.set(__self__, "started", started)
        if template is not None:
            pulumi.set(__self__, "template", template)
        if vm_id is not None:
            pulumi.set(__self__, "vm_id", vm_id)

    @property
    @pulumi.getter(name="nodeName")
    def node_name(self) -> pulumi.Input[str]:
        """
        The node name
        """
        return pulumi.get(self, "node_name")

    @node_name.setter
    def node_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "node_name", value)

    @property
    @pulumi.getter
    def clone(self) -> Optional[pulumi.Input['ContainerCloneArgs']]:
        """
        The cloning configuration
        """
        return pulumi.get(self, "clone")

    @clone.setter
    def clone(self, value: Optional[pulumi.Input['ContainerCloneArgs']]):
        pulumi.set(self, "clone", value)

    @property
    @pulumi.getter
    def console(self) -> Optional[pulumi.Input['ContainerConsoleArgs']]:
        """
        The console configuration
        """
        return pulumi.get(self, "console")

    @console.setter
    def console(self, value: Optional[pulumi.Input['ContainerConsoleArgs']]):
        pulumi.set(self, "console", value)

    @property
    @pulumi.getter
    def cpu(self) -> Optional[pulumi.Input['ContainerCpuArgs']]:
        """
        The CPU allocation
        """
        return pulumi.get(self, "cpu")

    @cpu.setter
    def cpu(self, value: Optional[pulumi.Input['ContainerCpuArgs']]):
        pulumi.set(self, "cpu", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def disk(self) -> Optional[pulumi.Input['ContainerDiskArgs']]:
        """
        The disks
        """
        return pulumi.get(self, "disk")

    @disk.setter
    def disk(self, value: Optional[pulumi.Input['ContainerDiskArgs']]):
        pulumi.set(self, "disk", value)

    @property
    @pulumi.getter
    def initialization(self) -> Optional[pulumi.Input['ContainerInitializationArgs']]:
        """
        The initialization configuration
        """
        return pulumi.get(self, "initialization")

    @initialization.setter
    def initialization(self, value: Optional[pulumi.Input['ContainerInitializationArgs']]):
        pulumi.set(self, "initialization", value)

    @property
    @pulumi.getter
    def memory(self) -> Optional[pulumi.Input['ContainerMemoryArgs']]:
        """
        The memory allocation
        """
        return pulumi.get(self, "memory")

    @memory.setter
    def memory(self, value: Optional[pulumi.Input['ContainerMemoryArgs']]):
        pulumi.set(self, "memory", value)

    @property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ContainerNetworkInterfaceArgs']]]]:
        """
        The network interfaces
        """
        return pulumi.get(self, "network_interfaces")

    @network_interfaces.setter
    def network_interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ContainerNetworkInterfaceArgs']]]]):
        pulumi.set(self, "network_interfaces", value)

    @property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> Optional[pulumi.Input['ContainerOperatingSystemArgs']]:
        """
        The operating system configuration
        """
        return pulumi.get(self, "operating_system")

    @operating_system.setter
    def operating_system(self, value: Optional[pulumi.Input['ContainerOperatingSystemArgs']]):
        pulumi.set(self, "operating_system", value)

    @property
    @pulumi.getter(name="poolId")
    def pool_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the pool to assign the container to
        """
        return pulumi.get(self, "pool_id")

    @pool_id.setter
    def pool_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pool_id", value)

    @property
    @pulumi.getter
    def started(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to start the container
        """
        return pulumi.get(self, "started")

    @started.setter
    def started(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "started", value)

    @property
    @pulumi.getter
    def template(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to create a template
        """
        return pulumi.get(self, "template")

    @template.setter
    def template(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "template", value)

    @property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> Optional[pulumi.Input[int]]:
        """
        The VM identifier
        """
        return pulumi.get(self, "vm_id")

    @vm_id.setter
    def vm_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "vm_id", value)


@pulumi.input_type
class _ContainerState:
    def __init__(__self__, *,
                 clone: Optional[pulumi.Input['ContainerCloneArgs']] = None,
                 console: Optional[pulumi.Input['ContainerConsoleArgs']] = None,
                 cpu: Optional[pulumi.Input['ContainerCpuArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 disk: Optional[pulumi.Input['ContainerDiskArgs']] = None,
                 initialization: Optional[pulumi.Input['ContainerInitializationArgs']] = None,
                 memory: Optional[pulumi.Input['ContainerMemoryArgs']] = None,
                 network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input['ContainerNetworkInterfaceArgs']]]] = None,
                 node_name: Optional[pulumi.Input[str]] = None,
                 operating_system: Optional[pulumi.Input['ContainerOperatingSystemArgs']] = None,
                 pool_id: Optional[pulumi.Input[str]] = None,
                 started: Optional[pulumi.Input[bool]] = None,
                 template: Optional[pulumi.Input[bool]] = None,
                 vm_id: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering Container resources.
        :param pulumi.Input['ContainerCloneArgs'] clone: The cloning configuration
        :param pulumi.Input['ContainerConsoleArgs'] console: The console configuration
        :param pulumi.Input['ContainerCpuArgs'] cpu: The CPU allocation
        :param pulumi.Input[str] description: The description
        :param pulumi.Input['ContainerDiskArgs'] disk: The disks
        :param pulumi.Input['ContainerInitializationArgs'] initialization: The initialization configuration
        :param pulumi.Input['ContainerMemoryArgs'] memory: The memory allocation
        :param pulumi.Input[Sequence[pulumi.Input['ContainerNetworkInterfaceArgs']]] network_interfaces: The network interfaces
        :param pulumi.Input[str] node_name: The node name
        :param pulumi.Input['ContainerOperatingSystemArgs'] operating_system: The operating system configuration
        :param pulumi.Input[str] pool_id: The ID of the pool to assign the container to
        :param pulumi.Input[bool] started: Whether to start the container
        :param pulumi.Input[bool] template: Whether to create a template
        :param pulumi.Input[int] vm_id: The VM identifier
        """
        if clone is not None:
            pulumi.set(__self__, "clone", clone)
        if console is not None:
            pulumi.set(__self__, "console", console)
        if cpu is not None:
            pulumi.set(__self__, "cpu", cpu)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if disk is not None:
            pulumi.set(__self__, "disk", disk)
        if initialization is not None:
            pulumi.set(__self__, "initialization", initialization)
        if memory is not None:
            pulumi.set(__self__, "memory", memory)
        if network_interfaces is not None:
            pulumi.set(__self__, "network_interfaces", network_interfaces)
        if node_name is not None:
            pulumi.set(__self__, "node_name", node_name)
        if operating_system is not None:
            pulumi.set(__self__, "operating_system", operating_system)
        if pool_id is not None:
            pulumi.set(__self__, "pool_id", pool_id)
        if started is not None:
            pulumi.set(__self__, "started", started)
        if template is not None:
            pulumi.set(__self__, "template", template)
        if vm_id is not None:
            pulumi.set(__self__, "vm_id", vm_id)

    @property
    @pulumi.getter
    def clone(self) -> Optional[pulumi.Input['ContainerCloneArgs']]:
        """
        The cloning configuration
        """
        return pulumi.get(self, "clone")

    @clone.setter
    def clone(self, value: Optional[pulumi.Input['ContainerCloneArgs']]):
        pulumi.set(self, "clone", value)

    @property
    @pulumi.getter
    def console(self) -> Optional[pulumi.Input['ContainerConsoleArgs']]:
        """
        The console configuration
        """
        return pulumi.get(self, "console")

    @console.setter
    def console(self, value: Optional[pulumi.Input['ContainerConsoleArgs']]):
        pulumi.set(self, "console", value)

    @property
    @pulumi.getter
    def cpu(self) -> Optional[pulumi.Input['ContainerCpuArgs']]:
        """
        The CPU allocation
        """
        return pulumi.get(self, "cpu")

    @cpu.setter
    def cpu(self, value: Optional[pulumi.Input['ContainerCpuArgs']]):
        pulumi.set(self, "cpu", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def disk(self) -> Optional[pulumi.Input['ContainerDiskArgs']]:
        """
        The disks
        """
        return pulumi.get(self, "disk")

    @disk.setter
    def disk(self, value: Optional[pulumi.Input['ContainerDiskArgs']]):
        pulumi.set(self, "disk", value)

    @property
    @pulumi.getter
    def initialization(self) -> Optional[pulumi.Input['ContainerInitializationArgs']]:
        """
        The initialization configuration
        """
        return pulumi.get(self, "initialization")

    @initialization.setter
    def initialization(self, value: Optional[pulumi.Input['ContainerInitializationArgs']]):
        pulumi.set(self, "initialization", value)

    @property
    @pulumi.getter
    def memory(self) -> Optional[pulumi.Input['ContainerMemoryArgs']]:
        """
        The memory allocation
        """
        return pulumi.get(self, "memory")

    @memory.setter
    def memory(self, value: Optional[pulumi.Input['ContainerMemoryArgs']]):
        pulumi.set(self, "memory", value)

    @property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ContainerNetworkInterfaceArgs']]]]:
        """
        The network interfaces
        """
        return pulumi.get(self, "network_interfaces")

    @network_interfaces.setter
    def network_interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ContainerNetworkInterfaceArgs']]]]):
        pulumi.set(self, "network_interfaces", value)

    @property
    @pulumi.getter(name="nodeName")
    def node_name(self) -> Optional[pulumi.Input[str]]:
        """
        The node name
        """
        return pulumi.get(self, "node_name")

    @node_name.setter
    def node_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "node_name", value)

    @property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> Optional[pulumi.Input['ContainerOperatingSystemArgs']]:
        """
        The operating system configuration
        """
        return pulumi.get(self, "operating_system")

    @operating_system.setter
    def operating_system(self, value: Optional[pulumi.Input['ContainerOperatingSystemArgs']]):
        pulumi.set(self, "operating_system", value)

    @property
    @pulumi.getter(name="poolId")
    def pool_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the pool to assign the container to
        """
        return pulumi.get(self, "pool_id")

    @pool_id.setter
    def pool_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pool_id", value)

    @property
    @pulumi.getter
    def started(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to start the container
        """
        return pulumi.get(self, "started")

    @started.setter
    def started(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "started", value)

    @property
    @pulumi.getter
    def template(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to create a template
        """
        return pulumi.get(self, "template")

    @template.setter
    def template(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "template", value)

    @property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> Optional[pulumi.Input[int]]:
        """
        The VM identifier
        """
        return pulumi.get(self, "vm_id")

    @vm_id.setter
    def vm_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "vm_id", value)


class Container(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 clone: Optional[pulumi.Input[pulumi.InputType['ContainerCloneArgs']]] = None,
                 console: Optional[pulumi.Input[pulumi.InputType['ContainerConsoleArgs']]] = None,
                 cpu: Optional[pulumi.Input[pulumi.InputType['ContainerCpuArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 disk: Optional[pulumi.Input[pulumi.InputType['ContainerDiskArgs']]] = None,
                 initialization: Optional[pulumi.Input[pulumi.InputType['ContainerInitializationArgs']]] = None,
                 memory: Optional[pulumi.Input[pulumi.InputType['ContainerMemoryArgs']]] = None,
                 network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContainerNetworkInterfaceArgs']]]]] = None,
                 node_name: Optional[pulumi.Input[str]] = None,
                 operating_system: Optional[pulumi.Input[pulumi.InputType['ContainerOperatingSystemArgs']]] = None,
                 pool_id: Optional[pulumi.Input[str]] = None,
                 started: Optional[pulumi.Input[bool]] = None,
                 template: Optional[pulumi.Input[bool]] = None,
                 vm_id: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Create a Container resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ContainerCloneArgs']] clone: The cloning configuration
        :param pulumi.Input[pulumi.InputType['ContainerConsoleArgs']] console: The console configuration
        :param pulumi.Input[pulumi.InputType['ContainerCpuArgs']] cpu: The CPU allocation
        :param pulumi.Input[str] description: The description
        :param pulumi.Input[pulumi.InputType['ContainerDiskArgs']] disk: The disks
        :param pulumi.Input[pulumi.InputType['ContainerInitializationArgs']] initialization: The initialization configuration
        :param pulumi.Input[pulumi.InputType['ContainerMemoryArgs']] memory: The memory allocation
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContainerNetworkInterfaceArgs']]]] network_interfaces: The network interfaces
        :param pulumi.Input[str] node_name: The node name
        :param pulumi.Input[pulumi.InputType['ContainerOperatingSystemArgs']] operating_system: The operating system configuration
        :param pulumi.Input[str] pool_id: The ID of the pool to assign the container to
        :param pulumi.Input[bool] started: Whether to start the container
        :param pulumi.Input[bool] template: Whether to create a template
        :param pulumi.Input[int] vm_id: The VM identifier
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ContainerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Container resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ContainerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ContainerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 clone: Optional[pulumi.Input[pulumi.InputType['ContainerCloneArgs']]] = None,
                 console: Optional[pulumi.Input[pulumi.InputType['ContainerConsoleArgs']]] = None,
                 cpu: Optional[pulumi.Input[pulumi.InputType['ContainerCpuArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 disk: Optional[pulumi.Input[pulumi.InputType['ContainerDiskArgs']]] = None,
                 initialization: Optional[pulumi.Input[pulumi.InputType['ContainerInitializationArgs']]] = None,
                 memory: Optional[pulumi.Input[pulumi.InputType['ContainerMemoryArgs']]] = None,
                 network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContainerNetworkInterfaceArgs']]]]] = None,
                 node_name: Optional[pulumi.Input[str]] = None,
                 operating_system: Optional[pulumi.Input[pulumi.InputType['ContainerOperatingSystemArgs']]] = None,
                 pool_id: Optional[pulumi.Input[str]] = None,
                 started: Optional[pulumi.Input[bool]] = None,
                 template: Optional[pulumi.Input[bool]] = None,
                 vm_id: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ContainerArgs.__new__(ContainerArgs)

            __props__.__dict__["clone"] = clone
            __props__.__dict__["console"] = console
            __props__.__dict__["cpu"] = cpu
            __props__.__dict__["description"] = description
            __props__.__dict__["disk"] = disk
            __props__.__dict__["initialization"] = initialization
            __props__.__dict__["memory"] = memory
            __props__.__dict__["network_interfaces"] = network_interfaces
            if node_name is None and not opts.urn:
                raise TypeError("Missing required property 'node_name'")
            __props__.__dict__["node_name"] = node_name
            __props__.__dict__["operating_system"] = operating_system
            __props__.__dict__["pool_id"] = pool_id
            __props__.__dict__["started"] = started
            __props__.__dict__["template"] = template
            __props__.__dict__["vm_id"] = vm_id
        super(Container, __self__).__init__(
            'proxmoxve:CT/container:Container',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            clone: Optional[pulumi.Input[pulumi.InputType['ContainerCloneArgs']]] = None,
            console: Optional[pulumi.Input[pulumi.InputType['ContainerConsoleArgs']]] = None,
            cpu: Optional[pulumi.Input[pulumi.InputType['ContainerCpuArgs']]] = None,
            description: Optional[pulumi.Input[str]] = None,
            disk: Optional[pulumi.Input[pulumi.InputType['ContainerDiskArgs']]] = None,
            initialization: Optional[pulumi.Input[pulumi.InputType['ContainerInitializationArgs']]] = None,
            memory: Optional[pulumi.Input[pulumi.InputType['ContainerMemoryArgs']]] = None,
            network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContainerNetworkInterfaceArgs']]]]] = None,
            node_name: Optional[pulumi.Input[str]] = None,
            operating_system: Optional[pulumi.Input[pulumi.InputType['ContainerOperatingSystemArgs']]] = None,
            pool_id: Optional[pulumi.Input[str]] = None,
            started: Optional[pulumi.Input[bool]] = None,
            template: Optional[pulumi.Input[bool]] = None,
            vm_id: Optional[pulumi.Input[int]] = None) -> 'Container':
        """
        Get an existing Container resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ContainerCloneArgs']] clone: The cloning configuration
        :param pulumi.Input[pulumi.InputType['ContainerConsoleArgs']] console: The console configuration
        :param pulumi.Input[pulumi.InputType['ContainerCpuArgs']] cpu: The CPU allocation
        :param pulumi.Input[str] description: The description
        :param pulumi.Input[pulumi.InputType['ContainerDiskArgs']] disk: The disks
        :param pulumi.Input[pulumi.InputType['ContainerInitializationArgs']] initialization: The initialization configuration
        :param pulumi.Input[pulumi.InputType['ContainerMemoryArgs']] memory: The memory allocation
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContainerNetworkInterfaceArgs']]]] network_interfaces: The network interfaces
        :param pulumi.Input[str] node_name: The node name
        :param pulumi.Input[pulumi.InputType['ContainerOperatingSystemArgs']] operating_system: The operating system configuration
        :param pulumi.Input[str] pool_id: The ID of the pool to assign the container to
        :param pulumi.Input[bool] started: Whether to start the container
        :param pulumi.Input[bool] template: Whether to create a template
        :param pulumi.Input[int] vm_id: The VM identifier
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ContainerState.__new__(_ContainerState)

        __props__.__dict__["clone"] = clone
        __props__.__dict__["console"] = console
        __props__.__dict__["cpu"] = cpu
        __props__.__dict__["description"] = description
        __props__.__dict__["disk"] = disk
        __props__.__dict__["initialization"] = initialization
        __props__.__dict__["memory"] = memory
        __props__.__dict__["network_interfaces"] = network_interfaces
        __props__.__dict__["node_name"] = node_name
        __props__.__dict__["operating_system"] = operating_system
        __props__.__dict__["pool_id"] = pool_id
        __props__.__dict__["started"] = started
        __props__.__dict__["template"] = template
        __props__.__dict__["vm_id"] = vm_id
        return Container(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def clone(self) -> pulumi.Output[Optional['outputs.ContainerClone']]:
        """
        The cloning configuration
        """
        return pulumi.get(self, "clone")

    @property
    @pulumi.getter
    def console(self) -> pulumi.Output[Optional['outputs.ContainerConsole']]:
        """
        The console configuration
        """
        return pulumi.get(self, "console")

    @property
    @pulumi.getter
    def cpu(self) -> pulumi.Output[Optional['outputs.ContainerCpu']]:
        """
        The CPU allocation
        """
        return pulumi.get(self, "cpu")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def disk(self) -> pulumi.Output[Optional['outputs.ContainerDisk']]:
        """
        The disks
        """
        return pulumi.get(self, "disk")

    @property
    @pulumi.getter
    def initialization(self) -> pulumi.Output[Optional['outputs.ContainerInitialization']]:
        """
        The initialization configuration
        """
        return pulumi.get(self, "initialization")

    @property
    @pulumi.getter
    def memory(self) -> pulumi.Output[Optional['outputs.ContainerMemory']]:
        """
        The memory allocation
        """
        return pulumi.get(self, "memory")

    @property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> pulumi.Output[Optional[Sequence['outputs.ContainerNetworkInterface']]]:
        """
        The network interfaces
        """
        return pulumi.get(self, "network_interfaces")

    @property
    @pulumi.getter(name="nodeName")
    def node_name(self) -> pulumi.Output[str]:
        """
        The node name
        """
        return pulumi.get(self, "node_name")

    @property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> pulumi.Output[Optional['outputs.ContainerOperatingSystem']]:
        """
        The operating system configuration
        """
        return pulumi.get(self, "operating_system")

    @property
    @pulumi.getter(name="poolId")
    def pool_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the pool to assign the container to
        """
        return pulumi.get(self, "pool_id")

    @property
    @pulumi.getter
    def started(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to start the container
        """
        return pulumi.get(self, "started")

    @property
    @pulumi.getter
    def template(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to create a template
        """
        return pulumi.get(self, "template")

    @property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> pulumi.Output[Optional[int]]:
        """
        The VM identifier
        """
        return pulumi.get(self, "vm_id")

