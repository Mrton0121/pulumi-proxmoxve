// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.ProxmoxVE.VM.Inputs
{

    public sealed class VirtualMachineMemoryGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The dedicated memory in megabytes (defaults to `512`).
        /// </summary>
        [Input("dedicated")]
        public Input<int>? Dedicated { get; set; }

        /// <summary>
        /// The floating memory in megabytes. The default is `0`, which disables "ballooning device" for the VM.
        /// Please note that Proxmox has ballooning enabled by default. To enable it, set `floating` to the same value as `dedicated`.
        /// See [Proxmox documentation](https://pve.proxmox.com/pve-docs/pve-admin-guide.html#qm_memory) section 10.2.6 for more information.
        /// </summary>
        [Input("floating")]
        public Input<int>? Floating { get; set; }

        /// <summary>
        /// Enable/disable hugepages memory (defaults to disable).
        /// </summary>
        [Input("hugepages")]
        public Input<string>? Hugepages { get; set; }

        /// <summary>
        /// Keep hugepages memory after the VM is stopped (defaults to `false`).
        /// 
        /// Settings `hugepages` and `keep_hugepages` are only allowed for `root@pam` authenticated user.
        /// And required `cpu.numa` to be enabled.
        /// </summary>
        [Input("keepHugepages")]
        public Input<bool>? KeepHugepages { get; set; }

        /// <summary>
        /// The shared memory in megabytes (defaults to `0`).
        /// </summary>
        [Input("shared")]
        public Input<int>? Shared { get; set; }

        public VirtualMachineMemoryGetArgs()
        {
        }
        public static new VirtualMachineMemoryGetArgs Empty => new VirtualMachineMemoryGetArgs();
    }
}
