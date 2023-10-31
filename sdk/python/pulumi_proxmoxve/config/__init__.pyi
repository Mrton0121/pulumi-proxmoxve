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

apiToken: Optional[str]
"""
The API token for the Proxmox VE API.
"""

endpoint: Optional[str]
"""
The endpoint for the Proxmox VE API.
"""

insecure: Optional[bool]
"""
Whether to skip the TLS verification step.
"""

otp: Optional[str]
"""
The one-time password for the Proxmox VE API.
"""

password: Optional[str]
"""
The password for the Proxmox VE API.
"""

ssh: Optional[str]
"""
The SSH configuration for the Proxmox nodes.
"""

tmpDir: Optional[str]
"""
The alternative temporary directory.
"""

username: Optional[str]
"""
The username for the Proxmox VE API.
"""

