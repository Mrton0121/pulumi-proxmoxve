// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.ProxmoxVE.Inputs
{

    public sealed class Vm2CloneGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the VM to clone.
        /// </summary>
        [Input("id", required: true)]
        public Input<int> Id { get; set; } = null!;

        /// <summary>
        /// The number of retries to perform when cloning the VM (default: 3).
        /// </summary>
        [Input("retries")]
        public Input<int>? Retries { get; set; }

        public Vm2CloneGetArgs()
        {
        }
        public static new Vm2CloneGetArgs Empty => new Vm2CloneGetArgs();
    }
}