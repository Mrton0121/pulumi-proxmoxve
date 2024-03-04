// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.ProxmoxVE.CT.Outputs
{

    [OutputType]
    public sealed class ContainerStartup
    {
        /// <summary>
        /// A non-negative number defining the delay in
        /// seconds before the next container is shut down.
        /// </summary>
        public readonly int? DownDelay;
        /// <summary>
        /// A non-negative number defining the general startup
        /// order.
        /// </summary>
        public readonly int? Order;
        /// <summary>
        /// A non-negative number defining the delay in
        /// seconds before the next container is started.
        /// </summary>
        public readonly int? UpDelay;

        [OutputConstructor]
        private ContainerStartup(
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
