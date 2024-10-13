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
    'GetAccountResult',
    'AwaitableGetAccountResult',
    'get_account',
    'get_account_output',
]

@pulumi.output_type
class GetAccountResult:
    """
    A collection of values returned by getAccount.
    """
    def __init__(__self__, account=None, directory=None, id=None, location=None, name=None, tos=None):
        if account and not isinstance(account, dict):
            raise TypeError("Expected argument 'account' to be a dict")
        pulumi.set(__self__, "account", account)
        if directory and not isinstance(directory, str):
            raise TypeError("Expected argument 'directory' to be a str")
        pulumi.set(__self__, "directory", directory)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if tos and not isinstance(tos, str):
            raise TypeError("Expected argument 'tos' to be a str")
        pulumi.set(__self__, "tos", tos)

    @property
    @pulumi.getter
    def account(self) -> 'outputs.GetAccountAccountResult':
        """
        The ACME account information.
        """
        return pulumi.get(self, "account")

    @property
    @pulumi.getter
    def directory(self) -> str:
        """
        The directory URL of the ACME account.
        """
        return pulumi.get(self, "directory")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The location URL of the ACME account.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The identifier of the ACME account to read.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tos(self) -> str:
        """
        The URL of the terms of service of the ACME account.
        """
        return pulumi.get(self, "tos")


class AwaitableGetAccountResult(GetAccountResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccountResult(
            account=self.account,
            directory=self.directory,
            id=self.id,
            location=self.location,
            name=self.name,
            tos=self.tos)


def get_account(name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccountResult:
    """
    Retrieves information about a specific ACME account.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_proxmoxve as proxmoxve

    all = proxmoxve.Acme.get_accounts()
    example = [proxmoxve.Acme.get_account(name=__value) for __key, __value in all.accounts]
    pulumi.export("dataProxmoxVirtualEnvironmentAcmeAccount", example)
    ```


    :param str name: The identifier of the ACME account to read.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('proxmoxve:Acme/getAccount:getAccount', __args__, opts=opts, typ=GetAccountResult).value

    return AwaitableGetAccountResult(
        account=pulumi.get(__ret__, 'account'),
        directory=pulumi.get(__ret__, 'directory'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        tos=pulumi.get(__ret__, 'tos'))
def get_account_output(name: Optional[pulumi.Input[Optional[str]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAccountResult]:
    """
    Retrieves information about a specific ACME account.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_proxmoxve as proxmoxve

    all = proxmoxve.Acme.get_accounts()
    example = [proxmoxve.Acme.get_account(name=__value) for __key, __value in all.accounts]
    pulumi.export("dataProxmoxVirtualEnvironmentAcmeAccount", example)
    ```


    :param str name: The identifier of the ACME account to read.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('proxmoxve:Acme/getAccount:getAccount', __args__, opts=opts, typ=GetAccountResult)
    return __ret__.apply(lambda __response__: GetAccountResult(
        account=pulumi.get(__response__, 'account'),
        directory=pulumi.get(__response__, 'directory'),
        id=pulumi.get(__response__, 'id'),
        location=pulumi.get(__response__, 'location'),
        name=pulumi.get(__response__, 'name'),
        tos=pulumi.get(__response__, 'tos')))
