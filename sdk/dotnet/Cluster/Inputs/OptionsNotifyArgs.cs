// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.ProxmoxVE.Cluster.Inputs
{

    public sealed class OptionsNotifyArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Cluster-wide notification settings for the HA fencing mode. Must be `always` | `never`.
        /// </summary>
        [Input("haFencingMode")]
        public Input<string>? HaFencingMode { get; set; }

        /// <summary>
        /// Cluster-wide notification settings for the HA fencing target.
        /// </summary>
        [Input("haFencingTarget")]
        public Input<string>? HaFencingTarget { get; set; }

        /// <summary>
        /// Cluster-wide notification settings for package updates. Must be `auto` | `always` | `never`.
        /// </summary>
        [Input("packageUpdates")]
        public Input<string>? PackageUpdates { get; set; }

        /// <summary>
        /// Cluster-wide notification settings for the package updates target.
        /// </summary>
        [Input("packageUpdatesTarget")]
        public Input<string>? PackageUpdatesTarget { get; set; }

        /// <summary>
        /// Cluster-wide notification settings for replication. Must be `always` | `never`.
        /// </summary>
        [Input("replication")]
        public Input<string>? Replication { get; set; }

        /// <summary>
        /// Cluster-wide notification settings for the replication target.
        /// </summary>
        [Input("replicationTarget")]
        public Input<string>? ReplicationTarget { get; set; }

        public OptionsNotifyArgs()
        {
        }
        public static new OptionsNotifyArgs Empty => new OptionsNotifyArgs();
    }
}