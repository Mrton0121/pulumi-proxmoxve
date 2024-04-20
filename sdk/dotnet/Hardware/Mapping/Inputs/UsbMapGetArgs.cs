// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.ProxmoxVE.Hardware.Mapping.Inputs
{

    public sealed class UsbMapGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The comment of the mapped USB device.
        /// </summary>
        [Input("comment")]
        public Input<string>? Comment { get; set; }

        /// <summary>
        /// The ID of the map.
        /// </summary>
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        /// <summary>
        /// The node name of the map.
        /// </summary>
        [Input("node", required: true)]
        public Input<string> Node { get; set; } = null!;

        /// <summary>
        /// The path of the map. For hardware mappings of type USB the path is optional and indicates that the device is mapped through the device ID instead of ports.
        /// </summary>
        [Input("path")]
        public Input<string>? Path { get; set; }

        public UsbMapGetArgs()
        {
        }
        public static new UsbMapGetArgs Empty => new UsbMapGetArgs();
    }
}
