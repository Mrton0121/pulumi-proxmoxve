// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.ProxmoxVE
{
    /// <summary>
    /// &gt; **DO NOT USE**
    /// This is an experimental implementation of a Proxmox VM resource using Plugin Framework.&lt;br&gt;&lt;br&gt;It is a Proof of Concept, highly experimental and **will** change in future. It does not support all features of the Proxmox API for VMs and **MUST NOT** be used in production.
    /// </summary>
    [ProxmoxVEResourceType("proxmoxve:index/vm2:Vm2")]
    public partial class Vm2 : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The description of the VM.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The name of the VM. Doesn't have to be unique.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The name of the node where the VM is provisioned.
        /// </summary>
        [Output("nodeName")]
        public Output<string> NodeName { get; private set; } = null!;

        [Output("timeouts")]
        public Output<Outputs.Vm2Timeouts?> Timeouts { get; private set; } = null!;


        /// <summary>
        /// Create a Vm2 resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Vm2(string name, Vm2Args args, CustomResourceOptions? options = null)
            : base("proxmoxve:index/vm2:Vm2", name, args ?? new Vm2Args(), MakeResourceOptions(options, ""))
        {
        }

        private Vm2(string name, Input<string> id, Vm2State? state = null, CustomResourceOptions? options = null)
            : base("proxmoxve:index/vm2:Vm2", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Vm2 resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Vm2 Get(string name, Input<string> id, Vm2State? state = null, CustomResourceOptions? options = null)
        {
            return new Vm2(name, id, state, options);
        }
    }

    public sealed class Vm2Args : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description of the VM.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The name of the VM. Doesn't have to be unique.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The name of the node where the VM is provisioned.
        /// </summary>
        [Input("nodeName", required: true)]
        public Input<string> NodeName { get; set; } = null!;

        [Input("timeouts")]
        public Input<Inputs.Vm2TimeoutsArgs>? Timeouts { get; set; }

        public Vm2Args()
        {
        }
        public static new Vm2Args Empty => new Vm2Args();
    }

    public sealed class Vm2State : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description of the VM.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The name of the VM. Doesn't have to be unique.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The name of the node where the VM is provisioned.
        /// </summary>
        [Input("nodeName")]
        public Input<string>? NodeName { get; set; }

        [Input("timeouts")]
        public Input<Inputs.Vm2TimeoutsGetArgs>? Timeouts { get; set; }

        public Vm2State()
        {
        }
        public static new Vm2State Empty => new Vm2State();
    }
}