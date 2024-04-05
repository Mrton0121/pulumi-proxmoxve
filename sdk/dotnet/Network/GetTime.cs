// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.ProxmoxVE.Network
{
    public static class GetTime
    {
        /// <summary>
        /// Retrieves the current time for a specific node.
        /// 
        /// ## Example Usage
        /// 
        /// &lt;!--Start PulumiCodeChooser --&gt;
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using ProxmoxVE = Pulumi.ProxmoxVE;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var firstNodeTime = ProxmoxVE.Network.GetTime.Invoke(new()
        ///     {
        ///         NodeName = "first-node",
        ///     });
        /// 
        /// });
        /// ```
        /// &lt;!--End PulumiCodeChooser --&gt;
        /// </summary>
        public static Task<GetTimeResult> InvokeAsync(GetTimeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetTimeResult>("proxmoxve:Network/getTime:getTime", args ?? new GetTimeArgs(), options.WithDefaults());

        /// <summary>
        /// Retrieves the current time for a specific node.
        /// 
        /// ## Example Usage
        /// 
        /// &lt;!--Start PulumiCodeChooser --&gt;
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using ProxmoxVE = Pulumi.ProxmoxVE;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var firstNodeTime = ProxmoxVE.Network.GetTime.Invoke(new()
        ///     {
        ///         NodeName = "first-node",
        ///     });
        /// 
        /// });
        /// ```
        /// &lt;!--End PulumiCodeChooser --&gt;
        /// </summary>
        public static Output<GetTimeResult> Invoke(GetTimeInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetTimeResult>("proxmoxve:Network/getTime:getTime", args ?? new GetTimeInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetTimeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// A node name.
        /// </summary>
        [Input("nodeName", required: true)]
        public string NodeName { get; set; } = null!;

        public GetTimeArgs()
        {
        }
        public static new GetTimeArgs Empty => new GetTimeArgs();
    }

    public sealed class GetTimeInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// A node name.
        /// </summary>
        [Input("nodeName", required: true)]
        public Input<string> NodeName { get; set; } = null!;

        public GetTimeInvokeArgs()
        {
        }
        public static new GetTimeInvokeArgs Empty => new GetTimeInvokeArgs();
    }


    [OutputType]
    public sealed class GetTimeResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The node's local time.
        /// </summary>
        public readonly string LocalTime;
        public readonly string NodeName;
        /// <summary>
        /// The node's time zone.
        /// </summary>
        public readonly string TimeZone;
        /// <summary>
        /// The node's local time formatted as UTC.
        /// </summary>
        public readonly string UtcTime;

        [OutputConstructor]
        private GetTimeResult(
            string id,

            string localTime,

            string nodeName,

            string timeZone,

            string utcTime)
        {
            Id = id;
            LocalTime = localTime;
            NodeName = nodeName;
            TimeZone = timeZone;
            UtcTime = utcTime;
        }
    }
}