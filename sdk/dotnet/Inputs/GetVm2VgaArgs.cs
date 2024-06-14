// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.ProxmoxVE.Inputs
{

    public sealed class GetVm2VgaInputArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Enable a specific clipboard.
        /// </summary>
        [Input("clipboard", required: true)]
        public Input<string> Clipboard { get; set; } = null!;

        /// <summary>
        /// The VGA memory in megabytes (4-512 MB). Has no effect with serial display.
        /// </summary>
        [Input("memory", required: true)]
        public Input<int> Memory { get; set; } = null!;

        /// <summary>
        /// The VGA type.
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public GetVm2VgaInputArgs()
        {
        }
        public static new GetVm2VgaInputArgs Empty => new GetVm2VgaInputArgs();
    }
}