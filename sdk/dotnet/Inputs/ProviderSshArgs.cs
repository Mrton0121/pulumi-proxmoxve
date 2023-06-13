// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.ProxmoxVE.Inputs
{

    public sealed class ProviderSshArgs : global::Pulumi.ResourceArgs
    {
        [Input("agent")]
        public Input<bool>? Agent { get; set; }

        [Input("agentSocket")]
        public Input<string>? AgentSocket { get; set; }

        [Input("nodes")]
        private InputList<Inputs.ProviderSshNodeArgs>? _nodes;
        public InputList<Inputs.ProviderSshNodeArgs> Nodes
        {
            get => _nodes ?? (_nodes = new InputList<Inputs.ProviderSshNodeArgs>());
            set => _nodes = value;
        }

        [Input("password")]
        private Input<string>? _password;
        public Input<string>? Password
        {
            get => _password;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _password = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        [Input("username")]
        public Input<string>? Username { get; set; }

        public ProviderSshArgs()
        {
        }
        public static new ProviderSshArgs Empty => new ProviderSshArgs();
    }
}