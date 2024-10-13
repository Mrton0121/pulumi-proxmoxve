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
from . import outputs

__all__ = [
    'GetPluginsResult',
    'AwaitableGetPluginsResult',
    'get_plugins',
    'get_plugins_output',
]

@pulumi.output_type
class GetPluginsResult:
    """
    A collection of values returned by getPlugins.
    """
    def __init__(__self__, id=None, plugins=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if plugins and not isinstance(plugins, list):
            raise TypeError("Expected argument 'plugins' to be a list")
        pulumi.set(__self__, "plugins", plugins)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def plugins(self) -> Sequence['outputs.GetPluginsPluginResult']:
        """
        List of ACME plugins
        """
        return pulumi.get(self, "plugins")


class AwaitableGetPluginsResult(GetPluginsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPluginsResult(
            id=self.id,
            plugins=self.plugins)


def get_plugins(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPluginsResult:
    """
    Retrieves the list of ACME plugins.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_proxmoxve as proxmoxve

    example = proxmoxve.Acme.get_plugins()
    pulumi.export("dataProxmoxVirtualEnvironmentAcmePlugins", example.plugins)
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('proxmoxve:Acme/getPlugins:getPlugins', __args__, opts=opts, typ=GetPluginsResult).value

    return AwaitableGetPluginsResult(
        id=pulumi.get(__ret__, 'id'),
        plugins=pulumi.get(__ret__, 'plugins'))
def get_plugins_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPluginsResult]:
    """
    Retrieves the list of ACME plugins.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_proxmoxve as proxmoxve

    example = proxmoxve.Acme.get_plugins()
    pulumi.export("dataProxmoxVirtualEnvironmentAcmePlugins", example.plugins)
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('proxmoxve:Acme/getPlugins:getPlugins', __args__, opts=opts, typ=GetPluginsResult)
    return __ret__.apply(lambda __response__: GetPluginsResult(
        id=pulumi.get(__response__, 'id'),
        plugins=pulumi.get(__response__, 'plugins')))
