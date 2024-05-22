// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.ProxmoxVE.Outputs
{

    [OutputType]
    public sealed class Vm2Cpu
    {
        /// <summary>
        /// The CPU cores that are used to run the VM’s vCPU. The value is a list of CPU IDs, separated by commas. The CPU IDs are zero-based.  For example, `0,1,2,3` (which also can be shortened to `0-3`) means that the VM’s vCPUs are run on the first four CPU cores. Setting `affinity` is only allowed for `root@pam` authenticated user.
        /// </summary>
        public readonly string? Affinity;
        /// <summary>
        /// The CPU architecture `&lt;aarch64 | x86_64&gt;` (defaults to the host). Setting `affinity` is only allowed for `root@pam` authenticated user.
        /// </summary>
        public readonly string? Architecture;
        /// <summary>
        /// The number of CPU cores per socket (defaults to `1`).
        /// </summary>
        public readonly int? Cores;
        /// <summary>
        /// Set of additional CPU flags. Use `+FLAG` to enable, `-FLAG` to disable a flag. Custom CPU models can specify any flag supported by QEMU/KVM, VM-specific flags must be from the following set for security reasons: `pcid`, `spec-ctrl`, `ibpb`, `ssbd`, `virt-ssbd`, `amd-ssbd`, `amd-no-ssb`, `pdpe1gb`, `md-clear`, `hv-tlbflush`, `hv-evmcs`, `aes`.
        /// </summary>
        public readonly ImmutableArray<string> Flags;
        /// <summary>
        /// The number of hotplugged vCPUs (defaults to `0`).
        /// </summary>
        public readonly int? Hotplugged;
        /// <summary>
        /// Limit of CPU usage (defaults to `0` which means no limit).
        /// </summary>
        public readonly int? Limit;
        /// <summary>
        /// Enable NUMA (defaults to `false`).
        /// </summary>
        public readonly bool? Numa;
        /// <summary>
        /// The number of CPU sockets (defaults to `1`).
        /// </summary>
        public readonly int? Sockets;
        /// <summary>
        /// Emulated CPU type, it's recommended to use `x86-64-v2-AES` or higher (defaults to `kvm64`). See https://pve.proxmox.com/pve-docs/pve-admin-guide.html#qm*virtual*machines_settings for more information.
        /// </summary>
        public readonly string? Type;
        /// <summary>
        /// CPU weight for a VM. Argument is used in the kernel fair scheduler. The larger the number is, the more CPU time this VM gets. Number is relative to weights of all the other running VMs.
        /// </summary>
        public readonly int? Units;

        [OutputConstructor]
        private Vm2Cpu(
            string? affinity,

            string? architecture,

            int? cores,

            ImmutableArray<string> flags,

            int? hotplugged,

            int? limit,

            bool? numa,

            int? sockets,

            string? type,

            int? units)
        {
            Affinity = affinity;
            Architecture = architecture;
            Cores = cores;
            Flags = flags;
            Hotplugged = hotplugged;
            Limit = limit;
            Numa = numa;
            Sockets = sockets;
            Type = type;
            Units = units;
        }
    }
}