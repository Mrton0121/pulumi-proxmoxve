// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.ProxmoxVE.VM.Outputs
{

    [OutputType]
    public sealed class VirtualMachineStartup
    {
        public readonly int? DownDelay;
        public readonly int? Order;
        public readonly int? UpDelay;

        [OutputConstructor]
        private VirtualMachineStartup(
            int? downDelay,

            int? order,

            int? upDelay)
        {
            DownDelay = downDelay;
            Order = order;
            UpDelay = upDelay;
        }
    }
}