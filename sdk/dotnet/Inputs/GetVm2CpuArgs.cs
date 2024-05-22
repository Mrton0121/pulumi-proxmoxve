// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.ProxmoxVE.Inputs
{

    public sealed class GetVm2CpuInputArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// List of host cores used to execute guest processes, for example: '0,5,8-11'
        /// </summary>
        [Input("affinity", required: true)]
        public Input<string> Affinity { get; set; } = null!;

        /// <summary>
        /// The CPU architecture.
        /// </summary>
        [Input("architecture", required: true)]
        public Input<string> Architecture { get; set; } = null!;

        /// <summary>
        /// The number of CPU cores per socket.
        /// </summary>
        [Input("cores", required: true)]
        public Input<int> Cores { get; set; } = null!;

        [Input("flags", required: true)]
        private InputList<string>? _flags;

        /// <summary>
        /// Set of additional CPU flags.
        /// </summary>
        public InputList<string> Flags
        {
            get => _flags ?? (_flags = new InputList<string>());
            set => _flags = value;
        }

        /// <summary>
        /// The number of hotplugged vCPUs.
        /// </summary>
        [Input("hotplugged", required: true)]
        public Input<int> Hotplugged { get; set; } = null!;

        /// <summary>
        /// Limit of CPU usage.
        /// </summary>
        [Input("limit", required: true)]
        public Input<int> Limit { get; set; } = null!;

        /// <summary>
        /// Enable NUMA.
        /// </summary>
        [Input("numa", required: true)]
        public Input<bool> Numa { get; set; } = null!;

        /// <summary>
        /// The number of CPU sockets.
        /// </summary>
        [Input("sockets", required: true)]
        public Input<int> Sockets { get; set; } = null!;

        /// <summary>
        /// Emulated CPU type.
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        /// <summary>
        /// CPU weight for a VM
        /// </summary>
        [Input("units", required: true)]
        public Input<int> Units { get; set; } = null!;

        public GetVm2CpuInputArgs()
        {
        }
        public static new GetVm2CpuInputArgs Empty => new GetVm2CpuInputArgs();
    }
}