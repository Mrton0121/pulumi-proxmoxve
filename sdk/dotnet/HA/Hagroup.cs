// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.ProxmoxVE.HA
{
    /// <summary>
    /// Manages a High Availability group in a Proxmox VE cluster.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using ProxmoxVE = Pulumi.ProxmoxVE;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var example = new ProxmoxVE.HA.HAGroup("example", new()
    ///     {
    ///         Group = "example",
    ///         Comment = "This is a comment.",
    ///         Nodes = 
    ///         {
    ///             { "node1", null },
    ///             { "node2", 2 },
    ///             { "node3", 1 },
    ///         },
    ///         Restricted = true,
    ///         NoFailback = false,
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// #!/usr/bin/env sh HA groups can be imported using their name, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import proxmoxve:HA/hAGroup:HAGroup example example
    /// ```
    /// </summary>
    [ProxmoxVEResourceType("proxmoxve:HA/hAGroup:HAGroup")]
    public partial class HAGroup : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The comment associated with this group
        /// </summary>
        [Output("comment")]
        public Output<string?> Comment { get; private set; } = null!;

        /// <summary>
        /// The identifier of the High Availability group to manage.
        /// </summary>
        [Output("group")]
        public Output<string> Group { get; private set; } = null!;

        /// <summary>
        /// A flag that indicates that failing back to a higher priority node is disabled for this HA group. Defaults to `false`.
        /// </summary>
        [Output("noFailback")]
        public Output<bool> NoFailback { get; private set; } = null!;

        /// <summary>
        /// The member nodes for this group. They are provided as a map, where the keys are the node names and the values represent their priority: integers for known priorities or `null` for unset priorities.
        /// </summary>
        [Output("nodes")]
        public Output<ImmutableDictionary<string, int>> Nodes { get; private set; } = null!;

        /// <summary>
        /// A flag that indicates that other nodes may not be used to run resources associated to this HA group. Defaults to `false`.
        /// </summary>
        [Output("restricted")]
        public Output<bool> Restricted { get; private set; } = null!;


        /// <summary>
        /// Create a HAGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public HAGroup(string name, HAGroupArgs args, CustomResourceOptions? options = null)
            : base("proxmoxve:HA/hAGroup:HAGroup", name, args ?? new HAGroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private HAGroup(string name, Input<string> id, HAGroupState? state = null, CustomResourceOptions? options = null)
            : base("proxmoxve:HA/hAGroup:HAGroup", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/muhlba91/pulumi-proxmoxve",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing HAGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static HAGroup Get(string name, Input<string> id, HAGroupState? state = null, CustomResourceOptions? options = null)
        {
            return new HAGroup(name, id, state, options);
        }
    }

    public sealed class HAGroupArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The comment associated with this group
        /// </summary>
        [Input("comment")]
        public Input<string>? Comment { get; set; }

        /// <summary>
        /// The identifier of the High Availability group to manage.
        /// </summary>
        [Input("group", required: true)]
        public Input<string> Group { get; set; } = null!;

        /// <summary>
        /// A flag that indicates that failing back to a higher priority node is disabled for this HA group. Defaults to `false`.
        /// </summary>
        [Input("noFailback")]
        public Input<bool>? NoFailback { get; set; }

        [Input("nodes", required: true)]
        private InputMap<int>? _nodes;

        /// <summary>
        /// The member nodes for this group. They are provided as a map, where the keys are the node names and the values represent their priority: integers for known priorities or `null` for unset priorities.
        /// </summary>
        public InputMap<int> Nodes
        {
            get => _nodes ?? (_nodes = new InputMap<int>());
            set => _nodes = value;
        }

        /// <summary>
        /// A flag that indicates that other nodes may not be used to run resources associated to this HA group. Defaults to `false`.
        /// </summary>
        [Input("restricted")]
        public Input<bool>? Restricted { get; set; }

        public HAGroupArgs()
        {
        }
        public static new HAGroupArgs Empty => new HAGroupArgs();
    }

    public sealed class HAGroupState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The comment associated with this group
        /// </summary>
        [Input("comment")]
        public Input<string>? Comment { get; set; }

        /// <summary>
        /// The identifier of the High Availability group to manage.
        /// </summary>
        [Input("group")]
        public Input<string>? Group { get; set; }

        /// <summary>
        /// A flag that indicates that failing back to a higher priority node is disabled for this HA group. Defaults to `false`.
        /// </summary>
        [Input("noFailback")]
        public Input<bool>? NoFailback { get; set; }

        [Input("nodes")]
        private InputMap<int>? _nodes;

        /// <summary>
        /// The member nodes for this group. They are provided as a map, where the keys are the node names and the values represent their priority: integers for known priorities or `null` for unset priorities.
        /// </summary>
        public InputMap<int> Nodes
        {
            get => _nodes ?? (_nodes = new InputMap<int>());
            set => _nodes = value;
        }

        /// <summary>
        /// A flag that indicates that other nodes may not be used to run resources associated to this HA group. Defaults to `false`.
        /// </summary>
        [Input("restricted")]
        public Input<bool>? Restricted { get; set; }

        public HAGroupState()
        {
        }
        public static new HAGroupState Empty => new HAGroupState();
    }
}
