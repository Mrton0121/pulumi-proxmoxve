// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.ProxmoxVE.VM.Inputs
{

    public sealed class VirtualMachineSerialDeviceArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The device (defaults to `socket`).
        /// - `/dev/*` - A host serial device.
        /// </summary>
        [Input("device")]
        public Input<string>? Device { get; set; }

        public VirtualMachineSerialDeviceArgs()
        {
        }
        public static new VirtualMachineSerialDeviceArgs Empty => new VirtualMachineSerialDeviceArgs();
    }
}